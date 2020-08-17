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

from validate import generate_universe
from validate import entity_instance
from validate import instance_parser
import argparse
import sys

# TODO add input and return type checks in all functions

if __name__ == '__main__':
  parser = argparse.ArgumentParser(
      description='Validate a YAML building configuration file')
  parser.add_argument('-i', '--input',
                      dest='filename',
                      required=True,
                      help='Filepath to YAML building configuration',
                      metavar='FILE')
  parser.add_argument('-m', '--modified-ontology-types',
                      dest='modified_types_filepath',
                      required=False,
                      help='Filepath to modified type filepaths',
                      metavar='MODIFIED_TYPE_FILEPATHS')
  arg = parser.parse_args()

  # SYNTAX VALIDATION
  print('\nValidator starting ...\n')
  filename = arg.filename

  # prints for syntax errors and exits gracefully
  raw_parse = instance_parser.parse_yaml(filename)

  print('Passed syntax checks!')

  modified_types_filepath = arg.modified_types_filepath

  print('Generating universe ...')
  universe = generate_universe.BuildUniverse(modified_types_filepath)

  if universe is None:
    print('\nError generating universe')
    sys.exit(0)

  print('Universe generated successfully')

  parsed = dict(raw_parse)

  entity_names = list(parsed.keys())
  for entity_name in entity_names:
    entity = dict(parsed[entity_name])
    instance = entity_instance.EntityInstance(entity,
                                              universe,
                                              set(entity_names))

    if not instance.IsValidEntityInstance():
      print(entity_name, 'is not a valid instance')
      sys.exit(0)

  print('File passes all checks!')
