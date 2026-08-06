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
import xlwings as xw
import pandas as pd
import yaml
import os
from itertools import permutations

from lib import model
from lib.model import StandardField
from yamlformat.validator.field_lib import FIELD_INCREMENT_REGEX
from pathlib import Path

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


def CheckIfAbstractTypeExists(constructed_type):
    # Prompt the user
    if constructed_type == None:
        typeName = input("Enter constructed typeName: ").strip()
    else:
        typeName = constructed_type.strip()

    # Extract general type (everything before the first underscore)
    general_type = typeName.split("_")[0]

    # Build path to the YAML file
    base_path = r"C:\Users\ErikAadalen\Documents\digitalbuildings\ontology\yaml\resources\HVAC\entity_types"
    file_path = os.path.join(base_path, f"{general_type}.yaml")

    # Check if file exists
    if not os.path.isfile(file_path):
        print(f"Ontology file for {general_type} does not exist at {file_path}")
        return

    # Load YAML
    with open(file_path, "r") as f:
        ontology_data = yaml.safe_load(f)

    # Check if exact type exists
    if typeName in ontology_data:
        print(colored('\n' + typeName + ' exists in ontology', 'green'))
        return

    # Check for permutation
    user_components = typeName.split("_")
    for existing_type in ontology_data.keys():
        if sorted(existing_type.split("_")) == sorted(user_components):
            print(colored(f"\n{typeName} is a permutation of an existing type", "yellow"))
            print(colored(f"Conflicting type: {existing_type}", "yellow"))
            return

    # If neither exact match nor permutation
    print(colored('\n' + typeName + ' does not exist in ontology', 'red'))


