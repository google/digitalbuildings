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
"""Tests tools.validators.instance_validator.telemetry_validator."""

from __future__ import absolute_import
from __future__ import print_function

import json
from os import path

from absl.testing import absltest

from tests import test_constants
from validate import entity_instance
from validate import handler
from validate import instance_parser
from validate import telemetry_validator


_TELEMETRY_PATH = test_constants.TEST_TELEMETRY
_INSTANCES_PATH = path.join(test_constants.TEST_INSTANCES, 'GOOD')

_MESSAGE_ATTRIBUTES_PATH_1 = path.join(
    _TELEMETRY_PATH, 'message_attributes_CHWS_WDT-17.json'
)
with open(_MESSAGE_ATTRIBUTES_PATH_1, encoding='utf-8') as f:
  _MESSAGE_ATTRIBUTES_1 = json.load(f)

_MESSAGE_ATTRIBUTES_PATH_2 = path.join(
    _TELEMETRY_PATH, 'message_attributes_DMP_EDM-17.json'
)
with open(_MESSAGE_ATTRIBUTES_PATH_2, encoding='utf-8') as f:
  _MESSAGE_ATTRIBUTES_2 = json.load(f)

_MESSAGE_ATTRIBUTES_PATH_3 = path.join(
    _TELEMETRY_PATH, 'message_attributes_SDC_EXT-17.json'
)
with open(_MESSAGE_ATTRIBUTES_PATH_3, encoding='utf-8') as f:
  _MESSAGE_ATTRIBUTES_3 = json.load(f)

_MESSAGE_ATTRIBUTES_PATH_4 = path.join(
    _TELEMETRY_PATH, 'message_attributes_FAN-17.json'
)
with open(_MESSAGE_ATTRIBUTES_PATH_4, encoding='utf-8') as f:
  _MESSAGE_ATTRIBUTES_4 = json.load(f)


class FakeMessage(object):

  def __init__(self, attributes, data):
    super().__init__()
    self.attributes = attributes
    self.data = data

  def ack(self):
    return NotImplemented


with open(
    path.join(_TELEMETRY_PATH, 'telemetry_good.json'), encoding='utf-8'
) as file:
  file_contents = file.read()
  _MESSAGEGOOD = FakeMessage(_MESSAGE_ATTRIBUTES_1, file_contents)
  _MESSAGEGOOD_2 = FakeMessage(_MESSAGE_ATTRIBUTES_3, file_contents)

with open(
    path.join(_TELEMETRY_PATH, 'telemetry_missing_point.json'), encoding='utf-8'
) as file:
  _MESSAGE_MISSING_POINT = FakeMessage(_MESSAGE_ATTRIBUTES_1, file.read())

with open(
    path.join(_TELEMETRY_PATH, 'telemetry_missing_point_partial.json'),
    encoding='utf-8',
) as file:
  _MESSAGE_MISSING_GOOD_POINT_PARTIAL = FakeMessage(
      _MESSAGE_ATTRIBUTES_1, file.read()
  )

with open(
    path.join(_TELEMETRY_PATH, 'telemetry_missing_present_value.json'),
    encoding='utf-8',
) as file:
  _MESSAGE_MISSING_PRESENT_VALUE = FakeMessage(
      _MESSAGE_ATTRIBUTES_1, file.read()
  )

with open(
    path.join(_TELEMETRY_PATH, 'telemetry_invalid_state.json'), encoding='utf-8'
) as file:
  _MESSAGE_INVALID_STATE = FakeMessage(_MESSAGE_ATTRIBUTES_2, file.read())

with open(
    path.join(_TELEMETRY_PATH, 'telemetry_invalid_json.json'), encoding='utf-8'
) as file:
  _MESSAGE_INVALID_JSON = FakeMessage(_MESSAGE_ATTRIBUTES_2, file.read())

with open(
    path.join(_TELEMETRY_PATH, 'telemetry_invalid_number.json'),
    encoding='utf-8',
) as file:
  _MESSAGE_INVALID_NUMBER = FakeMessage(_MESSAGE_ATTRIBUTES_1, file.read())

