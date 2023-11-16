# Copyright 2023 Google LLC
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
"""Representations and validators for DigitalBuildings Entities."""

from __future__ import annotations
from __future__ import print_function

import re
from typing import Any, Dict, List, Optional, Set, Tuple

import strictyaml as syaml

from validate import connection
from validate import field_translation as ft_lib
from validate import instance_parser as parse
from validate import link
from yamlformat.validator import entity_type_lib
from yamlformat.validator import findings_lib
from yamlformat.validator import presubmit_validate_types_lib as pvt


# pylint: disable=line-too-long
_CONFIG_UPDATE = parse.ConfigMode.UPDATE
_CONFIG_INIT = parse.ConfigMode.INITIALIZE
_CONFIG_EXPORT = parse.ConfigMode.EXPORT
# udmi present value: points.$name.present_value
# udmi units: pointset.points.$name.units
# where name follows: [a-z][a-z0-9]*(_[a-z0-9]+)*
_UDMI_PRESENT_VALUE_REGEX = (
    r'^(points.)[a-z][a-z0-9]*(_[a-z0-9]+)*(.present_value)$'
)
_UDMI_PRESENT_VALUE_PATTERN = re.compile(_UDMI_PRESENT_VALUE_REGEX)

_UDMI_UNIT_FIELD_REGEX = (
    r'^(pointset.points.)[a-z][a-z0-9]*(_[a-z0-9]+)*(.units)$'
)
_UDMI_UNIT_FIELD_PATTERN = re.compile(_UDMI_UNIT_FIELD_REGEX)

_DEVICE_NUMERIC_ID_REGEX = r'[0-9]{16}'
_DEVICE_NUMERIC_ID_PATTERN = re.compile(_DEVICE_NUMERIC_ID_REGEX)

# Faciltities naming patterns
MEZZANINE_PATTERN = '([0-9]*)M'
SINGLE_LETTER_PATTERN = 'R|D|LG|FB|S|SBA|SBB'
# Same as BASEMENT_LEVEL_PATERN
PERMUTED_NUMBER_LETTER_PATTERN = 'B[0-9]*|[0-9]+B'
# Same as GARAGE_LEVEL_PATTERN
LETTER_NUMBER_PATTERN = '(G|UG|M)[0-9]*'
# Same as NORMAL_PATTERN
NUMBERS_PATTERN = '[0-9]+'
EXTRA_INFO_PATTERN = '(.*)'

COUNTRY_ID_PATTERN = '[A-Za-z]{2}'
CITY_ID_PATTERN = '[A-Za-z]{2,4}'
BUILDING_ID_PATTERN = '[A-Za-z0-9]{2,10}'
FLOOR_ID_PATTERN = f'{MEZZANINE_PATTERN}|{SINGLE_LETTER_PATTERN}|{PERMUTED_NUMBER_LETTER_PATTERN}|{LETTER_NUMBER_PATTERN}|{NUMBERS_PATTERN}'
ROOM_ID_PATTERN = '([0-9A-Z]+)'

BUILDING_CODE_REGEX = (
    f'^{COUNTRY_ID_PATTERN}-{CITY_ID_PATTERN}-{BUILDING_ID_PATTERN}'
)
FLOOR_CODE_REGEX = BUILDING_CODE_REGEX + f'-({FLOOR_ID_PATTERN})'
ROOM_CODE_REGEX = FLOOR_CODE_REGEX + f'-({ROOM_ID_PATTERN})'
FACILITIES_ENTITY_CODE_REGEX = FLOOR_CODE_REGEX + f'-{EXTRA_INFO_PATTERN}'

_BUILDING_TYPE_NAME = 'BUILDING'
_FLOOR_TYPE_NAME = 'FLOOR'
_ROOM_TYPE_NAME = 'ROOM'
_FACILITIES_NAMESPACE = 'FACILITIES'


def _FieldIsAllowed(
    universe: pvt.ConfigUniverse,
    as_written_field_name: str,
    entity_type: Optional[entity_type_lib.EntityType] = None,
) -> bool:
  """Returns true if the name is plausibly correct in the provided context.

  See `_GetAllowedField_` for detail.

  Args:
    universe: the ConfigUniverse to validate against
    as_written_field_name: the field name string as written in the config
    entity_type: the EntityType of the entity the field is defined on
  """

  return (
      _GetAllowedField(universe, as_written_field_name, entity_type) is not None
  )


def _GetAllowedField(
    universe: pvt.ConfigUniverse,
    as_written_field_name: str,
    entity_type: Optional[entity_type_lib.EntityType] = None,
) -> Optional[str]:
  """Returns the most likely qualified field name given the provided context.

  If an entity type is provided, the method validates that the field is valid
  for the type. If no type is provided, method will validate that the field
  exists given the amount of qualification provided. For instance, a fully
  qualified field `HVAC/run_status` would be validated against the HVAC
  namespace's fields, but `run_status` would be validated against the global
  namespace. Shorthand syntax will be interpreted correctly when the type is
  applied.  For instance `run_status` shorthand (an unqualified field reference)
  would correctly validate against the HVAC namespace if the field was defined
  in that namespace and the provided type was a HVAC type.

  Args:
    universe: the ConfigUniverse to validate against
    as_written_field_name: the field name string as written in the config
    entity_type: the EntityType of the entity the field is deifned on
  """
  # Field could be qualified or unqualified in the config.  We want to know
  if entity_type and not entity_type.allow_undefined_fields:
    field_obj = entity_type.GetFieldFromConfigText(as_written_field_name)
    if field_obj:
      return entity_type_lib.BuildQualifiedField(field_obj)
    else:
      return None

  try:
    namespace, field_name = entity_type_lib.SeparateFieldNamespace(
        as_written_field_name
    )
  except TypeError:
    namespace = ''
    field_name = as_written_field_name
  std_field_name, _ = entity_type_lib.SeparateFieldIncrement(field_name)
  if universe.field_universe.IsFieldDefined(std_field_name, namespace):
    return namespace + '/' + as_written_field_name

  return None


