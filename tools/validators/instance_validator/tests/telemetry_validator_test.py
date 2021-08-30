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
"""Tests tools.validators.instance_validator.telemetry_validator."""

from __future__ import absolute_import
from __future__ import print_function

import json
from os import path

from absl.testing import absltest
from tests import test_constants
from validate import entity_instance
from validate import instance_parser
from validate import telemetry_error
from validate import telemetry_validator

_TELEMETRY_PATH = test_constants.TEST_TELEMETRY
_INSTANCES_PATH = path.join(test_constants.TEST_INSTANCES, 'GOOD')

_MESSAGE_ATTRIBUTES_PATH_1 = path.join(_TELEMETRY_PATH,
                                       'message_attributes_CHWS_WDT-17.json')
with open(_MESSAGE_ATTRIBUTES_PATH_1) as f:
  _MESSAGE_ATTRIBUTES_1 = json.load(f)

_MESSAGE_ATTRIBUTES_PATH_2 = path.join(_TELEMETRY_PATH,
                                       'message_attributes_DMP_EDM-17.json')
with open(_MESSAGE_ATTRIBUTES_PATH_2) as f:
  _MESSAGE_ATTRIBUTES_2 = json.load(f)

_MESSAGE_ATTRIBUTES_PATH_3 = path.join(_TELEMETRY_PATH,
                                       'message_attributes_SDC_EXT-17.json')
with open(_MESSAGE_ATTRIBUTES_PATH_3) as f:
  _MESSAGE_ATTRIBUTES_3 = json.load(f)

_MESSAGE_ATTRIBUTES_PATH_4 = path.join(_TELEMETRY_PATH,
                                       'message_attributes_FAN-17.json')
with open(_MESSAGE_ATTRIBUTES_PATH_4) as f:
  _MESSAGE_ATTRIBUTES_4 = json.load(f)


class FakeMessage(object):

  def __init__(self, attributes, data):
    super().__init__()
    self.attributes = attributes
    self.data = data

  def ack(self):
    return NotImplemented


with open(path.join(_TELEMETRY_PATH, 'telemetry_good.json')) as file:
  file_contents = file.read()
  _MESSAGE_GOOD = FakeMessage(_MESSAGE_ATTRIBUTES_1, file_contents)
  _MESSAGE_GOOD_2 = FakeMessage(_MESSAGE_ATTRIBUTES_3, file_contents)

with open(path.join(_TELEMETRY_PATH, 'telemetry_missing_point.json')) as file:
  _MESSAGE_MISSING_POINT = FakeMessage(_MESSAGE_ATTRIBUTES_1, file.read())

with open(path.join(_TELEMETRY_PATH,
                    'telemetry_missing_point_partial.json')) as file:
  _MESSAGE_MISSING_POINT_PARTIAL = FakeMessage(_MESSAGE_ATTRIBUTES_1,
                                               file.read())

with open(path.join(_TELEMETRY_PATH,
                    'telemetry_missing_present_value.json')) as file:
  _MESSAGE_MISSING_PRESENT_VALUE = FakeMessage(_MESSAGE_ATTRIBUTES_1,
                                               file.read())

with open(path.join(_TELEMETRY_PATH, 'telemetry_invalid_state.json')) as file:
  _MESSAGE_INVALID_STATE = FakeMessage(_MESSAGE_ATTRIBUTES_2, file.read())

with open(path.join(_TELEMETRY_PATH, 'telemetry_invalid_number.json')) as file:
  _MESSAGE_INVALID_NUMBER = FakeMessage(_MESSAGE_ATTRIBUTES_1, file.read())

with open(path.join(_TELEMETRY_PATH,
                    'telemetry_invalid_number_boolean.json')) as file:
  _MESSAGE_INVALID_NUMBER_BOOLEAN = FakeMessage(_MESSAGE_ATTRIBUTES_1,
                                                file.read())

with open(path.join(_TELEMETRY_PATH, 'telemetry_multiple_errors.json')) as file:
  _MESSAGE_MULTIPLE_ERRORS = FakeMessage(_MESSAGE_ATTRIBUTES_1, file.read())

  with open(path.join(_TELEMETRY_PATH,
                      'telemetry_good_multistates.json')) as file:
    _MESSAGE_GOOD_MULTIPLE_STATES = FakeMessage(_MESSAGE_ATTRIBUTES_4,
                                                file.read())