def CompareFieldsToSpecifiedType(general_types_data, secondary_general_types_data, abstract_data, secondary_abstract_data, constructed_type, standard_field_names):
    """Prompt user for constructed typeName, load ABSTRACT.yaml, collect required/optional
    fields for the abstract components, then prompt for a comma-separated list of
    standardFieldNames and categorize them against the required/optional sets.

    Produces four categories:
      - entered fields found in required
      - entered fields found in optional
      - entered fields not found in either
      - required fields not provided by the user
    """

    # Prompt user for constructed typeName
    if constructed_type is None:
        type_name = input("Enter constructed typeName: ").strip()
    else:
        type_name = constructed_type.strip()

    if not type_name:
        if constructed_type is None and standard_field_names is None:
            print("❌ No typeName provided.")
            return
        else:
            return False, None, False

    parts = type_name.split("_")
    if len(parts) < 2:
        if constructed_type is None and standard_field_names is None:
            print("❌ Invalid format. Expected at least one abstract after the general prefix.")
            return
        else:
            return False, None, False

    general_type = parts[0]
    abstract_types = parts[1:]

    # Collect required (uses) and optional (opt_uses) fields across all abstracts
    all_required_fields = set()
    all_optional_fields = set()
    required_field_to_abstracts = {}
    missing_abstracts = []
    missing_general_types = []

    # ----------------------------
    # Load GENERAL TYPES
    # ----------------------------
    if not general_types_data:
        general_types_path = (Path(__file__).parent/ "../../../ontology/yaml/resources/HVAC/entity_types/GENERALTYPES.yaml")
        with open(general_types_path, "r") as f:
            general_types_data = yaml.safe_load(f)
        secondary_general_types_path = (Path(__file__).parent/ "../../../ontology/yaml/resources/entity_types/global.yaml")
        with open(secondary_general_types_path, "r") as f:
            secondary_general_types_data = yaml.safe_load(f)
    try:
        info = general_types_data.get(general_type)
        secondary_info = secondary_general_types_data.get(general_type)

        if not info and not secondary_info:
            missing_general_types.append(general_type)

        if info != None:
            opt_uses = info.get("opt_uses", []) or []
            for field in opt_uses:
                all_optional_fields.add(str(field).strip().lower())
        if secondary_info != None:
            secondary_opt_uses = secondary_info.get("opt_uses", []) or []
            for field in secondary_opt_uses:
                all_optional_fields.add(str(field).strip().lower())

    except Exception:
        print(f"⚠️ Error pulling data from: {general_type}")

    # ----------------------------
    # Load ABSTRACT TYPES
    # ----------------------------

    for abstract_type in abstract_types:
        if not abstract_data:
            abstract_path = (Path(__file__).parent/ "../../../ontology/yaml/resources/HVAC/entity_types/ABSTRACT.yaml")
            with open(abstract_path, "r") as f:
                abstract_data = yaml.safe_load(f)
            secondary_abstract_path = (Path(__file__).parent/ "../../../ontology/yaml/resources/entity_types/ABSTRACT.yaml")
            with open(secondary_abstract_path, "r") as f:
                secondary_abstract_data = yaml.safe_load(f)
        try:
            info = abstract_data.get(abstract_type)
            for item in info.get("implements", []) or []:
                if item.startswith("/") == True:
                    for item in secondary_abstract_data.get(item.removeprefix("/")).get("uses", []):
                        info.setdefault("uses", []).append(item)
            if not info:
                missing_abstracts.append(abstract_type)
                continue

            uses = info.get("uses", []) or []
            opt_uses = info.get("opt_uses", []) or []

            for field in uses:
                norm_field = str(field).strip().lower()
                all_required_fields.add(norm_field)
                required_field_to_abstracts.setdefault(norm_field, set()).add(abstract_type)

            for field in opt_uses:
                all_optional_fields.add(str(field).strip().lower())
        except Exception:
            print(f"⚠️ Abstract not found in ABSTRACT.yaml: {abstract_type}")

    norm_required = set(all_required_fields)
    norm_optional = set(all_optional_fields)
    combined_defined = norm_required | norm_optional

    if missing_abstracts and constructed_type is None and standard_field_names is None:
        print("⚠️ Missing abstracts (not found in ABSTRACT.yaml):")
        for a in missing_abstracts:
            print(f"  - {a}")
    elif missing_abstracts:
        return False, missing_abstracts, False

    # Prompt user for standardFieldNames to check
    if standard_field_names is None:
        raw = input("Enter list of comma-separated standardFieldNames: ").strip()
    else:
        raw = ",".join(str(v) for v in standard_field_names).strip()

    if not raw:
        if constructed_type is not None and standard_field_names is not None:
            return False, None, True

    observed = {p.strip().lower() for p in raw.split(",") if p.strip()}

    # Categorize
    found_in_required = sorted(observed & norm_required)
    found_in_optional = sorted(observed & norm_optional)
    not_found = sorted(observed - combined_defined)
    required_missing = sorted(norm_required - observed)

    # Print concise categorized results
    if constructed_type is None and standard_field_names is None:
        print(colored(f"\nFound required points ({len(found_in_required)}):", "green"))
        for p in found_in_required:
            print(colored(f"  - {p}", "green"))

        print(colored(f"\nFound optional points ({len(found_in_optional)}):", "green"))
        for p in found_in_optional:
            print(colored(f"  - {p}", "green"))

        print(colored(f"\nUnexpected points (not defined in type) ({len(not_found)}):", "red"))
        for p in not_found:
            print(colored(f"  - {p}", "red"))

        print(colored(f"\nMissing required points ({len(required_missing)}):", "red"))
        for p in required_missing:
            abstracts = ", ".join(sorted(required_field_to_abstracts.get(p, [])))
            print(colored(f"  - {p}  (from: {abstracts})", "red"))

    if not not_found and not required_missing:
        return True, None, False
    else:
        return False, None, False


def load_excel(path):
    """
    Loads the Excel file into a pandas DataFrame using xlwings.
    Reads the entire used range, ignoring filters and hidden rows.
    Strips column names for consistent validation.
    """
    try:
        wb = xw.Book(path)
        sheet = wb.sheets[0]  # first sheet, adjust if needed

        # Read the full used range (ignores filters)
        df = sheet.used_range.options(pd.DataFrame, header=1, index=False).value

        # Sanitize column names
        df.columns = [str(col).strip() for col in df.columns]

        return df

    except FileNotFoundError:
        print(f"❌ File not found: {path}")
    except PermissionError:
        print(f"❌ Permission denied: The file '{path}' is likely open in another program. Please close it and try again.")
    except Exception as e:
        print(f"❌ Unexpected error while reading the file: {e}")

    return None