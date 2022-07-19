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
"""Tests for Import."""

import os

from absl.testing import absltest
from googleapiclient.discovery import build
from googleapiclient.http import HttpError
from googleapiclient.http import HttpMockSequence

from google3.third_party.digitalbuildings.tools.concrete_model.model import import_helper
from google3.third_party.digitalbuildings.tools.concrete_model.model.constants import SHEETS
from google3.third_party.digitalbuildings.tools.concrete_model.model.constants import V4
from google3.third_party.digitalbuildings.tools.concrete_model.tests.test_constants import TEST_BUILDING_CONFIG_PATH
from google3.third_party.digitalbuildings.tools.concrete_model.tests.test_constants import TEST_RESOURCES

_TEST_API_KEY = 'mock_api_key'


class ImportTest(absltest.TestCase):
  """Tests import methods for ABEL."""

  def testGetAllSheets(self):
    test_spreadsheet_range = ['Entities']
    test_request = os.path.join(TEST_RESOURCES, 'test_entities_sheet.json')
    mock_http = HttpMockSequence([({
        'status': '200'
    }, open(test_request, 'rb').read())])
    google_sheets_service = build(
        SHEETS, V4, http=mock_http, developerKey=_TEST_API_KEY)

    result_spreadsheet = import_helper.GetAllSheets(
        spreadsheet_id='mock_spreadsheet_id',
        spreadsheet_range=test_spreadsheet_range,
        google_sheets_service=google_sheets_service)

    self.assertNotEmpty(result_spreadsheet[test_spreadsheet_range[0]])
    self.assertIn(test_spreadsheet_range[0], result_spreadsheet)

  def testGetAllSheetsWithNoValues(self):
    test_spreadsheet_range = ['Entities']
    test_request = os.path.join(TEST_RESOURCES,
                                'test_blank_entities_sheet.json')
    mock_http = HttpMockSequence([({
        'status': '200'
    }, open(test_request, 'rb').read())])
    google_sheets_service = build(
        SHEETS, V4, http=mock_http, developerKey=_TEST_API_KEY)

    result_spreadsheet = import_helper.GetAllSheets(
        spreadsheet_id='spreadsheet_id',
        spreadsheet_range=test_spreadsheet_range,
        google_sheets_service=google_sheets_service)

    self.assertEmpty(result_spreadsheet[test_spreadsheet_range[0]])

  def testGetAllSheetsRaisesHttpError(self):
    test_spreadsheet_range = ['Entities']
    test_request = os.path.join(TEST_RESOURCES, 'test_entities_sheet.json')
    mock_http = HttpMockSequence([({
        'status': '403'
    }, open(test_request, 'rb').read())])
    google_sheets_service = build(
        SHEETS, V4, http=mock_http, developerKey=_TEST_API_KEY)

    with self.assertRaises(HttpError):
      import_helper.GetAllSheets(
          spreadsheet_id='spreadsheet_id',
          spreadsheet_range=test_spreadsheet_range,
          google_sheets_service=google_sheets_service)

  def testDeserializeBuildingConfiguration(self):
    test_building_config_path = os.path.join(TEST_BUILDING_CONFIG_PATH, 'GOOD',
                                             'guid_format.yaml')

    function_result = import_helper.DeserializeBuildingConfiguration(
        test_building_config_path)

    self.assertIsNotNone(function_result)

  def testDeserializeBuildingConfigurationRaisesFileNotFoundError(self):
    test_building_config_path = os.path.join(TEST_BUILDING_CONFIG_PATH, 'BAD',
                                             'guid_format.yaml')

    with self.assertRaises(FileNotFoundError):
      import_helper.DeserializeBuildingConfiguration(test_building_config_path)


if __name__ == '__main__':
  absltest.main()
