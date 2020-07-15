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
from __future__ import absolute_import

from os import path

from yamlformat.validator import external_file_lib
from yamlformat.validator import presubmit_validate_types_lib
from yamlformat.validator import namespace_validator
from yamlformat.validator import state_lib
from yamlformat.validator import subfield_lib
from yamlformat.validator import unit_lib
from yamlformat.validator import entity_type_lib
from yamlformat.validator import field_lib
from yamlformat.validator import parse_config_lib as parse

def build_config():
  """Builds and returns config for use in generating universes.

  Returns:
    config: a Config namedtuple containing lists of localpaths to config files.
  """

  yaml_files = external_file_lib._RecursiveDirWalk(path.join(
      '..', '..', '..', 'ontology', 'yaml', 'resources'))
  config = presubmit_validate_types_lib.SeparateConfigFiles(yaml_files)

  return config

def build_state_universe(config):
  """Builds a StateUniverse object.

  Args:
    config: a Config namedtuple containing lists of localpaths to config files.

  Returns:
     A StateUniverse that is fully populated with state content specified in
     the config.
  """

  state_universe = None

  if config.states:
    state_folders = parse.ParseStateFoldersFromFiles(config.states)
    state_universe = state_lib.StateUniverse(state_folders)

  return state_universe

def build_subfield_universe(config):
  """Builds SubfieldUniverse object.

  Args:
    config: a Config namedtuple containing lists of localpaths to config files.

  Returns:
     A SubfieldUniverse that is fully populated with subfield content
     specified in the config.
  """

  subfield_universe = None

  if config.subfields:
    subfield_folders = parse.ParseSubfieldFoldersFromFiles(config.subfields)
    subfield_universe = subfield_lib.SubfieldUniverse(subfield_folders)

  return subfield_universe

def build_unit_universe(config, subfield_universe):
  """Builds UnitUniverse object.

  Args:
    config: a Config namedtuple containing lists of localpaths to config files.
    subfield_universe: a SubfieldUniverse object to validate UnitUniverse.

  Returns:
     A UnitUniverse that is fully populated with unit content specified
     in the config.
  """

  unit_universe = None

  if config.units:
    unit_folders = parse.ParseUnitFoldersFromFiles(config.units,
                                                   subfield_universe)
    unit_universe = unit_lib.UnitUniverse(unit_folders)
    if subfield_universe:
      subfield_universe.ValidateUnits(unit_universe)

  return unit_universe

def build_field_universe(config, subfield_universe, state_universe):
  """Builds FieldUniverse object.

  Args:
    config: a Config namedtuple containing lists of localpaths to config files.
    subfield_universe: a SubfieldUniverse object to validate the FieldUniverse.
    state_universe: a StateUniverse object to validate the FieldUniverse.

  Returns:
     A FieldUniverse that is fully populated with field content specified
     in the config.
  """

  field_universe = None

  if config.fields:
    field_folders = parse.ParseFieldFoldersFromFiles(config.fields,
                                                     subfield_universe,
                                                     state_universe)
    field_universe = field_lib.FieldUniverse(field_folders)

  return field_universe

def build_type_universe(config, field_universe):
  """Builds TypeUniverse object.

  Args:
    config: a Config namedtuple containing lists of localpaths to config files.
    field_universe: a FieldUniverse object to validate the TypeUniverse.

  Returns:
     A TypeUniverse that is fully populated with type content specified
     in the config.
  """

  type_folders = parse.ParseTypeFoldersFromFiles(config.type_defs,
                                                 field_universe)
  type_universe = entity_type_lib.EntityTypeUniverse(type_folders)

  return type_universe

def build_universe():
  """Generates the ontology universe.

  Returns:
    Generated universe object.
  """

  ontology_validator_exists = path.exists(path.join(
      '..', 'ontology_validator'))
  ontology_exists = path.exists(path.join('..', '..', '..', 'ontology'))

  if not (ontology_validator_exists and ontology_exists):
    print('ERROR: ontology validator or ontology have changed locations')
    return None

  yaml_files = external_file_lib._RecursiveDirWalk(path.join(
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
