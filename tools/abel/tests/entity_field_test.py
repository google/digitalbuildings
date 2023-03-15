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
"""Tests for entity_field.py."""

from unittest import mock

from absl.testing import absltest

from model.constants import BC_GUID
from model.constants import ENTITY_CODE
from model.constants import MISSING
from model.constants import RAW_FIELD_NAME
from model.constants import RAW_UNIT_PATH
from model.constants import RAW_UNIT_VALUE
from model.constants import REPORTING_ENTITY_CODE
from model.constants import REPORTING_ENTITY_FIELD_NAME
from model.constants import REPORTING_ENTITY_GUID
from model.constants import STANDARD_FIELD_NAME
from model.constants import STANDARD_UNIT_VALUE
from model.entity_field import DimensionalValueField
from model.entity_field import MissingField
from model.entity_field import MultistateValueField
from model.guid_to_entity_map import GuidToEntityMap
from model.state import State
from model.units import Units
from google3.third_party.digitalbuildings.tools.abel.tests.test_constants import TEST_DIMENSIONAL_VALUE_FIELD_DICT
from google3.third_party.digitalbuildings.tools.abel.tests.test_constants import TEST_FIELD_DICT_NO_UNITS
from google3.third_party.digitalbuildings.tools.abel.tests.test_constants import TEST_MISSING_FIELD_DICT
from google3.third_party.digitalbuildings.tools.abel.tests.test_constants import TEST_RAW_FIELD_NAME
from google3.third_party.digitalbuildings.tools.abel.tests.test_constants import TEST_RAW_FIELD_NAME_2
from google3.third_party.digitalbuildings.tools.abel.tests.test_constants import TEST_REPORTING_ENTITY_CODE
from google3.third_party.digitalbuildings.tools.abel.tests.test_constants import TEST_REPORTING_FIELD_NAME
from google3.third_party.digitalbuildings.tools.abel.tests.test_constants import TEST_REPORTING_GUID
from google3.third_party.digitalbuildings.tools.abel.tests.test_constants import TEST_STANDARD_FIELD_NAME
from google3.third_party.digitalbuildings.tools.abel.tests.test_constants import TEST_STANDARD_FIELD_NAME_2
from google3.third_party.digitalbuildings.tools.abel.tests.test_constants import TEST_STANDARD_FIELD_NAME_3
from google3.third_party.digitalbuildings.tools.abel.tests.test_constants import TEST_STATE_DICT
from google3.third_party.digitalbuildings.tools.abel.tests.test_constants import TEST_UNITS
from google3.third_party.digitalbuildings.tools.abel.tests.test_constants import TEST_VIRTUAL_ENTITY_CODE
from google3.third_party.digitalbuildings.tools.abel.tests.test_constants import TEST_VIRTUAL_GUID
from validate import field_translation


class MissingFieldTest(absltest.TestCase):

  def testMissingFieldBuildsFromDict(self):
    test_missing_field = MissingField.FromDict(TEST_MISSING_FIELD_DICT)

    self.assertEqual(
        test_missing_field.std_field_name, TEST_STANDARD_FIELD_NAME_3
    )
    self.assertEqual(
        test_missing_field.mode, field_translation.PresenceMode.MISSING
    )
    self.assertEqual(
        test_missing_field.reporting_entity_field_name,
        TEST_STANDARD_FIELD_NAME_3,
    )
    self.assertEqual(
        test_missing_field.reporting_entity_guid, TEST_REPORTING_GUID
    )
    self.assertEqual(test_missing_field.entity_guid, TEST_REPORTING_GUID)
    self.assertEqual(test_missing_field.metadata, {'test': 'test metadata'})

  @mock.patch.object(GuidToEntityMap, 'GetEntityCodeByGuid')
  def testMissingFieldGetSpreadsheetRowMapping(self, test_get_code):
    test_get_code.return_value = TEST_REPORTING_ENTITY_CODE
    test_missing_field = MissingField.FromDict(TEST_MISSING_FIELD_DICT)
    expected_row_mapping = {
        STANDARD_FIELD_NAME: TEST_STANDARD_FIELD_NAME_3,
        RAW_FIELD_NAME: '',
        REPORTING_ENTITY_FIELD_NAME: TEST_STANDARD_FIELD_NAME_3,
        ENTITY_CODE: TEST_REPORTING_ENTITY_CODE,
        BC_GUID: TEST_REPORTING_GUID,
        REPORTING_ENTITY_CODE: TEST_REPORTING_ENTITY_CODE,
        REPORTING_ENTITY_GUID: TEST_REPORTING_GUID,
        MISSING: 'TRUE',
    }

    actual_row_mapping = test_missing_field.GetSpreadsheetRowMapping()

    self.assertEqual(expected_row_mapping, actual_row_mapping)


