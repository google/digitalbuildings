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

import colorama
from termcolor import colored

from google3.third_party.digitalbuildings.tools.explorer.lib import arg_parser
from google3.third_party.digitalbuildings.tools.explorer.lib import explorer_handler
from google3.third_party.digitalbuildings.tools.explorer.lib import parse_input

colorama.init()


def main(parsed_args):
  """Main method for DBO explorer."""
  print('Starting DBO explorer...')

  ontology = explorer_handler.Build(parsed_args.modified_types_filepath)
  done = False
  while not done:
    try:
      print(
          '\nHow would you like to query DBO\n' +
          '1: Get fields for a type name\n' +
          '2: Get types for a list of fields\n' +
          '3: Validate a field name\n' +
          'q: quit\n'
      )
      function_choice = input('Please select an option: ')
      if function_choice == '1':
        parse_input.GetFieldsForTypeName(ontology)
      elif function_choice == '2':
        parse_input.GetTypesForFieldList(ontology)
      elif function_choice == '3':
        parse_input.ValidateFieldName(ontology)
      elif function_choice == 'q':
        print('bye bye')
        done = True
      else:
        print(
            'You entered: ' + function_choice + '\n' +
            'Please enter a valid input'
        )
    except TypeError as type_error:
      print(colored(type_error, 'red'))
      continue
    except ValueError as value_error:
      print(colored(value_error, 'red'))
      continue
    except AttributeError as attribute_error:
      print(colored(attribute_error, 'red'))
      continue

if __name__ == '__main__':
  args = arg_parser.ParseArgs().parse_args(sys.argv[1:])
  main(args)
