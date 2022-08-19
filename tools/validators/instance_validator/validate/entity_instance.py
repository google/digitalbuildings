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

import strictyaml as syaml

from validate import connection
from validate import field_translation as ft_lib
from validate import instance_parser as parse
from validate import link
from yamlformat.validator import entity_type_lib
from yamlformat.validator import findings_lib
from yamlformat.validator import presubmit_validate_types_lib as pvt

_CONFIG_UPDATE = parse.ConfigMode.UPDATE
_CONFIG_INIT = parse.ConfigMode.INITIALIZE
_CONFIG_EXPORT = parse.ConfigMode.EXPORT


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

  def Validate(self, entity: EntityInstance) -> bool:
    """Returns true if an entity follows all instance and graph rules."""

    iv = InstanceValidator(self.universe, self.config_mode)
    gv = GraphValidator(self.universe, self.config_mode, self.entity_instances)
    # This will not return Combination validations if instance validations fail
    return iv.Validate(entity) and gv.Validate(entity)


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
          print(f'Orphan connection to: {conn_inst.source}')
          is_valid = False
        continue
      if self.entity_instances[
          conn_inst.source].operation == parse.EntityOperation.DELETE:
        print(f'Connection to deleted entity: {conn_inst.source}')
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
          print(f'Invalid link source entity GUID: {link_inst.source}')
          is_valid = False
        continue
      if self.entity_instances[
          link_inst.source].operation == parse.EntityOperation.DELETE:
        print(f'Link to deleted entity: {link_inst.source}')
        is_valid = False
        continue

      src_entity = self.entity_instances.get(link_inst.source)
      src_entity_type = self.universe.GetEntityType(src_entity.namespace,
                                                    src_entity.type_name)

      for _, source_field in link_inst.field_map.items():
        if not _FieldIsAllowed(self.universe, source_field, src_entity_type):
          print(f'Invalid link source field: {source_field}')
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

    This method assues the type is defined on the entity.

    Args:
      entity: EntityInstance to validate
    """

    if not self.universe:
      return True

    if self.universe.GetEntityTypeNamespace(entity.namespace) is None:
      print('Invalid namespace: ', entity.namespace)
      return False

    entity_type = self.universe.GetEntityType(entity.namespace,
                                              entity.type_name)
    if entity_type is None:
      print('Invalid entity type: ', entity.type_name)
      return False
    elif entity_type.is_abstract:
      print('Abstract types cannot be instantiated: ', entity.type_name)
      return False

    return True

  def _ValidateTranslation(self, entity: EntityInstance) -> bool:
    """Validate an entity's translation against the entity's type or ontology.

    If entity operation is ADD, this code ensures that all fields are in the
    defined type and all required fields of the type are defined.

    Args:
      entity: EntityInstance to validate

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
          print(f'Field {as_written_field_name} is not defined on the type')
        else:
          print(f'Field {as_written_field_name} is undefined in the universe')
        is_valid = False
      else:
        found_fields[qualified_field_name] = ft

    # Check that unmatched type fields are optional
    if entity_type and entity.operation == parse.EntityOperation.ADD:
      type_fields = entity_type.GetAllFields()
      unmatched = set(type_fields.keys()).difference(set(found_fields.keys()))
      for unmatched_name in unmatched:
        if not type_fields[unmatched_name].optional:
          print(f'Required field {unmatched_name} is missing from translation')
          is_valid = False

    # Check that translations are properly defined
    found_units = {}
    for qualified_field_name, ft in found_fields.items():
      if not self._FieldTranslationIsValid(qualified_field_name, ft):
        is_valid = False
      if isinstance(ft, ft_lib.DimensionalValue):
        for std_unit, raw_unit in ft.unit_mappings.items():
          if std_unit not in found_units:
            found_units[std_unit] = raw_unit
            continue
          if found_units[std_unit] != raw_unit:
            print(f'found two mappings for {std_unit}')
            is_valid = False

    return is_valid

  def _FieldTranslationIsValid(self, qualified_field_name: str,
                               ft: ft_lib.FieldTranslation):
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
        print('Units must be provided for dimensional value '
              f'{qualified_field_name}')
        return False

      if not ft.unit_mappings:
        print('At least one unit must be provided for dimensional value '
              f'{qualified_field_name}')
        return False

      is_valid = True
      for unit in ft.unit_mappings.keys():
        if unit not in valid_units:
          print(
              f'Field {qualified_field_name} has an undefined measurement unit:'
              + f' {unit}')
          is_valid = False
      return is_valid

    if isinstance(
        ft, ft_lib.DimensionalValue) and set(ft.unit_mappings) != {'no_units'}:
      print(f'Units are provided for non-dimensional value '
            f'{qualified_field_name}')
      return False

    valid_states = self.universe.GetStatesByField(qualified_field_name)
    if valid_states:
      if not isinstance(ft, ft_lib.MultiStateValue):
        print('States not provided for multi-state value '
              f'{qualified_field_name}')
        return False

      if not ft.states:
        print('At least one state must be provided for multi-state value '
              f'{qualified_field_name}')
        return False

      is_valid = True
      for state, value in ft.states.items():
        if state not in valid_states:
          print(f'Field {qualified_field_name} has an invalid state: {state}'
                f' (expected {", ".join(valid_states)})')
          is_valid = False
        raw_values = value if isinstance(value, list) else [value]
        for raw_value in raw_values:
          if ft.raw_values[raw_value] != state:
            print(f'Field {qualified_field_name} has raw value {raw_value} '
                  f'mapped to more than one state: {state} and '
                  f'{ft.raw_values[raw_value]}')
            is_valid = False

      return is_valid

    if isinstance(ft, ft_lib.MultiStateValue):
      print('Multiple states provided for a field that is not a multi-state'
            f' {qualified_field_name}')
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
        print(f'Connection type: {conn_inst.ctype} '
              'is undefined in the ontology')
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
      print('This entity is not allowed to be the target of links because it is'
            ' an instance of a passthrough entity type.')
      return False

    is_valid = True
    found_fields = set()
    for link_inst in entity.links:
      for target_field, source_field in link_inst.field_map.items():
        qualified_tgt_field = _GetAllowedField(self.universe, target_field,
                                               entity_type)
        if not qualified_tgt_field:
          print(f'Invalid link target field: {target_field} '
                f'for link: {link_inst}')
          is_valid = False
          continue
        qualified_src_field = _GetAllowedField(self.universe, source_field,
                                               None)
        if not qualified_src_field:
          print(f'Invalid link source field: {source_field} '
                f'for link: {link_inst}')
          is_valid = False
          continue

        found_fields.add(qualified_tgt_field)

        if not self._LinkUnitsMatch(qualified_src_field, qualified_tgt_field):
          is_valid = False
          continue

        if not self._LinkStatesMatch(qualified_src_field, qualified_tgt_field):
          is_valid = False
          continue

    if entity_type:
      for field_name, field in entity_type.GetAllFields().items():
        if not field.optional and field_name not in found_fields:
          print(f'Required field {field_name} is missing from links')
          is_valid = False

    return is_valid

  def _LinkUnitsMatch(self, source_field: str, target_field: str) -> bool:
    """Validates that units match between linked source and target fields."""

    source_units = self.universe.GetUnitsForMeasurement(source_field)
    target_units = self.universe.GetUnitsForMeasurement(target_field)
    if source_units != target_units:
      print(f'Unit mismatch in link from {source_field} to {target_field}')
      return False
    return True

  def _LinkStatesMatch(self, source_field: str, target_field: str) -> bool:
    """Validates that states match between linked source and target fields."""

    source_states = self.universe.GetStatesByField(source_field)
    target_states = self.universe.GetStatesByField(target_field)
    if source_states != target_states:
      print(f'State mismatch in link from {source_field} to {target_field}')
      return False
    return True

  def Validate(self, entity: EntityInstance) -> bool:
    """Uses the generated ontology universe to validate an entity.

    Args:
      entity: EntityInstance to validate

    Returns:
      True if the entity is valid
    """

    if IsEntityIdPresent(entity):
      print('Warning: Entity id detected in block. Planned deprecation, ',
        'will result in validation error in a future releases. Please ',
        'review digitalbuildings/ontology/docs/building_config.md for ',
        'more info')

    is_valid = True

    if entity.update_mask is not None:
      if entity.operation != parse.EntityOperation.UPDATE:
        print('Update mask is required for update operations')
        is_valid = False
      if entity.type_name is None:
        if parse.ENTITY_TYPE_KEY in entity.update_mask:
          print('Update mask to clear Entity Type not allowed')
          is_valid = False

    if not entity.guid:
      print('Entity GUID is required.')
      is_valid = False

    if not entity.code and entity.operation != parse.EntityOperation.DELETE:
      print('Entity code is required.')
      is_valid = False

    if (self.config_mode == _CONFIG_INIT and
        entity.operation != parse.EntityOperation.ADD):
      print('only ADD operation is allowed in INITIALIZE mode')
      return False

    if entity.operation == parse.EntityOperation.DELETE:
      return is_valid

    if self.config_mode in (_CONFIG_EXPORT, _CONFIG_UPDATE) and not entity.etag:
      print('etag is required on update or export')
      is_valid = False

    if entity.namespace is None or entity.type_name is None:
      if entity.operation == parse.EntityOperation.ADD:
        print('Required field not specified: type')
        is_valid = False
    else:
      if not self._ValidateType(entity):
        is_valid = False

    if not self._ValidateTranslation(entity):
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
    print('Type improperly formatted, a namespace is missing: ', type_str)
    raise TypeError(
        f'Type improperly formatted, a namespace is missing: {type_str}\n' +
        'Proper formatting is: NAMESPACE/TYPE_NAME')

  if len(type_parse) > 2:
    print('Type improperly formatted: ', type_str)
    raise TypeError(f'Type improperly formatted: {type_str}\n' +
                    'Proper formatting is: NAMESPACE/TYPE_NAME')

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
    raise ValueError(translation_body + ' is not a valid translation')

  translation = {}
  for std_field_name in translation_body:
    ft = translation_body[std_field_name]
    if isinstance(ft, str):
      if not ft:
        raise ValueError(
            'Translation details were empty for standard field name: ' +
            std_field_name)
      elif ft == ft_lib.PresenceMode.MISSING.value:
        translation[std_field_name] = ft_lib.UndefinedField(std_field_name)
        continue
      # TODO(b/187757180): support UDMI-compliant shorthand
      raise ValueError(ft + ' is not yet an allowed scalar')

    raw_field_name = str(ft[parse.PRESENT_VALUE_KEY])
    ft_object = None

    if parse.UNITS_KEY in ft:
      unit_field_name = ft[parse.UNITS_KEY][parse.UNIT_NAME_KEY]
      unit_mappings = ft[parse.UNITS_KEY][parse.UNIT_VALUES_KEY]
      ft_object = ft_lib.DimensionalValue(std_field_name, raw_field_name,
                                          unit_field_name, unit_mappings)

    if parse.STATES_KEY in ft:
      if ft_object:
        raise ValueError(
            'states and units are not allowed in the same translation')
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
        raise ValueError(
            'Only specify "UPDATE" operation when "update_mask" is present.'
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
      raise ValueError('Entity block cannot contain both "code" and "guid".')
    elif parse.ENTITY_CODE_KEY in entity_yaml:
      code = entity_yaml[parse.ENTITY_CODE_KEY]
      guid = entity_key
    elif parse.ENTITY_GUID_KEY in entity_yaml:
      # here we use the presence of ENTITY_GUID_KEY in the entity attributes as
      # as proxy that the block is keyed by code
      raise ValueError('Entity block must be keyed by guid.')
    else:
      raise ValueError('Entity block must contain either "code" or "guid".')

    if operation in [parse.EntityOperation.ADD, parse.EntityOperation.UPDATE]:
      if not guid:
        raise ValueError(
            'Entity block must contain "guid" for ADD/UPDATE operations.')

    namespace, type_name = None, None
    if parse.ENTITY_TYPE_KEY in entity_yaml:
      namespace, type_name = _ParseTypeString(
          entity_yaml[parse.ENTITY_TYPE_KEY])

    # introduce translations requirement for updating cloud_device_id; necessary
    # to use telemetry validator for cloud_device_id validation
    if update_mask:
      if parse.ENTITY_CLOUD_DEVICE_ID_KEY in entity_yaml[
          parse.UPDATE_MASK_KEY] and parse.TRANSLATION_KEY not in entity_yaml:
        raise ValueError('Update of cloud device id requires translations')
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
