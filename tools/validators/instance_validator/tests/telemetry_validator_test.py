# Copyright 2020 Google LLC
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

"""Tests tools.validators.instance_validator.telemetry_validator"""

from __future__ import absolute_import
from __future__ import print_function

import os
import json
import threading

from validate import instance_parser
from validate import telemetry_error
from validate import telemetry_validator
from absl.testing import absltest

_TELEMETRY_PATH = os.path.join('.', 'tests', 'fake_telemetry')
_INSTANCES_PATH = os.path.join('.', 'tests', 'fake_instances', 'GOOD')

_MESSAGE_ATTRIBUTES = os.path.join(_TELEMETRY_PATH, 'message_attributes.json')

class FakeMessage(object):
  def __init__(self, attributes, data):
    super().__init__()
    self.attributes = attributes
    self.data = data

_MESSAGE_GOOD = FakeMessage(
  json.loads(_MESSAGE_ATTRIBUTES),
  os.path.join(_TELEMETRY_PATH, 'telemetry_good.json'))

_MESSAGE_MISSING_POINT = FakeMessage(
  json.loads(_MESSAGE_ATTRIBUTES),
  os.path.join(_TELEMETRY_PATH, 'telemetry_missing_point.json'))

_MESSAGE_MISSING_PRESENT_VALUE = FakeMessage(
  json.loads(_MESSAGE_ATTRIBUTES),
  os.path.join(_TELEMETRY_PATH, 'telemetry_missing_present_value.json'))

_MESSAGE_INVALID_STATE = FakeMessage(
  json.loads(_MESSAGE_ATTRIBUTES),
  os.path.join(_TELEMETRY_PATH, 'telemetry_invalid_state.json'))

_MESSAGE_INVALID_NUMBER = FakeMessage(
  json.loads(_MESSAGE_ATTRIBUTES),
  os.path.join(_TELEMETRY_PATH, 'telemetry_invalid_number.json'))

_MESSAGE_MULTIPLE_ERRORS = FakeMessage(
  json.loads(_MESSAGE_ATTRIBUTES),
  os.path.join(_TELEMETRY_PATH, 'telemetry_multiple_errors.json'))

_ENTITIES = dict(
  instance_parser.parse_yaml(
    os.path.join(_INSTANCES_PATH, 'good_translation_units_and_states.yaml')))

NULL_CALLBACK = lambda: None

POINT_NAME = 'return_water_temperature_sensor'
POINT_NAME_2 = 'exhaust_air_damper_command'

class TelemetryValidatorTest(absltest.TestCase):

  def testTelemetryValidatorTimesOut(self):
    timeout = False
    timeoutCallback = lambda validator: timeout = True
    telemetry_validator.TelemetryValidator({}, 1, timeoutCallback)
    threading.Timer(2, lambda: self.assertIsTrue(timeout))

  def testTelemetryValidatorDetectsUnknownEntity(self):
    validator = telemetry_validator.TelemetryValidator({}, 1, NULL_CALLBACK)
    validator.ValidateMessage(_MESSAGE_GOOD)
    error = telemetry_error.TelemetryError(_ENTITIES, None, 'Unknown entity')
    self.assertIn(validator.validation_errors, error)

  def testTelemetryValidatorDetectsMissingPoint(self):
    validator = telemetry_validator.TelemetryValidator(
      _ENTITIES, 1, NULL_CALLBACK)
    validator.ValidateMessage(_MESSAGE_MISSING_POINT)
    error = telemetry_error.TelemetryError(
      _ENTITIES, POINT_NAME, 'Missing point')
    self.assertIn(validator.validation_errors, error)

  def testTelemetryValidatorDetectsMissingPresentValue(self):
    validator = telemetry_validator.TelemetryValidator(
      _ENTITIES, 1, NULL_CALLBACK)
    validator.ValidateMessage(_MESSAGE_MISSING_PRESENT_VALUE)
    error = telemetry_error.TelemetryError(
      _ENTITIES, POINT_NAME, 'Missing present value')
    self.assertIn(validator.validation_errors, error)

  def testTelemetryValidatorDetectsInvalidState(self):
    validator = telemetry_validator.TelemetryValidator(
      _ENTITIES, 1, NULL_CALLBACK)
    validator.ValidateMessage(_MESSAGE_INVALID_STATE)
    error = telemetry_error.TelemetryError(
      _ENTITIES, POINT_NAME_2, 'Invalid state: BAD_STATE')
    self.assertIn(validator.validation_errors, error)

  def testTelemetryValidatorDetectsInvalidNumber(self):
    validator = telemetry_validator.TelemetryValidator(
      _ENTITIES, 1, NULL_CALLBACK)
    validator.ValidateMessage(_MESSAGE_INVALID_NUMBER)
    error = telemetry_error.TelemetryError(
      _ENTITIES, POINT_NAME, 'Invalid number: BAD_NUMBER')
    self.assertIn(validator.validation_errors, error)

  def testTelemetryValidatorDetectsMultipleErrorsInMessage(self):
    validator = telemetry_validator.TelemetryValidator(
      _ENTITIES, 1, NULL_CALLBACK)
    validator.ValidateMessage(_MESSAGE_MULTIPLE_ERRORS)
    error_one = telemetry_error.TelemetryError(
      _ENTITIES, POINT_NAME, 'Missing point')
    error_two = telemetry_error.TelemetryError(
      _ENTITIES, POINT_NAME_2, 'Invalid state: false')
    self.assertIn(validator.validation_errors, error_one)
    self.assertIn(validator.validation_errors, error_two)

  def testTelemetryValidatorCallbackWhenAllEntitiesValidated(self):
    def ValidationCallback(validator):
      self.assertEmpty(validator.validation_errors)
      self.assertTrue(validator.AllEntitiesValidated)
    validator = telemetry_validator.TelemetryValidator(
      _ENTITIES, 1, ValidationCallback)
    validator.ValidateMessage(_MESSAGE_GOOD)

if __name__ == '__main__':
  absltest.main()
