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
"""Tests for telemetry_validator_report.py."""

from unittest import mock

from absl.testing import absltest

from validate import telemetry_validation_report as tvr
from validate.constants import ENTITY_CODE
from validate.constants import ENTITY_GUID
from validate.constants import ERROR_DEVICES
from validate.constants import EXPECTED_DEVICES
from validate.constants import EXPECTED_POINTS
from validate.constants import EXTRA_DEVICES
from validate.constants import EXTRA_POINTS
from validate.constants import INVALID_DIMENSIONAL_VALUES
from validate.constants import MESSAGE_TIMESTAMP
from validate.constants import MESSAGE_VERSION
from validate.constants import MISSING_DEVICES
from validate.constants import MISSING_POINTS
from validate.constants import MISSING_PRESENT_VALUES
from validate.constants import REPORT_TIMESTAMP
from validate.constants import TELEMETRY_MESSAGE_ERRORS
from validate.constants import TELEMETRY_MESSAGE_WARNINGS
from validate.constants import UNMAPPED_STATES


TEST_GUID = 'b93304dc-1dce-4f8b-8f69-8e34b93fa69c'
TEST_CODE = 'ABC_123'
TEST_TIMESTAMP = 'test_timestamp'

TELEMETRY_POINT_1 = 'return_water_temperature_sensor'
TELEMETRY_POINT_2 = 'supply_water_temperature_sensor'
EXPECTED_PAYLOAD_POINTS = [TELEMETRY_POINT_1, TELEMETRY_POINT_2]

MISSING_PAYLOAD_POINT = 'run_command'
EXTRA_PAYLOAD_POINT_1 = 'return_water_temperature_setpoint'
EXTRA_PAYLOAD_POINT_2 = 'supply_water_temperature_setpoint'
UNMAPPED_STATE = 'RUNNING'
INVALID_DIMENSIONAL_VALUE = 'NaN'

EXPECTED_REPORT_DEVICES = {
    'GUID_1': 'CODE_1',
    'GUID_2': 'CODE_2',
    'GUID_3': 'CODE_3',
}
EXTRA_DEVICE = {'EXTRA_CLOUD_DEVICE_ID': 'EXTRA_CODE'}
MISSING_DEVICE = {'MISSING_GUID': 'MISSING_CODE'}


