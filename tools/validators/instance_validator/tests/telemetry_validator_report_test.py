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

import datetime
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
from validate.constants import TIMESTAMP_FORMAT
from validate.constants import UNMAPPED_STATES


TEST_GUID = 'b93304dc-1dce-4f8b-8f69-8e34b93fa69c'
TEST_CODE = 'ABC_123'
TEST_TIMESTAMP = 'test_timestamp'


class TelemetryValidatorReportTest(absltest.TestCase):

  @mock.patch.object(tvr, 'datetime')
  def testGenerateReport(self, mock_datetime):
    mock_datetime.datetime.now().strftime.return_value = TEST_TIMESTAMP
    expected_points = [
        tvr.TelemetryPoint(
            point_name='return_water_temperature_sensor', present_value=100.0
        ),
        tvr.TelemetryPoint(
            point_name='supply_water_temperature_sensor', present_value=200.0
        ),
    ]
    missing_point = tvr.TelemetryPoint(
        point_name='run_command', present_value=True
    )
    extra_point_1 = tvr.TelemetryPoint(
        point_name='return_water_temperature_setpoint', present_value=100.0
    )
    extra_point_2 = tvr.TelemetryPoint(
        point_name='supply_water_temperature_setpoint', present_value=200.0
    )
    error_device = tvr.TelemetryMessageValidationBlock(
        guid='22d390ef-de1f-4cba-acee-ecf0f697fd2f',
        code='DEVICE_5',
        version=1,
        timestamp=TEST_TIMESTAMP,
        expected_points=expected_points,
    )
    error_device.AddMissingPoint(missing_point)
    error_device.AddExtraPoint(extra_point_1)
    error_device.AddExtraPoint(extra_point_2)
    expected_devices = {
        '633c8617-635f-4ee0-86df-78a996027ca1': 'DEVICE_1',
        '74dcafa4-6cfa-47ac-a127-0697f9b72005': 'DEVICE_2',
        '22d390ef-de1f-4cba-acee-ecf0f697fd2f': 'DEVICE_5',
    }
    extra_devices = {'cloud_device_id': 'DEVICE_3'}
    missing_devices = {'74dcafa4-6cfa-47ac-a127-0697f9b72005': 'DEVICE_2'}
    error_devices = [error_device]

    telemetry_validation_report = tvr.TelemetryValidationReport(
        expected_devices=expected_devices,
        extra_devices=extra_devices,
        missing_devices=missing_devices,
        error_devices=error_devices,
    )

    expected_validation_report_json = {
        REPORT_TIMESTAMP: TEST_TIMESTAMP,
        EXPECTED_DEVICES: expected_devices,
        EXTRA_DEVICES: extra_devices,
        MISSING_DEVICES: missing_devices,
        ERROR_DEVICES: [
            error_device.CreateJsonReportBlock()
            for error_device in error_devices
        ],
    }

    result_validation_report_json = telemetry_validation_report.GenerateReport()

    self.assertEqual(
        expected_validation_report_json, result_validation_report_json
    )