class CombinationValidator(object):
  """Combines Instance and Graph based validations into one step.

  Note, Actions requiring the ontology fail True if the ontology is not present.

  Attributes:
    universe: ConfigUniverse to validate against
    config_mode: defines how to approach validation (INITIALIZE = complete or
      UPDATE = partial)
    entity_instances: name to entity mapping of all entities in the config
  """

  def __init__(
      self,
      universe: pvt.ConfigUniverse,
      config_mode: parse.ConfigMode,
      entity_instances: Dict[str, EntityInstance],
  ):
    super().__init__()
    self.universe = universe
    self.config_mode = config_mode
    self.entity_instances = entity_instances

  def Validate(self, entity: EntityInstance, is_udmi: bool = True) -> bool:
    """Returns true if an entity follows all instance and graph rules.

    Args:
      entity: EntityInstance object to be validated against the ontology for
        content and connectivity.
      is_udmi: Indicate validation process under udmi specification; bool
        default True.
    """

    iv = InstanceValidator(self.universe, self.config_mode)
    gv = GraphValidator(self.universe, self.config_mode, self.entity_instances)
    # This will not return Combination validations if instance validations fail
    return iv.Validate(entity, is_udmi) and gv.Validate(entity)


class GraphValidator(object):
  """Class to support validation of inter-entity rules in config.

  This class assumes any rules that could have been validated internally on an
  entity have already passed validation.

  Note, Actions requiring the ontology fail True if the ontology is not present.

  Attributes:
    universe: ConfigUniverse to validate against
    config_mode: defines how to approach validation (INITIALIZE = complete or
      UPDATE = partial)
    entity_instances: name to entity mapping of all entities in the config
  """

  def __init__(
      self,
      universe: pvt.ConfigUniverse,
      config_mode: parse.ConfigMode,
      entity_instances: Dict[str, EntityInstance],
  ):
    super().__init__()
    self.universe = universe
    self.config_mode = config_mode
    self.entity_instances = entity_instances

  def _ConnectionsAreValid(self, entity: EntityInstance) -> bool:
    """Returns true if an entity's connections are complete."""
    if not entity.connections:
      return True

    is_valid = True
    for conn_inst in entity.connections:
      if conn_inst.source not in self.entity_instances:
        if self.config_mode in (_CONFIG_INIT, _CONFIG_UPDATE):
          print(
              f'[ERROR]\tEntity {entity.guid} ({entity.code}) is connected '
              f"to an entity that doesn't exist: {conn_inst.source}. Check "
              'that this entity is defined.'
          )
          is_valid = False
        continue
      if (
          self.entity_instances[conn_inst.source].operation
          == parse.EntityOperation.DELETE
      ):
        print(
            f'[ERROR]\tEntity {entity.guid} ({entity.code}) is connected to '
            f'a deleted entity: {conn_inst.source}.'
        )
        is_valid = False
    return is_valid

  def _LinksAreValid(self, entity: EntityInstance) -> bool:
    """Returns true if an entity's links are complete."""

    if entity.links is None:
      return True
    is_valid = True

    for link_inst in entity.links:
      if link_inst.source not in self.entity_instances.keys():
        print(
            f'[ERROR]\tEntity {entity.guid} ({entity.code}) links to an '
            f'invalid source: {link_inst.source}. Check that this source '
            'exists.'
        )
        is_valid = False
        continue
      # check that source entity contains target translation
      if self.config_mode != _CONFIG_UPDATE:
        source_entity = self.entity_instances[link_inst.source]
        for source_field_name in link_inst.field_map.values():
          if source_field_name not in source_entity.translation.keys():
            print(
                f'[ERROR]\tEntity {entity.guid} ({entity.code}) links to a'
                f' source entity: {source_entity.guid} ({source_entity.code})'
                ' that does not have the linked source field: '
                f'{source_field_name}. Check that this field on source'
                ' translation exists.'
            )
            is_valid = False
            continue
      elif (
          self.entity_instances[link_inst.source].operation
          == parse.EntityOperation.DELETE
      ):
        print(
            f'[ERROR]\tEntity {entity.guid} ({entity.code}) links to a '
            f'deleted entity: {link_inst.source}.'
        )
        is_valid = False
        continue

      src_entity = self.entity_instances.get(link_inst.source)
      src_entity_type = self.universe.GetEntityType(
          src_entity.namespace, src_entity.type_name
      )

      for _, source_field in link_inst.field_map.items():
        if not _FieldIsAllowed(self.universe, source_field, src_entity_type):
          print(
              f'[ERROR]\tEntity {entity.guid} ({entity.code}) defines a '
              'link field that is not valid in the ontology: '
              f'{source_field}. Confirm this field is defined in the '
              'ontology.'
          )
          is_valid = False
          continue

    return is_valid

  def Validate(self, entity: EntityInstance) -> bool:
    """Returns true if the entity follows all instance validation rules.

    Args:
      entity: EntityInstance to validate
    """

    if entity.operation == parse.EntityOperation.DELETE:
      return True

    is_valid = True

    if not self._ConnectionsAreValid(entity):
      is_valid = False

    if not self._LinksAreValid(entity):
      is_valid = False

    return is_valid


def IsEntityIdPresent(entity: EntityInstance) -> bool:
  """Returns true if the entity has an id; note: planned deprecation."""
  return entity.entity_id is not None


