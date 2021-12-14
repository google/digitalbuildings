# Copyright 2021 Google LLC
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

"""Main module for DBO explorer."""
import pyfiglet
import sys

from lib import explorer_handler
from lib import parse_input
from lib import arg_parser

def main(parsed_args):
  """Main method for DBO explorer."""
  figlet_out = pyfiglet.figlet_format('DBO Explorer', font='digital')
  print(figlet_out)
  print('Starting DBO explorer...')

  my_ontology = explorer_handler.Build(parsed_args.modified_types_filepath)
  done = False
  while not done:
    print(
        '\nHow would you like to query DBO\n' +
        '1: Get fields for a type name\n' +
        '2: Get types for a list of fields\n' +
        '3: Validate a field name\n' +
        'q: quit\n'
    )
    function_choice = input('Please select an option: ')
    if function_choice == '1':
      parse_input.GetFieldsForTypeName(my_ontology)
    elif function_choice == '2':
      parse_input.GetTypesForFieldList(my_ontology)
    elif function_choice == '3':
      parse_input.ValidateFieldName(my_ontology)
    elif function_choice == 'q':
      print('bye bye')
      done = True
    else:
      print(
          'You entered: ' + function_choice + '\n' +
          'Please enter a valid input'
      )

if __name__ == '__main__':
  args = arg_parser.ParseArgs().parse_args(sys.argv[1:])
  main(args)
