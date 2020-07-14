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

"""Generates the ontology universe for the instance validator."""

from __future__ import print_function

from sys import path
import os

# add universe building packages to path
path.append(os.path.abspath(os.path.join('..', 'ontology_validator')))
# add ontology files to path
path.append(os.path.exists(os.path.join('..', '..', '..', 'ontology')))

from yamlformat.validator import external_file_lib
from yamlformat.validator import presubmit_validate_types_lib
from yamlformat.validator import namespace_validator

def build_universe():
  """Generates the ontology universe.

  Returns:
    Generated universe object.
  """

  ontology_validator_exists = os.path.exists(os.path.join(
      '..', 'ontology_validator'))
  ontology_exists = os.path.exists(os.path.join('..', '..', '..', 'ontology'))

  if not (ontology_validator_exists and ontology_exists):
    print('ERROR: ontology validator or ontology have changed locations')
    return None

  yaml_files = external_file_lib._RecursiveDirWalk(os.path.join(
      '..', '..', '..', 'ontology', 'yaml', 'resources'))
  config = presubmit_validate_types_lib.SeparateConfigFiles(yaml_files)
  universe = presubmit_validate_types_lib.BuildUniverse(config)
  
  namespace_validation = namespace_validator.NamespaceValidator(
      universe.GetEntityTypeNamespaces())
  
  if not namespace_validation.IsValid():
    return None

  return universe

def parse_universe(universe):
  """Parses generated the ontology universe object into its subcomponents

  Args:
    universe: generated the ontology universe object

  Returns:
    fields: valid universe field types generated from the ontology
    subfields_map: valid universe subfield types generated from the ontology
    states_map: valid universe state types generated from the ontology
    units_map:  valid universe unit types generated from the ontology
    entities_map:  valid universe entity types generated from the ontology
  """
  states = universe.state_universe
  entities = universe.entity_type_universe
  units = universe.unit_universe
  subfields = universe.subfield_universe

  # USAGE: fields.IsFieldDefined('process_return_water_temperature_sensor', '')
  fields = universe.field_universe

  # consolidate all entity information into dictionary
  entities_map = {}
  entity_type_namespaces = entities.type_namespaces_map
  for namespace in entity_type_namespaces.keys():
    valid_types_map = entity_type_namespaces[namespace].valid_types_map

    namespace_name = entity_type_namespaces[namespace].namespace
    entities_map[namespace_name] = {}

    for valid_type_key in valid_types_map.keys():
      entity_type = valid_types_map[valid_type_key]
      entities_map[namespace_name][valid_type_key] = entity_type.GetAllFields()

  subfields_map = subfields.GetSubfieldsMap('')
  states_map = states.GetStatesMap('')
  units_map = units.GetUnitsMap('')

  return fields, subfields_map, states_map, units_map, entities_map
