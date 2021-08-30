# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the License);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an AS IS BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Parses and validates YAML instance files for syntax"""
from __future__ import print_function

import collections
import enum
import re
import sys
from typing import Callable, Dict, List, Optional, Type, TypeVar

import ruamel
import strictyaml as syaml

#### Program constants ####
# Size of entity block to send to the syntax validator
# Breaking up the file into blocks is necessary to increase performance
_ENTITIES_PER_BATCH = 2


class ConfigMode(enum.Enum):
  """Enumerated building config file processing modes."""
  INITIALIZE = 'INITIALIZE'
  UPDATE = 'UPDATE'
  EXPORT = 'EXPORT'

  @classmethod
  def FromString(cls, value: str):
    """Returns a ConfigMode instance matching the provided string."""
    for _, member in cls.__members__.items():
      if member.value == value:
        return member
    raise LookupError

  @classmethod
  def Default(cls):
    """Returns the default ConfigMode if no config block is provided."""
    return cls.INITIALIZE


class EntityOperation(enum.Enum):
  """Enumerated building config entity processing modes."""
  UPDATE = 'UPDATE'
  ADD = 'ADD'
  DELETE = 'DELETE'

  @classmethod
  def FromString(cls, value: str):
    """Returns a ConfigMode instance matching the provided string."""
    for _, member in cls.__members__.items():
      if member.value == value:
        return member
    raise LookupError


def _OrRegex(values: List[str]) -> syaml.Regex:
  """Returns a regex matching any term in the provided list."""
  r_str = '|'.join(['(' + o + ')' for o in values])
  return syaml.Regex('^' + r_str + '$')


E = TypeVar('E', bound=enum.Enum)


def EnumToRegex(enum_type: Optional[Type[E]] = None,
                omit: Optional[List[E]] = None,
                exactly: Optional[E] = None) -> syaml.Regex:
  """Returns a regex matching any value of an enum.

  Args:
    enum_type: enum type to include values of
    omit: enum values to excluse when iterating throught the enum
    exactly: an exact value to check.  This is mutually exclusive of other args
  """
  if exactly:
    if enum_type or omit:
      raise ValueError('Cannot specify an exact value with other constraints')
    return _OrRegex([exactly.value])
  if omit is None:
    omit = []
  return _OrRegex([v.value for v in list(enum_type) if v not in omit])


def _MergeSchemas(first: Dict[syaml.ScalarValidator, syaml.Validator],
                  second: Dict[syaml.ScalarValidator, syaml.Validator]):
  """Returns a copy of first, updated with the contents of second."""
  merged = first.copy()
  merged.update(second)
  return merged


#### Public Text parsing Constants ####
ENTITY_ID_KEY = 'id'
ENTITY_CLOUD_DEVICE_ID_KEY = 'cloud_device_id'
ENTITY_TYPE_KEY = 'type'
ENTITY_OPERATION_KEY = 'operation'

LINKS_KEY = 'links'
TRANSLATION_KEY = 'translation'
CONNECTIONS_KEY = 'connections'
METADATA_KEY = 'metadata'
PRESENT_VALUE_KEY = 'present_value'
POINTS = 'points'
UNITS_KEY = 'units'
UNIT_NAME_KEY = 'key'
UNIT_VALUES_KEY = 'values'
STATES_KEY = 'states'
UPDATE_MASK_KEY = 'update_mask'
ETAG_KEY = 'etag'

#### Text parsing constants ####
# Lines matching this pattern have no content and can be dropped
_IGNORE_PATTERN = re.compile(r'^(\W)*#|\n')

# Minimum threshold for a valid entity name.  Additional validation is required
# check adherence to more specific naming conventions
# Note: As-written this will capture the metadata key below, so logic should
# check for it first
_ENTITY_INSTANCE_REGEX = '^[A-Z][A-Z0-9\\-]+:'
_ENTITY_INSTANCE_PATTERN = re.compile(_ENTITY_INSTANCE_REGEX)

# Exact key for the configuration metadata block
_CONFIG_METADATA_KEY = 'CONFIG_METADATA'
_CONFIG_METADATA_REGEX = '^{0}:'.format(_CONFIG_METADATA_KEY)
_CONFIG_METADATA_PATTERN = re.compile(_CONFIG_METADATA_REGEX)
# Key that marks the mode to parse file in.
_CONFIG_MODE_KEY = 'operation'

