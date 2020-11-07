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

from validate import telemetry
from validate import telemetry_validator
from absl.testing import absltest

_TELEMETRY_PATH = os.path.join('.', 'tests', 'fake_telemetry')

_MESSAGE_ATTRIBUTES = os.path.join(_TELEMETRY_PATH, 'message_attributes.json')

_MESSAGE_GOOD = {
  attributes = json.loads(_MESSAGE_ATTRIBUTES),
  data = os.path.join(_TELEMETRY_PATH, 'telemetry.json')
}

_MESSAGE_MISSING_POINT = {
  attributes = json.loads(_MESSAGE_ATTRIBUTES),
  data = os.path.join(_TELEMETRY_PATH, 'telemetry_missing_point.json')),
}

ENTITY = ???

NULL_CALLBACK = lambda: None

class TelemetryValidatorTest(absltest.TestCase):

  def testTelemetryValidatorTimesOut(self):
    timeout = False
    telemetry_validator.TelemetryValidator({}, 1, lambda validator: timeout = True)
    threading.Timer(2, lambda: self.assertIsTrue(timeout))

  def testTelemetryValidatorDetectsUnknownEntity(self):
    validator = telemetry_validator.TelemetryValidator({}, 1, NULL_CALLBACK)
    validator.ValidateMessage(_MESSAGE_GOOD)
    error = telemetry_error.TelemetryError(ENTITY, None, "Unknown entity")
    self.assertIn(validator.validation_errors, error)

  def testTelemetryValidatorDetectsMissingPoint(self):
    validator = telemetry_validator.TelemetryValidator({ENTITY}, 1, NULL_CALLBACK)
    validator.ValidateMessage(_MESSAGE_MISSING_POINT)
    error = telemetry_error.TelemetryError(ENTITY, POINT_NAME, "Missing point")
    self.assertIn(validator.validation_errors, error)

  def testTelemetryValidatorDetectsInvalidState(self):
    validator = telemetry_validator.TelemetryValidator({ENTITY}, 1, NULL_CALLBACK)
    validator.ValidateMessage(_MESSAGE_INVALID_STATE)
    error = telemetry_error.TelemetryError(ENTITY, POINT_NAME, "Invalid state: BAD_STATE")
    self.assertIn(validator.validation_errors, error)

  def testTelemetryValidatorDetectsIntegerWithoutStatesOrUnits(self):
    validator = telemetry_validator.TelemetryValidator({ENTITY}, 1, NULL_CALLBACK)
    validator.ValidateMessage(_MESSAGE_BAD_INTEGER)
    error = telemetry_error.TelemetryError(
      ENTITY, POINT_NAME, "Integer value without states or units: 100")
    self.assertIn(validator.validation_errors, error)

  def testTelemetryValidatorDetectsNumberWithoutUnits(self):
    validator = telemetry_validator.TelemetryValidator({ENTITY}, 1, NULL_CALLBACK)
    validator.ValidateMessage(_MESSAGE_BAD_NUMBER)
    error = telemetry_error.TelemetryError(
      ENTITY, POINT_NAME, "Numeric value without units: 12.345")
    self.assertIn(validator.validation_errors, error)

  def testTelemetryValidatorDetectsMultipleErrorsInMessage(self):
    validator = telemetry_validator.TelemetryValidator({ENTITY}, 1, NULL_CALLBACK)
    validator.ValidateMessage(_MESSAGE_MISSING_POINT)
    error_one = telemetry_error.TelemetryError(ENTITY, POINT_NAME, "Missing point")
    error_two = telemetry_error.TelemetryError(
      ENTITY, POINT_NAME_2, "Invalid state: BAD_STATE")
    self.assertIn(validator.validation_errors, error_one)
    self.assertIn(validator.validation_errors, error_two)

  def _validationCallback(validator):
    self.assertEmpty(validator.validation_errors)
    self.assertTrue(validator.AllEntitiesValidated)

  def testTelemetryValidatorCallbackWhenAllEntitiesValidated(self):
    validator = telemetry_validator.TelemetryValidator({ENTITY}, 1, _validationCallback)
    validator.ValidateMessage(_MESSAGE_GOOD)

if __name__ == '__main__':
  absltest.main()