# TODO: fix inconsistency between telemetry parser expecting a string,
# but instance parser expecting a file


def _CreateEntityInstances(yaml_filename):
  parser = instance_parser.InstanceParser()
  parser.AddFile(path.join(_INSTANCES_PATH, yaml_filename))
  parser.Finalize()
  parsed_yaml = parser.GetEntities()

  entities = {}
  for entity_name, entity_yaml in parsed_yaml.items():
    entities[entity_name] = entity_instance.EntityInstance.FromYaml(entity_yaml)
  return entities


# A single test entity with numeric fields.
_ENTITIES_1 = _CreateEntityInstances('good_translation_units.yaml')
_ENTITY_NAME_1 = 'CHWS_WDT-17'

# A single test entity with multistate fields.
_ENTITIES_2 = _CreateEntityInstances('good_translation_states.yaml')
_ENTITY_NAME_2 = 'DMP_EDM-17'

# A set of two test entities with identical points.
_ENTITIES_3_4 = _CreateEntityInstances('good_translation_identical.yaml')
_ENTITY_NAME_3 = 'SDC_EXT-17'
_ENTITY_NAME_4 = 'SDC_EXT-18'
# A test entity to make sure that booleans are retrieved and validated.
_ENTITIES_5 = _CreateEntityInstances('good_translation_multi_states.yaml')
_ENTITY_NAME_5 = 'FAN-17'

_POINT_NAME_1 = 'points.return_water_temperature_sensor.present_value'
_POINT_NAME_2 = 'points.supply_water_temperature_sensor.present_value'
_POINT_NAME_3 = 'points.exhaust_air_damper_command.present_value'
_POINT_NAME_4 = 'points.exhaust_air_damper_status.present_value'

_NULL_CALLBACK = lambda validator: None


