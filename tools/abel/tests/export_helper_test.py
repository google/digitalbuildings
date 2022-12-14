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
"""Tests for Export Helper."""

import os
import tempfile

from absl.testing import absltest
from googleapiclient.discovery import build
from googleapiclient.http import HttpMockSequence

from model import import_helper
from model.constants import SHEETS
from model.constants import V4
from model.export_helper import BuildingConfigExport
from model.export_helper import GoogleSheetExport
from model.guid_to_entity_map import GuidToEntityMap
from model.model_builder import ModelBuilder
from model.model_error import SpreadsheetAuthorizationError
from google3.third_party.digitalbuildings.tools.abel.tests.test_constants import TEST_RESOURCES
from google3.third_party.digitalbuildings.tools.abel.tests.test_constants import TEST_SPREADSHEET

_GOOD_TEST_BUILDING_CONFIG = os.path.join(TEST_RESOURCES,
                                          'good_test_building_config.yaml')


# pylint: disable=consider-using-with
class ExportHelperTest(absltest.TestCase):
  """Tests export methods for ABEL."""

  def setUp(self):
    super().setUp()
    self.input_spreadsheet = TEST_SPREADSHEET
    self.guid_map = GuidToEntityMap()
    self.guid_map.Clear()

  def testWriteAllSheets(self):
    test_spreadsheet_range = ['Entities']
    update_entities_response = os.path.join(TEST_RESOURCES,
                                            'update_entities_response.json')
    import_building_config = import_helper.DeserializeBuildingConfiguration(
        _GOOD_TEST_BUILDING_CONFIG)
    model = ModelBuilder.FromBuildingConfig(import_building_config[0],
                                            import_building_config[1])
    mock_http = HttpMockSequence([({
        'status': '200'
    }, open(update_entities_response, 'rb').read())])
    google_sheets_service = build(
        SHEETS, V4, http=mock_http, developerKey='fake_key')
    export_helper = GoogleSheetExport()

    model.Build()
    model_dictionary = model.ToModelDictionary()
    result_spreadsheet_id = export_helper.WriteAllSheets(
        spreadsheet_id='fake_spreadsheet_id',
        spreadsheet_range=test_spreadsheet_range,
        model_dict=model_dictionary,
        google_sheets_service=google_sheets_service)

    self.assertEqual('fake_spreadsheet_id', result_spreadsheet_id)

  def testWriteAllsheetsRaisesSpreadsheetAuthorizationError(self):
    test_spreadsheet_range = ['Entities']
    update_entities_response = os.path.join(TEST_RESOURCES,
                                            'update_entities_response.json')
    import_building_config = import_helper.DeserializeBuildingConfiguration(
        _GOOD_TEST_BUILDING_CONFIG)
    model = ModelBuilder.FromBuildingConfig(import_building_config[0],
                                            import_building_config[1])
    mock_http = HttpMockSequence([({
        'status': '403'
    }, open(update_entities_response, 'rb').read())])

    google_sheets_service = build(
        SHEETS, V4, http=mock_http, developerKey='fake_key')
    export_helper = GoogleSheetExport()
    model.Build()
    model_dictionary = model.ToModelDictionary()

    with self.assertRaises(SpreadsheetAuthorizationError):
      export_helper.WriteAllSheets(
          spreadsheet_id='fake_spreadsheet_id',
          spreadsheet_range=test_spreadsheet_range,
          model_dict=model_dictionary,
          google_sheets_service=google_sheets_service)

  def testWriteOneSheetRaisesSpreadsheetAuthorizationError(self):
    test_spreadsheet_range = ['Entities']
    update_entities_response = os.path.join(TEST_RESOURCES,
                                            'update_entities_response.json')
    import_building_config = import_helper.DeserializeBuildingConfiguration(
        _GOOD_TEST_BUILDING_CONFIG)
    model = ModelBuilder.FromBuildingConfig(import_building_config[0],
                                            import_building_config[1])
    mock_http = HttpMockSequence([({
        'status': '403'
    }, open(update_entities_response, 'rb').read())])

    google_sheets_service = build(
        SHEETS, V4, http=mock_http, developerKey='fake_key')
    export_helper = GoogleSheetExport()
    model.Build()
    model_dictionary = model.ToModelDictionary()

    with self.assertRaises(SpreadsheetAuthorizationError):
      export_helper.WriteAllSheets(
          spreadsheet_id='fake_spreadsheet_id',
          spreadsheet_range=test_spreadsheet_range,
          model_dict=model_dictionary,
          google_sheets_service=google_sheets_service)

  def testExportBuildingConfiguration(self):
    export_filepath = os.path.join(tempfile.gettempdir(),
                                   'exported_building_config.yaml')
    model = ModelBuilder.FromSpreadsheet(TEST_SPREADSHEET)
    model.Build()
    export_helper = BuildingConfigExport(model)

    exported_building_config = export_helper.ExportBuildingConfiguration(
        export_filepath)

    self.assertTrue(os.path.exists(export_filepath))
    self.assertIsNotNone(exported_building_config)
    self.assertEqual(
        ['code', 'connections', 'links', 'type'],
        list(exported_building_config.get('test_virtual_guid').keys()))
    self.assertEqual(
        ['cloud_device_id', 'code', 'etag', 'translation', 'type'],
        list(exported_building_config.get('test_reporting_guid').keys()))
    self.assertIsInstance(
        exported_building_config.get('test_reporting_guid').get(
            'cloud_device_id'), str)
    self.assertEqual(
        exported_building_config.get('test_reporting_guid').get(
            'cloud_device_id'), '2541901344105616')
    states = exported_building_config.get('test_reporting_guid').get(
        'translation').get('fire_alarm_5').get('states')
    for raw_state in states.values():
      self.assertIsInstance(raw_state, str)
    units = exported_building_config.get('test_reporting_guid').get(
        'translation').get('supply_water_temperature_sensor_1').get('units')
    for raw_unit_value in units.get('values').values():
      self.assertIsInstance(raw_unit_value, str)

if __name__ == '__main__':
  absltest.main()