class InstanceValidator(object):
  """Class to support validation of intra-entity rules in config.

  Note: Actions requiring the ontology fail True if the ontology is not present.

  Attributes:
    universe: ConfigUniverse to validate against
    config_mode: defines how to approach validation (INITIALIZE = complete or
      UPDATE = partial)
  """

  def __init__(
      self, universe: pvt.ConfigUniverse, config_mode: parse.ConfigMode
  ):
    super().__init__()
    self.universe = universe
    self.config_mode = config_mode

  def _ValidateType(self, entity: EntityInstance) -> bool:
    """Returns true if an entity's type is in the ontology.

    This method assumes the type is defined on the entity.

    Args:
      entity: EntityInstance to validate
    """

    if not self.universe:
      return True

    if self.universe.GetEntityTypeNamespace(entity.namespace) is None:
      print(
          f'[ERROR]\tEntity {entity.guid} ({entity.code}) is defined with an '
          f'invalid namespace: {entity.namespace}. Confirm the namespace is '
          'defined in the ontology.'
      )
      return False

    entity_type = self.universe.GetEntityType(
        entity.namespace, entity.type_name
    )
    if entity_type is None:
      print(
          f'[ERROR]\tEntity {entity.guid} ({entity.code}) is defined with an '
          f'invalid entity type: {entity.type_name} in namespace '
          f'{entity.namespace}. Confirm the type is defined in the ontology, '
          'and in the correct namespace.'
      )
      return False
    elif entity_type.is_abstract:
      print(
          f'[ERROR]\tEntity {entity.guid} ({entity.code}) is defined with an '
          f'abstract entity type: {entity.type_name}. Abstract types cannot '
          'be applied to individual entity instances. Define a non-abstract '
          'type that uses this abstract type and apply that to this '
          'instance.'
      )
      return False

    return True

  def _ValidateCloudDeviceId(self, entity: EntityInstance) -> bool:
    """Cloud id validation.

    Validates that:
      - If a cloud_device_id is present it conforms to the Regex Pattern
      '[0-9]{16}'
      - If a cloud_device_id is present the entity has translations defined for
        ADD, UPDATE, and EXPORT operations.
      - If the entity has translations defined then it has a cloud_device_id

    Args:
      entity: EntityInstance to validate.

    Returns:
      Returns true if cloud device id exists and conforms to regex definition.
    """
    if entity.cloud_device_id and not entity.translation:
      if entity.operation in [
          parse.EntityOperation.UPDATE,
          parse.EntityOperation.ADD,
          parse.EntityOperation.EXPORT,
      ]:
        print(
            f'[ERROR]\tEntity {entity.guid} ({entity.code}) has a'
            ' cloud_device_id but is missing a translation. Reporting devices'
            ' must have a translation when cloud_device_id is present; unless'
            ' the operation is DELETE'
        )
    elif entity.translation and not entity.cloud_device_id:
      print(
          f'[ERROR]\tEntity {entity.guid} ({entity.code}) must have a'
          ' cloud_device_id, please refer to the documentation:'
          ' https://github.com/google/digitalbuildings/blob/master/ontology/docs/building_config.md#identifiers'
      )
    elif entity.translation and not _DEVICE_NUMERIC_ID_PATTERN.fullmatch(
        entity.cloud_device_id
    ):
      print(
          f'[ERROR]\tEntity {entity.guid} ({entity.code}) invalid'
          ' cloud_device_id, please refer to the documentation:'
          ' https://github.com/google/digitalbuildings/blob/master/ontology/docs/building_config.md#identifiers'
          f' {_DEVICE_NUMERIC_ID_REGEX}'
      )
    else:
      return True
    return False

  def _IsUdmiCompliant(self, entity, ft: ft_lib.DimensionalValue) -> bool:
    """Validates that a translation field is UDMI compliant.

    Args:
      entity: entity instance this field translation belongs to.
      ft: field translation instance.

    Returns:
      true if translation field are UDMI compliant.
    """
    is_valid = True
    if not _UDMI_PRESENT_VALUE_PATTERN.fullmatch(ft.raw_field_name):
      print(
          f'[ERROR]\tEntity {entity.guid} ({entity.code}) translates '
          f'field "{ft.raw_field_name}" with a present value pattern '
          'that does not conform to the UDMI pattern.'
          f'"{_UDMI_PRESENT_VALUE_REGEX}".'
      )
      is_valid = False
    if not _UDMI_UNIT_FIELD_PATTERN.fullmatch(ft.unit_field_name):
      print(
          f'[ERROR]\tEntity {entity.guid} ({entity.code}) translates '
          f'field "{ft.unit_field_name}" with a unit field name pattern '
          'that does not conform to UDMI pattern '
          f'"{_UDMI_UNIT_FIELD_REGEX}".'
      )
      is_valid = False
    return is_valid

  def _IsAllMissingFields(self, entity: EntityInstance) -> bool:
    """Validates that not all fields are marked as PresenceMode MISSING.

    Args:
      entity: EntityInstance to validate

    Returns:
      true if all translation fields are marked missing.
    """
    # pylint: disable=use-a-generator
    if all(
        [
            translation_field.mode == ft_lib.PresenceMode.MISSING
            for translation_field in entity.translation.values()
        ]
    ):
      print(
          f'[ERROR]\tEntity {entity.guid} ({entity.code}) has all field '
          'translations marked as MISSING. This is not allowed.'
      )
      return True
    return False

  def _ValidateTranslation(
      self, entity: EntityInstance, is_udmi: bool = True
  ) -> bool:
    """Validate an entity's translation against the entity's type or ontology.

    Validates a translation block on a reporting entity with a cloud device id.
    It asserts all fields are in the defined type and all required fields of the
    type are defined. It ensures that there is at least one field not marked
    with PresenceMode as MISSING.

    Args:
      entity: EntityInstance to validate
      is_udmi: Flag to validate under udmi; default True.

    Returns:
      Returns true when the translation is valid on a reporting entity.
    """
    if entity.translation is None:
      return True

    entity_type = self.universe.GetEntityType(
        entity.namespace, entity.type_name
    )
    found_fields = {}

    # ensure that not all fields are marked as MISSING
    if self._IsAllMissingFields(entity):
      return False

    is_valid = True
    # Check that defined fields are in the type
    for as_written_field_name, ft in entity.translation.items():
      qualified_field_name = _GetAllowedField(
          self.universe, as_written_field_name, entity_type
      )
      if not qualified_field_name:
        if entity_type and not entity_type.allow_undefined_fields:
          print(
              f'[ERROR]\tEntity {entity.guid} ({entity.code}) translates '
              f'field "{as_written_field_name}" which is not defined on the '
              f'type "{entity.type_name}"'
          )
        else:
          print(
              f'[ERROR]\tEntity {entity.guid} ({entity.code}) translates '
              f'field "{as_written_field_name}" which does not exist in the '
              'ontology.'
          )
        is_valid = False
      else:
        found_fields[qualified_field_name] = ft

    # Check that unmatched type fields are optional
    if entity_type and entity.operation == parse.EntityOperation.ADD:
      type_fields = entity_type.GetAllFields()
      unmatched = set(type_fields.keys()).difference(set(found_fields.keys()))
      for unmatched_name in unmatched:
        if not type_fields[unmatched_name].optional:
          print(
              f'[ERROR]\tEntity {entity.guid} ({entity.code}) missing field '
              f'"{unmatched_name}" which is required for assigned type '
              f'"{entity.type_name}"'
          )
          is_valid = False

    # Check that MISSING translation fields are handled properly.

    # Check that translations are properly defined
    found_units = {}
    type_fields = entity_type.GetAllFields()
    for qualified_field_name, ft in found_fields.items():
      if not self._FieldTranslationIsValid(qualified_field_name, ft, entity):
        is_valid = False

      # Check if the field is defined MISSING
      if isinstance(ft, ft_lib.UndefinedField):
        # If the type is allows undefined fields, we won't know if the field
        # is required or not explicitly. Warn the user, but don't check
        # for optionality.
        if entity_type.allow_undefined_fields:
          print(
              f'[WARNING]\tEntity {entity.guid} ({entity.code}) provides '
              f'MISSING translation for field {qualified_field_name} for a '
              f'type {entity.type_name}. This feature should '
              'only be used when the gateway cannot physically send required '
              'data and the virtual entity you are creating requires it. You '
              'must provide justification for all MISSING translations and '
              'that the applied virtual entity type is correct, otherwise '
              'your building config will be rejected.'
          )
        else:
          # If the field is MISSING and REQUIRED, warn the user.
          if not type_fields[qualified_field_name].optional:
            print(
                f'[WARNING]\tEntity {entity.guid} ({entity.code}) provides '
                f'MISSING translation for field {qualified_field_name} which '
                f'is required for type {entity.type_name}. This feature '
                'should only be used when the device cannot physically send '
                'required data and it truly is an instance of the assigned '
                'type. You must provide justification for all MISSING '
                'translations and that the applied type is correct, '
                'otherwise your building config will be rejected.'
            )

          # If its MISSING and OPTIONAL, raise error. They shouldn't do this.
          # Optional fields are automatically interpreted as missing if not
          # provided explicitly.
          if type_fields[qualified_field_name].optional:
            print(
                f'[ERROR]\tEntity {entity.guid} ({entity.code}) provides '
                f'MISSING translation for field {qualified_field_name}, '
                f'which is optional on type {entity.type_name}. The use of '
                'MISSING fields is strictly reserved for required fields. '
                'Adjust the translation and remove MISSING optional fields.'
            )
            is_valid = False

      if isinstance(ft, ft_lib.DimensionalValue):
        if is_udmi:
          is_valid &= self._IsUdmiCompliant(entity, ft)

        for std_unit, raw_unit in ft.unit_mapping.items():
          if std_unit not in found_units:
            found_units[std_unit] = raw_unit
            continue
          if found_units[std_unit] != raw_unit:
            print(
                f'[ERROR]\tEntity {entity.guid} ({entity.code}) defines '
                f'multiple raw units ({raw_unit},{std_unit}) to the same '
                'measurement type. Raw units are expected to be the same '
                'across the device: e.g. "degrees_fahrenheit" should not '
                'map to "deg_f" and "fahrenheit" on the same device '
                'translation.'
            )
            is_valid = False

    return is_valid

  def _ValidateUnits(
      self,
      qualified_field_name: str,
      ft: ft_lib.FieldTranslation,
      entity: EntityInstance,
  ):
    """Returns a boolean indicating whether or not the field units are valid.

    Method assumes field has already been checked for existence in the ontology.

    Args:
      qualified_field_name: A qualified field name for the field
      ft: Subclass of `FieldTranslation` for the field of the following:
        DimensionalValue, NonDimensionalValue
      entity: Instance of EntityInstance class

    Returns:
      true if units are valid or if units aren't required for the field
    """
    valid_units = self.universe.GetUnitsForMeasurement(qualified_field_name)
    if valid_units and set(valid_units).difference({'no_units'}):
      if not isinstance(ft, ft_lib.DimensionalValue):
        print(
            f'[ERROR]\tEntity {entity.guid} ({entity.code}) defines field '
            f'{qualified_field_name} but does not define valid units. '
            'Add units.'
        )
        return False

      if not ft.unit_mapping:
        print(
            'At least one unit must be provided for dimensional value '
            f'{qualified_field_name}'
        )
        return False

      unit = list(ft.unit_mapping.keys())[0]
      if unit not in valid_units:
        print(
            f'Field {qualified_field_name} has an undefined measurement unit:'
            + f' {unit}'
        )
        return False
      return True

    if isinstance(ft, ft_lib.DimensionalValue):
      if set(ft.unit_mapping) == {'no_units'}:
        return True
      print(
          'Units are provided for dimensional value'
          f' {qualified_field_name} that is defined to have "no_units" in the'
          ' ontology'
      )
      return False

    if isinstance(ft, ft_lib.NonDimensionalValue):
      return True

    return False

  def _ValidateStates(
      self,
      qualified_field_name: str,
      ft: ft_lib.FieldTranslation,
      entity: EntityInstance,
  ):
    """Returns a boolean indicating whether or not the field states are valid.

    Method assumes field has already been checked for existence in the ontology.

    Args:
      qualified_field_name: A qualified field name for the field
      ft: Subclass of `FieldTranslation` for the field of the following:
        MultiStateValue, NonDimensional
      entity: Instance of EntityInstance class

    Returns:
      true if the states are valid or if states aren't required for the field
    """
    valid_states = self.universe.GetStatesByField(qualified_field_name)
    if valid_states:
      if not isinstance(ft, ft_lib.MultiStateValue):
        print(
            f'[ERROR]\tEntity {entity.guid} ({entity.code}) defines field '
            f'{qualified_field_name} without states, which are expected on '
            'the field. Define states.'
        )
        return False

      is_valid = True
      for state, value in ft.states.items():
        if state not in valid_states:
          print(
              f'[ERROR]\tEntity {entity.guid} ({entity.code}) defines '
              f'field {qualified_field_name} with an invalid state: '
              f'{state}. Allowed states are ({str(valid_states)}).'
          )
          is_valid = False
        raw_values = value if isinstance(value, list) else [value]
        for raw_value in raw_values:
          if ft.raw_values[raw_value] != state:
            print(
                f'[ERROR]\tEntity {entity.guid} ({entity.code}) defines '
                f'field {qualified_field_name} has raw value {raw_value} '
                f'mapped to more than one state: {state} and '
                f'{ft.raw_values[raw_value]}'
            )
            is_valid = False

      return is_valid

    if isinstance(ft, ft_lib.MultiStateValue):
      print(
          f'[ERROR]\tEntity {entity.guid} ({entity.code}) defines field '
          f'{qualified_field_name} with states, but this field is not '
          'multi-state.'
      )
      return False

    if isinstance(ft, ft_lib.NonDimensionalValue):
      return True

    return False

  def _FieldTranslationIsValid(
      self,
      qualified_field_name: str,
      ft: ft_lib.FieldTranslation,
      entity: EntityInstance,
  ):
    """Returns a boolean indicating whether or not the field is valid.

    Method assumes field has already been checked for existence in the ontology.
    A field {@code FieldTranslation} is an instance of: {@code UndefinedField},
    {@code DimensionalValue}, {@code NonDimensionalValue}, or {@code
    MultistateValue}.

    Args:
      qualified_field_name: A qualified field name for the field
      ft: a `FieldTranslation` sublcass, for the field, of the following:
        UndefinedField, DimensionalValue, NonDimensionalValue, MultiStateValue.
      entity: Instance of EntityInstance class
    """
    if isinstance(ft, ft_lib.UndefinedField):
      return True

    if isinstance(ft, ft_lib.DimensionalValue):
      return self._ValidateUnits(qualified_field_name, ft, entity)

    if isinstance(ft, ft_lib.MultiStateValue):
      return self._ValidateStates(qualified_field_name, ft, entity)

    # field is instantiated as NonDimensionValue at parse time if neither units
    # or states are defined (for the field) on the entity in the building config.
    # it is necessary to validate both units and state here according to the
    # ontology.
    if isinstance(ft, ft_lib.NonDimensionalValue):
      return self._ValidateUnits(
          qualified_field_name, ft, entity
      ) and self._ValidateStates(qualified_field_name, ft, entity)

    return False

  def _ConnectionsAreValid(self, entity: EntityInstance) -> bool:
    """Validate's an entity's connections against the ontology universe.

    Checks both fields and connection type against the ontology.

    Args:
      entity: EntityInstance to validate

    Returns:
      Returns True if connection passes all checks or do not exist.
    """

    if not (self.universe.connection_universe and entity.connections):
      return True

    is_valid = True

    for conn_inst in entity.connections:
      conn_universe = self.universe.connection_universe
      if conn_universe and not conn_universe.IsDefined(conn_inst.ctype):
        print(
            f'[ERROR]\tEntity {entity.guid} ({entity.code}) defines '
            f'connection {conn_inst.ctype}, which does not exist in the '
            'ontology.'
        )
        is_valid = False

    return is_valid

  def _LinksAreValid(self, entity: EntityInstance) -> bool:
    """Validates an entity's links against the ontology universe.

    Logic checks the existence of both fields in the contology, additionally
    checking source against the type if the type is defined.

    Args:
      entity: EntityInstance to validate

    Returns:
      Returns true if fields in all links exist in ontology and relevant types.
    """

    if entity.links is None:
      return True

    entity_type = self.universe.GetEntityType(
        entity.namespace, entity.type_name
    )
    if entity_type and entity_type.allow_undefined_fields and entity.links:
      print(
          f'[ERROR]\tEntity {entity.guid} ({entity.code}) is not allowed to '
          'be the target of links because it is defined as a passthrough '
          'entity.'
      )
      return False

    is_valid = True
    found_fields = set()
    for link_inst in entity.links:
      for target_field, source_field in link_inst.field_map.items():
        qualified_tgt_field = _GetAllowedField(
            self.universe, target_field, entity_type
        )
        if not qualified_tgt_field:
          print(
              f'[ERROR]\tEntity {entity.guid} ({entity.code}) links to '
              f'target field {target_field} that is invalid for '
              f'link: {link_inst}'
          )
          is_valid = False
          continue
        qualified_src_field = _GetAllowedField(
            self.universe, source_field, None
        )
        if not qualified_src_field:
          print(
              f'[ERROR]\tEntity {entity.guid} ({entity.code}) links to '
              f'source field {source_field} that is invalid for '
              f'link: {link_inst}'
          )
          is_valid = False
          continue

        found_fields.add(qualified_tgt_field)

        if not self._LinkUnitsMatch(
            qualified_src_field, qualified_tgt_field, entity
        ):
          is_valid = False
          continue

        if not self._LinkStatesMatch(
            qualified_src_field, qualified_tgt_field, entity
        ):
          is_valid = False
          continue

    if entity_type:
      for field_name, field in entity_type.GetAllFields().items():
        if not field.optional and field_name not in found_fields:
          print(f'Required field {field_name} is missing from links')
          is_valid = False

    return is_valid

  def _LinkUnitsMatch(
      self, source_field: str, target_field: str, entity: EntityInstance
  ) -> bool:
    """Validates that units match between linked source and target fields."""

    source_units = self.universe.GetUnitsForMeasurement(source_field)
    target_units = self.universe.GetUnitsForMeasurement(target_field)
    if source_units != target_units:
      print(
          f'[ERROR]\tEntity {entity.guid} ({entity.code}) links target field '
          f'{target_field} to source field {source_field} but the units '
          'do not match between the fields.'
      )
      return False
    return True

  def _LinkStatesMatch(
      self, source_field: str, target_field: str, entity: EntityInstance
  ) -> bool:
    """Validates that states match between linked source and target fields."""

    source_states = self.universe.GetStatesByField(source_field)
    target_states = self.universe.GetStatesByField(target_field)
    if source_states != target_states:
      print(
          f'[ERROR]\tEntity {entity.guid} ({entity.code}) links target field '
          f'{target_field} to source field {source_field} but the states do '
          'not match between the fields.'
      )
      return False
    return True

  def _IsFaciltitiesEntitiesMatchPattern(self, entity: EntityInstance) -> bool:
    """Returns True if facilitities entities match regex patterns."""
    if entity.type_name == _BUILDING_TYPE_NAME:
      if not re.compile(BUILDING_CODE_REGEX).fullmatch(entity.code):
        print(
            f'Building code {entity.code} ({entity.guid}) does not match regex'
            f' pattern {BUILDING_CODE_REGEX}'
        )
        return False
    elif entity.type_name == _FLOOR_TYPE_NAME:
      if not re.compile(FLOOR_CODE_REGEX).fullmatch(entity.code):
        print(
            f'Floor code {entity.code} ({entity.guid}) does not match regex'
            f' pattern {FLOOR_CODE_REGEX}'
        )
        return False
    elif entity.type_name == _ROOM_TYPE_NAME:
      if not re.compile(ROOM_CODE_REGEX).fullmatch(entity.code):
        print(
            f'Room code {entity.code} ({entity.guid}) does not match regex'
            f' pattern {ROOM_CODE_REGEX}'
        )
        return False
    elif entity.namespace == _FACILITIES_NAMESPACE:
      if not re.compile(FACILITIES_ENTITY_CODE_REGEX).match(entity.code):
        print(
            f'Facilities entity with code {entity.code} ({entity.guid}) does'
            f' not match regex pattern {FACILITIES_ENTITY_CODE_REGEX}'
        )
        return False
    return True

  def _EntityOperationAndConfigModeValid(self, entity: EntityInstance) -> bool:
    """Validates the entity operation and config mode against DBO standards.

    The DBO standards allow for a building configuration file to contain a
    ConfigMode of either INITIALIZE or UPDATE. The entites continued within the
    building configuration are each allowed to have operations of either ADD,
    EXPORT, DELETE, or UPDATE. This method validates that the operations
    specified for the entities, in the building configuration, are in alignment
    with the building configuration ConfigMode and that that the entity(s)
    definition is correct for the operation specified. Please see
    https://github.com/google/digitalbuildings/blob/master/ontology/docs/building_config.md#building-configuration-modes

    Args:
      entity: EntityInstance to validate

    Returns:
      True if the entity is valid
    """
    if (
        self.config_mode == _CONFIG_INIT
        and entity.operation != parse.EntityOperation.ADD
    ):
      print(
          f'[ERROR]\tEntity {entity.guid} ({entity.code}) defines operation '
          f'{entity.operation} that is not valid. Only ADD operation is '
          'allowed in INITIALIZE mode.'
      )
      return False

    is_valid = True
    if entity.update_mask is not None:
      if entity.operation != parse.EntityOperation.UPDATE:
        print(
            f'[ERROR]\tEntity {entity.guid} ({entity.code}) requires update '
            'mask for update operations.'
        )
        is_valid = False
      if entity.type_name is None:
        if parse.ENTITY_TYPE_KEY in entity.update_mask:
          print(
              f'[ERROR]\tEntity {entity.guid} ({entity.code}) must define a '
              'clear Entity Type if performing an update.'
          )
          is_valid = False
      if parse.ENTITY_CLOUD_DEVICE_ID_KEY in entity.update_mask:
        print('Update to Cloud Device ID not allowed')
        is_valid = False

    if not entity.code and entity.operation != parse.EntityOperation.DELETE:
      print(
          f'[ERROR]\tEntity {entity.guid} is missing a code. This must be '
          'provided.'
      )
      is_valid = False

    if (
        self.config_mode in (_CONFIG_EXPORT, _CONFIG_UPDATE)
        and not entity.etag
        and entity.operation != parse.EntityOperation.ADD
    ):
      print(
          f'[ERROR]\tEntity {entity.guid} ({entity.code}) is missing an '
          'etag, which is required for EXPORT or UPDATE operations.'
      )
      is_valid = False

    if entity.namespace is None:
      if entity.operation == parse.EntityOperation.ADD:
        print(
            f'[ERROR]\tEntity {entity.guid} ({entity.code}) is missing a '
            'namespace for its type.'
        )
        is_valid = False

    if entity.type_name is None:
      if entity.operation == parse.EntityOperation.ADD:
        print(
            f'[ERROR]\tEntity {entity.guid} ({entity.code}) is missing a '
            'type definition.'
        )
        is_valid = False
    else:
      if not self._ValidateType(entity):
        is_valid = False

    return is_valid

  def Validate(self, entity: EntityInstance, is_udmi: bool = True) -> bool:
    """Uses the generated ontology universe to validate an entity.

    Args:
      entity: EntityInstance to validate
      is_udmi: flag to validate under udmi; default True.

    Returns:
      True if the entity is valid
    """

    if IsEntityIdPresent(entity):
      print(
          f'[WARNING]\tEntity {entity.guid} ({entity.code}) defines "id" but '
          'this will be deprecated in future releases. Please review '
          'https://github.com/google/digitalbuildings/'
          'ontology/docs/building_config.md for more '
          'information.'
      )

    is_valid = True
    if not entity.guid:
      print(
          f'[ERROR]\tEntity ({entity.code}) is missing a GUID. This must be '
          'provided.'
      )
      is_valid = False

    entity_type = self.universe.GetEntityType(
      entity.namespace, entity.type_name
    )
    if entity_type:
      if entity_type.GetAllFields():
        if not entity.translation and not entity.links:
          print(f'[ERROR]\tEntity ({entity.guid}: {entity.code}) Has a type '
                'which has defined fields but this instance has neither links '
                'nor a translation.')
          is_valid = False

    if not self._EntityOperationAndConfigModeValid(entity):
      is_valid = False

    if not self._ValidateTranslation(entity, is_udmi):
      is_valid = False

    if not self._ConnectionsAreValid(entity):
      is_valid = False

    if not self._LinksAreValid(entity):
      is_valid = False

    if not self._ValidateCloudDeviceId(entity):
      is_valid = False

    if not self._IsFaciltitiesEntitiesMatchPattern(entity):
      is_valid = False

    return is_valid


