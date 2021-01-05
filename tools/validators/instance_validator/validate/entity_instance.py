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

"""Uses ontology universe to validate parsed instance data."""

from __future__ import print_function

from validate import connection
from validate import field_translation
from validate import link
from yamlformat.validator import findings_lib

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


# TODO(nkilmer): move parsing and validation logic in this class into subclasses
class EntityInstance(findings_lib.Findings):
  """Uses information from the generated ontology universe to validate
  an entity instance. An entity instance is composed of at least an id and a
  type. For example: {'id': 'FACILITIES/12345', 'type': 'FACILITIES/BUILDING'}.

  Args:
    entity_yaml: parsed instance YAML file formatted as dictionary
  """

  def __init__(self, entity_yaml):
    super().__init__()

    self.id = None
    if ID_KEY in entity_yaml.keys():
      self.id = entity_yaml[ID_KEY]

    self.namespace, self.type_name = None, None
    if TYPE_KEY in entity_yaml.keys():
      self.namespace, self.type_name = self._ParseTypeString(
          entity_yaml[TYPE_KEY])

    self.translation = None
    if TRANSLATION_KEY in entity_yaml.keys():
      self.translation = self._ParseTranslation(
          entity_yaml[TRANSLATION_KEY])

    self.connections = None
    if CONNECTIONS_KEY in entity_yaml.keys():
      self.connections = self._ParseConnections(
          entity_yaml[CONNECTIONS_KEY])

    self.links = None
    if LINKS_KEY in entity_yaml.keys():
      self.links = self._ParseLinks(entity_yaml[LINKS_KEY])


  def _ParseTypeString(self, type_str):
    """Parses an entity type string into a namespace and type name.

    Args:
      type_str: entity type string from YAML

    Returns:
      Type namespace string
      Type name string
    """

    type_parse = type_str.split('/')

    if len(type_parse) == 1:
      print('Type improperly formatted, a namespace is missing: '
            , type_str)
      raise TypeError('Type improperly formatted, a namespace is missing: '
                      , type_str)

    if len(type_parse) > 2:
      print('Type improperly formatted: ', type_str)
      raise TypeError('Type improperly formatted: ', type_str)

    return type_parse[0], type_parse[1]


  def _ParseTranslation(self, translation_body):
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


  def _ParseConnections(self, connections_body):
    """Parses YAML defining the connections between an entity and other
    entities, which are the sources of the connections.

    Args:
      connections_body: YAML body for the entity connections

    Returns:
      A set of Connection instances
    """

    connections = set()

    for source_entity, connection_type in connections_body.items():
      connections.add(connection.Connection(connection_type, source_entity))

    return connections


  def _ParseLinks(self, links_body):
    """Parses YAML defining the links between the fields of this entity and
    other source entities.

    Args:
      links_body: YAML body for the entity links

    Returns:
      A set of Link instances
    """

    links = set()

    for source_entity, field_map in links_body.items():
      links.add(link.Link(source_entity, field_map))

    return links


  def _ValidateType(self, universe):
    """Uses information from the generated ontology universe to validate
    an entity's type.

    Returns:
      Returns boolean for validity of entity type.
    """

    if universe.GetEntityTypeNamespace(self.namespace) is None:
      print('Invalid namespace: ', self.namespace)
      return False

    entity_type = universe.GetEntityType(self.namespace, self.type_name)
    if entity_type is None:
      print('Invalid entity type: ', self.type_name)
      return False
    elif entity_type.is_abstract:
      print('Abstract types cannot be instantiated: ', self.type_name)
      return False

    return True


  def _ValidateTranslation(self, universe):
    """Uses information from the generated ontology universe to validate
    an entity's translation if it exists.

    Returns:
      Returns boolean for validity of entity translation, defaults to True if
      translation is not specified.
    """

    if self.translation is None:
      return True

    if isinstance(self.translation, str):
      if self.translation == TRANSLATION_COMPLIANT:
        return True
      else:
        print('Invalid translation compliance string: ', self.translation)
        return False

    is_valid = True

    entity_type = universe.GetEntityType(self.namespace, self.type_name)
    type_fields = entity_type.GetAllFields()
    found_fields = set()

    for field_name, ft in self.translation.items():
      # TODO(charbull): the key in the dictionary all_fields_dict starts
      # with `/`, needs to be cleaned
      key_field_name = '/' + field_name

      if key_field_name not in type_fields.keys():
        print('Field {0} is not defined on the type'.format(field_name))
        is_valid = False
        continue

      found_fields.add(key_field_name)

      valid_units = universe.GetUnitsMapByMeasurement(field_name)
      if valid_units:
        for unit in ft.units.keys():
          if unit not in valid_units:
            print('Field {0} has an invalid unit: {1}'.format(field_name, unit))
            is_valid = False

      valid_states = universe.GetStatesByField(field_name)
      if valid_states:
        for state in ft.states.keys():
          if state not in valid_states:
            print('Field {0} has an invalid state: {1}'
                  .format(field_name, state))
            is_valid = False

    for field_name, field in type_fields.items():
      if not field.optional and field_name not in found_fields:
        print('Required field {0} is missing from translation'
              .format(field_name))
        is_valid = False

    return is_valid


  def _ValidateConnections(self, universe):
    """Uses information from the generated ontology universe to validate
    an entity's connections. Connections are not currently generated in the
    ontology universe, so this code assumes the contents are a set.

    Returns:
      Returns boolean for validity of entity connections.
    """

    # TODO(nkilmer): validate existence of connection source entities

    if universe.connections_universe is None or self.connections is None:
      return True

    is_valid = True

    for conn_inst in self.connections:
      if conn_inst.ctype not in universe.connections_universe:
        print('Invalid connection type: {0}'.format(conn_inst.ctype))
        is_valid = False

    return is_valid


  def _ValidateLinks(self, universe, entity_instances):
    """Uses information from the generated ontology universe to validate
    the links key of an entity.

    Args:
      universe: ConfigUniverse generated from the ontology
      entity_instances: dictionary containing all instances

    Returns:
      Returns boolean for validity of links key, defaulting to True if the
      key is not present.
    """

    if self.links is None:
      return True

    is_valid = True

    entity_type = universe.GetEntityType(self.namespace, self.type_name)
    type_fields = entity_type.GetAllFields()
    found_fields = set()

    for link_inst in self.links:
      if link_inst.source not in entity_instances.keys():
        print('Invalid link source entity name: {0}'.format(link_inst.source))
        is_valid = False
        continue

      src_entity = entity_instances.get(link_inst.source)
      src_namespace = src_entity.namespace
      src_type_name = src_entity.type_name
      src_entity_type = universe.GetEntityType(src_namespace,
                                               src_type_name)

      for source_field, target_field in link_inst.field_map.items():
        # assumes that the namespace is '' for now
        if not entity_type.HasField('/' + target_field):
          print('Invalid link target field: ', target_field)
          is_valid = False
          continue

        if not src_entity_type.HasField('/' + source_field):
          print('Invalid link source field: ', source_field)
          is_valid = False
          continue

        found_fields.add('/' + target_field)

        if not self._ValidateLinkUnitsMatch(universe,
                                            source_field, target_field):
          is_valid = False
          continue

        if not self._ValidateLinkStatesMatch(universe,
                                             source_field, target_field):
          is_valid = False
          continue

    for field_name, field in type_fields.items():
      if not field.optional and field_name not in found_fields:
        print('Required field {0} is missing from links'.format(field_name))
        is_valid = False

    return is_valid


  def _ValidateLinkUnitsMatch(self, universe, source_field, target_field):
    """Validates that units match between linked source and target fields."""

    source_units = universe.GetUnitsMapByMeasurement(source_field)
    target_units = universe.GetUnitsMapByMeasurement(target_field)
    if source_units != target_units:
      print('Unit mismatch in link from {0} to {1}'\
            .format(source_field, target_field))
      return False
    return True


  def _ValidateLinkStatesMatch(self, universe, source_field, target_field):
    """Validates that states match between linked source and target fields."""

    source_states = universe.GetStatesByField(source_field)
    target_states = universe.GetStatesByField(target_field)
    if source_states != target_states:
      print('State mismatch in link from {0} to {1}'
            .format(source_field, target_field))
      return False
    return True


  def IsValidEntityInstance(self, universe=None, entity_instances=None):
    """Uses the generated ontology universe to validate an entity.

    Args:
      universe: ConfigUniverse generated from the ontology
      entity_instances: dictionary containing all entity instances

    Returns:
      True if the entity is valid
    """

    is_valid = True

    if self.id is None:
      print('Required field not specified: id')
      is_valid = False

    if self.namespace is None or self.type_name is None:
      print('Required field not specified: type')
      is_valid = False

    if universe is None:
      return is_valid

    if not self._ValidateType(universe):
      is_valid = False

    if not self._ValidateTranslation(universe):
      is_valid = False

    if not self._ValidateConnections(universe):
      is_valid = False

    if not self._ValidateLinks(universe, entity_instances):
      is_valid = False

    return is_valid
