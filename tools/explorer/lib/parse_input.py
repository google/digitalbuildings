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
import yaml
import pandas as pd
import xlwings as xw
import os
import math
import re
import sys

# pylint: disable=g-importing-member
import colorama
from collections import defaultdict
from termcolor import colored
from itertools import zip_longest

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


def CompareFieldsToSpecifiedType(ontology, loadsheet_check, typeName, point_list_input):
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

    # Prompt for type name if running interactively
    if not loadsheet_check:
        type_name = CheckIfAbstractTypeExists(ontology, loadsheet_check)
    else:
        type_name = typeName

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

    if not loadsheet_check:
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

    else:
        matched_points = set(point_list_input)

        found_required = all_required_points & matched_points
        missing_required = all_required_points - matched_points
        found_optional = all_optional_points & matched_points
        unexpected_points = matched_points - (all_required_points | all_optional_points)

        if missing_required or unexpected_points:
            return False
        else:
            return True


def CheckIfAbstractTypeExists(ontology, loadsheet_check):
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
                if loadsheet_check == False:
                    print(colored('\n' + existing_type + ' exists in ontology', 'green'))
                return input_type

            existing_parts = existing_type.split('_')
            if len(existing_parts) < 2:
                continue

            existing_prefix = existing_parts[0]
            existing_components = existing_parts[1:]

            if (existing_prefix == input_prefix and set(existing_components) == set(input_components) and existing_components != input_components):
                # Same components, different order = permutation match
                if loadsheet_check == False:
                    print(colored(f"\n{input_type} is a permutation of an existing abstract type in ABSTRACT.yaml!", "yellow"))
                    print(colored(f"Conflicting type: {existing_type}", "yellow"))
                return input_type

    if loadsheet_check == False:
        print(colored('\n' + input_type + ' does not exist in ontology', 'yellow'))
    return input_type


