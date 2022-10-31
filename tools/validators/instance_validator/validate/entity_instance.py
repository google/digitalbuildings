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
"""Representations and validators for DigitalBuildings Entities."""

from __future__ import annotations
from __future__ import print_function

from typing import Any, Dict, List, Optional, Set, Tuple
import re

import strictyaml as syaml

from validate import connection
from validate import field_translation as ft_lib
from validate import instance_parser as parse
from validate import link
from yamlformat.validator import entity_type_lib
from yamlformat.validator import findings_lib
from yamlformat.validator import presubmit_validate_types_lib as pvt

# pylint: disable=consider-using-f-string

_CONFIG_UPDATE = parse.ConfigMode.UPDATE
_CONFIG_INIT = parse.ConfigMode.INITIALIZE
_CONFIG_EXPORT = parse.ConfigMode.EXPORT
# udmi present value: points.$name.present_value
# where name follows: [a-z][a-z0-9]*(_[a-z0-9]+)*
_UDMI_PRESENT_VALUE_REGEX = \
  r'^(points.)[a-z][a-z0-9]*(_[a-z0-9]+)*(.present_value)$'
_UDMI_PRESENT_VALUE_PATTERN = re.compile(_UDMI_PRESENT_VALUE_REGEX)


def _FieldIsAllowed(
    universe: pvt.ConfigUniverse,
    as_written_field_name: str,
    entity_type: Optional[entity_type_lib.EntityType] = None) -> bool:
  """Returns true if the name is plausibly correct in the provided context.

  See `_GetAllowedField_` for detail.

  Args:
    universe: the ConfigUniverse to validate against
    as_written_field_name: the field name string as written in the config
    entity_type: the EntityType of the entity the field is defined on
  """

  return _GetAllowedField(universe, as_written_field_name,
                          entity_type) is not None


