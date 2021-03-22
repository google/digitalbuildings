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

from __future__ import print_function

from typing import Optional, Dict, Set, Tuple

import strictyaml as syaml

from validate import connection
from validate import field_translation
from validate import instance_parser
from validate import link
from yamlformat.validator import entity_type_lib
from yamlformat.validator import findings_lib
from yamlformat.validator import presubmit_validate_types_lib as pvt

TRANSLATION_COMPLIANT = 'COMPLIANT'

ID_KEY = 'id'
TYPE_KEY = 'type'

LINKS_KEY = 'links'
TRANSLATION_KEY = 'translation'
CONNECTIONS_KEY = 'connections'
PRESENT_VALUE = 'present_value'
POINTS = 'points'
UNITS_KEY = 'units'
UNIT_VALUES_KEY = 'unit_values'
VALUES_KEY = 'values'
STATES_KEY = 'states'
OPERATION_KEY = 'operation'
UPDATE_MASK_KEY = 'update_mask'
ETAG_KEY = 'etag'


def _FieldIsAllowed(
    universe: pvt.ConfigUniverse,
    field_name: str,
    entity_type: Optional[entity_type_lib.EntityType] = None) -> bool:
  if entity_type:
    return entity_type.HasField('/' + field_name)
  return universe.field_universe.IsFieldDefined(field_name, '')


class CombinationValidator(object):
  """Combines Instance and Graph based validations into one step.

  Note: Actions requiring the ontology fail True if the ontology is not present.

  Attributes:
    universe: ConfigUniverse to validate against
    config_mode: defines how to approach validation (INITIALIZE = complete or
      UPDATE = partial)
    entity_instances: name to entity mapping of all entities in the config
  """

  def __init__(self, universe: pvt.ConfigUniverse,
               config_mode: instance_parser.ConfigMode,
               entity_instances: Dict[str, 'EntityInstance']):
    super().__init__()
    self.universe = universe
    self.config_mode = config_mode
    self.entity_instances = entity_instances

  def Validate(self, entity: 'EntityInstance') -> bool:
    """Returns true if an entity follows all instance and graph rules."""

    iv = InstanceValidator(self.universe, self.config_mode)
    gv = GraphValidator(self.universe, self.config_mode, self.entity_instances)
    # This will not return Combination validations if instance validations fail
    return iv.Validate(entity) and gv.Validate(entity)


class GraphValidator(object):
  """Class to support validation of inter-entity rules in config.

  This class assumes any rules that could have been validated internally on an
  entity have already passed validation.

  Note: Actions requiring the ontology fail True if the ontology is not present.

  Attributes:
    universe: ConfigUniverse to validate against
    config_mode: defines how to approach validation (INITIALIZE = complete or
      UPDATE = partial)
    entity_instances: name to entity mapping of all entities in the config
  """

  def __init__(self, universe: pvt.ConfigUniverse,
               config_mode: instance_parser.ConfigMode,
               entity_instances: Dict[str, 'EntityInstance']):
    super().__init__()
    self.universe = universe
    self.config_mode = config_mode
    self.entity_instances = entity_instances

  def _ConnectionsAreValid(self, entity: 'EntityInstance') -> bool:
    """Returns true if an entity's connections are complete."""
    if not entity.connections:
      return True

    is_valid = True
    for conn_inst in entity.connections:
      if conn_inst.source not in self.entity_instances:
        if self.config_mode == instance_parser.ConfigMode.INITIALIZE:
          print('Orphan connection to: {0}'.format(conn_inst.source))
          is_valid = False
        continue
      if self.entity_instances[
          conn_inst.source].operation == instance_parser.EntityOperation.DELETE:
        print('Connection to deleted entity: {0}'.format(conn_inst.source))
        is_valid = False
    return is_valid

  def _LinksAreValid(self, entity: 'EntityInstance') -> bool:
    """Returns true if an entity's links are complete."""

    if entity.links is None:
      return True
    is_valid = True

    for link_inst in entity.links:
      if link_inst.source not in self.entity_instances.keys():
        if self.config_mode == instance_parser.ConfigMode.INITIALIZE:
          print('Invalid link source entity name: {0}'.format(link_inst.source))
          is_valid = False
        continue
      if self.entity_instances[
          link_inst.source].operation == instance_parser.EntityOperation.DELETE:
        print('Link to deleted entity: {0}'.format(link_inst.source))
        is_valid = False
        continue

      src_entity = self.entity_instances.get(link_inst.source)
      src_entity_type = self.universe.GetEntityType(src_entity.namespace,
                                                    src_entity.type_name)

      for source_field, _ in link_inst.field_map.items():
        if not _FieldIsAllowed(self.universe, source_field, src_entity_type):
          print('Invalid link source field: ', source_field)
          is_valid = False
          continue

    return is_valid

  def Validate(self, entity: 'EntityInstance') -> bool:
    """Returns true if the entity follows all instance validation rules.

    Args:
      entity: EntityInstance to validate
    """

    if entity.operation == instance_parser.EntityOperation.DELETE:
      return True

    is_valid = True

    if not self._ConnectionsAreValid(entity):
      is_valid = False

    if not self._LinksAreValid(entity):
      is_valid = False

    return is_valid