def LoadsheetValidationChecks(ontology):
    def validate_loadsheet_columns(df):
        """
        Ensures that all the required columns are present in the loadsheet.
        """

        # Clean column names
        df.columns = [str(col).strip() for col in df.columns]

        required_columns = [
            "location", "controlProgram", "name", "type", "path", "deviceId", 
            "objectType", "objectId", "objectName", "units", "required", 
            "isMissing", "manuallyMapped", "building", "generalType", 
            "typeName", "assetName", "fullAssetPath", "standardFieldName"
        ]

        missing_columns = [col for col in required_columns if col not in df.columns]

        if missing_columns:
            print("❌ The following required columns are missing from the loadsheet:")
            for col in missing_columns:
                print(f" - {col}")
            return False
        else:
            return True

    def validate_no_leading_trailing_spaces(df):
        """
        Checks for and flags any leading or trailing spaces in listed columns.
        """

        columns_to_check = [
            "location", "controlProgram", "name", "type", "path", "deviceId",
            "objectType", "objectId", "objectName", "units", "required",
            "isMissing", "manuallyMapped", "building", "generalType",
            "typeName", "assetName", "fullAssetPath", "standardFieldName"
        ]
        failed_rows = []

        for col in columns_to_check:
            if col not in df.columns:
                # Skip missing columns — or optionally report them elsewhere
                continue

            # Only check rows where the value is a string
            for idx, val in df[col].items():
                if isinstance(val, str):
                    if val != val.strip():
                        excel_row = idx + 2  # Excel row numbering
                        failed_rows.append((excel_row, col, val))

        if failed_rows:
            print("❌ Leading or trailing spaces found in columns:")
            for row_num, col, val in failed_rows:
                print(f"Row {row_num}, column '{col}': '{val}'")
            return False
        else:
            return True

    def validate_required_column(df):
        """
        Validates that every row of the 'required' column only contains 'YES' or 'NO' (case-insensitive).
        """

        if 'required' not in df.columns:
            print("❌ Error: 'required' column not found.")
            return None

        df['required_cleaned'] = df['required'].astype(str).str.strip().str.upper()
        invalid_required = df[~df['required_cleaned'].isin(['YES', 'NO'])]

        if not invalid_required.empty:
            print("❌ Invalid entries in 'required' column:")
            for idx, _ in invalid_required.iterrows():
                print(f"Row {idx + 2}")
            return None  # Fail
        
        return df  # Pass

    def validate_required_flag_on_populated_rows(df):
        """
        Ensures that if any of the core identifying fields ('standardFieldName', etc.) are populated,
        then the 'required' column must be set to 'YES'.
        """

        # Sanitize column names
        df.columns = [str(col).strip() for col in df.columns]

        check_fields = ['standardFieldName']  # add other identifying fields if needed
        failed_rows = []

        for idx, row in df.iterrows():
            required = str(row.get('required_cleaned', row.get('required', ''))).strip().upper()

            # Identify non-empty fields correctly (ignore NaN)
            non_blank_fields = {}
            for field in check_fields:
                value = row.get(field, None)
                if pd.notna(value) and str(value).strip() != "":
                    non_blank_fields[field] = str(value).strip()

            if non_blank_fields and required != 'YES':
                # Use first non-blank field for error message
                failing_field, value = next(iter(non_blank_fields.items()))
                excel_row = idx + 2  # Excel-style row number
                failed_rows.append((excel_row, failing_field, value, required))

        if failed_rows:
            print("❌ Rows with populated fields must have required='YES':")
            for row_num, field, value, required in failed_rows:
                print(f"Row {row_num}: {field}='{value}', required='{required}'")
            return False
        else:
            return True

    def validate_required_fields_populated(df):
        """
        Ensures the following fields are populated for every row where 'required' = 'YES' and 'isMissing' = 'NO.
        """

        columns_to_check = [ 
            "location", "controlProgram", "name", "type", "path",
            "deviceId", "objectType", "objectId"
        ]

        failed_rows = []

        # Normalize case and strip for filtering columns
        required_mask = df['required'].astype(str).str.strip().str.upper() == 'YES'
        not_missing_mask = df['isMissing'].astype(str).str.strip().str.upper() == 'NO'

        filtered_df = df[required_mask & not_missing_mask]

        for idx, row in filtered_df.iterrows():
            missing_cols = []
            for col in columns_to_check:
                val = str(row.get(col, '')).strip()
                if val == '' or val.lower() == 'nan':
                    missing_cols.append(col)

            if missing_cols:
                excel_row = idx + 2  # Excel row numbering
                failed_rows.append((excel_row, missing_cols))

        if failed_rows:
            print("❌ Rows with required='YES' and isMissing='NO' must have these fields populated:")
            for row_num, cols in failed_rows:
                print(f"Row {row_num}: Missing or blank columns: {cols}")
            return False
        else:
            return True

    def validate_missing_required_rows(df):
        """
        Ensures that the following fields are blank or non-blank for every row where
        'required' = 'YES' and 'isMissing' = 'YES'.
        Works safely with DataFrames loaded via xlwings (where blanks may appear as None).
        """

        must_be_blank = [
            "location", "controlProgram", "name", "type", "path",
            "deviceId", "objectType", "objectId", "objectName"
        ]

        must_not_be_blank = [
            "building", "generalType", "typeName",
            "assetName", "fullAssetPath", "standardFieldName"
        ]

        failed_rows = []

        # Normalize required/isMissing columns for filtering
        required_yes = (
            df.get('required', pd.Series()).astype(str).str.strip().str.upper() == 'YES'
        )
        is_missing_yes = (
            df.get('isMissing', pd.Series()).astype(str).str.strip().str.upper() == 'YES'
        )
        filtered_df = df[required_yes & is_missing_yes]

        for idx, row in filtered_df.iterrows():
            # Excel row = dataframe index + 2 (1 for header + 1 for 1-based Excel indexing)
            excel_row = idx + 2
            issues = []

            # Check must-be-blank fields
            for col in must_be_blank:
                val = row.get(col, None)
                if val is None:
                    continue
                # Convert to string safely
                sval = str(val).strip()
                if sval and sval.lower() not in ('nan', 'none'):
                    issues.append(f"{col} should be blank (found '{sval}')")

            # Check must-not-be-blank fields
            for col in must_not_be_blank:
                val = row.get(col, None)
                sval = "" if val is None else str(val).strip()
                if not sval or sval.lower() in ('nan', 'none'):
                    issues.append(f"{col} must not be blank")

            if issues:
                failed_rows.append((excel_row, issues))

        if failed_rows:
            print("❌ Validation failed for rows where required='YES' and isMissing='YES':")
            for row_num, issues in failed_rows:
                print(f"Row {row_num}:")
                for issue in issues:
                    print(f"  - {issue}")
            return False
        else:
            return True

    def validate_all_standard_field_names(df):
        """
        Ensures all standardFieldNames are valid telemetry fields within the DBO. 
        """
        required_yes = df[df['required_cleaned'] == 'YES']
        invalid_rows = []

        for idx, row in required_yes.iterrows():
            field_name = str(row.get('standardFieldName', '')).strip()
            excel_row = idx + 2  # Adjust for header + zero indexing

            if field_name == "":
                invalid_rows.append((excel_row, field_name))

            if not field_name:
                invalid_rows.append((excel_row, "<BLANK>"))
                continue

            global_namespace_string = 'GLOBAL'
            namespace_list = ['', 'HVAC', 'LIGHTING']
            valid_namespaces = []
            for namespace in namespace_list:
                standard_field = model.StandardField(namespace, field_name)
                if ontology.IsFieldValid(standard_field):
                    if not namespace:
                        valid_namespaces.append(global_namespace_string)
                    else:
                        valid_namespaces.append(namespace)

            if not valid_namespaces:
                invalid_rows.append((excel_row, field_name))

        if invalid_rows:
            print("❌ Invalid or missing 'standardFieldName' entries:")
            for excel_row, field in invalid_rows:
                print(f"Row {excel_row}: '{field}'")
            return False
        else:
            return True

    def validate_units(df, ontology):
        """
        Ensures that all units match the expected DBO units based on standardFieldName.

        Rules:
        - Only rows with required_cleaned == 'YES' are validated.
        - For standardFieldNames that include keywords like 'alarm', 'count', 'mode',
            the units column *must* contain 'no-units' (we accept common variants).
        - For other fields, words in the standardFieldName are looked up in the ontology's
            unit universe. If the ontology returns units for any word, the sheet unit must
            match one of the ontology units (normalized).
        - If the ontology returns no units for the field, the sheet unit is valid only if
            it's 'no-units' (or variant). Otherwise it's flagged.
        """

        # sanitize column names if not already done by load_excel
        df.columns = [str(col).strip() for col in df.columns]

        # Build mask for required == 'YES' (NaN-safe)
        required_series = df.get('required_cleaned', df.get('required', pd.Series()))
        required_mask = required_series.apply(lambda x: pd.notna(x) and str(x).strip().upper() == 'YES')
        required_yes = df[required_mask]

        invalid_unit_rows = []
        no_unit_keywords = ['alarm', 'count', 'mode']
        allowed_no_unit_values = {'no_units', 'no-units', 'no units', 'no_units'}  # normalized variants

        for idx, row in required_yes.iterrows():
            # Excel row number (header + 1)
            excel_row = idx + 2

            # standardFieldName (NaN-safe, stripped)
            sf_raw = row.get('standardFieldName', None)
            field = "" if pd.isna(sf_raw) else str(sf_raw).strip()

            # units from sheet normalized (lower + replace - and spaces with _)
            units_raw = row.get('units', None)
            unit_in_sheet = ""
            if pd.notna(units_raw):
                unit_in_sheet = str(units_raw).strip().lower().replace('-', '_').replace(' ', '_')

            # If field contains any of the no-unit keywords, require 'no-units'
            field_lower = field.lower()
            if any(keyword in field_lower for keyword in no_unit_keywords):
                if unit_in_sheet != 'no_units':
                    # Not acceptable: should be 'no-units'
                    invalid_unit_rows.append((excel_row, field or "<empty>", row.get('units', '')))
                continue  # done with this row

            # Otherwise, attempt to find units via ontology
            words = [w for w in field.split('_') if w.strip()] if field else []
            found_units = False
            valid_units_set = set()

            for word in words:
                w = word.strip().lower()
                if not w:
                    continue
                try:
                    units_map = ontology.universe.unit_universe.GetUnitsForMeasurement(w)
                    # units_map may be dict-like or iterable; normalize access
                    if units_map is None:
                        continue
                    if hasattr(units_map, 'keys'):
                        unit_keys = list(units_map.keys())
                    else:
                        unit_keys = list(units_map)
                    if unit_keys:
                        found_units = True
                        for u in unit_keys:
                            if u is None:
                                continue
                            # normalize ontology unit strings the same way as sheet units
                            normalized = str(u).lower().replace('-', '_').replace(' ', '_')
                            valid_units_set.add(normalized)
                except Exception:
                    # If ontology lookup fails for this word, ignore and continue trying other words
                    continue

            # If ontology provided no units for any word
            if not found_units:
                # accept 'no-units' (sheet) as valid; anything else is invalid
                if unit_in_sheet == 'no_units':
                    continue
                else:
                    invalid_unit_rows.append((excel_row, field or "<empty>", row.get('units', '')))
                    continue

            # If ontology did provide units, ensure sheet unit matches one of them
            if unit_in_sheet not in valid_units_set:
                invalid_unit_rows.append((excel_row, field or "<empty>", row.get('units', '')))

        # Report results
        if invalid_unit_rows:
            print("\n❌ Rows with units that do not match ontology units:")
            for excel_row, field, unit_val in invalid_unit_rows:
                print(f"Row {excel_row}: standardFieldName='{field}', units='{unit_val}'")
            return False

        return True

    def validate_full_asset_path(df):
        """
        Checks that 'fullAssetPath' follows the format 'building:generalType:assetName'
        for all rows where 'required' = 'YES', unless assetName is 'IGNORE'.
        """

        if 'fullAssetPath' not in df.columns:
            print("❌ Error: 'fullAssetPath' column not found.")
            return False

        required_yes = df[df['required_cleaned'] == 'YES']
        invalid_rows = []

        for idx, row in required_yes.iterrows():
            asset_name = str(row.get('assetName', '')).strip()
            if asset_name.upper() == 'IGNORE':
                continue  # Skip validation for these rows

            building = str(row.get('building', '')).strip()
            general_type = str(row.get('generalType', '')).strip()
            expected_path = f"{building}:{general_type}:{asset_name}"

            actual_path = str(row.get('fullAssetPath', '')).strip()
            excel_row = idx + 2

            if actual_path != expected_path:
                invalid_rows.append((excel_row, actual_path or "<BLANK>", expected_path))

        if invalid_rows:
            print("❌ Invalid 'fullAssetPath' entries (expected 'building:generalType:assetName'):")
            for excel_row, actual, expected in invalid_rows:
                print(f"Row {excel_row}: actual='{actual}', expected='{expected}'")
            return False
        else:
            return True

    def validate_object_type_for_command_status(df):
        """
        Validates that standardFieldNames containing 'run_command', 'run_status', 'damper_command', 'damper_status',
        'valve_command', or 'valve_status' have an objectType of 'BV', 'BI', 'BO', or 'MSV'. Only enforced when required='YES' and isMissing='NO'.
        """

        target_keywords = {
            'run_command', 'run_status',
            'damper_command', 'damper_status',
            'valve_command', 'valve_status'
        }
        valid_object_types = {'BV', 'BI', 'BO', 'MSV'}
        failed_rows = []

        # Filter to required == YES and isMissing == NO
        required_yes = df['required'].astype(str).str.strip().str.upper() == 'YES'
        is_missing_no = df['isMissing'].astype(str).str.strip().str.upper() == 'NO'
        filtered_df = df[required_yes & is_missing_no]

        for idx, row in filtered_df.iterrows():
            standard_field = str(row.get('standardFieldName', '')).strip().lower()
            object_type = str(row.get('objectType', '')).strip().upper()
            excel_row = idx + 2

            if any(keyword in standard_field for keyword in target_keywords):
                if object_type not in valid_object_types:
                    failed_rows.append((excel_row, standard_field, object_type or "<BLANK>"))

        if failed_rows:
            print("❌ Invalid objectType for control/status-related standardFieldNames (required='YES' and isMissing='NO'):")
            for row_num, field, obj_type in failed_rows:
                print(f"Row {row_num}: standardFieldName='{field}', objectType='{obj_type}' (must be one of {sorted(valid_object_types)})")
            return False
        else:
            return True

    def validate_object_type_for_measurement_points(df):
        """
        Validates that standardFieldNames ending in '_sensor', '_setpoint', '_count', or '_percentage'
        have an objectType of 'AV', 'AI', or 'AO'. Only enforced when required='YES' and isMissing='NO'.
        """

        target_suffixes = ['_sensor', '_setpoint', '_count', '_percentage']
        valid_object_types = {'AV', 'AI', 'AO'}
        failed_rows = []

        # Filter to required == YES and isMissing == NO
        required_yes = df['required'].astype(str).str.strip().str.upper() == 'YES'
        is_missing_no = df['isMissing'].astype(str).str.strip().str.upper() == 'NO'
        filtered_df = df[required_yes & is_missing_no]

        for idx, row in filtered_df.iterrows():
            standard_field = str(row.get('standardFieldName', '')).strip().lower()
            object_type = str(row.get('objectType', '')).strip().upper()
            excel_row = idx + 2

            if any(suffix in standard_field for suffix in target_suffixes):
                if object_type not in valid_object_types:
                    failed_rows.append((excel_row, standard_field, object_type or "<BLANK>"))

        if failed_rows:
            print("❌ Invalid objectType for sensor/setpoint/count/percentage standardFieldNames (required='YES' and isMissing='NO'):")
            for row_num, field, obj_type in failed_rows:
                print(f"Row {row_num}: standardFieldName='{field}', objectType='{obj_type}' (must be one of {sorted(valid_object_types)})")
            return False
        else:
            return True

    def validate_alarm_types(df):
        """
        Ensures that standardFieldNames containing 'alarm' have a type value of 'BALM'.
        """
        
        required_yes = df[df['required_cleaned'] == 'YES']
        invalid_rows = []

        for idx, row in required_yes.iterrows():
            field_name = str(row.get('standardFieldName', '')).lower()
            field_type = str(row.get('type', '')).strip()
            excel_row = idx + 2

            if 'alarm' in field_name and field_type != 'BALM':
                invalid_rows.append((excel_row, field_name, field_type))

        if invalid_rows:
            print("❌ Rows where standardFieldName contains 'alarm' but type is not 'BALM':")
            for row_num, sf_name, t_val in invalid_rows:
                print(f"Row {row_num}: standardFieldName='{sf_name}', type='{t_val}'")
            return False
        return True

    def validate_unique_standard_fields_per_asset(df):
        """
        Confirms that each standardFieldName is unique within a given assetName,
        excluding rows where assetName is 'IGNORE'.
        """

        required_yes = df[df['required_cleaned'] == 'YES']
        # Exclude rows where assetName is 'IGNORE'
        required_yes = required_yes[required_yes['assetName'].str.strip().str.upper() != 'IGNORE']

        duplicates = []

        # Group by assetName and look for duplicated standardFieldNames
        grouped = required_yes.groupby('assetName')

        for asset, group in grouped:
            duplicates_in_group = group[group.duplicated('standardFieldName', keep=False)]
            if not duplicates_in_group.empty:
                for idx, row in duplicates_in_group.iterrows():
                    excel_row = idx + 2
                    duplicates.append((excel_row, asset, row['standardFieldName']))

        if duplicates:
            print("❌ Duplicate standardFieldNames found for the same assetName:")
            for row_num, asset, field in duplicates:
                print(f"Row {row_num}: assetName='{asset}', standardFieldName='{field}'")
            return False

        return True

    def validate_unique_typename_per_asset(df):
        """
        Ensures that each assetName maps to a single unique typeName.
        Ignores rows where typeName is blank or NaN.
        """

        # Sanitize column names
        df.columns = [str(col).strip() for col in df.columns]

        # Filter out rows where 'typeName' is blank or NaN
        df_filtered = df[df['typeName'].apply(lambda x: pd.notna(x) and str(x).strip() != '')]

        grouped = df_filtered.groupby('assetName')

        failed_assets = []

        for asset_name, group in grouped:
            type_names = group['typeName'].apply(lambda x: str(x).strip()).unique()
            if len(type_names) > 1:
                for idx in group.index:
                    excel_row = idx + 2  # Excel rows are 1-indexed (+ header)
                    failed_assets.append((excel_row, asset_name, type_names.tolist()))

        if failed_assets:
            print("❌ Each assetName must have only one unique typeName:")
            seen = set()
            for _, asset, type_names in failed_assets:
                if asset not in seen:
                    print(f"assetName='{asset}' has multiple typeNames: {type_names}")
                    seen.add(asset)
            return False
        else:
            return True

    def validate_typenames_exist(df, ontology):
        """
        Ensures every typeName listed in the required rows of the spreadsheet exists in the ontology.
        Only reports once per unique (assetName, typeName) pair.
        """

        # Filter to only required rows
        required_yes = df[df['required_cleaned'] == 'YES']

        # Gather all valid type names from the ontology
        all_valid_types = set()
        for ns in ontology.universe.GetEntityTypeNamespaces():
            all_valid_types.update(ns.valid_types_map.keys())

        # Track invalid (assetName, typeName) pairs
        invalid_assets = set()

        for idx, row in required_yes.iterrows():
            type_name = str(row.get('typeName', '')).strip()
            asset_name = str(row.get('assetName', '')).strip()
            if type_name and type_name not in all_valid_types:
                invalid_assets.add((asset_name, type_name))

        # Output result
        if invalid_assets:
            print("❌ The following typeNames do not exist in the ontology:")
            for asset, type_name in sorted(invalid_assets):
                print(f"assetName='{asset}', typeName='{type_name}'")
            return False
        else:
            return True
        
    def validate_typename_matches_standard_fields(df, ontology):
        """
        Verifies that the set of standardFieldNames assigned to each assetName exactly matches 
        the expected set defined in the ontology for the given typeName.
        """

        # Sanitize column names
        df.columns = [str(col).strip() for col in df.columns]

        # Filter rows where required_cleaned is 'YES' (NaN-safe)
        required_yes = df[df['required_cleaned'].apply(lambda x: pd.notna(x) and str(x).strip().upper() == 'YES')]

        grouped = required_yes.groupby('assetName')

        failed_assets = []

        for asset_name, group in grouped:
            # Only include non-empty standardFieldNames
            standard_fields = [
                str(val).strip()
                for val in group['standardFieldName']
                if pd.notna(val) and str(val).strip() != ''
            ]
            type_name = group['typeName'].iloc[0] if pd.notna(group['typeName'].iloc[0]) else ''

            if not CompareFieldsToSpecifiedType(ontology, True, type_name, standard_fields):
                for idx in group.index:
                    excel_row = idx + 2
                    failed_assets.append((excel_row, asset_name, type_name))

        if failed_assets:
            print("❌ standardFieldNames do not 100% match typeName definitions:")
            seen = set()
            for _, asset, type_name in failed_assets:
                if asset not in seen:
                    print(f"assetName='{asset}', typeName='{type_name}'")
                    seen.add(asset)
            return False
        else:
            return True

    def validate_permuted_abstract_types(df, ontology):
        """
        Checks that no unique typeName in the loadsheet is a permutation of an existing
        abstract type in the ontology.

        Only non-blank typeNames are considered. 
        Reports one conflict per typeName.
        """
        # Get unique non-blank typeNames from the loadsheet
        type_names_in_sheet = df['typeName'].dropna().astype(str).str.strip()
        unique_type_names = type_names_in_sheet[type_names_in_sheet != ''].unique()

        # Prepare conflicts list
        permuted_conflicts = []

        # Loop through each unique typeName
        for type_name in unique_type_names:
            # Split into prefix and components
            parts = type_name.split('_')
            if len(parts) < 2:
                continue  # skip underspecified types
            prefix = parts[0]
            components = parts[1:]

            # Compare against all existing ontology typeNames
            for tns in ontology.universe.GetEntityTypeNamespaces():
                for existing_type in tns.valid_types_map.keys():
                    if existing_type == type_name:
                        continue  # skip exact match

                    existing_parts = existing_type.split('_')
                    if len(existing_parts) < 2:
                        continue
                    existing_prefix = existing_parts[0]
                    existing_components = existing_parts[1:]

                    # Check for same prefix and same set of components (permutation)
                    if prefix == existing_prefix and set(components) == set(existing_components):
                        permuted_conflicts.append((type_name, existing_type))
                        break  # only report first conflict per typeName

        # Report conflicts
        if permuted_conflicts:
            print("❌ Permuted abstract type conflicts detected:")
            for sheet_type, ontology_type in permuted_conflicts:
                # Find all assetNames using this typeName
                assets = df[df['typeName'].astype(str).str.strip() == sheet_type]['assetName'].unique()
                asset_list = ', '.join([str(a) for a in assets if a])
                print(f"typeName='{sheet_type}' (assets: {asset_list}) conflicts with existing ontology type '{ontology_type}'")
            return False

        return True

    file_path = input("Enter the absolute file path to your loadsheet: ").strip('"')
    print()

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

    # -----------------------
    # Main validation loop
    # -----------------------
    while True:
        df = load_excel(file_path)
        if df is None:
            return
        df_cleaned = None

        validations = [
            ("Loadsheet contains the correct columns", validate_loadsheet_columns, None),
            ("No leading or trailing spaces found in cells", validate_no_leading_trailing_spaces, None),
            ("All rows in 'required' column contain 'YES' or 'NO'", validate_required_column, None),
            ("All rows containing asset data are correctly marked with required='YES'", validate_required_flag_on_populated_rows, None),
            ("All necessary columns populated where required='YES' and isMissing='NO'", validate_required_fields_populated, None),
            ("All necessary columns populated where required='YES' and isMissing='YES'", validate_missing_required_rows, None),
            ("All standardFieldNames are valid", validate_all_standard_field_names, None),
            ("All units are valid and match with corresponding standardFieldNames", validate_units, ontology),
            ("All fullAssetPaths are valid", validate_full_asset_path, None),
            ("All binary standardFieldNames have binary objectType values", validate_object_type_for_command_status, None),
            ("All analog standardFieldNames have analog objectType values", validate_object_type_for_measurement_points, None),
            ("All alarms have the correct BALM type", validate_alarm_types, None),
            ("No duplicate standardFieldNames within a single asset", validate_unique_standard_fields_per_asset, None),
            ("All assetNames have exactly one typeName", validate_unique_typename_per_asset, None),
            ("All typeNames exist in the ontology", validate_typenames_exist, ontology),
            ("All standardFieldName sets are a 100% ontology match with their corresponding typeName", validate_typename_matches_standard_fields, ontology),
            ("No permuted abstract types found in ontology", validate_permuted_abstract_types, ontology)
        ]

        check_index = 0
        while check_index < len(validations):
            desc, func, arg = validations[check_index]

            # Run the check
            if func == validate_required_column:
                df_cleaned = func(df)
                result = df_cleaned is not None
            elif arg is not None:
                result = func(df_cleaned if df_cleaned is not None else df, arg)
            else:
                result = func(df_cleaned if df_cleaned is not None else df)

            # Handle failure
            if not result:
                while True:
                    choice = input(
                        f"\nPlease fix these issues. Then choose one of the following:\n"
                        "1) Rerun validation checks\n"
                        "2) Proceed with remaining checks despite failure\n"
                        "3) Quit\n"
                        "\nEnter choice: "
                    ).strip()

                    if choice == "1":
                        print("\nRerunning validation checks...\n")
                        break  # exit inner loop to rerun all validations
                    elif choice == "2":
                        print(f"\n⚠️ Proceeding with remaining checks despite failure: {desc}")
                        check_index += 1
                        break  # skip this failed check and continue
                    elif choice == "3":
                        print("\n👋 Exiting validation.")
                        return
                    else:
                        print("\n❌ Invalid choice. Please enter 1, 2, or 3.")

                if choice == "1":
                    break  # break out of validation loop to reload Excel and restart
            else:
                print(f"✅ {desc}")
                check_index += 1  # move to next validation

        else:
            # All validations completed
            print("\n🎉 All validations completed!")

            rerun = input("\nPress Enter to rerun all validation checks, or type 'q' to quit: ").strip().lower()
            if rerun == 'q':
                print("👋 Exiting validation.")
                break
            else:
                print("🔄 Rerunning validation checks...\n")