class TelemetryValidatorReportTest(absltest.TestCase):

  @mock.patch.object(tvr, 'datetime')
  def setUp(self, mock_datetime):
    super().setUp()
    mock_datetime.datetime.now().strftime.return_value = TEST_TIMESTAMP
    self.telemetry_validation_report = tvr.TelemetryValidationReport(
        EXPECTED_REPORT_DEVICES
    )
    self.error_device = tvr.TelemetryMessageValidationBlock(
        guid='22d390ef-de1f-4cba-acee-ecf0f697fd2f',
        code='DEVICE_5',
        version=1,
        timestamp=TEST_TIMESTAMP,
        expected_points=EXPECTED_PAYLOAD_POINTS,
    )

  @mock.patch.object(tvr, 'datetime')
  def testGenerateReport_fromFullInitialize_success(self, mock_datetime):
    mock_datetime.datetime.now().strftime.return_value = TEST_TIMESTAMP

    self.error_device.AddMissingPoint(MISSING_PAYLOAD_POINT)
    self.error_device.AddExtraPoint(EXTRA_PAYLOAD_POINT_1)
    self.error_device.AddExtraPoint(EXTRA_PAYLOAD_POINT_2)
    error_devices = [self.error_device]

    telemetry_validation_report = tvr.TelemetryValidationReport(
        expected_devices=EXPECTED_REPORT_DEVICES,
        extra_devices=EXTRA_DEVICE,
        missing_devices=MISSING_DEVICE,
        error_devices=error_devices,
    )

    expected_validation_report_json = {
        REPORT_TIMESTAMP: TEST_TIMESTAMP,
        EXPECTED_DEVICES: EXPECTED_REPORT_DEVICES,
        EXTRA_DEVICES: EXTRA_DEVICE,
        MISSING_DEVICES: MISSING_DEVICE,
        ERROR_DEVICES: [
            error_device.CreateJsonReportBlock()
            for error_device in error_devices
        ],
    }

    result_validation_report_json = telemetry_validation_report.GenerateReport()

    self.assertEqual(
        expected_validation_report_json, result_validation_report_json
    )

  def testAddExtraDevice_success(self):
    self.telemetry_validation_report.AddExtraDevice(EXTRA_DEVICE)

    self.assertEqual(
        self.telemetry_validation_report.extra_devices, EXTRA_DEVICE
    )

  def testGenerateReport_WithExtraDevice_success(self):
    self.telemetry_validation_report.AddExtraDevice(EXTRA_DEVICE)

    expected_validation_report_json = {
        REPORT_TIMESTAMP: TEST_TIMESTAMP,
        EXPECTED_DEVICES: EXPECTED_REPORT_DEVICES,
        EXTRA_DEVICES: EXTRA_DEVICE,
        MISSING_DEVICES: {},
        ERROR_DEVICES: [],
    }

    result_validation_report_json = (
        self.telemetry_validation_report.GenerateReport()
    )

    self.assertEqual(
        expected_validation_report_json, result_validation_report_json
    )

  def testAddMissingDevice_success(self):
    self.telemetry_validation_report.AddMissingDevice(MISSING_DEVICE)

    self.assertEqual(
        self.telemetry_validation_report.missing_devices, MISSING_DEVICE
    )

  def testGenerateReport_withMissingDevice_success(self):
    self.telemetry_validation_report.AddMissingDevice(MISSING_DEVICE)

    expected_validation_report_json = {
        REPORT_TIMESTAMP: TEST_TIMESTAMP,
        EXPECTED_DEVICES: EXPECTED_REPORT_DEVICES,
        EXTRA_DEVICES: {},
        MISSING_DEVICES: MISSING_DEVICE,
        ERROR_DEVICES: [],
    }

    result_validation_report_json = (
        self.telemetry_validation_report.GenerateReport()
    )

    self.assertEqual(
        expected_validation_report_json, result_validation_report_json
    )

  def testAddErrorDevice_success(self):
    self.telemetry_validation_report.AddErrorDevice(self.error_device)

    self.assertEqual(
        self.telemetry_validation_report.error_devices[0], self.error_device
    )

  def testGenerateReport_withErrorDevice_success(self):
    self.telemetry_validation_report.AddErrorDevice(self.error_device)

    expected_validation_report_json = {
        REPORT_TIMESTAMP: TEST_TIMESTAMP,
        EXPECTED_DEVICES: EXPECTED_REPORT_DEVICES,
        EXTRA_DEVICES: {},
        MISSING_DEVICES: {},
        ERROR_DEVICES: [self.error_device.CreateJsonReportBlock()],
    }

    result_validation_report_json = (
        self.telemetry_validation_report.GenerateReport()
    )

    self.assertEqual(
        expected_validation_report_json, result_validation_report_json
    )