class InstanceValidator(object):
  """Class to support validation of intra-entity rules in config.

  Note: Actions requiring the ontology fail True if the ontology is not present.

  Attributes:
    universe: ConfigUniverse to validate against
    config_mode: defines how to approach validation (INITIALIZE = complete or
      UPDATE = partial)
  """

  def __init__(self, universe: pvt.ConfigUniverse,
               config_mode: instance_parser.ConfigMode):
    super().__init__()
    self.universe = universe
    self.config_mode = config_mode

  def _ValidateType(self, entity: 'EntityInstance') -> bool:
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

  def _ValidateTranslation(self, entity: 'EntityInstance') -> bool:
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

    if isinstance(entity.translation, str):
      if entity.translation == TRANSLATION_COMPLIANT:
        return True
      else:
        print('Invalid translation compliance string: ', entity.translation)
        return False

    is_valid = True
    entity_type = self.universe.GetEntityType(entity.namespace,
                                              entity.type_name)
    found_fields = {}

    # Check that defined fields are in the type
    for field_name, ft in entity.translation.items():
      if not _FieldIsAllowed(self.universe, field_name, entity_type):
        if entity_type:
          print('Field {0} is not defined on the type'.format(field_name))
        else:
          print('Field {0} is undefined in the universe'.format(field_name))
        is_valid = False
      else:
        found_fields['/' + field_name] = ft

    # Check that unmatched type fields are optional
    if entity_type and entity.operation == instance_parser.EntityOperation.ADD:
      type_fields = entity_type.GetAllFields()
      unmatched = set(type_fields.keys()).difference(set(found_fields.keys()))
      for unmatched_name in unmatched:
        if not type_fields[unmatched_name].optional:
          print('Required field {0} is missing from translation'.format(
              unmatched_name))
          is_valid = False

    # Check that units are properly defined
    for field_name, ft in found_fields.items():
      valid_units = self.universe.GetUnitsMapByMeasurement(field_name)
      if valid_units:
        for unit in ft.units.keys():
          if unit not in valid_units:
            print('Field {0} has an invalid unit: {1}'.format(field_name, unit))
            is_valid = False
      else:
        valid_states = self.universe.GetStatesByField(field_name)
        if valid_states:
          for state in ft.states.keys():
            if state not in valid_states:
              print('Field {0} has an invalid state: {1}'.format(
                  field_name, state))
              is_valid = False

    return is_valid

  def _ConnectionsAreValid(self, entity: 'EntityInstance') -> bool:
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
        print('Invalid connection type: {0}'.format(conn_inst.ctype))
        is_valid = False

    return is_valid

  def _LinksAreValid(self, entity: 'EntityInstance') -> bool:
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
    is_valid = True

    entity_type = self.universe.GetEntityType(entity.namespace,
                                              entity.type_name)

    found_fields = set()
    for link_inst in entity.links:
      for source_field, target_field in link_inst.field_map.items():
        # assumes that the namespace is '' for now
        if not _FieldIsAllowed(self.universe, target_field, entity_type):
          print('Invalid link target field: ', target_field)
          is_valid = False
          continue

        if not _FieldIsAllowed(self.universe, source_field, None):
          print('Invalid link source field: ', source_field)
          is_valid = False
          continue

        found_fields.add('/' + target_field)

        if not self._LinkUnitsMatch(source_field, target_field):
          is_valid = False
          continue

        if not self._LinkStatesMatch(source_field, target_field):
          is_valid = False
          continue

    if entity_type:
      for field_name, field in entity_type.GetAllFields().items():
        if not field.optional and field_name not in found_fields:
          print('Required field {0} is missing from links'.format(field_name))
          is_valid = False

    return is_valid

  def _LinkUnitsMatch(self, source_field: str, target_field: str) -> bool:
    """Validates that units match between linked source and target fields."""

    source_units = self.universe.GetUnitsMapByMeasurement(source_field)
    target_units = self.universe.GetUnitsMapByMeasurement(target_field)
    if source_units != target_units:
      print('Unit mismatch in link from {0} to {1}'\
            .format(source_field, target_field))
      return False
    return True

  def _LinkStatesMatch(self, source_field: str, target_field: str) -> bool:
    """Validates that states match between linked source and target fields."""

    source_states = self.universe.GetStatesByField(source_field)
    target_states = self.universe.GetStatesByField(target_field)
    if source_states != target_states:
      print('State mismatch in link from {0} to {1}'.format(
          source_field, target_field))
      return False
    return True

  def Validate(self, entity: 'EntityInstance') -> bool:
    """Uses the generated ontology universe to validate an entity.

    Args:
      entity: EntityInstance to validate

    Returns:
      True if the entity is valid
    """
    is_valid = True

    # This check should never fail as syntax checks currently catch this
    if not entity.id:
      print('All entities require IDs')
      is_valid = False

    if (self.config_mode == instance_parser.ConfigMode.INITIALIZE and
        entity.operation != instance_parser.EntityOperation.ADD):
      print('only ADD operation is allowed in INITIALIZE mode')
      return False

    if entity.operation == instance_parser.EntityOperation.DELETE:
      return is_valid

    # This check should never fail as syntax checks currently catch this
    if (entity.operation == instance_parser.EntityOperation.UPDATE
        and not entity.etag):
      print('etag is required on update')
      is_valid = False

    if entity.namespace is None or entity.type_name is None:
      if entity.operation == instance_parser.EntityOperation.ADD:
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
    raise TypeError('Type improperly formatted, a namespace is missing: ',
                    type_str)

  if len(type_parse) > 2:
    print('Type improperly formatted: ', type_str)
    raise TypeError('Type improperly formatted: ', type_str)

  return type_parse[0], type_parse[1]


