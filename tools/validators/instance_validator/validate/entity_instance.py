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
    super().__init__()
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

    if len(type_parse) == 1:
      print('Type improperly formatted, a namespace is missing: '
            , entity_type_str)
      return False

    if len(type_parse) > 2:
      print('Type improperly formatted: ', entity_type_str)
      return False

    self.namespace = type_parse[0]
    self.entity_type = type_parse[1]

    if self.universe.GetEntityTypeNamespace(self.namespace) is None:
      print('Invalid namespace:', self.namespace)
      return False

    entity_type_universe = self.universe.GetEntityType(self.namespace,
                                                       self.entity_type)
    if entity_type_universe is None:
      print('Invalid entity type:', self.entity_type)
      return False
    elif entity_type_universe.is_abstract:
      print('Abstract types cannot be directly used:', self.entity_type)
      return False


    return True

  def _ValidateLinks(self, entity_instances):
    """Uses information from the generated ontology universe to validate
    the links key of an entity.
    Args:
      entity_instances: dictionary containing all instances
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
      # todo:refactor into classes
      # scan all standard fields and ensure they're defined
      fields_map = dict(links[entity_name])
      source_entity_instance = entity_instances.get(entity_name)
      # this is valid type, the check already happened
      src_entity_type_str = str(source_entity_instance.entity['type'])
      src_type_parse = src_entity_type_str.split('/')
      src_namespace = src_type_parse[0]
      src_type = src_type_parse[1]
      src_entity_type = self.universe.GetEntityType(src_namespace, src_type)
      target_entity_type = self.universe.GetEntityType(self.namespace,
                                                       self.entity_type)
      all_fields_dict = src_entity_type.GetAllFields().copy()
      for source_field, target_field  in fields_map.items():
        opt_wrapper_field = all_fields_dict.pop('/'+source_field.data, None)
        if opt_wrapper_field is None:  # an extra field that should not be here
          print('Invalid extra link present:', source_field.data)
          return False
        # check the fields are present
        # assumes that the namespace is `` for now
        if not src_entity_type.HasField('/'+source_field.data):
          print('Invalid links field source: ', source_field)
          return False
        if not target_entity_type.HasField('/'+target_field.data):
          print('Invalid links field target: ', target_field)
          return False
        # check the units are matching
        valid_units_src = source_entity_instance.universe\
          .GetUnitsMapByMeasurement(source_field.data)
        valid_units_target = self .universe\
          .GetUnitsMapByMeasurement(target_field.data)
        # when one is None and not the other
        if valid_units_src != valid_units_target:
          print('Links dont have the same units: ',
                valid_units_src, valid_units_target)
          print('Links error for the following fields (source, target): '
                , source_field, target_field)
          return False
        if valid_units_src is not None \
            and set(valid_units_src) != set(valid_units_target):
              print('Links dont have the same units: '
                    ,valid_units_src, valid_units_target)
              print('Links error for the following fields (source, target): '
                    , source_field, target_field)
              return False
        # check the states are matching
        valid_states_src = source_entity_instance.universe\
          .GetStatesByField(source_field.data)
        valid_states_target = self.universe\
          .GetStatesByField(target_field.data)
        # when one is None and not the other
        if valid_units_src != valid_units_target:
          print('Links dont have the same states: '
                , valid_states_src, valid_states_target)
          print('Links error for the following fields (source, target): '
                , source_field, target_field)
          return False
        if valid_states_src is not None and \
            set(valid_states_src) != set(valid_states_target):
          print('Links dont have the same states: ',
                valid_states_src, valid_states_target)
          print('Links error for the following fields (source, target): '
                , source_field, target_field)
          return False
      # check if the rest of the links not included are optional
      for optional_field_name in all_fields_dict.values():
        if not optional_field_name.optional:
          print('Links does not use the mandatory field: ',
                optional_field_name.field.field)
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

    # TODO(charbull): refactor this while refactoring the class
    # validate fields
    entity_type_str = str(self.entity['type'])
    type_parse = entity_type_str.split('/')
    namespace = type_parse[0]
    entity_type = type_parse[1]
    entity_type = self.universe.GetEntityType(namespace, entity_type)
    # TODO(charbull): no need to copy here, just keep the key
    #  in a set when it is seen, will refactor in the next PR
    all_fields_dict = entity_type.GetAllFields().copy()

    # iterate through each translation device key and determine its form
    for field_name in translation_body.keys():
      # check if keys are UDMI compliant
      if isinstance(translation_body[field_name].data, str):
        continue

      #check if the field_name is on the type
      #TODO(charbull), the key in the dictionary
      #all_fields_dict starts with `/`, needs to be cleaned
      #pop the field out
      key_field_name = '/'+field_name.data
      opt_wrapper_field = all_fields_dict.pop(key_field_name, None)
      if opt_wrapper_field is None: #an extra field that should not be here
        print('Invalid extra field present:', field_name)
        return False

      translation_map = translation_body[field_name]

      # check if keys are UDMI compliant then skip the units and states
      if isinstance(translation_body[field_name].data, str):
        continue

      valid_units = self.universe.GetUnitsMapByMeasurement(field_name.data)
      if valid_units:
        if self.units in translation_map.keys():
          unit_values_map = translation_map[self.units]
          for unit in unit_values_map['values']:
            if unit not in valid_units:
              print('Invalid translation unit:', unit)
              print('Field translation: ', field_name.data)
              return False
        # the UDMI format
        elif self.unit_values in translation_map.keys():
          unit_values_map = translation_map[self.unit_values].data
          for unit in unit_values_map.keys():
            if unit not in valid_units:
              print('Invalid translation unit:', unit)
              print('Field translation: ', field_name.data)
              return False

      valid_states = self.universe.GetStatesByField(field_name.data)
      if valid_states:
        if self.states in translation_map.keys():
          states_map = translation_map[self.states]
          for state in states_map.keys():
            if state not in valid_states:
              print('Invalid translation state', state)
              print('Field translation: ', field_name.data)
              return False

    #check if the rest of the fields not included are optional
    for optional_field_name in all_fields_dict.values():
      if not optional_field_name.optional:
        print('Translation does not use the mandatory field: ',
              optional_field_name.field.field)
        return False


    return True

  def IsValidEntityInstance(self, entity_instances=None):
    """Uses information from the generated ontology universe to validate an
    entity.
    Args:
      entity_instances: dictionary containing all instances.
    Returns:
      Returns boolean for validity of entity.
    """
    for req_key in self.required_keys:
      if req_key not in self.entity.keys():
        print('Missing required key:', req_key)
        return False

    if not self._ValidateType():
      print('Invalid type')
      return False

    if not self._ValidateLinks(entity_instances):
      print('Invalid links')
      return False

    if not self._ValidateTranslation():
      print('Invalid translation')
      return False

    if not self._ValidateConnections():
      print('Invalid connections')
      return False

    return True