class TelemetryMessageValidationBlockTest(absltest.TestCase):

  def testInit(self):
    expected_points = [
        tvr.TelemetryPoint(
            point_name='return_water_temperature_sensor', present_value=100.0
        ),
        tvr.TelemetryPoint(
            point_name='supply_water_temperature_sensor', present_value=200.0
        ),
    ]
    test_validation_block = tvr.TelemetryMessageValidationBlock(
        guid=TEST_GUID,
        code=TEST_CODE,
        version=1,
        timestamp=datetime.datetime.now(tz=datetime.timezone.utc).strftime(
            TIMESTAMP_FORMAT
        ),
        expected_points=expected_points,
    )

    self.assertEqual(test_validation_block.guid, TEST_GUID)
    self.assertEqual(test_validation_block.code, TEST_CODE)
    self.assertEqual(test_validation_block.version, 1)
    self.assertEqual(test_validation_block.expected_points, expected_points)

  def testJsonReportBlockStringFormat(self):
    expected_points = [
        tvr.TelemetryPoint(
            point_name='return_water_temperature_sensor', present_value=100.0
        ),
        tvr.TelemetryPoint(
            point_name='supply_water_temperature_sensor', present_value=200.0
        ),
    ]
    missing_point = tvr.TelemetryPoint(
        point_name='run_command', present_value=True
    )
    extra_point_1 = tvr.TelemetryPoint(
        point_name='return_water_temperature_setpoint', present_value=100.0
    )
    extra_point_2 = tvr.TelemetryPoint(
        point_name='supply_water_temperature_setpoint', present_value=200.0
    )

    expected_json_dict = {
        MESSAGE_TIMESTAMP: TEST_TIMESTAMP,
        MESSAGE_VERSION: 1,
        ENTITY_CODE: TEST_CODE,
        ENTITY_GUID: TEST_GUID,
        EXPECTED_POINTS: {
            'return_water_temperature_sensor': {'present_value': 100.0},
            'supply_water_temperature_sensor': {'present_value': 200.0},
        },
        TELEMETRY_MESSAGE_ERRORS: {
            MISSING_POINTS: {'run_command': {'present_value': True}},
            MISSING_PRESENT_VALUES: {},
            INVALID_DIMENSIONAL_VALUES: {},
        },
        TELEMETRY_MESSAGE_WARNINGS: {
            EXTRA_POINTS: {
                'return_water_temperature_setpoint': {'present_value': 100.0},
                'supply_water_temperature_setpoint': {'present_value': 200.0},
            },
            UNMAPPED_STATES: {},
        },
    }

    test_validation_block = tvr.TelemetryMessageValidationBlock(
        guid=TEST_GUID,
        code=TEST_CODE,
        version=1,
        timestamp=TEST_TIMESTAMP,
        expected_points=expected_points,
    )
    test_validation_block.AddMissingPoint(missing_point)
    test_validation_block.AddExtraPoint(extra_point_1)
    test_validation_block.AddExtraPoint(extra_point_2)

    result_json_dict = test_validation_block.CreateJsonReportBlock()

    self.assertEqual(expected_json_dict, result_json_dict)

  def testMissingTimetsampAndVersion(self):
    expected_points = [
        tvr.TelemetryPoint(
            point_name='return_water_temperature_sensor', present_value=100.0
        ),
        tvr.TelemetryPoint(
            point_name='supply_water_temperature_sensor', present_value=200.0
        ),
    ]
    test_validation_block = tvr.TelemetryMessageValidationBlock(
        guid=TEST_GUID,
        code=TEST_CODE,
        expected_points=expected_points,
    )

    self.assertEqual(test_validation_block.guid, TEST_GUID)
    self.assertEqual(test_validation_block.code, TEST_CODE)
    self.assertIsNone(test_validation_block.version)
    self.assertIsNone(test_validation_block.timestamp)
    self.assertEqual(test_validation_block.expected_points, expected_points)

  def testMessageBlockAddsDescription(self):
    expected_points = [
        tvr.TelemetryPoint(
            point_name='return_water_temperature_sensor', present_value=100.0
        ),
        tvr.TelemetryPoint(
            point_name='supply_water_temperature_sensor', present_value=200.0
        ),
    ]
    test_validation_block = tvr.TelemetryMessageValidationBlock(
        guid=TEST_GUID,
        code=TEST_CODE,
        expected_points=expected_points,
        description='test description',
    )

    self.assertEqual(test_validation_block.description, 'test description')
    self.assertEqual(test_validation_block.guid, TEST_GUID)
    self.assertEqual(test_validation_block.code, TEST_CODE)
    self.assertEqual(test_validation_block.expected_points, expected_points)


if __name__ == '__main__':
  absltest.main()
