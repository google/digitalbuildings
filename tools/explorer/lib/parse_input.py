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
from collections import defaultdict
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
  for i, match in enumerate(ontology.GetEntityTypesFromFields(standard_field_list)):
    entity_type_match_dict[i] = match
  for i in range(DEFAULT_MATCHED_TYPES_LIST_SIZE):
    match = entity_type_match_dict[i]
    score = match._match_score
    entity_type = str(match._entity_type.typename)
    if score == 100:
        color = 'green'
    elif score >= 80:
        color = 'yellow'
    else:
        color = 'red'
    print(colored(f'{i+1}. {entity_type} -- score:{score}', color))

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
  for field in sorted(complete_match_list, key=lambda x: x, reverse=False):
    print(colored(field, 'green'))


def CompareFieldsToSpecifiedType(ontology, point_list_input):
    """Prompts user for abstract type and point list, then compares against ABSTRACT.yaml definitions."""

    entity_type_map = {}
    dict_list = []

    # Collect entity type maps from ontology
    for tns in ontology.universe.GetEntityTypeNamespaces():
        dict_list.append(tns.valid_types_map)

    largest_dict = max(dict_list, key=lambda d: len(d))

    # Build mapping of abstract types -> required/optional fields
    for entity_type in largest_dict:
        if "_" not in entity_type:
            entity_type_map[entity_type] = {'uses': [], 'opt_uses': []}
            for key, opt_wrapper in largest_dict[entity_type].GetAllFields().items():
                field_name = key.lstrip("/")
                is_optional = opt_wrapper.optional
                if not is_optional:
                    entity_type_map[entity_type]['uses'].append(field_name)
                else:
                    entity_type_map[entity_type]['opt_uses'].append(field_name)

    type_name = CheckIfAbstractTypeExists(ontology)

    parts = type_name.split('_')

    required_points_by_type = {}
    optional_points_by_type = {}
    all_required_points = set()
    all_optional_points = set()

    # Build forward maps
    for key in parts:
        if key in entity_type_map:
            uses = entity_type_map[key]['uses']
            opt_uses = entity_type_map[key].get('opt_uses', [])
            required_points_by_type[key] = set(uses)
            optional_points_by_type[key] = set(opt_uses)
            all_required_points.update(uses)
            all_optional_points.update(opt_uses)
        else:
            if key != "SENSOR":
                print(colored(f"Warning: Abstract type '{key}' not found in ontology!", "yellow"))

    # Build reverse map: field -> contributing abstract types
    field_to_types = defaultdict(set)
    for key, fields in required_points_by_type.items():
        for field in fields:
            field_to_types[field].add(key)

    # Detect and strip redundant abstract components
    redundant_types = []
    for key in parts[1:]:
        if key not in required_points_by_type and key not in optional_points_by_type:
            continue

        other_keys = [k for k in parts if k != key and (k in required_points_by_type or k in optional_points_by_type)]

        others_combined_required = set().union(*(required_points_by_type.get(k, set()) for k in other_keys))
        unique_required = required_points_by_type.get(key, set()) - others_combined_required

        others_combined_optional = set().union(*(optional_points_by_type.get(k, set()) for k in other_keys))
        unique_optional = optional_points_by_type.get(key, set()) - others_combined_optional

        if not unique_required and not unique_optional:
            redundant_types.append(key)

    if redundant_types:
        print(colored("\nRedundant abstract types (do not contribute unique required or optional points):", "red", attrs=["bold"]))
        for rt in redundant_types:
            print(colored(f"- {rt}", "red"))

    filtered_keys = [k for k in parts if k not in redundant_types]

    # Rebuild sets after removing redundant components
    all_required_points = set()
    all_optional_points = set()
    for key in filtered_keys:
        if key in entity_type_map:
            uses = entity_type_map[key].get('uses', [])
            opt_uses = entity_type_map[key].get('opt_uses', [])
            all_required_points.update(uses)
            all_optional_points.update(opt_uses)

    matched_points = set()

    while True:
        point_list_input = input(
            "\nEnter a comma-separated list of observed points "
            "(press 'f' to view full required/optional point lists, press 'q' to quit): "
        ).strip().lower()

        if point_list_input == "q":
            print(colored("\nExiting point comparison loop.", "cyan"))
            break
        elif point_list_input == "f":
            sorted_required = sorted(all_required_points)
            sorted_optional = sorted(all_optional_points)
            max_len = max(len(sorted_required), len(sorted_optional))
            required_col = sorted_required + [""] * (max_len - len(sorted_required))
            optional_col = sorted_optional + [""] * (max_len - len(sorted_optional))

            print("\n" + colored("Required points".ljust(50), "yellow") + colored(" Optional points", "cyan"))
            print("_" * 50 + " " + "_" * 50)
            for req, opt in zip(required_col, optional_col):
                req_str = colored(req.ljust(50), "yellow")
                opt_str = colored(opt, "cyan")
                print(f"{req_str} {opt_str}")
            continue

        observed_points = {p.strip() for p in point_list_input.split(',') if p.strip()}
        matched_points = observed_points

        found_required = all_required_points & matched_points
        missing_required = all_required_points - matched_points
        found_optional = all_optional_points & matched_points
        unexpected_points = matched_points - (all_required_points | all_optional_points)

        if found_required:
            print(colored(f"\nFound required points ({len(found_required)}):", "green"))
            for p in sorted(found_required):
                print(colored(f"- {p}", "green"))

        if found_optional:
            print(colored(f"\nFound optional points ({len(found_optional)}):", "green"))
            for p in sorted(found_optional):
                print(colored(f"- {p}", "green"))

        if missing_required:
            print(colored(f"\nMissing required points ({len(missing_required)}):", "red"))

            # Build list of tuples (point, types)
            missing_with_sources = []
            for p in sorted(missing_required):
                sources = [k for k, v in required_points_by_type.items() if p in v]
                missing_with_sources.append((p, sources))

            # Determine max left column width for alignment
            max_point_len = max(len(p) for p, _ in missing_with_sources)
            align_width = max_point_len + 4  # padding for spacing and arrows

            for p, sources in missing_with_sources:
                src_text = f"from abstract type(s): {', '.join(sources)}" if sources else "from abstract type(s): N/A"
                print(
                    colored(f"- {p.ljust(align_width, ' ')}", "red")
                    + colored(f"----> {src_text}", "yellow")
                )

        if unexpected_points:
            print(colored(f"\nUnexpected points (not defined in type) ({len(unexpected_points)}):", "red"))
            for p in sorted(unexpected_points):
                print(colored(f"- {p}", "red"))

        if missing_required or unexpected_points:
            print(colored("\nPlease enter more points to complete the required set and remove unexpected ones.", "cyan"))
        else:
            print(colored("\nThe list of points is a 100% match!", "green", attrs=["bold"]))
            break


def CheckIfAbstractTypeExists(ontology):
    input_type = input("Enter constructed typeName: ").strip()
    input_parts = input_type.split('_')
    if len(input_parts) < 2:
        print("Invalid input: must include at least one prefix and one component.")
        return False, None

    input_prefix = input_parts[0]
    input_components = input_parts[1:]

    for tns in ontology.universe.GetEntityTypeNamespaces():
        for existing_type in tns.valid_types_map.keys():
            if existing_type == input_type:
                print(colored('\n' + existing_type + ' exists in ontology', 'green'))
                return input_type

            existing_parts = existing_type.split('_')
            if len(existing_parts) < 2:
                continue

            existing_prefix = existing_parts[0]
            existing_components = existing_parts[1:]

            if (existing_prefix == input_prefix and set(existing_components) == set(input_components) and existing_components != input_components):
                # Same components, different order = permutation match
                print(colored(f"\n{input_type} is a permutation of an existing abstract type in ABSTRACT.yaml!", "yellow"))
                print(colored(f"Conflicting type: {existing_type}", "yellow"))
                return input_type

    print(colored('\n' + input_type + ' does not exist in ontology', 'yellow'))
    return input_type