def _GetAllowedField(
    universe: pvt.ConfigUniverse,
    as_written_field_name: str,
    entity_type: Optional[entity_type_lib.EntityType] = None) -> Optional[str]:
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
        as_written_field_name)
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

  def __init__(self, universe: pvt.ConfigUniverse,
               config_mode: parse.ConfigMode,
               entity_instances: Dict[str, EntityInstance]):
    super().__init__()
    self.universe = universe
    self.config_mode = config_mode
    self.entity_instances = entity_instances

  def Validate(self, entity: EntityInstance, is_udmi: bool= False) -> bool:
    """Returns true if an entity follows all instance and graph rules.

    Arguments
      entity: EntityInstance object to be validated against the ontology for
        content and connectivity.
      is_udmi: flag to indicate process of validation under udmi specification;
        bool default False.
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

  def __init__(self, universe: pvt.ConfigUniverse,
               config_mode: parse.ConfigMode,
               entity_instances: Dict[str, EntityInstance]):
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
          print('[ERROR]\tEntity {guid} ({code}) is connected to an '
                'entity that doesn\'t exist: {orphan}. Check that this '
                'entity is defined.'.format(guid=entity.guid,
                                            code=entity.code,
                                            orphan=conn_inst.source)
                )
          is_valid = False
        continue
      if self.entity_instances[
          conn_inst.source].operation == parse.EntityOperation.DELETE:
        print('[ERROR]\tEntity {guid} ({code}) is connected to a '
              'deleted entity: {delent}.'.format(guid=entity.guid,
                                                 code=entity.guid,
                                                 delent=conn_inst.source)
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
        if self.config_mode == _CONFIG_INIT or _CONFIG_UPDATE:
          print('[ERROR]\tEntity {guid} ({code}) links to an invalid '
                'source: {source}. Check that this source exists.'
                .format(
                  guid=entity.guid,
                  code=entity.code,
                  source=link_inst.source)
                )
          is_valid = False
        continue
      if self.entity_instances[
          link_inst.source].operation == parse.EntityOperation.DELETE:
        print('[ERROR]\tEntity {guid} ({code}) links to a deleted '
              'entity: {delent}.'.format(guid=entity.guid,
                                         code=entity.code,
                                         delent=link_inst.source)
              )
        is_valid = False
        continue

      src_entity = self.entity_instances.get(link_inst.source)
      src_entity_type = self.universe.GetEntityType(src_entity.namespace,
                                                    src_entity.type_name)

      for _, source_field in link_inst.field_map.items():
        if not _FieldIsAllowed(self.universe, source_field, src_entity_type):
          print('[ERROR]\tEntity {guid} ({code}) defines a link field '
                'that is not valid in the ontology: {field}. Confirm this '
                'field is defined in the ontology.'
                .format(
                  guid=entity.guid,
                  code=entity.code,
                  field=source_field)
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
  return entity.entity_id is not None


class InstanceValidator(object):
  """Class to support validation of intra-entity rules in config.

  Note: Actions requiring the ontology fail True if the ontology is not present.

  Attributes:
    universe: ConfigUniverse to validate against
    config_mode: defines how to approach validation (INITIALIZE = complete or
      UPDATE = partial)
  """

  def __init__(self, universe: pvt.ConfigUniverse,
               config_mode: parse.ConfigMode):
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
      print('[ERROR]\tEntity {guid} ({code}) is defined with an '
            'invalid namespace: {namespace}. Confirm the namespace is '
            'defined in the ontology.'.format(guid=entity.guid,
                                              code=entity.code,
                                              namespace=entity.namespace))
      return False

    entity_type = self.universe.GetEntityType(entity.namespace,
                                              entity.type_name)
    if entity_type is None:
      print('[ERROR]\tEntity {guid} ({code}) is defined with an '
            'invalid entity type: {et} in namespace {namespace}. Confirm '
            'the type is defined in the ontology, and in the correct '
            'namespace.'.format(guid=entity.guid,
                                code=entity.code,
                                et=entity.type_name,
                                namespace=entity.namespace)
            )
      return False
    elif entity_type.is_abstract:
      print('[ERROR]\tEntity {guid} ({code}) is defined with an '
            'abstract entity type: {et}. Abstract types cannot be applied to '
            'individual entity instances. Define a non-abstract type that '
            'uses this abstract type and apply that to this instance.'
            .format(
              guid=entity.guid,
              code=entity.code,
              et=entity.type_name)
            )
      return False

    return True

  def _ValidateTranslation(
    self,
    entity: EntityInstance,
    is_udmi: bool= False) -> bool:
    """Validate an entity's translation against the entity's type or ontology.

    If entity operation is ADD, this code ensures that all fields are in the
    defined type and all required fields of the type are defined.

    Args:
      entity: EntityInstance to validate
      is_udmi: flag to validate under udmi; defaults to false

    Returns:
      Returns boolean for validity of entity translation, defaults to True if
      translation is not specified.
    """
    if entity.translation is None:
      return True

    is_valid = True
    entity_type = self.universe.GetEntityType(entity.namespace,
                                              entity.type_name)
    found_fields = {}

    # Check that defined fields are in the type
    for as_written_field_name, ft in entity.translation.items():
      qualified_field_name = _GetAllowedField(self.universe,
                                              as_written_field_name,
                                              entity_type)
      if not qualified_field_name:
        if entity_type and not entity_type.allow_undefined_fields:
          print('[ERROR]\tEntity {guid} ({code}) translates field '
                '"{field}" which is not defined on the type "{et}"'
                .format(
                  guid=entity.guid,
                  code=entity.code,
                  field=as_written_field_name,
                  et=entity.type_name)
                )
        else:
          print('[ERROR]\tEntity {guid} ({code}) translates field '
                '"{field}" which does not exist in the ontology.'
                .format(
                  guid=entity.guid,
                  code=entity.code,
                  field=as_written_field_name)
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
          print('[ERROR]\tEntity {guid} ({code}) missing field '
                '"{field}" which is required for assigned type "{et}"'
                .format(
                  guid=entity.guid,
                  code=entity.code,
                  field=unmatched_name,et=entity.type_name)
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

        # If its MISSING and REQUIRED, warn the user.
        if not type_fields[qualified_field_name].optional:
          print('[WARNING]\tEntity {guid} ({code}) provides MISSING '
                'translation for field {field} which is required for type '
                '{etype}. This feature should only be '
                'used when the device cannot physically send required data and '
                'it truly is an instance of the assigned type. You must '
                'provide justification for all MISSING translations and that '
                'the applied type is correct, otherwise your building config '
                'will be rejected.'.format(guid=entity.guid,
                                           code=entity.code,
                                           field=qualified_field_name,
                                           etype=entity.type_name)
                )

        # If its MISSING and OPTIONAL, raise rror. They shouldn't do this.
        # Optional fields are automatically interpreted as missing if not
        # provided explicitly.
        if type_fields[qualified_field_name].optional:
          print('[ERROR]\tEntity {guid} ({code}) provides MISSING '
                'translation for field {field}, which is optional on '
                'type {etype}. The use of MISSING fields is strictly '
                'reserved for required fields. Adjust the '
                'translation and remove MISSING optional fields.'
                .format(guid=entity.guid,
                        code=entity.code,
                        field=qualified_field_name,
                        etype=entity.type_name)
                )
          is_valid = False
      if isinstance(ft, ft_lib.DimensionalValue):
        if is_udmi and not _UDMI_PRESENT_VALUE_PATTERN.fullmatch(
          ft.raw_field_name):
          print('[ERROR]\tEntity {guid} ({code}) translates field '
                '"{field}" with a present value pattern that does not conform '
                'to UDMI pattern "{pat}".'
                .format(guid=entity.guid,
                        code=entity.code,
                        field=ft.raw_field_name,
                        pat=_UDMI_PRESENT_VALUE_REGEX)
                )
          is_valid = False
        for std_unit, raw_unit in ft.unit_mappings.items():
          if std_unit not in found_units:
            found_units[std_unit] = raw_unit
            continue
          if found_units[std_unit] != raw_unit:
            print('[ERROR]\tEntity {guid} ({code}) defines multiple '
                  'raw units ({raw_unit},{std_unit}) to the same measurement '
                  'type. Raw units are expected to be the same across the '
                  'device: e.g. "degrees_fahrenheit" should not map to '
                  '"deg_f" and "fahrenheit" on the same device translation.'
                  .format(guid=entity.guid,
                          code=entity.code,
                          raw_unit=raw_unit,
                          std_unit=std_unit)
                  )
            is_valid = False

    return is_valid

  def _FieldTranslationIsValid(self, qualified_field_name: str,
                               ft: ft_lib.FieldTranslation,
                               entity: EntityInstance):
    """Returns a boolean indicating whether or not the translation is valid.

    Method assumes field has already been checked for existence in the ontology.

    Args:
      qualified_field_name: a qualified field name for the field
      ft: subclass of `FieldTranslation` for the field
    """
    if isinstance(ft, ft_lib.UndefinedField):
      return True

    valid_units = self.universe.GetUnitsForMeasurement(qualified_field_name)
    if valid_units and set(valid_units).difference({'no_units'}):
      if not isinstance(ft, ft_lib.DimensionalValue):
        print('[ERROR]\tEntity {guid} ({code}) defines field {field} '
              'but does not define valid units. Add units.'
              .format(guid=entity.guid,
                      code=entity.code,
                      field=qualified_field_name)
              )
        # print('Units must be provided for dimensional value '
        #       f'{qualified_field_name}')
        return False

      # Is this a duplicate of the error above?
      if not ft.unit_mappings:
        print('[ERROR]\tEntity {guid} ({code}) defines field {field} '
              'without providing at least one unit. Add at least one unit.'
              .format(guid=entity.guid,
                      code=entity.code,
                      field=qualified_field_name)
              )
        # print('At least one unit must be provided for dimensional value '
        #       f'{qualified_field_name}')
        return False

      is_valid = True
      for unit in ft.unit_mappings.keys():
        if unit not in valid_units:
          print('[ERROR]\tEntity {guid} ({code}) defines field '
                '{field} with undefined units: {unit}.'
                .format(guid=entity.guid,
                        code=entity.code,
                        field=qualified_field_name,
                        unit=unit)
                )
          is_valid = False
      return is_valid

    if isinstance(
        ft, ft_lib.DimensionalValue) and set(ft.unit_mappings) != {'no_units'}:
      print('[ERROR]\tEntity {guid} ({code}) defines {field} with '
            'units, but this is not a dimensional field. Remove units and '
            'add states.'.format(guid=entity.guid,
                                 code=entity.code,
                                 field=qualified_field_name)
            )
      return False

    valid_states = self.universe.GetStatesByField(qualified_field_name)
    if valid_states:
      if not ft.states:
        print('[ERROR]\tEntity {guid} ({code}) defines field {field} '
              'without states, which are expected for this field. Define '
              'states.'.format(guid=entity.guid,
                               code=entity.code,
                               field=qualified_field_name)
              )
        return False

      is_valid = True
      for state, value in ft.states.items():
        if state not in valid_states:
          print('[ERROR]\tEntity {guid} ({code}) defines field {field} '
            'with an invalid state: {state}. Allowed states are '
            '({valid_states}).'.format(guid=entity.guid,
                                       code=entity.code,
                                       field=qualified_field_name,
                                       state=state,
                                       valid_states=str(valid_states))
            )
          is_valid = False
        raw_values = value if isinstance(value, list) else [value]
        for raw_value in raw_values:
          if ft.raw_values[raw_value] != state:
            print('[ERROR]\tEntity {guid} ({code}) defines field '
                  '{field} has raw value {raw_value} mapped to more than '
                  'one state: {state} and {other}'
                  .format(guid=entity.guid,
                          code=entity.code,
                          field=qualified_field_name,
                          raw_value=raw_value,
                          state=state,
                          other=ft.raw_values[raw_value])
                  )
            is_valid = False

      return is_valid

    # is below check correct? shouldnt it be IF NOT INSTANCE?
    if isinstance(ft, ft_lib.MultiStateValue):
      print('[ERROR]\tEntity {guid} ({code}) defines field {field} '
            'with states, but this field is not multi-state.'
            .format(guid=entity.guid,
                    code=entity.code,
                    field=qualified_field_name)
            )
      return False

    return True

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
        print('[ERROR]\tEntity {guid} ({code}) defines connection '
              '{cnxn}, which does not exist in the ontology.'
              .format(guid=entity.guid,
                      code=entity.code,
                      cnxn=conn_inst.ctype)
              )
        is_valid = False

    return is_valid

  def _LinksAreValid(self, entity: EntityInstance) -> bool:
    """Validates an entity's links against the ontology universe.

    Logic checks the existence of both fields in the contology, additionally
    checking source againt the type if the type is defined.

    Args:
      entity: EntityInstance to validate

    Returns:
      Returns true if fields in all links exist in ontology and relevant types.
    """

    if entity.links is None:
      return True

    entity_type = self.universe.GetEntityType(entity.namespace,
                                              entity.type_name)
    if entity_type and entity_type.allow_undefined_fields and entity.links:
      print('[ERROR]\tEntity {guid} ({code}) is not allowed to be the '
            'target of links because it is defined as a passthrough entity.'
            .format(guid=entity.guid,
                    code=entity.code)
            )
      return False

    is_valid = True
    found_fields = set()
    for link_inst in entity.links:
      for target_field, source_field in link_inst.field_map.items():
        qualified_tgt_field = _GetAllowedField(self.universe, target_field,
                                               entity_type)
        if not qualified_tgt_field:
          print('[ERROR]\tEntity {guid} ({code}) links to target '
                'field {target_field} that is invalid for link: {link_inst}'
                .format(guid=entity.guid,
                        code=entity.code,
                        target_field=target_field,
                        link_inst=link_inst)
                )
          is_valid = False
          continue
        qualified_src_field = _GetAllowedField(self.universe, source_field,
                                               None)
        if not qualified_src_field:
          print('[ERROR]\tEntity {guid} ({code}) links to source field '
            '{source_field} that is invalid for link: {link_inst}'
            .format(guid=entity.guid,
                    code=entity.code,
                    source_field=source_field,
                    link_inst=link_inst)
            )
          is_valid = False
          continue

        found_fields.add(qualified_tgt_field)

        if not self._LinkUnitsMatch(qualified_src_field,
                                    qualified_tgt_field,
                                    entity):
          is_valid = False
          continue

        if not self._LinkStatesMatch(qualified_src_field,
                                     qualified_tgt_field,
                                     entity):
          is_valid = False
          continue

    if entity_type:
      for field_name, field in entity_type.GetAllFields().items():
        if not field.optional and field_name not in found_fields:
          print(f'Required field {field_name} is missing from links')
          is_valid = False

    return is_valid

  def _LinkUnitsMatch(self,
                      source_field: str,
                      target_field: str,
                      entity: EntityInstance) -> bool:
    """Validates that units match between linked source and target fields."""

    source_units = self.universe.GetUnitsForMeasurement(source_field)
    target_units = self.universe.GetUnitsForMeasurement(target_field)
    if source_units != target_units:
      print('[ERROR]\tEntity {guid} ({code}) links target field '
            '{target_field} to source field {source_field} but the units '
            'do not match between the fields.'
            .format(guid=entity.guid,
                    code=entity.code,
                    target_field=target_field,
                    source_field=source_field)
            )
      return False
    return True

  def _LinkStatesMatch(self,
                       source_field: str,
                       target_field: str,
                       entity: EntityInstance) -> bool:
    """Validates that states match between linked source and target fields."""

    source_states = self.universe.GetStatesByField(source_field)
    target_states = self.universe.GetStatesByField(target_field)
    if source_states != target_states:
      print('[ERROR]\tEntity {guid} ({code}) links target field '
            '{target_field} to source field {source_field} but the states do '
            'not match between the fields.'
            .format(guid=entity.guid,
                    code=entity.code,
                    target_field=target_field,
                    source_field=source_field)
            )
      return False
    return True

  def Validate(self, entity: EntityInstance, is_udmi: bool= False) -> bool:
    """Uses the generated ontology universe to validate an entity.

    Args:
      entity: EntityInstance to validate
      is_udmi: flag to validate under udmi; defaults to false

    Returns:
      True if the entity is valid
    """

    if IsEntityIdPresent(entity):
      print('[WARNING]\tEntity {guid} ({code}) defines "id" but this '
            'will be deprecated in future releases. Please review '
            'digitalbuildings/ontology/docs/building_config.md for more '
            'information.'.format(guid=entity.guid,
                                  code=entity.code)
            )

    is_valid = True

    if entity.update_mask is not None:
      if entity.operation != parse.EntityOperation.UPDATE:
        print('[ERROR]\tEntity {guid} ({code}) requires update mask '
              'for update operations.'.format(guid=entity.guid,
                                              code=entity.code)
              )
        is_valid = False
      if entity.type_name is None:
        if parse.ENTITY_TYPE_KEY in entity.update_mask:
          print('[ERROR]\tEntity {guid} ({code}) must define a clear '
                'Entity Type if performing an update.'
                .format(guid=entity.guid,
                        code=entity.code)
                )
          # What is this error? Why would we ever
          # allow an entity without a type?
          # print('Update mask to clear Entity Type not allowed')
          is_valid = False

    if not entity.guid:
      print('[ERROR]\tEntity ({code}) is missing a GUID. This must be '
            'provided.'.format(code=entity.code)
            )
      is_valid = False

    if not entity.code and entity.operation != parse.EntityOperation.DELETE:
      print('[ERROR]\tEntity {guid} is missing a code. This must be '
            'provided.'.format(guid=entity.guid)
            )
      is_valid = False

    if (self.config_mode == _CONFIG_INIT and
        entity.operation != parse.EntityOperation.ADD):
      print('[ERROR]\tEntity {guid} ({code}) defines operation '
            '{operation} that is not valid. Only ADD operation is allowed in '
            'INITIALIZE mode.'.format(guid=entity.guid,
                                      code=entity.code,
                                      operation=entity.operation)
            )
      return False

    if entity.operation == parse.EntityOperation.DELETE:
      return is_valid

    if self.config_mode in (_CONFIG_EXPORT, _CONFIG_UPDATE) and not entity.etag:
      print('[ERROR]\tEntity {guid} ({code}) is missing an etag, which '
            'is required for EXPORT or UPDATE operations.'
            .format(guid=entity.guid,
                    code=entity.code)
            )
      is_valid = False

    if entity.namespace is None:
      if entity.operation == parse.EntityOperation.ADD:
        print('[ERROR]\tEntity {guid} ({code}) is missing a namespace '
          'for its type.'.format(guid=entity.guid,
                                 code=entity.code)
          )
        is_valid = False

    if entity.type_name is None:
      if entity.operation == parse.EntityOperation.ADD:
        print('[ERROR]\tEntity {guid} ({code}) is missing a type '
              'definition.'.format(guid=entity.guid,
                                   code=entity.code)
              )
        is_valid = False

    else:
      if not self._ValidateType(entity):
        is_valid = False

    if not self._ValidateTranslation(entity, is_udmi):
      is_valid = False

    if not self._ConnectionsAreValid(entity):
      is_valid = False

    if not self._LinksAreValid(entity):
      is_valid = False

    # TODO(berkoben): ADD entity needs transl'n or links if type has fields

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
    print('[ERROR]\tNamespace is missing for type: {type_str}. Proper '
          'format is NAMESPACE/TYPE_NAME.'.format(type_str=type_str)
          )
    raise TypeError

  if len(type_parse) > 2:
    print('[ERROR]\tType is improperly formatted: {type_str}. Proper '
          'formatting is: NAMESPACE/TYPE_NAME'
          .format(type_str=type_str)
          )
    raise TypeError

  return type_parse[0], type_parse[1]


def _ParseTranslation(
    translation_body: syaml.YAML) -> Dict[str, ft_lib.FieldTranslation]:
  """Parses YAML defining the translation of an entity's points.

  see:
  https://github.com/google/digitalbuildings/blob/master/ontology/docs/building_config.md#defining-translations

  Args:
    translation_body: YAML body for the entity translation

  Returns:
    A dictionary from field names to FieldTranslation instances
  """

  if isinstance(translation_body, str):
    print('[ERROR]\tTranslation body "{tb}" is not valid.'
          .format(tb=translation_body)
          )
    raise ValueError

  translation = {}
  for std_field_name in translation_body:
    ft = translation_body[std_field_name]
    if isinstance(ft, str):
      if not ft:
        print('[ERROR]\tTranslation details are empty for field: '
              '{std_field_name}.'.format(std_field_name=std_field_name)
              )
        raise ValueError
      elif ft == ft_lib.PresenceMode.MISSING.value:
        translation[std_field_name] = ft_lib.UndefinedField(std_field_name)
        continue
      # TODO(b/187757180): support UDMI-compliant shorthand
      print('[ERROR]\tThis is not an allowed scalar: {ft}.'
            .format(ft=ft)
            )
      raise ValueError

    raw_field_name = str(ft[parse.PRESENT_VALUE_KEY])
    ft_object = None

    if parse.UNITS_KEY in ft:
      unit_field_name = ft[parse.UNITS_KEY][parse.UNIT_NAME_KEY]
      unit_mappings = ft[parse.UNITS_KEY][parse.UNIT_VALUES_KEY]
      ft_object = ft_lib.DimensionalValue(std_field_name, raw_field_name,
                                          unit_field_name, unit_mappings)

    if parse.STATES_KEY in ft:
      if ft_object:
        print('[ERROR]\tStates and units are not allowed in the same '
              'field translation.')
        raise ValueError
      ft_object = ft_lib.MultiStateValue(std_field_name, raw_field_name,
                                         ft[parse.STATES_KEY])

    if not ft_object:
      ft_object = ft_lib.NonDimensionalValue(std_field_name, raw_field_name)

    translation[std_field_name] = ft_object

  return translation


def _ParseConnections(
    connections_body: List[Tuple[str, Any]]) -> Set[connection.Connection]:
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
            connection.Connection(connection_type, source_entity_guid))

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

  def __init__(self,
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
               update_mask=None):
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

  @classmethod
  def FromYaml(
      cls,
      entity_key: str,
      entity_yaml: Dict[str, Any],
      default_operation: parse.EntityOperation
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
    update_mask = None
    # prepare flags
    mask_present = parse.UPDATE_MASK_KEY in entity_yaml
    operation_present = parse.ENTITY_OPERATION_KEY in entity_yaml

    # case 1: need to check that the mask and operation match
    if mask_present and operation_present:
      # validate that operation is UPDATE if update_mask is present
      if parse.EntityOperation.FromString(entity_yaml[
          parse.ENTITY_OPERATION_KEY]) != parse.EntityOperation.UPDATE:
        print('[ERROR]\tOnly specify UPDATE operation when '
              '"update_mask" is present.')
        raise ValueError
      update_mask = entity_yaml[parse.UPDATE_MASK_KEY]
      operation = parse.EntityOperation.UPDATE
    # case 2: update_mask implies update operation
    elif mask_present:
      update_mask = entity_yaml[parse.UPDATE_MASK_KEY]
      operation = parse.EntityOperation.UPDATE
    # case 3: no update_mask; check yaml block if operation is specified
    elif operation_present:
      operation = parse.EntityOperation.FromString(
          entity_yaml[parse.ENTITY_OPERATION_KEY])
    # case 4: no update_mask or operation in entity block; default to ConfigMode
    # GetDefaultOperation
    else:
      operation = default_operation

    # we require that entities be keyed by guid
    code = None
    guid = None
    if (parse.ENTITY_CODE_KEY in entity_yaml and
        parse.ENTITY_GUID_KEY in entity_yaml):
      print('[ERROR]\tEntity block cannot contain both "code" and "guid".')
      raise ValueError
    elif parse.ENTITY_CODE_KEY in entity_yaml:
      code = entity_yaml[parse.ENTITY_CODE_KEY]
      guid = entity_key
    elif parse.ENTITY_GUID_KEY in entity_yaml:
      # here we use the presence of ENTITY_GUID_KEY in the entity attributes as
      # as proxy that the block is keyed by code
      print('[ERROR]\tEntity block must be keyed by a guid.')
      raise ValueError
    else:
      print('[ERROR]\tEntity block must contain either "code" or "guid".')
      raise ValueError('No code or guid keys in block.')

    if operation in [parse.EntityOperation.ADD, parse.EntityOperation.UPDATE]:
      if not guid:
        print('[ERROR]\tEntity block must contain "guid" for '
              'ADD/UPDATE operations.')
        raise ValueError

    namespace, type_name = None, None
    if parse.ENTITY_TYPE_KEY in entity_yaml:
      namespace, type_name = _ParseTypeString(
          entity_yaml[parse.ENTITY_TYPE_KEY])

    # introduce translations requirement for updating cloud_device_id; necessary
    # to use telemetry validator for cloud_device_id validation
    if update_mask:
      if parse.ENTITY_CLOUD_DEVICE_ID_KEY in entity_yaml[
          parse.UPDATE_MASK_KEY] and parse.TRANSLATION_KEY not in entity_yaml:
        print('[ERROR]\tUpdate of cloud device id requires translations.')
        raise ValueError('Update of cloud device id requires translation.')

    translation = None
    cloud_device_id = None
    if parse.TRANSLATION_KEY in entity_yaml:
      translation = _ParseTranslation(entity_yaml[parse.TRANSLATION_KEY])
      cloud_device_id = entity_yaml[parse.ENTITY_CLOUD_DEVICE_ID_KEY]

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
        update_mask=update_mask)