class TelemetryMessageValidationBlockTest(absltest.TestCase):

  def setUp(self):
    super().setUp()
    self.validation_block = tvr.TelemetryMessageValidationBlock(
        guid=TEST_GUID,
        code=TEST_CODE,
        version=1,
        timestamp=TEST_TIMESTAMP,
        expected_points=EXPECTED_PAYLOAD_POINTS,
    )

  def testInitialize_success(self):
    self.assertEqual(self.validation_block.guid, TEST_GUID)
    self.assertEqual(self.validation_block.code, TEST_CODE)
    self.assertEqual(self.validation_block.version, 1)
    self.assertEqual(
        self.validation_block.expected_points, EXPECTED_PAYLOAD_POINTS
    )

  def testAddMissingPoint_setsValidToFalse_success(self):
    self.validation_block.AddMissingPoint(MISSING_PAYLOAD_POINT)

    self.assertEqual(
        self.validation_block.missing_points[0], MISSING_PAYLOAD_POINT
    )
    self.assertFalse(self.validation_block.valid)

  def testAddExtraPoint_setsValidToFalse_success(self):
    self.validation_block.AddExtraPoint(EXTRA_PAYLOAD_POINT_1)

    self.assertEqual(
        self.validation_block.extra_points[0], EXTRA_PAYLOAD_POINT_1
    )
    self.assertFalse(self.validation_block.valid)

  def testAddUnmappedState_setsValidToFalse_success(self):
    self.validation_block.AddUnmappedState(UNMAPPED_STATE, TELEMETRY_POINT_1)

    self.assertEqual(
        self.validation_block.unmapped_states[0],
        (TELEMETRY_POINT_1, UNMAPPED_STATE),
    )
    self.assertFalse(self.validation_block.valid)

  def testAddInvalidDimensionalValue_setsValidToFalse_success(self):
    self.validation_block.AddInvalidDimensionalValue(
        INVALID_DIMENSIONAL_VALUE, TELEMETRY_POINT_2
    )

    self.assertEqual(
        self.validation_block.invalid_dimensional_values[0],
        (TELEMETRY_POINT_2, INVALID_DIMENSIONAL_VALUE),
    )
    self.assertFalse(self.validation_block.valid)

  def testAddMissingPresentValue_setsValidToFalse_success(self):
    self.validation_block.AddMissingPresentValue(TELEMETRY_POINT_1)

    self.assertEqual(
        self.validation_block.missing_present_values[0], TELEMETRY_POINT_1
    )
    self.assertFalse(self.validation_block.valid)

  def testCreateJsonReportBlock_fromFilledBlocked_success(self):
    expected_json_dict = {
        MESSAGE_TIMESTAMP: TEST_TIMESTAMP,
        MESSAGE_VERSION: 1,
        ENTITY_CODE: TEST_CODE,
        ENTITY_GUID: TEST_GUID,
        EXPECTED_POINTS: [
            'return_water_temperature_sensor',
            'supply_water_temperature_sensor',
        ],
        TELEMETRY_MESSAGE_ERRORS: {
            MISSING_POINTS: ['run_command'],
            MISSING_PRESENT_VALUES: [],
            INVALID_DIMENSIONAL_VALUES: {
                'supply_water_temperature_sensor': 'NaN'
            },
        },
        TELEMETRY_MESSAGE_WARNINGS: {
            EXTRA_POINTS: [
                'return_water_temperature_setpoint',
                'supply_water_temperature_setpoint',
            ],
            UNMAPPED_STATES: {'return_water_temperature_sensor': 'RUNNING'},
        },
    }

    self.validation_block.AddMissingPoint(MISSING_PAYLOAD_POINT)
    self.validation_block.AddExtraPoint(EXTRA_PAYLOAD_POINT_1)
    self.validation_block.AddExtraPoint(EXTRA_PAYLOAD_POINT_2)
    self.validation_block.AddUnmappedState(UNMAPPED_STATE, TELEMETRY_POINT_1)
    self.validation_block.AddInvalidDimensionalValue(
        INVALID_DIMENSIONAL_VALUE, TELEMETRY_POINT_2
    )

    result_json_dict = self.validation_block.CreateJsonReportBlock()

    self.assertEqual(expected_json_dict, result_json_dict)

  def testInit_missingTimestampAndVersion_success(self):
    test_validation_block = tvr.TelemetryMessageValidationBlock(
        guid=TEST_GUID,
        code=TEST_CODE,
        expected_points=EXPECTED_PAYLOAD_POINTS,
    )

    self.assertEqual(test_validation_block.guid, TEST_GUID)
    self.assertEqual(test_validation_block.code, TEST_CODE)
    self.assertIsNone(test_validation_block.version)
    self.assertIsNone(test_validation_block.timestamp)
    self.assertEqual(
        test_validation_block.expected_points, EXPECTED_PAYLOAD_POINTS
    )

  def testAddDescription_setsValidToFalse_success(self):
    self.validation_block.AddDescription('test description')

    self.assertEqual(self.validation_block.description, 'test description')
    self.assertFalse(self.validation_block.valid)


if __name__ == '__main__':
  absltest.main()
