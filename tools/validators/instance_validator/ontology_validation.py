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

def _validate_type(entity, entities_map):
  """Uses information from the generated ontology universe to validate
  an entity's type.

  Args:
    entity: parsed instance YAML file formatted as dictionary
    entities_map: valid universe entity types generated from ontology

  Returns:
    Throws Exceptions if entity type is invalid.
  """
  entity_type_str = str(entity['type'])
  type_parse = entity_type_str.split('/')

  if len(type_parse) != 2:
    raise Exception('type improperly formatted:', entity_type_str)

  namespace = type_parse[0]
  entity_type = type_parse[1]

  if namespace not in entities_map.keys():
    raise Exception('invalid namespace:', namespace)

  if entity_type not in entities_map[namespace].keys():
    raise Exception('invalid entity type:', entity_type)

def validate_entity(entity, fields,
                    subfields_map, states_map, units_map, entities_map):
  """Uses information from generated ontology universe to validate an entity.

  Args:
    entity: parsed instance YAML file formatted as dictionary
    fields: valid universe field types generated from ontology
    subfields_map: valid universe subfield types generated from ontology
    states_map: valid universe state types generated from ontology
    units_map:  valid universe unit types generated from ontology
    entities_map:  valid universe entity types generated from ontology

  Returns:
    Throws Exceptions if entity is invalid.
  """
  _validate_type(entity, entities_map)
