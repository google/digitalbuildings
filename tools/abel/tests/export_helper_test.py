# Copyright 2023 Google LLC
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

# pylint: disable=g-importing-member
from absl.testing import absltest
from googleapiclient.discovery import build
from googleapiclient.http import HttpMockSequence

from model import import_helper
from model.constants import ENTITY_FIELDS
from model.constants import SHEETS
from model.constants import V4
from model.export_helper import BuildingConfigExport
from model.export_helper import GoogleSheetExport
from model.model_builder import Model
from model.model_error import SpreadsheetAuthorizationError
from tests.test_constants import TEST_BAD_MULTISTATE_FIELD_DICT_NO_STATES
from tests.test_constants import TEST_FIELD_DICT_NO_REPORTING_FIELD_NAME
from tests.test_constants import TEST_FIELD_DICT_NO_UNITS
from tests.test_constants import TEST_RESOURCES
from tests.test_constants import TEST_SPREADSHEET


_GOOD_TEST_BUILDING_CONFIG = os.path.join(
    TEST_RESOURCES, 'good_test_building_config.yaml'
)


# pylint: disable=consider-using-with
# pylint: disable=unused-variable
class ExportHelperTest(absltest.TestCase):
  """Tests export methods for ABEL."""

  def setUp(self):
    super().setUp()
    self.input_spreadsheet = TEST_SPREADSHEET.copy()

    self.export_filepath = os.path.join(
        tempfile.gettempdir(), 'exported_building_config.yaml'
    )
    # Add fields to spreadsheet specifically for export testing
    self.input_spreadsheet[ENTITY_FIELDS].append(
        TEST_FIELD_DICT_NO_REPORTING_FIELD_NAME
    )
    self.input_spreadsheet[ENTITY_FIELDS].append(TEST_FIELD_DICT_NO_UNITS)
    # Build model
    unbuilt_model, operations = Model.Builder.FromSpreadsheet(
        self.input_spreadsheet
    )
    model = unbuilt_model.Build()
    # Export a building config dictionary
    self.export_helper = BuildingConfigExport(model)

  def testWriteAllSheets(self):
    update_entities_response = os.path.join(
        TEST_RESOURCES, 'update_entities_response.json'
    )
    import_building_config = import_helper.DeserializeBuildingConfiguration(
        _GOOD_TEST_BUILDING_CONFIG
    )
    unbuilt_model, operations = Model.Builder.FromBuildingConfig(
        import_building_config[0], import_building_config[1]
    )
    model = unbuilt_model.Build()
    mock_http = HttpMockSequence(
        [({'status': '200'}, open(update_entities_response, 'rb').read())]
    )
    google_sheets_service = build(
        SHEETS, V4, http=mock_http, developerKey='fake_key'
    )
    export_helper = GoogleSheetExport()

    model_dictionary = model.ToModelDictionary(operations)
    create_spreadsheet_response = export_helper.CreateSpreadsheet(
        model_dict=model_dictionary,
        google_sheets_service=google_sheets_service,
    )

    self.assertIsNotNone(create_spreadsheet_response)

  def testWriteAllsheetsRaisesSpreadsheetAuthorizationError(self):
    update_entities_response = os.path.join(
        TEST_RESOURCES, 'update_entities_response.json'
    )
    import_building_config = import_helper.DeserializeBuildingConfiguration(
        _GOOD_TEST_BUILDING_CONFIG
    )
    unbuilt_model, operations = Model.Builder.FromBuildingConfig(
        import_building_config[0], import_building_config[1]
    )
    model = unbuilt_model.Build()
    mock_http = HttpMockSequence(
        [({'status': '403'}, open(update_entities_response, 'rb').read())]
    )

    google_sheets_service = build(
        SHEETS, V4, http=mock_http, developerKey='fake_key'
    )
    export_helper = GoogleSheetExport()

    model_dictionary = model.ToModelDictionary(operations)

    with self.assertRaises(SpreadsheetAuthorizationError):
      export_helper.CreateSpreadsheet(
          model_dict=model_dictionary,
          google_sheets_service=google_sheets_service,
      )

  def testWriteOneSheetRaisesSpreadsheetAuthorizationError(self):
    update_entities_response = os.path.join(
        TEST_RESOURCES, 'update_entities_response.json'
    )
    import_building_config = import_helper.DeserializeBuildingConfiguration(
        _GOOD_TEST_BUILDING_CONFIG
    )
    unbuilt_model, operations = Model.Builder.FromBuildingConfig(
        import_building_config[0], import_building_config[1]
    )
    model = unbuilt_model.Build()
    mock_http = HttpMockSequence(
        [({'status': '403'}, open(update_entities_response, 'rb').read())]
    )

    google_sheets_service = build(
        SHEETS, V4, http=mock_http, developerKey='fake_key'
    )
    export_helper = GoogleSheetExport()
    model_dictionary = model.ToModelDictionary(operations)

    with self.assertRaises(SpreadsheetAuthorizationError):
      export_helper.CreateSpreadsheet(
          model_dict=model_dictionary,
          google_sheets_service=google_sheets_service,
      )

  def testExportBuildingConfigExportsVirtualEntityKeysCorrectly(self):
    exported_building_config = (
        self.export_helper.ExportInitBuildingConfiguration(self.export_filepath)
    )
    expected_keys = ['code', 'etag', 'connections', 'links', 'type']
    exported_keys = list(
        exported_building_config.get('test_virtual_guid').keys()
    )
    # model = Model.Builder.FromSpreadsheet(TEST_SPREADSHEET).Build()
    # export_helper = BuildingConfigExport(model)

    self.assertEqual(expected_keys, exported_keys)

  def testExportBuildingConfigExportsReportingEntityKeysCorrectly(self):
    exported_building_config = (
        self.export_helper.ExportInitBuildingConfiguration(self.export_filepath)
    )
    expected_keys = ['cloud_device_id', 'code', 'etag', 'translation', 'type']
    exported_keys = list(
        exported_building_config.get('test_reporting_guid').keys()
    )

    self.assertEqual(expected_keys, exported_keys)

  def testExportBuildingConfigExportsCloudDeviceIDAsString(self):
    exported_building_config = (
        self.export_helper.ExportInitBuildingConfiguration(self.export_filepath)
    )
    expected_cdid = '2541901344105616'
    exported_cdid = exported_building_config.get('test_reporting_guid').get(
        'cloud_device_id'
    )

    self.assertIsInstance(exported_cdid, str)
    self.assertEqual(exported_cdid, expected_cdid)

  def testExportBuildingConfigExportsMultiStateValueFieldStates(self):
    exported_building_config = (
        self.export_helper.ExportInitBuildingConfiguration(self.export_filepath)
    )
    multi_state_value_field_states = (
        exported_building_config.get('test_reporting_guid')
        .get('translation')
        .get('fire_alarm_5')
        .get('states')
    )

    self.assertIsInstance(multi_state_value_field_states.get('ON'), str)
    self.assertEqual(multi_state_value_field_states.get('ON'), 'TRUE')

  def testExportBuildingConfigExportsUnitsCorrectly(self):
    exported_building_config = (
        self.export_helper.ExportInitBuildingConfiguration(self.export_filepath)
    )
    exported_units = (
        exported_building_config.get('test_reporting_guid')
        .get('translation')
        .get('supply_water_temperature_sensor_1')
        .get('units')
        .get('values')
    )

    self.assertIsInstance(exported_units.get('pascals'), str)
    self.assertEqual(exported_units.get('pascals'), 'Pa')

  def testExportBuildingConfigExportsLinksCorrectly(self):
    exported_building_config = (
        self.export_helper.ExportInitBuildingConfiguration(self.export_filepath)
    )
    exported_links = exported_building_config.get('test_virtual_guid').get(
        'links'
    )

    self.assertEqual(list(exported_links.keys()), ['test_reporting_guid'])
    self.assertLen(exported_links.get('test_reporting_guid').items(), 2)
    self.assertEqual(
        exported_links.get('test_reporting_guid'),
        {
            'supply_water_temperature_sensor': (
                'supply_water_temperature_sensor_1'
            ),
            'cooling_stage_run_count': 'cooling_stage_run_count',
        },
    )

  def testExportBuildingConfigRaisesValueErrorForBadMultistate(self):
    bad_input_spreadsheet = TEST_SPREADSHEET.copy()
    bad_input_spreadsheet[ENTITY_FIELDS].append(
        TEST_BAD_MULTISTATE_FIELD_DICT_NO_STATES
    )
    unbuilt_model, operations = Model.Builder.FromSpreadsheet(
        self.input_spreadsheet
    )
    model = unbuilt_model.Build()
    export_helper = BuildingConfigExport(model)

    with self.assertRaises(ValueError):
      export_helper.ExportInitBuildingConfiguration(self.export_filepath)


if __name__ == '__main__':
  absltest.main()