class MultistateValueFieldTest(absltest.TestCase):

  def testMultistateValueFieldBuildsFromDict(self):
    test_multi_state_value_field_instance = MultistateValueField.FromDict(
        TEST_FIELD_DICT_NO_UNITS
    )

    self.assertEqual(
        test_multi_state_value_field_instance.std_field_name,
        TEST_STANDARD_FIELD_NAME_2,
    )
    self.assertEqual(
        test_multi_state_value_field_instance.raw_field_name,
        TEST_RAW_FIELD_NAME_2,
    )
    self.assertEqual(
        test_multi_state_value_field_instance.metadata,
        {'test': 'test metadata'},
    )

  def testAddState(self):
    test_multi_state_value_field_instance = MultistateValueField.FromDict(
        TEST_FIELD_DICT_NO_UNITS
    )
    test_state = State.FromDict(TEST_STATE_DICT)

    test_multi_state_value_field_instance.AddState(test_state)

    self.assertEqual(
        test_multi_state_value_field_instance.states.pop(), test_state
    )

  def testAddStateRaisesTypeError(self):
    test_multi_state_value_field_instance = MultistateValueField.FromDict(
        TEST_FIELD_DICT_NO_UNITS
    )

    with self.assertRaises(TypeError):
      test_multi_state_value_field_instance.AddState('state_string')

  def testTwoMultistateValueFieldAreEqual(self):
    multi_state_value_field_instance = MultistateValueField.FromDict(
        TEST_FIELD_DICT_NO_UNITS
    )
    multi_state_value_field_instance_2 = MultistateValueField.FromDict(
        TEST_FIELD_DICT_NO_UNITS
    )

    self.assertEqual(
        multi_state_value_field_instance, multi_state_value_field_instance_2
    )

  def testTwoMultistateValueFieldAreNotEqual(self):
    multi_state_value_field_instance = MultistateValueField.FromDict(
        TEST_FIELD_DICT_NO_UNITS
    )
    multi_state_value_field_instance_2 = MultistateValueField.FromDict(
        TEST_FIELD_DICT_NO_UNITS
    )
    multi_state_value_field_instance_2.std_field_name = 'bad_name'

    self.assertNotEqual(
        multi_state_value_field_instance, multi_state_value_field_instance_2
    )

  @mock.patch.object(GuidToEntityMap, 'GetEntityCodeByGuid')
  def testMultistateValueFieldGetSpreadsheetRowMapping(self, test_get_code):
    test_get_code.return_value = TEST_REPORTING_ENTITY_CODE
    multi_state_value_field_instance = MultistateValueField.FromDict(
        TEST_FIELD_DICT_NO_UNITS
    )
    expected_row_mapping = {
        STANDARD_FIELD_NAME: TEST_STANDARD_FIELD_NAME_2,
        RAW_FIELD_NAME: TEST_RAW_FIELD_NAME_2,
        REPORTING_ENTITY_FIELD_NAME: TEST_REPORTING_FIELD_NAME,
        ENTITY_CODE: TEST_REPORTING_ENTITY_CODE,
        BC_GUID: TEST_REPORTING_GUID,
        REPORTING_ENTITY_CODE: TEST_REPORTING_ENTITY_CODE,
        REPORTING_ENTITY_GUID: TEST_REPORTING_GUID,
        MISSING: 'FALSE',
    }

    actual_row_mapping = (
        multi_state_value_field_instance.GetSpreadsheetRowMapping()
    )

    self.assertEqual(expected_row_mapping, actual_row_mapping)

  def testToString(self):
    multi_state_value_field_instance = MultistateValueField.FromDict(
        TEST_FIELD_DICT_NO_UNITS
    )

    self.assertEqual(
        str(multi_state_value_field_instance), 'test_reporting_guid: fire_alarm'
    )


