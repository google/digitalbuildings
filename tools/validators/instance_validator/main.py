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

import parser
import sys
# ONTOLOGY VALIDATION
# import ontology_validation
# import generate_universe

# TODO add input and return type checks in all functions

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('USAGE: python3 schema.py yaml_file_path')
        sys.exit(1)
    
    # SYNTAX VALIDATION
    print('\nValidator starting ...')
    filename = sys.argv[1]

    # throws errors for syntax
    parsed = dict(parser.parse_yaml(filename))

    print('Passed syntax checks!')

    # ONTOLOGY VALIDATION
    '''
    print('Building ontology universe ...')

    universe = generate_universe.build_universe()
    fields, subfields_map, states_map, units_map, entities_map = generate_universe.parse_universe(universe)

    entity_names = list(parsed.keys())

    for name in entity_names:
        entity = dict(parsed[name])
        ontology_validation.validate_entity(entity, fields, subfields_map, states_map, units_map, entities_map)

    print('Passed all checks!\n')
    '''