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
import ast
import pyfiglet
import sys
from termcolor import colored
from typing import List

from lib import explorer
from lib import model
from lib.model import StandardField
from lib import arg_parser

def _InputFieldsManually(ontology) -> List[StandardField]:
  """Method to take individual field inputs from user and return as a list.

  Args:
    ontology: An instance of OntologyWrapper class.

  Returns:
    A list of StandardField objects.
  """
  standard_field_list = []
  field_number = input('Number of entity fields: ')
  for i in range(1, int(field_number)+1):
    field_name = input(f'{i}. What is the field name?\nname: ')
    standard_field = model.StandardField(
        standard_field_name=field_name,
        namespace_name=''
    )
    if ontology.IsFieldValid(standard_field):
      standard_field_list.append(standard_field)
  return standard_field_list

def _InputFieldsFromCSV(ontology) -> List[StandardField]:
  """Method to take batch field inputs from user and return as a list

  Args:
    ontology: An instance of OntologyWrapper class.

  Returns:
    A list of StandardField objects
  """
  standard_field_list = []
  raw_fields = input('Paste your fields here: ')
  raw_field_list = raw_fields.replace(' ', '').split(',')
  for field in raw_field_list:
    standard_field = StandardField(
        standard_field_name=field,
        namespace_name=''
    )
    if ontology.IsFieldValid(standard_field):
      standard_field_list.append(standard_field)
  return standard_field_list

def _GetFieldsForTypeName(ontology):
  """Prints a list of corresponding fields for an ontological entity type.

  Args:
    ontology: An instance of the OntologyWrapper class.
  """
  namespace = input('Enter a namespace: ').upper()
  type_name = input(f'Enter a type name defined in {namespace}: ').upper()
  fields = ontology.GetFieldsForTypeName(namespace, type_name)
  print(f'\nFields for {namespace}/{type_name}:')
  for field in fields:
    print(colored(field, 'green'))

def _GetTypesForFieldList(ontology):
  """Prints a list of entity types matching a list of input fields

  Args:
    ontology: An instance of the OntologyWrapper class.
  """
  print('1. Input fields one by one\n2. Paste comma-separated list of fields')
  input_decision = input('Input type: ')
  if ast.literal_eval(input_decision) == 1:
    standard_field_list = _InputFieldsManually(ontology)
  elif ast.literal_eval(input_decision) == 2:
    standard_field_list = _InputFieldsFromCSV(ontology)

  entity_type_match_dict = {}
  for i, match in enumerate(ontology.GetEntityTypesFromFields(
      standard_field_list)):
    entity_type_match_dict[i] = match
  for i in range(10):
    print(colored(f'{i+1}. {entity_type_match_dict[i]}', 'green'))
  match_selection = input('Would you like to see all matches?(y/n):\n')
  if match_selection == 'y':
    for i, match in entity_type_match_dict.items():
      print(f'{i+1}. {match}')
  print('Would you like to see field comparisons for any of these matches?')
  visualize = input('(y/n): ')
  if visualize == 'y':
    visualize_done = False
    while not visualize_done:
      comparison_number = ast.literal_eval(input(
          'which match would you like to visualize?\nmatch number: '))
      print_match = entity_type_match_dict[comparison_number - 1]
      print(ontology.PrintFieldSetComparison(print_match))
      repeat_comparison = input(
          'Would you like to see another match comparison?\n(y/n): ')
      if repeat_comparison == 'n':
        break
      elif repeat_comparison == 'y':
        continue
      else:
        raise ValueError('Please enter proper value for decision tree')

def _ValidateFieldName(ontology):
  """Prints whether a fully qualified field is valid in the DB ontology.

  Args:
    ontology: An instance of the OntologyWrapper class
  """
  namespace = input('Enter a namespace(leave blank for global): ').upper()
  field_name = input('Enter a field name to validate: ')
  standard_field = model.StandardField(namespace, field_name)
  field_is_valid = ontology.IsFieldValid(standard_field)
  if namespace == '':
    namespace = 'global namespace'
  if field_is_valid:
    print(colored(
        f'{field_name} is defined in {namespace}: {field_is_valid}', 'green'))
  else:
    print(colored(
        f'{field_name} is defined in {namespace}: {field_is_valid}', 'red'))

def main(parsed_args):
  """Main method for DBO explorer."""
  figlet_out = pyfiglet.figlet_format('DBO Explorer', font='digital')
  print(figlet_out)
  print('Starting DBO explorer...')

  my_ontology = explorer.Build(parsed_args.modified_types_filepath)
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
      _GetFieldsForTypeName(my_ontology)
    elif function_choice == '2':
      _GetTypesForFieldList(my_ontology)
    elif function_choice == '3':
      _ValidateFieldName(my_ontology)
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
