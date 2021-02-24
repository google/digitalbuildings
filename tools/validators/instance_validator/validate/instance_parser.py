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
import strictyaml as syaml
import ruamel
import sys

#### Program constants ####
# Size of entity block to send to the syntax validator
# Breaking up the file into blocks is necessary to increase performance
_ENTITIES_PER_BATCH = 1

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

# Value for a udmi compliant translation
_COMPLIANT_REGEX = u'^COMPLIANT$'

# A valid device field must match this
_FIELD_REGEX = u'^[a-z]+[a-z0-9]*(?:_[a-z]+[a-z0-9]*)*(?:_[0-9]+)*$'
"""Schema separately parses translation to account for multiple valid formats

github.com/google/digitalbuildings/blob/master/ontology/docs/building_config.md
#defining-translations
"""
_TRANSLATION_SCHEMA = syaml.Regex(_COMPLIANT_REGEX) | syaml.MapPattern(
    syaml.Regex(_FIELD_REGEX),
    syaml.Str() | syaml.Map({
        'present_value':
            syaml.Str(),
        syaml.Optional('states'):
            syaml.MapPattern(syaml.Regex(u'^[A-Z][A-Z_]+'), syaml.Str()),
        syaml.Optional('units'):
            syaml.Map({
                'key': syaml.Str(),
                'values': syaml.MapPattern(syaml.Str(), syaml.Str())
            }),
        syaml.Optional('unit_values'):
            syaml.MapPattern(syaml.Str(), syaml.Str())
    }))

_METADATA_SCHEMA = syaml.Map(
    {syaml.Optional(_CONFIG_MODE_KEY): syaml.Regex(u'^[A-Z][A-Z_]+')})

_ENTITY_VALIDATOR_BASE_SCHEMA = {
    'id':
        syaml.Str(),
    # TODO(b/166472270): revisit connection syntax
    #  validation. Current code might not follow
    #  the spec.
    syaml.Optional('connections'):
        syaml.MapPattern(syaml.Str(), syaml.Str())
        | syaml.Seq(syaml.MapPattern(syaml.Str(), syaml.Str())),
    syaml.Optional('links'):
        syaml.MapPattern(
            syaml.Str(),
            syaml.MapPattern(
                syaml.Regex(_FIELD_REGEX), syaml.Regex(_FIELD_REGEX))),
    syaml.Optional('translation'):
        _TRANSLATION_SCHEMA,
    syaml.Optional('metadata'):
        syaml.Any()
}


def _BuildFromKV(k: syaml.ScalarValidator,
                 v: syaml.Validator) -> syaml.Validator:
  """Allows a base validator to be defined once and reused with additions."""
  d = _ENTITY_VALIDATOR_BASE_SCHEMA.copy()
  d[k] = v
  return syaml.MapPattern(syaml.Str(), syaml.Map(d))


# Validates entities in INITIALIZE mode
_ENTITY_SCHEMA_INIT = _BuildFromKV('type', syaml.Str())
# Validates entities in UPDATE mode
_ENTITY_SCHEMA_UPDATE = _BuildFromKV(syaml.Optional('type'), syaml.Str())


def _ValidateBlockWithSchema(content: syaml.YAML,
                             schema: syaml.Validator) -> syaml.YAML:
  """Validates an entity instance based on a syaml-formatted YAML schema.

  Args:
    content: an entity instance in yaml format
    schema: YAML schema in syaml format

  Returns:
    Returns the parsed YAML data in a strictyaml-provided datastructure
    which is similar to a Python dictionary.
  """
  try:
    parsed = syaml.load(content, schema)
  except (ValueError, ruamel.yaml.parser.ParserError,
          ruamel.yaml.scanner.ScannerError,
          syaml.exceptions.YAMLValidationError,
          syaml.exceptions.DuplicateKeysDisallowed,
          syaml.exceptions.InconsistentIndentationDisallowed) as exception:
    print(exception)
    sys.exit(0)

  return parsed


class ConfigMode(enum.Enum):
  """Enumerated building config file processing modes."""
  INITIALIZE = 'INITIALIZE'
  UPDATE = 'UPDATE'

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
    """Return the YAML object derived from parsing the input files.

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
    all_content = {}
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
            self._ValidateMetadataBlock(entity_instance_block)
            entity_instance_block = ''
            in_config = False

          # wait until entity instance block reaches _ENTITIES_PER_BATCH
          elif found_entities > _ENTITIES_PER_BATCH:
            self._queued_entity_blocks.append(entity_instance_block)
            self._ProcessEntities()
            entity_instance_block = ''
            found_entities = 0
          found_entities += 1

        entity_instance_block = entity_instance_block + line

    # handle the singleton case
    if in_config:
      # parse the config block
      self._ValidateMetadataBlock(entity_instance_block)
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
        self._ValidateEntityBlock(self._queued_entity_blocks.popleft())
      except IndexError:
        break

  def _ValidateMetadataBlock(self, unvalidated_block: str) -> None:
    """Validates the metadata block and extracts the processing mode."""
    validated = _ValidateBlockWithSchema(unvalidated_block, _METADATA_SCHEMA)
    mode_str = validated.get(_CONFIG_MODE_KEY, None)
    if mode_str is not None:
      self._config_mode = ConfigMode.FromString(mode_str)
    else:
      self._config_mode = ConfigMode.Default()

  def _ValidateEntityBlock(self, unvalidated_block) -> None:
    """Validates a block of entities and adds them to the validated blocks.

    Args:
      unvalidated_block: string. A block of unvalidated entities

    Raises:
      KeyError: if self._config_mode is not set to a known value.
    """
    if ConfigMode.INITIALIZE == self._config_mode:
      schema = _ENTITY_SCHEMA_INIT
    elif ConfigMode.UPDATE == self._config_mode:
      schema = _ENTITY_SCHEMA_UPDATE
    else:
      raise KeyError('No valid _config_mode is set')

    validated = _ValidateBlockWithSchema(unvalidated_block, schema)

    for key in validated.data.keys():
      if key in self._validated_entities:
        raise ValueError('Duplicate key {0}'.format(key))

    self._validated_entities.update(validated.data)