# A valid device field must match this
_FIELD_REGEX = u'^[a-z]+[a-z0-9]*(?:_[a-z]+[a-z0-9]*)*(?:_[0-9]+)*$'
"""Schema separately parses translation to account for multiple valid formats

github.com/google/digitalbuildings/blob/master/ontology/docs/building_config.md
#defining-translations
"""
_TRANSLATION_SCHEMA = syaml.MapPattern(
    syaml.Regex(_FIELD_REGEX),
    # Note: This block is somewhat permissive as the logic was difficult to
    # implement in syaml.  Additional validation occurs in EntityInstance
    syaml.Str() | syaml.Map({
        PRESENT_VALUE_KEY:
            syaml.Str(),
        syaml.Optional(STATES_KEY):
            syaml.MapPattern(syaml.Regex(u'^[A-Z][A-Z_]+'), syaml.Str()),
        syaml.Optional(UNITS_KEY):
            syaml.Map({
                UNIT_NAME_KEY: syaml.Str(),
                UNIT_VALUES_KEY: syaml.MapPattern(syaml.Str(), syaml.Str())
            }),
    }))

_METADATA_SCHEMA = syaml.Map({
    syaml.Optional(_CONFIG_MODE_KEY):
        EnumToRegex(ConfigMode, [ConfigMode.EXPORT])
})

_ENTITY_ID_SCHEMA = {ENTITY_ID_KEY: syaml.Str()}
_ENTITY_CLOUD_DEVICE_ID_SCHEMA = {
    syaml.Optional(ENTITY_CLOUD_DEVICE_ID_KEY): syaml.Str()
}
_ENTITY_ATTRIB_SCHEMA = {
    # TODO(b/166472270): revisit connection syntax
    #  validation. Current code might not follow
    #  the spec.
    syaml.Optional(CONNECTIONS_KEY):
        syaml.MapPattern(syaml.Str(), syaml.Str())
        | syaml.Seq(syaml.MapPattern(syaml.Str(), syaml.Str())),
    syaml.Optional(LINKS_KEY):
        syaml.MapPattern(
            syaml.Str(),
            syaml.MapPattern(
                syaml.Regex(_FIELD_REGEX), syaml.Regex(_FIELD_REGEX))),
    syaml.Optional(TRANSLATION_KEY):
        _TRANSLATION_SCHEMA,
    syaml.Optional(METADATA_KEY):
        syaml.Any()
}
_ENTITY_IDS_SCHEMA = _MergeSchemas(_ENTITY_ID_SCHEMA,
                                   _ENTITY_CLOUD_DEVICE_ID_SCHEMA)
_ENTITY_BASE_SCHEMA = _MergeSchemas(_ENTITY_IDS_SCHEMA, _ENTITY_ATTRIB_SCHEMA)
_ENTITY_INIT_SCHEMA = _MergeSchemas(_ENTITY_BASE_SCHEMA,
                                    {ENTITY_TYPE_KEY: syaml.Str()})
_ENTITY_UPDATE_SCHEMA = _MergeSchemas(
    _ENTITY_BASE_SCHEMA, {
        ETAG_KEY:
            syaml.Str(),
        syaml.Optional(ENTITY_TYPE_KEY):
            syaml.Str(),
        syaml.Optional(ENTITY_OPERATION_KEY):
            EnumToRegex(exactly=EntityOperation.UPDATE),
        syaml.Optional(UPDATE_MASK_KEY):
            syaml.UniqueSeq(syaml.Str())
    })
_ENTITY_ADD_SCHEMA = _MergeSchemas(
    _ENTITY_BASE_SCHEMA, {
        ENTITY_TYPE_KEY: syaml.Str(),
        ENTITY_OPERATION_KEY: EnumToRegex(exactly=EntityOperation.ADD)
    })
_ENTITY_DELETE_SCHEMA = _MergeSchemas(
    _ENTITY_ID_SCHEMA,
    {ENTITY_OPERATION_KEY: EnumToRegex(exactly=EntityOperation.DELETE)})


