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
"""Module to import google sheets or Building Configurations into ABEL."""

import os
from typing import Any, Dict, List

# pylint: disable=g-importing-member
from googleapiclient.discovery import Resource
from googleapiclient.http import HttpError

from model.constants import BODY_VALUE_RANGE_KEY
from model.constants import SITE_TYPE_NAME
from model.model_error import SpreadsheetAuthorizationError
from model.site import Site
from validate import handler


def _ImportSheetFromGoogleSheets(
    spreadsheet_id: str, named_range: str, google_sheets_service: Resource
) -> List[Dict[str, str]]:
  """Parses a single sheet into a list of python dictionaries.

  Calls the google sheets api to get a single sheet from a Google Sheets
  spreadsheet. Then, parses the result into python data types.

  Args:
    spreadsheet_id: Identifier for a Google Sheets spreadsheet.
    named_range: Name of the sheet, rows, and columns to write to in a Google
      Sheets spreadsheet. e.g. Entities!A1:Z1867
    google_sheets_service: A Google Python API Client discovery Resource
      instance with methods for interacting with the Google Sheets service.

  Returns:
    A list of Python dictionaries modeling rows in a spreadhsheet. Each
    dictionary(row) is composed of cell values keyed by column headers.

  Raises:
    SpreadsheetAuthorizationError: If the Google Sheets API request returns an
    error.
  """
  spreadsheet_rows = []
  try:
    sheet = google_sheets_service.spreadsheets()
    request = sheet.values().get(
        spreadsheetId=spreadsheet_id, range=named_range
    )
    google_sheets_spreadsheet = request.execute()
  except HttpError as http_error:
    raise SpreadsheetAuthorizationError(
        spreadsheet_id=spreadsheet_id,
        resp=http_error.resp,
        content=http_error.content,
    ) from http_error

  values = google_sheets_spreadsheet.get(BODY_VALUE_RANGE_KEY, [])
  if values:
    headers = dict(enumerate(values[0]))
    for row_index in range(1, len(values)):
      row = values[row_index]
      spreadsheet_rows.append(
          {
              headers[i]: row[i] if i < len(row) else []
              for i in range(len(headers))
          }
      )
  return spreadsheet_rows


def GetAllSheets(
    spreadsheet_id: str,
    spreadsheet_range: List[str],
    google_sheets_service: Resource,
) -> Dict[str, object]:
  """Parses a Google Sheets spreadsheet into a python dictionary.

  Args:
    spreadsheet_id: an alphanumeric identifier for a Google Sheets spreadsheet.
    spreadsheet_range: A list of table names.
    google_sheets_service: A resource object containing methods for interacting
      with the Google Sheets API.

  Returns:
    A dictionary of dictionaries modeling sheets in a spreadsheet keyed by table
    names.
  """
  google_spreadsheet_model = {}
  for sheet_name in spreadsheet_range:
    google_spreadsheet_model[sheet_name] = _ImportSheetFromGoogleSheets(
        spreadsheet_id, sheet_name, google_sheets_service
    )
  return google_spreadsheet_model


def DeserializeBuildingConfiguration(filepath: str) -> Dict[str, Any]:
  """Deserializes a building configuration into Instance Validator data types.

  Args:
    filepath: Path to a Building Configuration.

  Returns:
    A tuple where the first entry is an ABEL Site instance read from the
    building config and the second entry is a mapping of guids to Instance
    Validator EntityInstance instances.

  Raises:
    FileNotFoundError: Raised when path to building config does not exist.
  """
  if not os.path.exists(filepath):
    raise FileNotFoundError(f'{filepath} does not exist.')
  else:
    # Deserialize returns a tuple with a mapping of entity instances and config
    # mode block. Strip the config block and return with a Site instance.
    deserialized_bc = handler.Deserialize(yaml_files=[filepath])[0]
    site = None
    for instance in deserialized_bc.values():
      if instance.type_name == SITE_TYPE_NAME:
        site = instance
    del deserialized_bc[site.guid]
    abel_site = Site(code=site.code, guid=site.guid)
    return (abel_site, deserialized_bc)