def _ParseTypeString(type_str: syaml.YAML) -> Tuple[str, str]:
  """Parses an entity type string into a namespace and type name.

  Args:
    type_str: entity type string from YAML

  Returns:
    Type namespace string
    Type name string
  """

  type_parse = type_str.split('/')

  if len(type_parse) == 1:
    raise TypeError(
        f'Namespace is malformed for type: {type_str}. Proper '
        'format is NAMESPACE/TYPE_NAME.'
    )

  if len(type_parse) > 2:
    raise TypeError(
        f'Type is improperly formatted: {type_str}. Proper '
        'formatting is: NAMESPACE/TYPE_NAME'
    )

  return type_parse[0], type_parse[1]


def _ParseTranslation(
    translation_body: syaml.YAML,
) -> Dict[str, ft_lib.FieldTranslation]:
  """Parses YAML defining the translation of an entity's points.

  see:
  https://github.com/google/digitalbuildings/blob/master/ontology/docs/building_config.md#defining-translations

  Args:
    translation_body: YAML body for the entity translation

  Returns:
    A dictionary from field names to FieldTranslation instances
  """

  if isinstance(translation_body, str):
    raise ValueError(f'Translation body "{translation_body}" is not valid.')

  translation = {}
  for std_field_name, ft in translation_body.items():
    if isinstance(ft, str):
      if not ft:
        raise ValueError(
            f'Translation details are empty for field: {std_field_name}.'
        )
      elif ft == ft_lib.PresenceMode.MISSING.value:
        translation[std_field_name] = ft_lib.UndefinedField(std_field_name)
        continue
      # TODO(b/187757180): support UDMI-compliant shorthand
      raise ValueError(f'This is not an allowed scalar: {ft}.')

    raw_field_name = str(ft[parse.PRESENT_VALUE_KEY])
    ft_object = _ParseUnitsAndValueRange(ft, std_field_name, raw_field_name)

    if parse.STATES_KEY in ft:
      if ft_object:
        raise ValueError(
            'States and units are not allowed in the same field translation.'
        )
      for value in ft[parse.STATES_KEY].values():
        if not value or value is None:
          raise ValueError(
              'States must have defined string key and value pairs'
          )
      ft_object = ft_lib.MultiStateValue(
          std_field_name, raw_field_name, ft[parse.STATES_KEY]
      )

    if not ft_object:
      ft_object = ft_lib.NonDimensionalValue(std_field_name, raw_field_name)

    translation[std_field_name] = ft_object

  return translation