class DimensionalValueFieldTest(absltest.TestCase):

  def testDimensionalValueFieldBuildsFromDict(self):
    test_dimensional_value_field_instance = DimensionalValueField.FromDict(
        TEST_DIMENSIONAL_VALUE_FIELD_DICT
    )

    self.assertEqual(
        test_dimensional_value_field_instance.std_field_name,
        TEST_STANDARD_FIELD_NAME,
    )
    self.assertEqual(
        test_dimensional_value_field_instance.raw_field_name,
        TEST_RAW_FIELD_NAME,
    )
    self.assertIsInstance(test_dimensional_value_field_instance.units, Units)
    self.assertEqual(
        test_dimensional_value_field_instance.metadata,
        {'test': 'test metadata'},
    )

  def testAddUnits(self):
    test_dimensional_value_field_instance = DimensionalValueField.FromDict(
        TEST_DIMENSIONAL_VALUE_FIELD_DICT
    )
    expected_units = Units(
        raw_unit_path='points.filter_differential_pressure_setpoint.units',
        standard_to_raw_unit_map={'pascals': 'Pa'},
    )

    self.assertEqual(
        test_dimensional_value_field_instance.units.raw_unit_path,
        expected_units.raw_unit_path,
    )
    self.assertEqual(
        test_dimensional_value_field_instance.units.standard_to_raw_unit_map,
        expected_units.standard_to_raw_unit_map,
    )

  def testSetUnitsRaisesTypeError(self):
    test_dimensional_value_field_instance = DimensionalValueField.FromDict(
        TEST_DIMENSIONAL_VALUE_FIELD_DICT
    )

    with self.assertRaises(TypeError):
      test_dimensional_value_field_instance.units = 'bad_units'

  def testSetUnitsRaisesValueError(self):
    test_dimensional_value_field_instance = DimensionalValueField.FromDict(
        TEST_DIMENSIONAL_VALUE_FIELD_DICT
    )

    with self.assertRaises(ValueError):
      test_dimensional_value_field_instance.units = TEST_UNITS

  def testDimensionalValueFieldEquality(self):
    test_dimensional_value_field_instance_1 = DimensionalValueField.FromDict(
        TEST_DIMENSIONAL_VALUE_FIELD_DICT
    )
    test_dimensional_value_field_instance_2 = DimensionalValueField.FromDict(
        TEST_DIMENSIONAL_VALUE_FIELD_DICT
    )

    self.assertEqual(
        test_dimensional_value_field_instance_1,
        test_dimensional_value_field_instance_2,
    )

  def testToString(self):
    test_dimensional_value_field_instance = DimensionalValueField.FromDict(
        TEST_DIMENSIONAL_VALUE_FIELD_DICT
    )

    self.assertEqual(
        str(test_dimensional_value_field_instance),
        'test_virtual_guid: supply_water_temperature_sensor',
    )

  @mock.patch.object(GuidToEntityMap, 'GetEntityCodeByGuid')
  def testGetSpreadsheetRowMapping(self, test_get_code):
    test_get_code.side_effect = [
        TEST_VIRTUAL_ENTITY_CODE,
        TEST_REPORTING_ENTITY_CODE,
    ]
    test_dimensional_value_field_instance = DimensionalValueField.FromDict(
        TEST_DIMENSIONAL_VALUE_FIELD_DICT
    )
    expected_row_mapping = {
        STANDARD_FIELD_NAME: TEST_STANDARD_FIELD_NAME,
        RAW_FIELD_NAME: TEST_RAW_FIELD_NAME,
        REPORTING_ENTITY_FIELD_NAME: TEST_STANDARD_FIELD_NAME + '_1',
        ENTITY_CODE: TEST_VIRTUAL_ENTITY_CODE,
        BC_GUID: TEST_VIRTUAL_GUID,
        REPORTING_ENTITY_CODE: TEST_REPORTING_ENTITY_CODE,
        REPORTING_ENTITY_GUID: TEST_REPORTING_GUID,
        MISSING: 'FALSE',
        RAW_UNIT_PATH: 'points.filter_differential_pressure_setpoint.units',
        STANDARD_UNIT_VALUE: 'pascals',
        RAW_UNIT_VALUE: 'Pa',
    }

    actual_row_mapping = (
        test_dimensional_value_field_instance.GetSpreadsheetRowMapping()
    )

    self.assertEqual(expected_row_mapping, actual_row_mapping)


if __name__ == '__main__':
  absltest.main()
