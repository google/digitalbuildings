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
from yamlformat.validator import findings_lib

class EntityInstance(findings_lib.Findings):
  """Uses information from the generated ontology universe to validate
  an entity instance. An entity instance is composed of at least an id and a
  type. For example: {'id': 'FACILITIES/12345', 'type': 'FACILITIES/BUILDING'}.

  Args:
    entity instance: parsed instance YAML file formatted as dictionary
    universe: ConfigUniverse generated from the ontology
    config_entity_names: list of entity names in instance YAML file
  """

  def __init__(self, entity, universe, config_entity_names):
    super(EntityInstance, self).__init__()
    self.entity = entity
    self.universe = universe
    self.config_entity_names = config_entity_names
    self.required_keys = ('id', 'type')
    self.links = 'links'
    self.translation_key = 'translation'
    self.translation_compliant = 'COMPLIANT'
    self.unit_values = 'unit_values'
    self.states = 'states'
    self.units = 'units'
    self.values = 'values'
    self.key = 'key'
    self.connections = 'connections'

  def _ValidateConnections(self):
    """Uses information from the generated ontology universe to validate
    an entity's connections. Connections are not currently generated in the
    ontology universe, so this code assumes the contents are a set.

    Returns:
      Returns boolean for validity of entity connections.
    """
    if self.universe.connections_universe is None:
      # connections are not being generated
      return True

    if self.connections not in self.entity.keys():
      # connections are not included in this building config
      return True

    connections_map = dict(self.entity[self.connections])
    connections = set(connections_map.values())
    diff = connections.difference(self.universe.connections_universe)
    if diff != set():
      print('Invalid connections:', diff)
      return False

    return True

  def _ValidateType(self):
    """Uses information from the generated ontology universe to validate
    an entity's type.

    Returns:
      Returns boolean for validity of entity type.
    """
    entity_type_str = str(self.entity['type'])
    type_parse = entity_type_str.split('/')

    if len(type_parse) != 2:
      print('Type improperly formatted:', entity_type_str)
      return False

    namespace = type_parse[0]
    entity_type = type_parse[1]

    if self.universe.GetEntityTypeNamespace(namespace) is None:
      print('Invalid namespace:', namespace)
      return False

    if self.universe.GetEntityType(namespace, entity_type) is None:
      print('Invalid entity type:', entity_type)
      return False

    return True

  def _ValidateLinks(self):
    """Uses information from the generated ontology universe to validate
    the links key of an entity.

    Returns:
      Returns boolean for validity of links key, defaulting to True if the
      key is not present.
    """
    if self.links not in self.entity.keys():
      return True

    links = dict(self.entity[self.links])
    for entity_name in links.keys():
      # ensure first level keys refer to other entities in config file
      if entity_name not in self.config_entity_names:
        print('Invalid links entity name', entity_name)
        return False

      # scan all standard fields and ensure they're defined
      fields_map = dict(links[entity_name])
      field_universe = self.universe.field_universe
      for sourcename in fields_map.keys():
        if not field_universe.IsFieldDefined(fields_map[sourcename], ''):
          print('Invalid links field source', sourcename)
          return False

    return True

  def _ValidateTranslation(self):
    """Uses information from the generated ontology universe to validate
    an entity's translation if it exists.

    Returns:
      Returns boolean for validity of entity translation, defaults to True if
      translation is not specified.
    """
    if self.translation_key not in self.entity.keys():
      return True

    translation_body = self.entity[self.translation_key]
    if isinstance(translation_body.data, str):
      if translation_body.data == self.translation_compliant:
        return True
      else:
        print('Invalid translation compliance string', translation_body.data)
        return False

    # iterate through each translation device key and determine its form
    for device_name in translation_body.keys():
      # check if keys are UDMI compliant
      if isinstance(translation_body[device_name].data, str):
        continue

      device_map = translation_body[device_name]
      valid_units = self.universe.unit_universe.GetUnitsMap('').keys()
      valid_states = self.universe.state_universe.GetStatesMap('').keys()

      # three remaining possibilities for translation format
      if self.unit_values in device_map.keys():
        unit_values_map = device_map[self.unit_values]
        for unit in unit_values_map.keys():
          if unit not in valid_units:
            print('Invalid translation unit', unit)
            return False
      elif self.states in device_map.keys():
        states_map = device_map[self.states]
        for state in states_map.keys():
          if state not in valid_states:
            print('Invalid translation state', state)
            return False
      elif self.units in device_map.keys():
        # check that the unit map has keys named `keys`, `values`
        units_map = device_map[self.units]
        if self.key not in units_map.keys():
          print('Invalid units translation is missing key', self.key)
          return False
        if self.values not in units_map.keys():
          print('Invalid units translation is missing values', self.values)
          return False

        unit_values_map = units_map[self.values]
        for unit in unit_values_map.keys():
          if unit not in valid_units:
            print('Invalid translation unit', unit)
            return False
      else:
        print('Translation has improper keys:', device_name)
        return False

    return True

  def IsValidEntityInstance(self):
    """Uses information from the generated ontology universe to validate an
    entity.

    Returns:
      Returns boolean for validity of entity.
    """
    for req_key in self.required_keys:
      if req_key not in self.entity.keys():
        print('Missing required key:', req_key)
        return False

    if not self._ValidateType():
      print('Invalid type key')
      return False

    if not self._ValidateLinks():
      print('Invalid links key')
      return False

    if not self._ValidateTranslation():
      print('Invalid translation key')
      return False

    if not self._ValidateConnections():
      print('Invalid connections key')
      return False

    return True
