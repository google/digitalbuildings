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

"""Main of the instance validator. This script takes a YAML building
configuration file as an argument and validates it for coherence with the
Digital Buildings ontology.

This is done by first ensuring the file syntax is valid YAML, then by
parsing the ontology and comparing it with the file contents.

This tool allows clients to independently validate their configuration files. 
It saves time and provides more accuracy than manual error checks."""

from __future__ import print_function

import instance_parser
import argparse

# TODO add input and return type checks in all functions

if __name__ == '__main__':
  parser = argparse.ArgumentParser(
      description='Validate a YAML building configuration file')
  parser.add_argument('-i', '--input',
                      dest='filename',
                      required=True,
                      help='Filepath to YAML building configuration',
                      metavar='FILE')
  arg = parser.parse_args()

  # SYNTAX VALIDATION
  print('\nValidator starting ...')
  filename = arg.filename

  # throws errors for syntax
  parsed = dict(instance_parser.parse_yaml(filename))

  print('Passed syntax checks!')

  # ONTOLOGY VALIDATION
  '''
  print('Building ontology universe ...')

  universe = generate_universe.build_universe()
  parsed_univ = generate_universe.parse_universe(universe)

  # TODO(https://github.com/google/digitalbuildings/issues/42): 
      replace this assignment logic with NamedTuple ontology generation
  fields, subfields_map, states_map, units_map, entities_map = parsed_univ

  entity_names = list(parsed.keys())

  for name in entity_names:
    entity = dict(parsed[name])
    ontology_validation.validate_entity(entity,
                                        fields,
                                        subfields_map,
                                        states_map,
                                        units_map,
                                        entities_map)

  print('Passed all checks!\n')
  '''
