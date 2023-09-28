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
import re
from typing import List

# pylint: disable=g-importing-member
import colorama
from termcolor import colored

from lib import model
from lib.model import StandardField
from yamlformat.validator.field_lib import FIELD_INCREMENT_REGEX

colorama.init()
DEFAULT_MATCHED_TYPES_LIST_SIZE = 10
DELIMITER_REGEX = r'[\s|\r|\n|,|/|;]+'


def _InputFieldsFromUser() -> List[StandardField]:
  """Method to take in field inputs from the user.

  Returns:
    A list of StandardField objects corresponding to the input field names.
  """
  raw_input_string = input('Enter your fields here as a comma separated list: ')
  standard_field_list = []
  for field in re.split(DELIMITER_REGEX, raw_input_string):
    split_field = re.split(FIELD_INCREMENT_REGEX, field)
    standard_field = StandardField(
        standard_field_name=split_field[0],
        namespace_name='',
        increment=split_field[1],
    )
    standard_field_list.append(standard_field)
  return standard_field_list


def _PrintFieldMatchComparison(ontology, entity_type_match_dict) -> None:
  """Function to prompt the user to see field set comparisons.

  Comparisons are made between an input set of fields and an entity type defined
  in the ontology. This function prompts the user for which matches they would
  like to compare their set of fields with.

  Args:
    ontology: An instance of the OntologyWrapper class.
    entity_type_match_dict: A dictionary of enumerated Match class instances.
  """
  visualize = input(
      'Would you like to see field comparisons for these matches? (y/n): '
  )
  if visualize == 'y':
    visualize_done = False
    while not visualize_done:
      comparison_number = ast.literal_eval(
          input('which match would you like to visualize?\nmatch number: ')
      )
      if not isinstance(comparison_number, int):
        print(colored('Please enter a valid numerical input', 'red'))
      print_match = entity_type_match_dict[comparison_number - 1]
      print(ontology.PrintFieldSetComparison(print_match))
      repeat_comparison = input(
          'Would you like to see another match comparison?\n(y/n): '
      )
      if repeat_comparison == 'n':
        break
      elif repeat_comparison == 'y':
        continue
      else:
        raise ValueError('Please enter proper value for decision tree')


def GetFieldsForTypeName(ontology):
  """Prints a list of corresponding fields for an ontology entity type.

  Args:
    ontology: An instance of the OntologyWrapper class.
  """
  namespace = input('Enter a namespace: ').upper()
  type_name = input(f'Enter a type name defined in {namespace}: ').upper()
  fields = ontology.GetFieldsForTypeName(namespace, type_name)
  print(f'\nFields for {namespace}/{type_name}:')
  for required_field in [field for field in fields if not field.IsOptional()]:
    print(colored(required_field, 'green'))
  for optional_field in [field for field in fields if field.IsOptional()]:
    print(colored(optional_field, 'yellow'))


def GetTypesForFieldList(ontology):
  """Prints a list of entity types matching a list of input fields.

  Args:
    ontology: An instance of the OntologyWrapper class.
  """
  standard_field_list = _InputFieldsFromUser()

  entity_type_match_dict = {}
  for i, match in enumerate(
      ontology.GetEntityTypesFromFields(standard_field_list)
  ):
    entity_type_match_dict[i] = match
  for i in range(DEFAULT_MATCHED_TYPES_LIST_SIZE):
    print(colored(f'{i+1}. {entity_type_match_dict[i]}', 'green'))
  _PrintFieldMatchComparison(ontology, entity_type_match_dict)
  match_selection = input('Would you like to see all matches? (y/n): ')
  if match_selection == 'y':
    for i, match in [
        (index, match)
        for index, match in entity_type_match_dict.items()
        if match.GetMatchScore() > 0
    ]:
      print(colored(f'{i+1}. {match}', 'green'))
  _PrintFieldMatchComparison(ontology, entity_type_match_dict)


def ValidateFieldName(ontology):
  """Prints whether a fully qualified field is valid in the DB ontology.

  Args:
    ontology: An instance of the OntologyWrapper class
  """
  raw_fields = input('Enter fields to validate as a comma separated list: ')
  fields = re.split(DELIMITER_REGEX, raw_fields)
  global_namespace_string = 'GLOBAL'
  namespace_list = ['', 'HVAC', 'LIGHTING']
  valid_fields_map = {}
  for field_name in fields:
    valid_fields_map[field_name] = []
    for namespace in namespace_list:
      standard_field = model.StandardField(namespace, field_name)
      if ontology.IsFieldValid(standard_field):
        if not namespace:
          valid_fields_map.get(field_name).append(global_namespace_string)
        else:
          valid_fields_map.get(field_name).append(namespace)
  for field_name in fields:
    valid_namespaces = valid_fields_map.get(field_name)
    if valid_namespaces:
      print(
          colored(
              f'{field_name} is defined in the ontology under namespaces:'
              f' {valid_namespaces}',
              'green',
          )
      )
    else:
      print(colored(f'{field_name} is not defined in the ontology', 'red'))


def GetFieldsForSubfieldList(ontology):
  """Prints a list of fields matching a list of input subfields.

  Args:
    ontology: An instance of the OntologyWrapper class
  """
  raw_subfields = input('Enter your subfields here as a comma separated list: ')
  subfields = re.split(DELIMITER_REGEX, raw_subfields)

  all_fields = ontology.universe.field_universe.GetFieldsMap()

  complete_match_list = []

  for field in all_fields:
    if all(subfield in field for subfield in subfields):
      complete_match_list.append(field[1:])

  print(f'\nComplete matches for {subfields}:')
  for field in sorted(
    complete_match_list,
    key=lambda x: x,
    reverse=False
  ):
    print(colored(field, 'green'))