def _ParseTranslation(
    translation_body: syaml.YAML
) -> Dict[str, field_translation.FieldTranslation]:
  """Parses YAML defining the translation of an entity's points.

  Args:
    translation_body: YAML body for the entity translation

  Returns:
    A dictionary from field names to FieldTranslation instances
  """

  if isinstance(translation_body, str):
    return translation_body

  translation = {}
  # TODO(b/176094783): reuse the tuple from the ontology validator
  for std_field_name in translation_body.keys():
    if isinstance(translation_body[std_field_name], str):
      continue
    # TODO(b/176097512): Manually defined non UDMI translations should be
    #  accepted by the validator
    ft = translation_body[std_field_name]

    raw_field_name = str(ft[PRESENT_VALUE])\
      .replace(PRESENT_VALUE, '')\
      .replace(POINTS, '')\
      .replace('.', '')

    units = dict()
    if UNITS_KEY in ft.keys():
      units = ft[UNITS_KEY][VALUES_KEY]
    elif UNIT_VALUES_KEY in ft.keys():
      units = ft[UNIT_VALUES_KEY]

    states = dict()
    if STATES_KEY in ft.keys():
      states = ft[STATES_KEY]

    translation[std_field_name] = field_translation.FieldTranslation(
        std_field_name, raw_field_name, units, states)

  return translation


