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
# import threading

from validate import instance_parser
from validate import telemetry_error
from validate import telemetry_validator
from absl.testing import absltest

_TELEMETRY_PATH = os.path.join('.', 'tests', 'fake_telemetry')
_INSTANCES_PATH = os.path.join('.', 'tests', 'fake_instances', 'GOOD')

_MESSAGE_ATTRIBUTES_PATH_1 = os.path.join(_TELEMETRY_PATH,
                                          'message_attributes_CHWS_WDT-17.json')
_MESSAGE_ATTRIBUTES_1 = json.load(open(_MESSAGE_ATTRIBUTES_PATH_1))

_MESSAGE_ATTRIBUTES_PATH_2 = os.path.join(_TELEMETRY_PATH,
                                          'message_attributes_DMP_EDM-17.json')
_MESSAGE_ATTRIBUTES_2 = json.load(open(_MESSAGE_ATTRIBUTES_PATH_2))

class FakeMessage(object):
  def __init__(self, attributes, data):
    super().__init__()
    self.attributes = attributes
    self.data = data

  def ack(self):
    return NotImplemented

with open(os.path.join(_TELEMETRY_PATH,
                       'telemetry_good.json')) as file:
  _MESSAGE_GOOD = FakeMessage(_MESSAGE_ATTRIBUTES_1, file.read())

with open(os.path.join(_TELEMETRY_PATH,
                       'telemetry_missing_point.json')) as file:
  _MESSAGE_MISSING_POINT = FakeMessage(_MESSAGE_ATTRIBUTES_1, file.read())

with open(os.path.join(_TELEMETRY_PATH,
                       'telemetry_missing_present_value.json')) as file:
  _MESSAGE_MISSING_PRESENT_VALUE = FakeMessage(
    _MESSAGE_ATTRIBUTES_1, file.read())

with open(os.path.join(_TELEMETRY_PATH,
                       'telemetry_invalid_state.json')) as file:
  _MESSAGE_INVALID_STATE = FakeMessage(_MESSAGE_ATTRIBUTES_2, file.read())

with open(os.path.join(_TELEMETRY_PATH,
                       'telemetry_invalid_number.json')) as file:
  _MESSAGE_INVALID_NUMBER = FakeMessage(_MESSAGE_ATTRIBUTES_1, file.read())

with open(os.path.join(_TELEMETRY_PATH,
                       'telemetry_invalid_number_boolean.json')) as file:
  _MESSAGE_INVALID_NUMBER_BOOLEAN = FakeMessage(
    _MESSAGE_ATTRIBUTES_1, file.read())

with open(os.path.join(_TELEMETRY_PATH,
                       'telemetry_multiple_errors.json')) as file:
  _MESSAGE_MULTIPLE_ERRORS = FakeMessage(_MESSAGE_ATTRIBUTES_1, file.read())

# TODO: fix inconsistency between telemetry parser expecting a string,
# but instance parser expecting a file

_ENTITY_NAME_1 = 'CHWS_WDT-17'
_ENTITY_1 = dict(
  instance_parser.parse_yaml(
    os.path.join(_INSTANCES_PATH, 'good_translation_units.yaml')))

_ENTITY_NAME_2 = 'DMP_EDM-17'
_ENTITY_2 = dict(
  instance_parser.parse_yaml(
    os.path.join(_INSTANCES_PATH, 'good_translation_states.yaml')))

_POINT_NAME_1 = 'return_water_temperature_sensor'
_POINT_NAME_2 = 'supply_water_temperature_sensor'
_POINT_NAME_3 = 'exhaust_air_damper_command'
_POINT_NAME_4 = 'exhaust_air_damper_status'

_NULL_CALLBACK = lambda validator: None

