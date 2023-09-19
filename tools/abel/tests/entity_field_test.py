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
"""Tests for entity_field.py."""

from unittest import mock

from absl.testing import absltest

# pylint: disable=g-importing-member
from model.constants import CONDITION
from model.constants import CONDITION_TYPE
from model.constants import DATA_VALIDATION
from model.constants import MISSING_FALSE
from model.constants import MISSING_TRUE
from model.constants import ONE_OF_LIST
from model.constants import SHOW_CUSTOM_UI
from model.constants import STRICT_VALIDATION
from model.constants import STRING_VALUE
from model.constants import USER_ENTERED_VALUE
from model.constants import VALUES
from model.entity_field import DimensionalValueField
from model.entity_field import MissingField
from model.entity_field import MultistateValueField
from model.guid_to_entity_map import GuidToEntityMap
from model.state import State
from model.units import Units
from tests.test_constants import TEST_DIMENSIONAL_REPORTING_FIELD_NAME
from tests.test_constants import TEST_DIMENSIONAL_VALUE_FIELD_DICT
from tests.test_constants import TEST_DIMENSIONAL_VALUE_RAW_FIELD_NAME
from tests.test_constants import TEST_DIMENSIONAL_VALUE_STANDARD_FIELD_NAME
from tests.test_constants import TEST_FIELD_DICT_NO_UNITS
from tests.test_constants import TEST_MISSING_FIELD_DICT
from tests.test_constants import TEST_MISSING_STANDARD_FIELD_NAME
from tests.test_constants import TEST_MULTISTATE_RAW_FIELD_NAME
from tests.test_constants import TEST_MULTISTATE_REPORTING_FIELD_NAME
from tests.test_constants import TEST_MULTISTATE_STANDARD_FIELD_NAME
from tests.test_constants import TEST_MULTISTATE_VALUE_FIELD_DICT
from tests.test_constants import TEST_RAW_FIELD_NAME_NO_UNITS
from tests.test_constants import TEST_REPORTING_ENTITY_CODE
from tests.test_constants import TEST_REPORTING_GUID
from tests.test_constants import TEST_STANDARD_FIELD_NAME_NO_UNITS
from tests.test_constants import TEST_STATE_DICT
from tests.test_constants import TEST_UNITS
from tests.test_constants import TEST_VIRTUAL_ENTITY_CODE
from tests.test_constants import TEST_VIRTUAL_GUID
from validate import field_translation


class MissingFieldTest(absltest.TestCase):

  def testMissingFieldBuildsFromDict(self):
    test_missing_field = MissingField.FromDict(TEST_MISSING_FIELD_DICT)

    self.assertEqual(
        test_missing_field.std_field_name, TEST_MISSING_STANDARD_FIELD_NAME
    )
    self.assertEqual(
        test_missing_field.mode, field_translation.PresenceMode.MISSING
    )
    self.assertEqual(
        test_missing_field.reporting_entity_field_name,
        TEST_MISSING_STANDARD_FIELD_NAME,
    )
    self.assertEqual(
        test_missing_field.reporting_entity_guid, TEST_REPORTING_GUID
    )
    self.assertEqual(test_missing_field.entity_guid, TEST_REPORTING_GUID)

  def testMissingFieldEquality(self):
    test_missing_field_1 = MissingField.FromDict(TEST_MISSING_FIELD_DICT)
    test_missing_field_2 = MissingField.FromDict(TEST_MISSING_FIELD_DICT)

    self.assertEqual(test_missing_field_1, test_missing_field_2)

  def testMissingFieldInequality(self):
    test_missing_field_1 = MissingField.FromDict(TEST_MISSING_FIELD_DICT)
    test_missing_field_2 = MissingField.FromDict(TEST_MISSING_FIELD_DICT)
    test_missing_field_2.std_field_name = 'bad_name'

    self.assertNotEqual(test_missing_field_1, test_missing_field_2)

  def testMissingFieldEqualityRaisesTypeError(self):
    test_missing_field = MissingField.FromDict(TEST_MISSING_FIELD_DICT)

    # pylint: disable=unnecessary-dunder-call
    with self.assertRaises(TypeError):
      test_missing_field.__eq__('not a field')

  @mock.patch.object(GuidToEntityMap, 'GetEntityCodeByGuid')
  def testMissingFieldGetSpreadsheetRowMapping(self, test_get_code):
    test_get_code.return_value = TEST_REPORTING_ENTITY_CODE
    test_missing_field = MissingField.FromDict(TEST_MISSING_FIELD_DICT)
    test_guid_to_entity_map = GuidToEntityMap()
    expected_row_mapping = {
        VALUES: [
            {
                USER_ENTERED_VALUE: {
                    STRING_VALUE: TEST_MISSING_STANDARD_FIELD_NAME
                }
            },
            {USER_ENTERED_VALUE: {STRING_VALUE: ''}},
            {USER_ENTERED_VALUE: {STRING_VALUE: TEST_REPORTING_ENTITY_CODE}},
            {USER_ENTERED_VALUE: {STRING_VALUE: TEST_REPORTING_GUID}},
            {USER_ENTERED_VALUE: {STRING_VALUE: TEST_REPORTING_ENTITY_CODE}},
            {USER_ENTERED_VALUE: {STRING_VALUE: TEST_REPORTING_GUID}},
            {
                USER_ENTERED_VALUE: {STRING_VALUE: MISSING_TRUE},
                DATA_VALIDATION: {
                    CONDITION: {
                        CONDITION_TYPE: ONE_OF_LIST,
                        VALUES: [
                            {USER_ENTERED_VALUE: MISSING_TRUE},
                            {USER_ENTERED_VALUE: MISSING_FALSE},
                        ],
                    },
                    STRICT_VALIDATION: True,
                    SHOW_CUSTOM_UI: True,
                },
            },
        ]
    }

    actual_row_mapping = test_missing_field.GetSpreadsheetRowMapping(
        guid_to_entity_map=test_guid_to_entity_map
    )

    self.assertEqual(expected_row_mapping, actual_row_mapping)