class TelemetryValidatorTest(absltest.TestCase):

  # TODO: fix this in a way that pylint accepts
  # def testTelemetryValidatorTimesOut(self):
  #   timeout = False
  #   def TimeoutCallback(_):
  #     timeout = True
  #   telemetry_validator.TelemetryValidator({}, 1, TimeoutCallback)
  #   threading.Timer(2, lambda: self.assertIsTrue(timeout))

  def testTelemetryValidatorGetErrorsReturnsAllErrors(self):
    validator = telemetry_validator.TelemetryValidator(_ENTITIES_1, 1,
                                                       _NULL_CALLBACK)
    error_one = telemetry_error.TelemetryError(_ENTITY_NAME_1, _POINT_NAME_1,
                                               'Test error 1')
    error_two = telemetry_error.TelemetryError(_ENTITY_NAME_2, _POINT_NAME_2,
                                               'Test error 2')

    validator.AddError(error_one)
    validator.AddError(error_two)
    errors = validator.GetErrors()

    self.assertIn(error_one, errors)
    self.assertIn(error_two, errors)
    self.assertEqual(len(errors), 2)

  def testTelemetryValidatorGetUnvalidatedEntitiesReturnsMissingEntities(self):
    validator = telemetry_validator.TelemetryValidator(_ENTITIES_3_4, 1,
                                                       _NULL_CALLBACK)

    validator.ValidateMessage(_MESSAGE_GOOD_2)

    unvalidated_entities = validator.GetUnvalidatedEntityNames()
    self.assertNotIn(_ENTITY_NAME_3, unvalidated_entities)
    self.assertIn(_ENTITY_NAME_4, unvalidated_entities)
    self.assertEqual(len(unvalidated_entities), 1)

  def testTelemetryValidatorIgnoresMissingPointOnPartialUpdate(self):
    validator = telemetry_validator.TelemetryValidator(_ENTITIES_1, 1,
                                                       _NULL_CALLBACK)

    validator.ValidateMessage(_MESSAGE_MISSING_POINT_PARTIAL)

    self.assertEmpty(validator.GetErrors())

  def testTelemetryValidatorDetectsMissingPoint(self):
    validator = telemetry_validator.TelemetryValidator(_ENTITIES_1, 1,
                                                       _NULL_CALLBACK)

    validator.ValidateMessage(_MESSAGE_MISSING_POINT)

    error = telemetry_error.TelemetryError(
        _ENTITY_NAME_1, _POINT_NAME_2, 'Field missing from '
        'telemetry message')
    errors = validator.GetErrors()
    self.assertIn(error, errors)
    self.assertEqual(len(errors), 1)

  def testTelemetryValidatorDetectsMissingPresentValue(self):
    validator = telemetry_validator.TelemetryValidator(_ENTITIES_1, 1,
                                                       _NULL_CALLBACK)

    validator.ValidateMessage(_MESSAGE_MISSING_PRESENT_VALUE)

    error = telemetry_error.TelemetryError(
        _ENTITY_NAME_1, _POINT_NAME_1, 'Missing number in telemetry message'
        ': None')

    errors = validator.GetErrors()
    self.assertIn(error, errors)
    self.assertEqual(len(errors), 1)

  def testTelemetryValidatorDetectsInvalidState(self):
    validator = telemetry_validator.TelemetryValidator(_ENTITIES_2, 1,
                                                       _NULL_CALLBACK)

    validator.ValidateMessage(_MESSAGE_INVALID_STATE)

    error1 = telemetry_error.TelemetryError(
        _ENTITY_NAME_2, _POINT_NAME_3, 'Missing state in telemetry message'
        ': None')
    error2 = telemetry_error.TelemetryError(
        _ENTITY_NAME_2, _POINT_NAME_4, 'Missing state in telemetry message'
        ': None')

    errors = validator.GetErrors()
    self.assertIn(error1, errors)
    self.assertIn(error2, errors)
    self.assertEqual(len(errors), 2)

  def testTelemetryValidatorDetectsNoneValue(self):
    validator = telemetry_validator.TelemetryValidator(_ENTITIES_1, 1,
                                                       _NULL_CALLBACK)

    validator.ValidateMessage(_MESSAGE_INVALID_NUMBER)

    error = telemetry_error.TelemetryError(
        _ENTITY_NAME_1, _POINT_NAME_1, 'Missing number in telemetry message'
        ': None')

    errors = validator.GetErrors()
    self.assertIn(error, errors)
    self.assertEqual(len(errors), 1)

  def testTelemetryValidatorDetectsBooleanAsInvalidNumber(self):
    validator = telemetry_validator.TelemetryValidator(_ENTITIES_1, 1,
                                                       _NULL_CALLBACK)

    validator.ValidateMessage(_MESSAGE_INVALID_NUMBER_BOOLEAN)

    error = telemetry_error.TelemetryError(
        _ENTITY_NAME_1, _POINT_NAME_1, 'Invalid number in telemetry message'
        ': false')

    errors = validator.GetErrors()
    self.assertIn(error, errors)
    self.assertEqual(len(errors), 1)

  def testTelemetryValidatorDetectsMultipleErrorsInMessage(self):
    validator = telemetry_validator.TelemetryValidator(_ENTITIES_1, 1,
                                                       _NULL_CALLBACK)

    validator.ValidateMessage(_MESSAGE_MULTIPLE_ERRORS)

    error_one = telemetry_error.TelemetryError(
        _ENTITY_NAME_1, _POINT_NAME_1, 'Missing number in telemetry '
        'message: None')
    error_two = telemetry_error.TelemetryError(
        _ENTITY_NAME_1, _POINT_NAME_2, 'Field missing from telemetry '
        'message')

    errors = validator.GetErrors()
    self.assertIn(error_one, errors)
    self.assertIn(error_two, errors)
    self.assertEqual(len(errors), 2)

  def testTelemetryValidatorCallbackWhenAllEntitiesValidated(self):

    def ValidationCallback(validator):
      self.assertEmpty(validator.GetErrors())
      self.assertTrue(validator.AllEntitiesValidated())

    validator = telemetry_validator.TelemetryValidator(_ENTITIES_1, 1,
                                                       ValidationCallback)

    validator.ValidateMessage(_MESSAGE_GOOD)

  def testTelemetryValidatorOnMultiStateWithBooleanSuccess(self):

    def ValidationCallback(validator):
      self.assertEmpty(validator.GetErrors())
      self.assertTrue(validator.AllEntitiesValidated())

    validator = telemetry_validator.TelemetryValidator(_ENTITIES_5, 1,
                                                       ValidationCallback)

    validator.ValidateMessage(_MESSAGE_GOOD_MULTIPLE_STATES)


if __name__ == '__main__':
  absltest.main()
