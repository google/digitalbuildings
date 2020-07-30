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
  """

  def __init__(self, entity, universe):
    super(EntityInstance, self).__init__()
    self.entity = entity
    self.universe = universe
    self.required_keys = ('id', 'type')
    self.translation_key = 'translation'
    self.translation_compliant = 'COMPLIANT'

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
      if 'unit_values' in device_map.keys():
        unit_values_map = device_map['unit_values']
        for unit in unit_values_map.keys():
          if unit not in valid_units:
            print('Invalid translation unit', unit)
            return False
      elif 'states' in device_map.keys():
        states_map = device_map['states']
        for state in states_map.keys():
          if state not in valid_states:
            print('Invalid translation state', state)
            return False
      elif 'units' in device_map.keys():
        # check that the unit map has keys named `keys`, `values`
        units_map = device_map['units']
        if 'key' not in units_map.keys():
          print('Invalid units translation is missing key')
          return False
        if 'values' not in units_map.keys():
          print('Invalid units translation is missing values')
          return False

        unit_values_map = units_map['values']
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

    return self._ValidateType() and self._ValidateTranslation()
