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
import sys

from lib import arg_parser
from lib import explorer
from lib import model
import pyfiglet


def main(parsed_args):
  """Main method for DBO explorer."""
  figlet_out = pyfiglet.figlet_format('DBO Explorer', font='digital')
  print(figlet_out)
  print('Starting DBO explorer...')

  my_ontology = explorer.Build(parsed_args.modified_types_filepath)
  done = False
  while not done:
    print('\nHow would you like to query DBO\n' +
          '1: Get fields for a type name\n' +
          '2: Get types for a list of fields\n' + '3: Validate a field name\n' +
          'q: quit\n')
    function_choice = input('Please select an option: ')
    if function_choice == '1':
      namespace = input('Enter a namespace: ').upper()
      type_name = input(f'Enter a type name defined in {namespace}: ').upper()
      fields = my_ontology.GetFieldsForTypeName(namespace, type_name)
      print(f'\nFields for {namespace}/{type_name}:')
      for field in fields:
        print(field)
    elif function_choice == '2':
      print('This functionality is still under construction.\n' +
            'Please pick another option.')
    elif function_choice == '3':
      namespace = input('Enter a namespace: ').upper()
      field_name = input('Enter a field name to validate: ')
      standard_field = model.StandardField(namespace, field_name)
      field_is_valid = my_ontology.IsFieldValid(standard_field)
      if not namespace:
        namespace = 'global'
      print(f'{field_name} is defined in {namespace}: {field_is_valid}')
    elif function_choice == 'q':
      print('bye bye')
      done = True
    else:
      print('You entered: ' + function_choice + '\n' +
            'Please enter a valid input')


if __name__ == '__main__':
  args = arg_parser.ParseArgs().parse_args(sys.argv[1:])
  main(args)