def _ParseConnections(
    connections_body: syaml.YAML) -> Set[connection.Connection]:
  """Parses YAML defining connections between one entity and other.

  Connections are always defined on the target entity.

  Args:
    connections_body: YAML body for the entity connections

  Returns:
    A set of Connection instances
  """

  connections = set()

  for source_entity, connection_type in connections_body.items():
    connections.add(connection.Connection(connection_type, source_entity))

  return connections


def _ParseLinks(links_body: syaml.YAML) -> Set[link.Link]:
  """Parses YAML defining links between the fields of one entity and another.

  Links are always defined on the target entity.

  Args:
    links_body: YAML body for the entity links

  Returns:
    A set of Link instances
  """

  links = set()

  for source_entity, field_map in links_body.items():
    links.add(link.Link(source_entity, field_map))

  return links


# TODO(nkilmer): move parsing and validation logic in this class into subclasses
# TODO(berkoben): Change name to Entity
# TODO(berkoben): Extract operation and etag to a wrapper class
# TODO(berkoben): Add name attribute
class EntityInstance(findings_lib.Findings):
  """Class representing an instance of an entity.

  Attributes:
    operation: EntityOperation to be performed on the entity
    id: unique identifier string for the entity
    namespace: string for entity type's namespace
    type_name: string referring to the entity's type,
    translation: dict mapping from standard fields to FieldTranslations,
    connections: set of Connections,
    links: Set of links
    etag: opaque string representing the revision this entity is based on
    update_mask: list of dot delimited paths to update (to clear them)
  """

  def __init__(self,
               operation,
               entity_id,
               namespace=None,
               type_name=None,
               translation=None,
               connections=None,
               links=None,
               etag=None,
               update_mask=None):
    super().__init__()

    self.operation = operation
    self.id = entity_id
    self.namespace = namespace
    self.type_name = type_name
    self.translation = translation
    self.connections = connections
    self.links = links
    self.update_mask = update_mask
    self.etag = etag

  @classmethod
  def FromYaml(
      cls,
      entity_yaml,
      default_operation: Optional[
          instance_parser.EntityOperation] = instance_parser.EntityOperation.ADD
  ):
    operation = default_operation
    if OPERATION_KEY in entity_yaml:
      operation = instance_parser.EntityOperation.FromString(
          entity_yaml[OPERATION_KEY])

    entity_id = None
    if ID_KEY in entity_yaml:
      entity_id = entity_yaml[ID_KEY]

    namespace, type_name = None, None
    if TYPE_KEY in entity_yaml:
      namespace, type_name = _ParseTypeString(entity_yaml[TYPE_KEY])

    translation = None
    if TRANSLATION_KEY in entity_yaml:
      translation = _ParseTranslation(entity_yaml[TRANSLATION_KEY])

    connections = None
    if CONNECTIONS_KEY in entity_yaml:
      connections = _ParseConnections(entity_yaml[CONNECTIONS_KEY])

    links = None
    if LINKS_KEY in entity_yaml:
      links = _ParseLinks(entity_yaml[LINKS_KEY])

    update_mask = None
    if UPDATE_MASK_KEY in entity_yaml:
      update_mask = entity_yaml[UPDATE_MASK_KEY]

    etag = None
    if ETAG_KEY in entity_yaml:
      etag = entity_yaml[ETAG_KEY]

    return cls(operation, entity_id, namespace, type_name, translation,
               connections, links, etag, update_mask)