class MultistateValueFieldTest(absltest.TestCase):

  def testMultistateValueFieldBuildsFromDict(self):
    test_multi_state_value_field_instance = MultistateValueField.FromDict(
        TEST_MULTISTATE_VALUE_FIELD_DICT
    )

    self.assertEqual(
        test_multi_state_value_field_instance.std_field_name,
        TEST_MULTISTATE_STANDARD_FIELD_NAME,
    )
    self.assertEqual(
        test_multi_state_value_field_instance.raw_field_name,
        TEST_MULTISTATE_RAW_FIELD_NAME,
    )

  def testAddState(self):
    test_multi_state_value_field_instance = MultistateValueField.FromDict(
        TEST_MULTISTATE_VALUE_FIELD_DICT
    )
    test_state = State.FromDict(TEST_STATE_DICT)

    test_multi_state_value_field_instance.AddState(test_state)

    self.assertEqual(
        test_multi_state_value_field_instance.states.pop(), test_state
    )

  def testAddStateRaisesTypeError(self):
    test_multi_state_value_field_instance = MultistateValueField.FromDict(
        TEST_MULTISTATE_VALUE_FIELD_DICT
    )

    with self.assertRaises(TypeError):
      test_multi_state_value_field_instance.AddState('state_string')

  def testTwoMultistateValueFieldAreEqual(self):
    multi_state_value_field_instance = MultistateValueField.FromDict(
        TEST_MULTISTATE_VALUE_FIELD_DICT
    )
    multi_state_value_field_instance_2 = MultistateValueField.FromDict(
        TEST_MULTISTATE_VALUE_FIELD_DICT
    )

    self.assertEqual(
        multi_state_value_field_instance, multi_state_value_field_instance_2
    )

  def testTwoMultistateValueFieldAreNotEqual(self):
    multi_state_value_field_instance = MultistateValueField.FromDict(
        TEST_MULTISTATE_VALUE_FIELD_DICT
    )
    multi_state_value_field_instance_2 = MultistateValueField.FromDict(
        TEST_MULTISTATE_VALUE_FIELD_DICT
    )
    multi_state_value_field_instance_2.std_field_name = 'bad_name'

    self.assertNotEqual(
        multi_state_value_field_instance, multi_state_value_field_instance_2
    )

  @mock.patch.object(GuidToEntityMap, 'GetEntityCodeByGuid')
  def testMultistateValueFieldGetSpreadsheetRowMapping(self, test_get_code):
    test_get_code.return_value = TEST_REPORTING_ENTITY_CODE
    multi_state_value_field_instance = MultistateValueField.FromDict(
        TEST_MULTISTATE_VALUE_FIELD_DICT
    )
    test_guid_to_entity_map = GuidToEntityMap()
    expected_row_mapping = {
        VALUES: [
            {
                USER_ENTERED_VALUE: {
                    STRING_VALUE: TEST_MULTISTATE_STANDARD_FIELD_NAME
                }
            },
            {
                USER_ENTERED_VALUE: {
                    STRING_VALUE: TEST_MULTISTATE_RAW_FIELD_NAME
                }
            },
            {
                USER_ENTERED_VALUE: {
                    STRING_VALUE: TEST_MULTISTATE_REPORTING_FIELD_NAME
                }
            },
            {USER_ENTERED_VALUE: {STRING_VALUE: TEST_REPORTING_ENTITY_CODE}},
            {USER_ENTERED_VALUE: {STRING_VALUE: TEST_REPORTING_GUID}},
            {USER_ENTERED_VALUE: {STRING_VALUE: TEST_REPORTING_ENTITY_CODE}},
            {USER_ENTERED_VALUE: {STRING_VALUE: TEST_REPORTING_GUID}},
            {
                USER_ENTERED_VALUE: {STRING_VALUE: MISSING_FALSE},
                DATA_VALIDATION: {
                    CONDITION: {
                        CONDITION_TYPE: ONE_OF_LIST,
                        VALUES: [
                            {USER_ENTERED_VALUE: MISSING_TRUE},
                            {USER_ENTERED_VALUE: MISSING_FALSE},
                        ],
                    },
                    STRICT_VALIDATION: True,
                    SHOW_CUSTOM_UI: True,
                },
            },
        ]
    }

    actual_row_mapping = (
        multi_state_value_field_instance.GetSpreadsheetRowMapping(
            guid_to_entity_map=test_guid_to_entity_map
        )
    )

    self.assertEqual(expected_row_mapping, actual_row_mapping)

  def testToString(self):
    multi_state_value_field_instance = MultistateValueField.FromDict(
        TEST_MULTISTATE_VALUE_FIELD_DICT
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
        TEST_DIMENSIONAL_VALUE_STANDARD_FIELD_NAME,
    )
    self.assertEqual(
        test_dimensional_value_field_instance.raw_field_name,
        TEST_DIMENSIONAL_VALUE_RAW_FIELD_NAME,
    )
    self.assertIsInstance(test_dimensional_value_field_instance.units, Units)

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
    test_guid_to_entity_map = GuidToEntityMap()
    expected_row_mapping = {
        VALUES: [
            {
                USER_ENTERED_VALUE: {
                    STRING_VALUE: TEST_DIMENSIONAL_VALUE_STANDARD_FIELD_NAME
                }
            },
            {
                USER_ENTERED_VALUE: {
                    STRING_VALUE: TEST_DIMENSIONAL_VALUE_RAW_FIELD_NAME
                }
            },
            {
                USER_ENTERED_VALUE: {
                    STRING_VALUE: TEST_DIMENSIONAL_REPORTING_FIELD_NAME
                }
            },
            {USER_ENTERED_VALUE: {STRING_VALUE: TEST_VIRTUAL_ENTITY_CODE}},
            {USER_ENTERED_VALUE: {STRING_VALUE: TEST_VIRTUAL_GUID}},
            {USER_ENTERED_VALUE: {STRING_VALUE: TEST_REPORTING_ENTITY_CODE}},
            {USER_ENTERED_VALUE: {STRING_VALUE: TEST_REPORTING_GUID}},
            {
                USER_ENTERED_VALUE: {STRING_VALUE: MISSING_FALSE},
                DATA_VALIDATION: {
                    CONDITION: {
                        CONDITION_TYPE: ONE_OF_LIST,
                        VALUES: [
                            {USER_ENTERED_VALUE: MISSING_TRUE},
                            {USER_ENTERED_VALUE: MISSING_FALSE},
                        ],
                    },
                    STRICT_VALIDATION: True,
                    SHOW_CUSTOM_UI: True,
                },
            },
            {
                USER_ENTERED_VALUE: {
                    STRING_VALUE: (
                        'points.filter_differential_pressure_setpoint.units'
                    )
                }
            },
            {USER_ENTERED_VALUE: {STRING_VALUE: 'pascals'}},
            {USER_ENTERED_VALUE: {STRING_VALUE: 'Pa'}},
        ]
    }

    actual_row_mapping = (
        test_dimensional_value_field_instance.GetSpreadsheetRowMapping(
            guid_to_entity_map=test_guid_to_entity_map
        )
    )

    self.assertEqual(expected_row_mapping, actual_row_mapping)


class NoUnitsFieldTest(absltest.TestCase):

  def testNoUnitsFieldBuildsFromDict(self):
    no_units_field_instance = DimensionalValueField.FromDict(
        TEST_FIELD_DICT_NO_UNITS
    )
    expected_no_units_mapping = {'no-units': 'no-units'}

    self.assertEqual(
        no_units_field_instance.std_field_name,
        TEST_STANDARD_FIELD_NAME_NO_UNITS,
    )
    self.assertEqual(
        no_units_field_instance.raw_field_name, TEST_RAW_FIELD_NAME_NO_UNITS
    )
    self.assertEqual(
        no_units_field_instance.std_field_name,
        TEST_STANDARD_FIELD_NAME_NO_UNITS,
    )
    self.assertIsNotNone(no_units_field_instance.units)
    self.assertEqual(
        no_units_field_instance.units.standard_to_raw_unit_map,
        expected_no_units_mapping,
    )


if __name__ == '__main__':
  absltest.main()