def _ParseUnitsAndValueRange(
    ft: Dict[str, Any], std_field_name: str, raw_field_name: str
) -> ft_lib.DimensionalValue:
  """Parses the value range and units (if any) from a field translation.

  see:
  https://github.com/google/digitalbuildings/blob/master/ontology/docs/building_config.md#defining-translations

  Args:
    ft: YAML body for the entity translation for a particular field
    std_field_name: The standard field name to which the translation belongs
    raw_field_name: The raw field name for the field

  Returns:
    A DimensionalValue object or None
  """

  if parse.UNITS_KEY in ft:
    unit_field_name = ft[parse.UNITS_KEY][parse.UNIT_NAME_KEY]
    unit_mapping = ft[parse.UNITS_KEY][parse.UNIT_VALUES_KEY]
    if len(unit_mapping) != 1:
      raise ValueError(
          'There should be exactly 1 unit mapping in the translation for '
          + f'field "{std_field_name}".'
      )
    if parse.VALUE_RANGE_KEY in ft:
      value_range = str(ft[parse.VALUE_RANGE_KEY])
      range_values = value_range.split(',')
      if len(range_values) != 2:
        raise ValueError(
            f'Value range in the translation for field "{std_field_name}" '
            + 'should be formatted: <min>,<max>.'
        )
      min_value = float(range_values[0].strip())
      max_value = float(range_values[1].strip())
      if min_value >= max_value:
        raise ValueError(
            f'Value range in the translation for field "{std_field_name}" '
            + 'should have a min value that is less than the max value.'
        )
      # pylint: disable=too-many-function-args
      return ft_lib.DimensionalValue(
          std_field_name,
          raw_field_name,
          unit_field_name,
          unit_mapping,
          (min_value, max_value),
      )
    return ft_lib.DimensionalValue(
        std_field_name, raw_field_name, unit_field_name, unit_mapping
    )
  elif parse.VALUE_RANGE_KEY in ft:
    raise ValueError(
        'A value range cannot be provided without units in the translation '
        + f'for field "{std_field_name}".'
    )
  return None