with open(
    path.join(_TELEMETRY_PATH, 'telemetry_invalid_number_boolean.json'),
    encoding='utf-8',
) as file:
  _MESSAGE_INVALID_NUMBER_BOOLEAN = FakeMessage(
      _MESSAGE_ATTRIBUTES_1, file.read()
  )

with open(
    path.join(_TELEMETRY_PATH, 'telemetry_multiple_errors.json'),
    encoding='utf-8',
) as file:
  _MESSAGE_MULTIPLE_ERRORS = FakeMessage(_MESSAGE_ATTRIBUTES_1, file.read())

with open(
    path.join(_TELEMETRY_PATH, 'telemetry_good_multistates.json'),
    encoding='utf-8',
) as file:
  _MESSAGEGOOD_MULTIPLE_STATES = FakeMessage(_MESSAGE_ATTRIBUTES_4, file.read())

with open(
    path.join(_TELEMETRY_PATH, 'telemetry_string_state.json'), encoding='utf-8'
) as file:
  _MESSAGE_STRING_STATES = FakeMessage(_MESSAGE_ATTRIBUTES_2, file.read())

with open(
    path.join(_TELEMETRY_PATH, 'telemetry_good_states_list.json'),
    encoding='utf-8',
) as file:
  _MESSAGEGOOD_STATES_LIST = FakeMessage(_MESSAGE_ATTRIBUTES_2, file.read())

# TODO(nkilmer): fix inconsistency between telemetry parser expecting a string,
# but instance parser expecting a file


def _CreateEntityInstances(yaml_filename):
  parser = instance_parser.InstanceParser()
  parser.AddFile(path.join(_INSTANCES_PATH, yaml_filename))
  parser.Finalize()
  default_operation = handler.GetDefaultOperation(parser.GetConfigMode())
  parsed_yaml = parser.GetEntities()

  parsed_entities = {}
  for key, value in parsed_yaml.items():
    parsed_entities.update(
        {
            key: entity_instance.EntityInstance.FromYaml(
                key, value, default_operation=default_operation
            )
        }
    )
  return parsed_entities


# A single test entity with numeric fields.
GOOD_ENTITIES_1 = _CreateEntityInstances('translation_units.yaml')
GOOD_ENTITY_NAME_1 = 'CHWS_WDT-17'

# A single test entity with multistate fields.
GOOD_ENTITIES_2 = _CreateEntityInstances('translation_states.yaml')
GOOD_ENTITY_NAME_2 = 'DMP_EDM-17'

# A set of two test entities with identical points.
GOOD_ENTITIES_3_4 = _CreateEntityInstances('translation_identical.yaml')
GOOD_ENTITY_NAME_3 = 'SDC_EXT-17'
GOOD_ENTITY_NAME_4 = 'SDC_EXT-18'
# A test entity to make sure that booleans are retrieved and validated.
GOOD_ENTITIES_5 = _CreateEntityInstances('translation_multi_states.yaml')
GOOD_ENTITY_NAME_5 = 'FAN-17'

# A test entity with a field that maps multiple raw values to one state.
GOOD_ENTITIES_6 = _CreateEntityInstances('translation_states_list.yaml')
GOOD_ENTITY_NAME_6 = 'DMP_EDM-17'

# A test entity with a field that maps multiple raw values to one state.
GOOD_ENTITIES_7 = _CreateEntityInstances('translation_string_states.yaml')
GOOD_ENTITY_NAME_7 = 'DMP_EDM-17'

GOOD_POINT_NAME_1 = 'points.return_water_temperature_sensor.present_value'
GOOD_POINT_NAME_2 = 'points.supply_water_temperature_sensor.present_value'
GOOD_POINT_NAME_3 = 'points.exhaust_air_damper_command.present_value'
GOOD_POINT_NAME_4 = 'points.exhaust_air_damper_status.present_value'


def _NullCallback(validator) -> None:
  """Replacement for _NULL_CALLBACK lambda function."""
  if validator:
    return None
  return None


