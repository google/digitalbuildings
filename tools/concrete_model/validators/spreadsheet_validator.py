# Copyright 2022 Google LLC
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
"""Module to validate a google sheets spreadsheet."""

import collections
import logging
from typing import Any, Dict, List

from google3.third_party.digitalbuildings.tools.concrete_model.model.constants import ALL_CONNECTION_HEADERS
from google3.third_party.digitalbuildings.tools.concrete_model.model.constants import ALL_ENTITY_HEADERS
from google3.third_party.digitalbuildings.tools.concrete_model.model.constants import ALL_FIELD_HEADERS
from google3.third_party.digitalbuildings.tools.concrete_model.model.constants import ALL_SITE_HEADERS
from google3.third_party.digitalbuildings.tools.concrete_model.model.constants import ALL_STATE_HEADERS
from google3.third_party.digitalbuildings.tools.concrete_model.model.constants import BUILDING_CODE
from google3.third_party.digitalbuildings.tools.concrete_model.model.constants import CONNECTIONS
from google3.third_party.digitalbuildings.tools.concrete_model.model.constants import ENTITIES
from google3.third_party.digitalbuildings.tools.concrete_model.model.constants import ENTITY_CODE
from google3.third_party.digitalbuildings.tools.concrete_model.model.constants import ENTITY_FIELDS
from google3.third_party.digitalbuildings.tools.concrete_model.model.constants import REQUIRED_CONNECTION_HEADERS
from google3.third_party.digitalbuildings.tools.concrete_model.model.constants import REQUIRED_ENTITY_HEADERS
from google3.third_party.digitalbuildings.tools.concrete_model.model.constants import REQUIRED_FIELD_HEADERS
from google3.third_party.digitalbuildings.tools.concrete_model.model.constants import REQUIRED_SITE_HEADERS
from google3.third_party.digitalbuildings.tools.concrete_model.model.constants import REQUIRED_STATE_HEADERS
from google3.third_party.digitalbuildings.tools.concrete_model.model.constants import SITES
from google3.third_party.digitalbuildings.tools.concrete_model.model.constants import SOURCE_ENTITY_CODE
from google3.third_party.digitalbuildings.tools.concrete_model.model.constants import STANDARD_FIELD_NAME
from google3.third_party.digitalbuildings.tools.concrete_model.model.constants import STATES
from google3.third_party.digitalbuildings.tools.concrete_model.model.constants import TARGET_ENTITY_CODE
from google3.third_party.digitalbuildings.tools.concrete_model.validators.spreadsheet_error import ConnectionDependencyError
from google3.third_party.digitalbuildings.tools.concrete_model.validators.spreadsheet_error import CrossSheetDependencyError
from google3.third_party.digitalbuildings.tools.concrete_model.validators.spreadsheet_error import DuplicateCodeError
from google3.third_party.digitalbuildings.tools.concrete_model.validators.spreadsheet_error import MissingSpreadsheetValueError
from google3.third_party.digitalbuildings.tools.concrete_model.validators.spreadsheet_error import SpreadsheetHeaderError

_COLUMN_HEADER_INDEX = 1
_ROW_START_INDEX = 2