def _ParseConnections(
    connections_body: List[Tuple[str, Any]]
) -> Set[connection.Connection]:
  """Parses YAML defining connections between one entity and another.

  Entites are identified by GUID.

  Connections are always defined on the target entity.

  Args:
    connections_body: YAML body for the entity connections

  Returns:
    A set of Connection instances
  """

  connections = set()

  for source_entity_guid, item_body in connections_body:
    if isinstance(item_body, str):
      connections.add(connection.Connection(item_body, source_entity_guid))
    else:
      for connection_type in item_body:
        connections.add(
            connection.Connection(connection_type, source_entity_guid)
        )

  return connections


def _ParseLinks(links_body: List[Tuple[str, Any]]) -> Set[link.Link]:
  """Parses YAML defining links between the fields of one entity and another.

  Entities are identified by GUID.

  Links are always defined on the target entity.

  Args:
    links_body: list of tuples with the source entity GUID and field map.

  Returns:
    A set of Link instances
  """

  links = set()

  for source_entity_guid, field_map in links_body:
    links.add(link.Link(source_entity_guid, field_map))

  return links


def _ParseOperationAndUpdateMask(
    entity_yaml: Dict[str, Any], default_operation: parse.EntityOperation
) -> Tuple[parse.EntityOperation, List[str]]:
  """Helper method to parse the entity operation and update_mask (if present).

  Args:
    entity_yaml: yaml document containing entity data.
    default_operation: a parse.EntityOpertion of ADD, EXPORT, DELETE, or UPDATE

  Returns:
    operation: entity operation - ADD, EXPORT, DELETE, UPDATE
    update_mask: list of entity attributes to modify if operation is UPDATE

  Raises:
    ValueError: if update_mask is present with any operation other than UPDATE
  """

  update_mask = None
  # prepare flags
  mask_present = parse.UPDATE_MASK_KEY in entity_yaml
  operation_present = parse.ENTITY_OPERATION_KEY in entity_yaml

  # case 1: need to check that the mask and operation match
  if mask_present and operation_present:
    # validate that operation is UPDATE if update_mask is present
    if (
        parse.EntityOperation.FromString(
            entity_yaml[parse.ENTITY_OPERATION_KEY]
        )
        != parse.EntityOperation.UPDATE
    ):
      raise ValueError(
          'Only specify UPDATE operation when "update_mask" is present.'
      )
    update_mask = entity_yaml[parse.UPDATE_MASK_KEY]
    operation = parse.EntityOperation.UPDATE
  # case 2: update_mask implies update operation
  elif mask_present:
    update_mask = entity_yaml[parse.UPDATE_MASK_KEY]
    operation = parse.EntityOperation.UPDATE
  # case 3: no update_mask; check yaml block if operation is specified
  elif operation_present:
    operation = parse.EntityOperation.FromString(
        entity_yaml[parse.ENTITY_OPERATION_KEY]
    )
  # case 4: no update_mask or operation in entity block; default to ConfigMode
  # GetDefaultOperation
  else:
    operation = default_operation

  return operation, update_mask