class TelemetryValidatorTest(absltest.TestCase):

  # TODO: fix this in a way that pylint accepts
  # def testTelemetryValidatorTimesOut(self):
  #   timeout = False
  #   def TimeoutCallback(_):
  #     timeout = True
  #   telemetry_validator.TelemetryValidator({}, 1, TimeoutCallback)
  #   threading.Timer(2, lambda: self.assertIsTrue(timeout))

  def testTelemetryValidatorDetectsUnknownEntity(self):
    validator = telemetry_validator.TelemetryValidator({}, 1, _NULL_CALLBACK)
    validator.ValidateMessage(_MESSAGE_GOOD)
    error = telemetry_error.TelemetryError(
      _ENTITY_NAME_1, None, 'Unknown entity')
    self.assertIn(error, validator.validation_errors)

  def testTelemetryValidatorDetectsMissingPoint(self):
    validator = telemetry_validator.TelemetryValidator(
      _ENTITY_1, 1, _NULL_CALLBACK)
    validator.ValidateMessage(_MESSAGE_MISSING_POINT)
    error = telemetry_error.TelemetryError(
      _ENTITY_NAME_1, _POINT_NAME_2, 'Missing point')
    self.assertIn(error, validator.validation_errors)

  def testTelemetryValidatorDetectsMissingPresentValue(self):
    validator = telemetry_validator.TelemetryValidator(
      _ENTITY_1, 1, _NULL_CALLBACK)
    validator.ValidateMessage(_MESSAGE_MISSING_PRESENT_VALUE)
    error = telemetry_error.TelemetryError(
      _ENTITY_NAME_1, _POINT_NAME_1, 'Missing present value')
    self.assertIn(error, validator.validation_errors)

  def testTelemetryValidatorDetectsInvalidState(self):
    validator = telemetry_validator.TelemetryValidator(
      _ENTITY_2, 1, _NULL_CALLBACK)
    validator.ValidateMessage(_MESSAGE_INVALID_STATE)
    error = telemetry_error.TelemetryError(
      _ENTITY_NAME_2, _POINT_NAME_3, 'Invalid state: BAD_STATE')
    self.assertIn(error, validator.validation_errors)

  def testTelemetryValidatorDetectsInvalidNumber(self):
    validator = telemetry_validator.TelemetryValidator(
      _ENTITY_1, 1, _NULL_CALLBACK)
    validator.ValidateMessage(_MESSAGE_INVALID_NUMBER)
    error = telemetry_error.TelemetryError(
      _ENTITY_NAME_1, _POINT_NAME_1, 'Invalid number: BAD_NUMBER')
    self.assertIn(error, validator.validation_errors)

  def testTelemetryValidatorDetectsBooleanAsInvalidNumber(self):
    validator = telemetry_validator.TelemetryValidator(
      _ENTITY_1, 1, _NULL_CALLBACK)
    validator.ValidateMessage(_MESSAGE_INVALID_NUMBER_BOOLEAN)
    error = telemetry_error.TelemetryError(
      _ENTITY_NAME_1, _POINT_NAME_1, 'Invalid number: False')
    self.assertIn(error, validator.validation_errors)

  def testTelemetryValidatorDetectsMultipleErrorsInMessage(self):
    validator = telemetry_validator.TelemetryValidator(
      _ENTITY_1, 1, _NULL_CALLBACK)
    validator.ValidateMessage(_MESSAGE_MULTIPLE_ERRORS)
    error_one = telemetry_error.TelemetryError(
      _ENTITY_NAME_1, _POINT_NAME_1, 'Invalid number: BAD_NUMBER')
    error_two = telemetry_error.TelemetryError(
      _ENTITY_NAME_1, _POINT_NAME_2, 'Missing point')
    self.assertIn(error_one, validator.validation_errors)
    self.assertIn(error_two, validator.validation_errors)

  def testTelemetryValidatorCallbackWhenAllEntitiesValidated(self):
    def ValidationCallback(validator):
      self.assertEmpty(validator.validation_errors)
      self.assertTrue(validator.AllEntitiesValidated())
    validator = telemetry_validator.TelemetryValidator(
      _ENTITY_1, 1, ValidationCallback)
    validator.ValidateMessage(_MESSAGE_GOOD)

if __name__ == '__main__':
  absltest.main()