class TelemetryValidatorTest(absltest.TestCase):

  # TODO(nkilmer): fix this in a way that pylint accepts
  # def testTelemetryValidatorTimesOut(self):
  #   timeout = False
  #   def TimeoutCallback(_):
  #     timeout = True
  #   telemetry_validator.TelemetryValidator({}, 1, TimeoutCallback)
  #   threading.Timer(2, lambda: self.assertIsTrue(timeout))

  def testTelemetryValidatorGetUnvalidatedEntitiesReturnsMissingEntities(self):
    validator = telemetry_validator.TelemetryValidator(
        GOOD_ENTITIES_3_4, 1, is_udmi=False, callback=_NullCallback
    )

    validator.ValidateMessage(_MESSAGEGOOD_2)
    validator.validated_entities.update({'fake_entity_code': True})

    unvalidated_entities = validator.GetUnvalidatedEntities()
    self.assertNotIn(GOOD_ENTITY_NAME_3, unvalidated_entities.values())
    self.assertIn(GOOD_ENTITY_NAME_4, unvalidated_entities.values())
    self.assertLen(unvalidated_entities, 1)
    self.assertLen(validator.GetExtraEntities(), 1)

  def testTelemetryValidatorGetUnvalidatedEntitiesReturnsExtraEntities(self):
    validator = telemetry_validator.TelemetryValidator(
        GOOD_ENTITIES_3_4, 1, is_udmi=False, callback=_NullCallback
    )
    validator.ValidateMessage(_MESSAGEGOOD_2)
    validator.validated_entities.update(
        {'fake_entity_guid': 'fake_entity_code'}
    )

    validator.GetUnvalidatedEntities()

    extra_entities = validator.GetExtraEntities()
    self.assertLen(extra_entities, 1)
    self.assertNotIn(GOOD_ENTITY_NAME_3, extra_entities.values())
    self.assertNotIn(GOOD_ENTITY_NAME_4, extra_entities.values())
    self.assertIn('fake_entity_code', extra_entities.values())

  def testTelemetryValidatorIgnoresMissingPointOnPartialUpdate(self):
    validator = telemetry_validator.TelemetryValidator(
        GOOD_ENTITIES_1, 1, is_udmi=False, callback=_NullCallback
    )

    validator.ValidateMessage(_MESSAGE_MISSING_GOOD_POINT_PARTIAL)

    self.assertEmpty(validator.GetInvalidMessageBlocks())

  def testTelemetryValidatorDetectsMissingPoint(self):
    validator = telemetry_validator.TelemetryValidator(
        GOOD_ENTITIES_1, 1, is_udmi=False, callback=_NullCallback
    )

    validator.ValidateMessage(_MESSAGE_MISSING_POINT)
    error_blocks = validator.GetInvalidMessageBlocks()

    self.assertLen(error_blocks, 1)
    self.assertLen(error_blocks[0].missing_points, 1)

  def testTelemetryValidatorDetectsMissingPresentValue(self):
    validator = telemetry_validator.TelemetryValidator(
        GOOD_ENTITIES_1, 1, is_udmi=False, callback=_NullCallback
    )

    validator.ValidateMessage(_MESSAGE_MISSING_PRESENT_VALUE)
    error_blocks = validator.GetInvalidMessageBlocks()

    self.assertLen(error_blocks, 1)
    self.assertLen(error_blocks[0].missing_present_values, 1)

  def testTelemetryValidatorDetectsUnmappedState(self):
    validator = telemetry_validator.TelemetryValidator(
        GOOD_ENTITIES_2, 1, is_udmi=False, callback=_NullCallback
    )

    validator.ValidateMessage(_MESSAGE_INVALID_STATE)
    error_blocks = validator.GetInvalidMessageBlocks()

    self.assertLen(error_blocks, 1)
    self.assertLen(error_blocks[0].unmapped_states, 2)

  def testTelemetryValidatorDetectsStringAsInvalidNumber(self):
    validator = telemetry_validator.TelemetryValidator(
        GOOD_ENTITIES_1, 1, is_udmi=False, callback=_NullCallback
    )

    validator.ValidateMessage(_MESSAGE_INVALID_NUMBER)
    error_blocks = validator.GetInvalidMessageBlocks()

    self.assertLen(error_blocks, 1)
    self.assertLen(error_blocks[0].invalid_dimensional_values, 1)

  def testTelemetryValidatorDetectsBooleanAsInvalidNumber(self):
    validator = telemetry_validator.TelemetryValidator(
        GOOD_ENTITIES_1, 1, is_udmi=False, callback=_NullCallback
    )

    validator.ValidateMessage(_MESSAGE_INVALID_NUMBER_BOOLEAN)
    error_blocks = validator.GetInvalidMessageBlocks()

    self.assertLen(error_blocks, 1)
    self.assertLen(error_blocks[0].invalid_dimensional_values, 1)

  def testTelemetryValidatorDetectsMultipleErrorsInMessage(self):
    validator = telemetry_validator.TelemetryValidator(
        GOOD_ENTITIES_1, 1, is_udmi=False, callback=_NullCallback
    )

    validator.ValidateMessage(_MESSAGE_MULTIPLE_ERRORS)
    error_blocks = validator.GetInvalidMessageBlocks()

    self.assertLen(error_blocks, 1)
    self.assertLen(error_blocks[0].invalid_dimensional_values, 1)
    self.assertLen(error_blocks[0].missing_points, 1)

  def testTelemetryValidatorCallbackWhenAllEntitiesValidated(self):
    def ValidationCallback(validator):
      self.assertEmpty(validator.GetInvalidMessageBlocks())
      self.assertTrue(validator.AllEntitiesValidated())

    validator = telemetry_validator.TelemetryValidator(
        GOOD_ENTITIES_1, 1, is_udmi=False, callback=ValidationCallback
    )

    validator.ValidateMessage(_MESSAGEGOOD)

  def testTelemetryValidatorAddsExtraDevicesWhenValidated(self):
    validator = telemetry_validator.TelemetryValidator(
        GOOD_ENTITIES_2, 1, is_udmi=False, callback=_NullCallback
    )

    validator.ValidateMessage(_MESSAGE_MISSING_PRESENT_VALUE)
    extra_enities = validator.GetExtraEntities()
    missing_entities = validator.GetUnvalidatedEntities()

    self.assertLen(extra_enities, 1)
    self.assertLen(missing_entities, 1)
    self.assertIn(GOOD_ENTITY_NAME_1, extra_enities.values())
    self.assertIn(GOOD_ENTITY_NAME_2, missing_entities.values())

  def testTelemetryValidatorOnMultiStateWithBooleanSuccess(self):
    def ValidationCallback(validator):
      self.assertEmpty(validator.GetInvalidMessageBlocks())
      self.assertTrue(validator.AllEntitiesValidated())

    validator = telemetry_validator.TelemetryValidator(
        GOOD_ENTITIES_5, 1, is_udmi=False, callback=ValidationCallback
    )
    validator.ValidateMessage(_MESSAGEGOOD_MULTIPLE_STATES)

  def testTelemetryValidatorOnMultiStateWithRawValueList(self):
    def ValidationCallback(validator):
      self.assertEmpty(validator.GetInvalidMessageBlocks())
      self.assertTrue(validator.AllEntitiesValidated())

    validator = telemetry_validator.TelemetryValidator(
        GOOD_ENTITIES_6, 1, is_udmi=False, callback=ValidationCallback
    )

    validator.ValidateMessage(_MESSAGEGOOD_STATES_LIST)

  def testTelemetryValidatorOnMultiStateWithStringSuccess(self):
    def ValidationCallback(validator):
      self.assertEmpty(validator.GetInvalidMessageBlocks())
      self.assertTrue(validator.AllEntitiesValidated())

    validator = telemetry_validator.TelemetryValidator(
        GOOD_ENTITIES_7, 1, is_udmi=False, callback=ValidationCallback
    )

    validator.ValidateMessage(_MESSAGE_STRING_STATES)

  def testInvalidJsonMessageDoesNotRaiseException(self):
    def ValidationCallback(validator):
      self.assertEmpty(validator.GetInvalidMessageBlocks())
      self.assertTrue(validator.AllEntitiesValidated())

    validator = telemetry_validator.TelemetryValidator(
        GOOD_ENTITIES_1, 1, is_udmi=False, callback=ValidationCallback
    )

    validator.ValidateMessage(_MESSAGE_INVALID_JSON)


if __name__ == '__main__':
  absltest.main()