# TODO(nkilmer): move parsing and validation logic in this class into subclasses
# TODO(berkoben): Change name to Entity
# TODO(berkoben): Extract operation and etag to a wrapper class
class EntityInstance(findings_lib.Findings):
  """Class representing an instance of an entity.

  Attributes:
    operation: EntityOperation to be performed on the entity
    id: deprecated, corresponds to an internal primary key for an entity
    guid: globally unique identifier string for the entity
    code: human-friendly name string for the entity
    cloud_device_id: the numeric cloud device id found in Cloud IoT
    namespace: string for entity type's namespace
    type_name: string referring to the entity's type,
    translation: dict mapping from standard fields as specified in the config
      file to FieldTranslations,
    connections: set of Connections,
    links: Set of links
    etag: opaque string representing the revision this entity is based on
    update_mask: list of dot delimited paths to update (to clear them)
  """

  def __init__(
      self,
      operation,
      guid,
      code,
      cloud_device_id=None,
      namespace=None,
      type_name=None,
      translation=None,
      connections=None,
      links=None,
      etag=None,
      entity_id=None,
      update_mask=None,
  ):
    super().__init__()

    self.operation = operation
    self.guid = guid
    self.code = code
    self.cloud_device_id = cloud_device_id
    self.namespace = namespace
    self.type_name = type_name
    self.translation = translation
    self.connections = connections
    self.links = links
    self.etag = etag
    self.entity_id = entity_id
    self.update_mask = update_mask

  def __eq__(self, other):
    return (
        self.guid == other.guid
        and self.code == other.code
        and self.cloud_device_id == other.cloud_device_id
        and self.operation == other.operation
        and self.etag == other.etag
        and self.entity_id == other.entity_id
        and self.update_mask == other.update_mask
        and self.namespace == other.namespace
        and self.type_name == other.type_name
    )

  def __hash__(self):
    return hash((
        self.guid,
        self.code,
        self.cloud_device_id,
        self.operation,
        self.etag,
        self.entity_id,
        self.update_mask,
        self.namespace,
        self.type_name,
    ))

  @classmethod
  def FromYaml(
      cls,
      entity_key: str,
      entity_yaml: Dict[str, Any],
      default_operation: parse.EntityOperation,
  ) -> EntityInstance:
    """Class method to instantiate an Entity Instance from yaml.

    Args:
      entity_key: yaml mapping key (code or GUID) for entity_yaml.
      entity_yaml: yaml document containing entity data.
      default_operation: entity operation - ADD or EXPORT.

    Returns:
      An instance of EntityInstance class.

    Raises:
      ValueError: if an invalid combination of "code" and "guid" are in
        entity_yaml.
    """
    operation, update_mask = _ParseOperationAndUpdateMask(
        entity_yaml, default_operation
    )

    # we require that entities be keyed by guid
    if (
        parse.ENTITY_CODE_KEY in entity_yaml
        and parse.ENTITY_GUID_KEY in entity_yaml
    ):
      raise ValueError('Entity block cannot contain both "code" and "guid".')
    elif parse.ENTITY_CODE_KEY in entity_yaml:
      code = entity_yaml[parse.ENTITY_CODE_KEY]
      guid = entity_key
    elif parse.ENTITY_GUID_KEY in entity_yaml:
      # here we use the presence of ENTITY_GUID_KEY in the entity attributes as
      # as proxy that the block is keyed by code
      raise ValueError('Entity block must be keyed by a guid. Please adjust.')
    else:
      raise ValueError(
          'Keys "code" and "guid" missing from entity block. '
          'Fix this by adding one of these keys to the entity '
          'definition.'
      )

    if operation in [parse.EntityOperation.ADD, parse.EntityOperation.UPDATE]:
      if not guid:
        raise ValueError(
            'Entity block must contain "guid" for ADD/UPDATE operations.'
        )

    namespace, type_name = None, None
    if parse.ENTITY_TYPE_KEY in entity_yaml:
      namespace, type_name = _ParseTypeString(
          entity_yaml[parse.ENTITY_TYPE_KEY]
      )

    # introduce translations requirement for updating cloud_device_id; necessary
    # to use telemetry validator for cloud_device_id validation
    if update_mask:
      if (
          parse.ENTITY_CLOUD_DEVICE_ID_KEY in entity_yaml[parse.UPDATE_MASK_KEY]
          and parse.TRANSLATION_KEY not in entity_yaml
      ):
        raise ValueError('Update of cloud device id requires translation.')

    translation = None
    cloud_device_id = entity_yaml.get(parse.ENTITY_CLOUD_DEVICE_ID_KEY)
    if parse.TRANSLATION_KEY in entity_yaml:
      translation = _ParseTranslation(entity_yaml[parse.TRANSLATION_KEY])

    connections = None
    if parse.CONNECTIONS_KEY in entity_yaml:
      connections_body = entity_yaml[parse.CONNECTIONS_KEY].items()
      connections = _ParseConnections(connections_body)

    links = None
    if parse.LINKS_KEY in entity_yaml:
      links_body = entity_yaml[parse.LINKS_KEY].items()
      links = _ParseLinks(links_body)

    etag = None
    if parse.ETAG_KEY in entity_yaml:
      etag = entity_yaml[parse.ETAG_KEY]

    # deprecated; kept for legacy reasons
    entity_id = None
    if parse.ENTITY_ID_KEY in entity_yaml:
      entity_id = entity_yaml[parse.ENTITY_ID_KEY]

    return cls(
        operation,
        guid=guid,
        code=code,
        cloud_device_id=cloud_device_id,
        namespace=namespace,
        type_name=type_name,
        translation=translation,
        connections=connections,
        links=links,
        etag=etag,
        entity_id=entity_id,
        update_mask=update_mask,
    )
