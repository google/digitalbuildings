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
"""Tests for EntityField class."""

from absl.testing import absltest

from model.constants import BC_GUID
from model.constants import DATA_TYPE
from model.constants import DEVICE_ID
from model.constants import LINKED_ENTITY_GUID
from model.constants import METADATA
from model.constants import RAW_FIELD_NAME
from model.constants import RAW_STATE
from model.constants import RAW_UNIT_PATH
from model.constants import RAW_UNIT_VALUE
from model.constants import STANDARD_FIELD_NAME
from model.constants import STANDARD_STATE
from model.constants import STANDARD_UNIT_VALUE
from model.entity_field import EntityField
from model.state import State
from model.telemetry_format import TelemetryFormat
from model.units import Units
from google3.third_party.digitalbuildings.tools.concrete_model.tests.test_constants import TEST_DEVICE_ID
from google3.third_party.digitalbuildings.tools.concrete_model.tests.test_constants import TEST_RAW_FIELD_NAME
from google3.third_party.digitalbuildings.tools.concrete_model.tests.test_constants import TEST_REPORTING_GUID
from google3.third_party.digitalbuildings.tools.concrete_model.tests.test_constants import TEST_STANDARD_FIELD_NAME

_TEST_ENTITY_FIELD_DICT = {
    STANDARD_FIELD_NAME: TEST_STANDARD_FIELD_NAME,
    RAW_FIELD_NAME: TEST_RAW_FIELD_NAME,
    LINKED_ENTITY_GUID: None,
    BC_GUID: TEST_REPORTING_GUID,
    DATA_TYPE: TelemetryFormat.UDMI,
    DEVICE_ID: TEST_DEVICE_ID,
    RAW_UNIT_PATH: None,
    STANDARD_UNIT_VALUE: None,
    RAW_UNIT_VALUE: None,
    METADATA + '.test': 'test metadata'
}

_TEST_ENTITY_FIELD_DICT_WITH_UNITS = {
    STANDARD_FIELD_NAME:
        TEST_STANDARD_FIELD_NAME,
    RAW_FIELD_NAME:
        TEST_RAW_FIELD_NAME,
    LINKED_ENTITY_GUID:
        None,
    BC_GUID:
        TEST_REPORTING_GUID,
    DATA_TYPE:
        TelemetryFormat.UDMI,
    DEVICE_ID:
        TEST_DEVICE_ID,
    RAW_UNIT_PATH:
        'pointset.points.filter_differential_pressure_setpoint.units',
    STANDARD_UNIT_VALUE:
        'pascals',
    RAW_UNIT_VALUE:
        'Pa',
    METADATA + '.test':
        'test metadata'
}

_TEST_STATE = State.FromDict({
    BC_GUID: 'test_guid',
    STANDARD_FIELD_NAME: 'discharge_fan_run_command',
    STANDARD_STATE: 'ON',
    RAW_STATE: 'TRUE'
})

_TEST_UNITS = Units(
    raw_unit_path='points.return_air_temperature_sensor.units',
    standard_to_raw_unit_map={'degrees_celsius': 'degC'})


class EntityFieldTest(absltest.TestCase):

  def testEntityFieldBuildsFromDict(self):
    test_entity_field_instance = EntityField.FromDict(
        _TEST_ENTITY_FIELD_DICT_WITH_UNITS)

    self.assertEqual(test_entity_field_instance.standard_field_name,
                     TEST_STANDARD_FIELD_NAME)
    self.assertEqual(test_entity_field_instance.raw_field_name,
                     TEST_RAW_FIELD_NAME)
    self.assertEqual(test_entity_field_instance.data_type,
                     TelemetryFormat.UDMI)
    self.assertEqual(test_entity_field_instance.device_id, TEST_DEVICE_ID)
    self.assertIsInstance(test_entity_field_instance.units, Units)
    self.assertEqual(test_entity_field_instance.metadata,
                     {'test': 'test metadata'})

  def testAddState(self):
    test_entity_field_instance = EntityField.FromDict(_TEST_ENTITY_FIELD_DICT)

    test_entity_field_instance.states = [_TEST_STATE]

    self.assertEqual(test_entity_field_instance.states.pop(), _TEST_STATE)

  def testAddStateRaisesTypeError(self):
    test_entity_field_instance = EntityField.FromDict(_TEST_ENTITY_FIELD_DICT)

    with self.assertRaises(TypeError):
      test_entity_field_instance.AddState('state_string')

  def testAddUnits(self):
    test_entity_field_instance = EntityField.FromDict(_TEST_ENTITY_FIELD_DICT)

    test_entity_field_instance.units = _TEST_UNITS

    self.assertEqual(test_entity_field_instance.units, _TEST_UNITS)

  def testEntityFieldWithStatesRaisesAttributeError(self):
    test_entity_field_instance = EntityField.FromDict(_TEST_ENTITY_FIELD_DICT)

    test_entity_field_instance.states = [_TEST_STATE]

    with self.assertRaises(AttributeError):
      test_entity_field_instance.units = _TEST_UNITS

  def testEntityFieldWithUnitsRaisesAttributeError(self):
    test_entity_field_instance = EntityField.FromDict(
        _TEST_ENTITY_FIELD_DICT_WITH_UNITS)

    with self.assertRaises(AttributeError):
      test_entity_field_instance.states = [_TEST_STATE]

if __name__ == '__main__':
  absltest.main()