class SpreadsheetValidator(object):
  """Runs validations on a spreadsheet and logs results."""

  def __init__(self, filepath: str):
    self.filepath = filepath

  def Validate(self, parsed_spreadsheet: Dict[str, List[Dict[str,
                                                             str]]]) -> bool:
    """Performs initial validation on a concrete model spreadsheet.

    This method validates the following in order:
      1. All column headers are present in a spreadsheet. All is defined in
        constants.py
      2. If the above validation passes then a subset of those headers are
        validated such that they contain cell values for every row in the
        spreadsheet.
      3. Validates cell values referenced in multiple sheets exist.

    Args:
      parsed_spreadsheet: A concrete model spreadsheet parsed into python data
        types.

    Returns:
      A boolean value indicating whether parsed_spreadsheet is valid.
    """
    validation_parameters = [
        (SITES, parsed_spreadsheet[SITES], REQUIRED_SITE_HEADERS,
         ALL_SITE_HEADERS),
        (ENTITIES, parsed_spreadsheet[ENTITIES], REQUIRED_ENTITY_HEADERS,
         ALL_ENTITY_HEADERS),
        (ENTITY_FIELDS, parsed_spreadsheet[ENTITY_FIELDS],
         REQUIRED_FIELD_HEADERS, ALL_FIELD_HEADERS),
        (STATES, parsed_spreadsheet[STATES], REQUIRED_STATE_HEADERS,
         ALL_STATE_HEADERS),
        (CONNECTIONS, parsed_spreadsheet[CONNECTIONS],
         REQUIRED_CONNECTION_HEADERS, ALL_CONNECTION_HEADERS)
    ]
    validation_errors = []
    is_valid = True

    entities_sheet = parsed_spreadsheet[ENTITIES]
    validation_errors += self._ValidateEntityCodes(entities_sheet)
    for parameter_list in validation_parameters:
      validation_errors += self._ValidateHeaders(
          table=parameter_list[0],
          parsed_sheet=parameter_list[1],
          column_headers=parameter_list[3])
    # Validate spreadsheet contents only after required spreadsheet headers
    # are present.
    if not validation_errors:
      for parameter_list in validation_parameters:
        validation_errors += self._ValidateContents(
            table=parameter_list[0],
            parsed_sheet=parameter_list[1],
            col_headers_values=parameter_list[2])
      validation_errors += self._ValidateAcrossSheets(
          parsed_spreadsheet=parsed_spreadsheet)
      validation_errors += self._ValidateConnections(
          parsed_spreadsheet=parsed_spreadsheet)
    if validation_errors:
      self._LogErrors(validation_errors=validation_errors)
      is_valid = False
    return is_valid

  def _ValidateContents(
      self, table: str, parsed_sheet: List[Dict[str, str]],
      col_headers_values: List[str]) -> List[MissingSpreadsheetValueError]:
    """Validates cell values for a given table in a concrete model spreadsheet.

    This method does not validate that all cells in a row are not empty. It only
    checks that the cells in columns keyed by column_headers are non-empty, and
    logs the results.

    Args:
      table: Name of the table to validate.
      parsed_sheet: List of dictionaries modeling rows containing cell values by
        column headers.
      col_headers_values: List of required column headers where no cell value is
        empty for a given column.

    Returns:
      A boolean value for whether parsed_sheet is valid.
    """
    validation_errors = []
    for row_number, row in enumerate(parsed_sheet, _ROW_START_INDEX):
      for header in col_headers_values:
        if not row[header]:
          validation_errors.append(
              MissingSpreadsheetValueError(
                  table=table,
                  row=row_number,
                  column=header,
                  message=f'{table} entry must have a {header}'))
    return validation_errors

  def _ValidateAcrossSheets(
      self, parsed_spreadsheet: Dict[str, List[Dict[str, str]]]
  ) -> List[CrossSheetDependencyError]:
    """Validates that cell values referencing values across sheets exist.

    Some values  in tables reference rows in other tables, e.g. states reference
    fields, and fields reference entities. This method validates that the
    elements references by one sheet exist in the sheet it is referencing.
    Connections can reference values in multiple sheets and are validated
    separately. See _ValidateConnections().

    Args:
      parsed_spreadsheet: A concrete model spreadsheet parsed into python data
        types.

    Returns:
      A list of SpreadsheetError instances.
    """
    validation_errors = []
    cross_sheet_list = [(STATES, ENTITY_FIELDS, STANDARD_FIELD_NAME,
                         STANDARD_FIELD_NAME),
                        (ENTITY_FIELDS, ENTITIES, ENTITY_CODE, ENTITY_CODE)]
    for cross_sheet_set in cross_sheet_list:
      source_table, target_table, source_column_header, target_column_header = cross_sheet_set
      for row_number, row in enumerate(parsed_spreadsheet[source_table],
                                       _ROW_START_INDEX):
        if row[source_column_header] not in (
            row[target_column_header]
            for row in parsed_spreadsheet[target_table]):
          validation_errors.append(
              CrossSheetDependencyError(
                  source_table=source_table,
                  target_table=target_table,
                  row=row_number,
                  column=source_column_header,
                  cell_value=row[source_column_header]))
    return validation_errors

  def _ValidateHeaders(
      self, table: str, parsed_sheet: List[Dict[str, str]],
      column_headers: List[str]) -> List[SpreadsheetHeaderError]:
    """Validates that a spreadsheet contains column headers.

    Args:
      table: Name of the table to validate.
      parsed_sheet: List of dictionaries modeling rows containing cell values by
        column headers.
      column_headers: List of column headers.

    Returns:
      A list of SpreadsheetError instances.
    """
    validation_errors = []
    parsed_headers = set()
    header_difference = set()
    for row in parsed_sheet:
      parsed_headers = parsed_headers.union(set(row.keys()))
      header_difference = header_difference.union(
          set(column_headers).difference(parsed_headers))
    if header_difference:
      for header in header_difference:
        validation_errors.append(
            SpreadsheetHeaderError(
                table=table,
                header=header,
                message=f'{table} missing required column header: {header}'))
    return validation_errors

  def _ValidateConnections(
      self, parsed_spreadsheet: Dict[str, List[Dict[str, str]]]
  ) -> List[ConnectionDependencyError]:
    """Validates connections in a concrete model spreadsheet.

    Some values in the connections table reference codes in both the entities
    and sites table. This method validates that codes in the connections table
    are present in either the entities table or the sites table.

    Args:
      parsed_spreadsheet: A concrete model spreadsheet parsed into python data
        types.

    Returns:
      A list of SpreadsheetError instances.
    """
    validation_errors = []
    connections_sheet = parsed_spreadsheet[CONNECTIONS]
    entities_sheet = parsed_spreadsheet[ENTITIES]
    sites_sheet = parsed_spreadsheet[SITES]
    # codes - set of all entity codes present in both the Entities and
    # Sites sheets
    codes = set(row[ENTITY_CODE] for row in entities_sheet).union(
        set(row[BUILDING_CODE] for row in sites_sheet))
    # TODO(b/236416344) Create better error message for connection errors.
    for row_number, connection in enumerate(connections_sheet,
                                            _ROW_START_INDEX):
      if connection[SOURCE_ENTITY_CODE] not in codes:
        validation_errors.append(
            ConnectionDependencyError(
                row=row_number,
                missing_code=connection[SOURCE_ENTITY_CODE],
                present_code=connection[TARGET_ENTITY_CODE]))
      if connection[TARGET_ENTITY_CODE] not in codes:
        validation_errors.append(
            ConnectionDependencyError(
                row=row_number,
                missing_code=connection[SOURCE_ENTITY_CODE],
                present_code=connection[TARGET_ENTITY_CODE]))
    return validation_errors

  def _ValidateEntityCodes(
      self, sheet: List[Dict[str, str]]) -> List[DuplicateCodeError]:
    """Validates that a spreadsheet does not contain duplicate entity codes.

    Args:
      sheet: A sheet to be validated for dulicate codes.

    Returns:
      A list of SpreadsheetError instances for duplicate entity codes.
    """
    validation_errors = []
    list_of_codes = [row[ENTITY_CODE] for row in sheet]
    duplicates = [
        code for code, count in collections.Counter(list_of_codes).items()
        if count > 1
    ]
    for duplicate in duplicates:
      validation_errors.append(
          DuplicateCodeError(
              code=duplicate,
              message=f'Entity Code: {duplicate} is defined more than once in {ENTITIES} table.'
          ))
    return validation_errors

  def _LogErrors(self, validation_errors: List[Any]) -> None:
    logging.basicConfig(
        filename=self.filepath,
        filemode='w',
        format='%(levelname)s - %(message)s',
    )
    logger = logging.getLogger()
    for error in validation_errors:
      logger.error(error)