class InstanceParser():
  """One-shot state machine for parsing and syntax checking YAML config files.

  Class facilitates structural syntax validation, including duplication
  detection, of multiple config files passed one at a time.  The primary utility
  of using a state machine is to encapsulate the logic of digging out
  configuration data from the fileset to configure syntax validation before
  running it without using unnecessary memory.
  """

  def __init__(self):
    self._queued_entity_blocks = collections.deque()
    self._config_mode = None
    self._validated_entities = {}
    self._is_final = False

  def Finalize(self) -> None:
    """Finalize the state machine, applying defaults if no config was found."""
    if self._is_final:
      return
    if not self._config_mode:
      self._config_mode = ConfigMode.Default()
    self._ProcessEntities()
    self._is_final = True

  def GetEntities(self) -> syaml.YAML:
    """Returns the YAML object derived from parsing the input files.

    Raises:
      AssertionError: if Finalize() has not been called
    """
    assert self._is_final, 'State machine is not final. Call Finalize()'
    return self._validated_entities

  def GetConfigMode(self) -> ConfigMode:
    """Returns the processing mode defined in the config.

    Raises:
      AssertionError: if the config has not been found or default applied.
    """
    assert self._config_mode, ('Mode unset. If all files are added, call '
                               'Finalize()')
    return self._config_mode

  def AddFile(self, filename: str) -> None:
    """Add a new file for parsing by the state machine.

    Args:
      filename: a path to a file for reading with open()
    """
    entity_instance_block = ''
    found_entities = 0
    in_config = False
    with open(filename) as file:
      for line in file:
        if _IGNORE_PATTERN.match(line):
          continue

        if _CONFIG_METADATA_PATTERN.match(line):
          if self._config_mode:
            raise ValueError('Metadata block defined multiple times')
          # queue everything in the current block so the config can be isolated
          if entity_instance_block:
            self._queued_entity_blocks.append(entity_instance_block)
            entity_instance_block = ''
            found_entities = 0
          in_config = True
          continue

        if _ENTITY_INSTANCE_PATTERN.match(line):
          # If the last block was config, send it for parsing
          if in_config:
            self._ValidateBlock(entity_instance_block,
                                self._ValidateMetadataContent)
            entity_instance_block = ''
            in_config = False

          # wait until entity instance block reaches _ENTITIES_PER_BATCH
          elif found_entities >= _ENTITIES_PER_BATCH:
            self._queued_entity_blocks.append(entity_instance_block)
            self._ProcessEntities()
            entity_instance_block = ''
            found_entities = 0
          found_entities += 1

        entity_instance_block = entity_instance_block + line

    # handle the singleton case
    if in_config:
      # parse the config block
      self._ValidateBlock(entity_instance_block, self._ValidateMetadataContent)
    elif found_entities > 0:
      # try to process any queued entities
      self._queued_entity_blocks.append(entity_instance_block)
      self._ProcessEntities()

  def _ProcessEntities(self) -> None:
    """Validates all queued entity blocks if and only if config is defined."""
    # Do nothing if the config has not been processed.
    if not self._config_mode:
      return

    # Validate all queued blocks
    while True:
      try:
        self._ValidateBlock(self._queued_entity_blocks.popleft(),
                            self._ValidateEntityBlock)
      except IndexError:
        break

  def _ValidateMetadataContent(self, metadata_block: syaml.YAML) -> None:
    """Validates the metadata block and extracts the operation mode.

    Args:
      metadata_block: YAML contents of the config metadata block
    """
    mode_str = metadata_block.get(_CONFIG_MODE_KEY, None)
    if mode_str is not None:
      self._config_mode = ConfigMode.FromString(mode_str)
    else:
      self._config_mode = ConfigMode.Default()

  def _ValidateEntityContent(self, entity: syaml.YAML) -> None:
    """Validates the contents of a single entity.

    The logic will select the appropriate validation schema based on the
    config_mode of the container and the defined EntityOperation, if any.

    Args:
      entity: YAML object for the entityContents

    Raises:
      KeyError: if self._config_mode is not set to a known value.
    """
    if ConfigMode.INITIALIZE == self._config_mode:
      schema = syaml.Map(_ENTITY_INIT_SCHEMA)
    elif ConfigMode.UPDATE == self._config_mode:
      schema = syaml.Map(_ENTITY_UPDATE_SCHEMA)
      if ENTITY_OPERATION_KEY in entity:
        if entity[ENTITY_OPERATION_KEY] == EntityOperation.ADD.value:
          schema = syaml.Map(_ENTITY_ADD_SCHEMA)
        elif entity[ENTITY_OPERATION_KEY] == EntityOperation.DELETE.value:
          schema = syaml.Map(_ENTITY_DELETE_SCHEMA)
    else:
      raise KeyError('No valid _config_mode is set')

    entity.revalidate(schema)

    if TRANSLATION_KEY in entity.data.keys():
      if ENTITY_CLOUD_DEVICE_ID_KEY not in entity.data.keys():
        raise KeyError('cloud_device_id required when translation is present.')

  def _ValidateEntityBlock(self, block: syaml.YAML) -> None:
    """Validates a block of entities and adds them to the validated blocks.

    Args:
      block: YAML representing one or more entities

    Raises:
      ValueError: if block contains a key that has already been found.
    """

    for key in block.keys():
      if key in self._validated_entities:
        raise ValueError('Duplicate key {0}'.format(key))
      self._ValidateEntityContent(block.get(key))
    self._validated_entities.update(block.data)

  def _ValidateBlock(self, unvalidated_block: str,
                     validation_fn: Callable[[syaml.YAML], None]) -> None:
    """Validates a yaml-formatted string using the provided function.

    Args:
      unvalidated_block: string. A block of unvalidated entities
      validation_fn: a validation function that takes YAML as an argument
    """
    try:
      validated = syaml.load(unvalidated_block,
                             syaml.MapPattern(syaml.Str(), syaml.Any()))
      validation_fn(validated)

    except (ValueError, ruamel.yaml.parser.ParserError,
            ruamel.yaml.scanner.ScannerError,
            syaml.exceptions.YAMLValidationError,
            syaml.exceptions.DuplicateKeysDisallowed,
            syaml.exceptions.InconsistentIndentationDisallowed) as exception:
      print(exception)
      sys.exit(0)
