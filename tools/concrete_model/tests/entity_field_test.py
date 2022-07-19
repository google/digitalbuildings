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

from model.entity_field import EntityField
from model.state import State
from model.units import Units
from concrete_model.tests.test_constants import TEST_ENTITY_FIELD_DICT_WITH_NO_UNITS
from concrete_model.tests.test_constants import TEST_ENTITY_FIELD_DICT_WITH_UNITS
from concrete_model.tests.test_constants import TEST_RAW_FIELD_NAME
from concrete_model.tests.test_constants import TEST_STANDARD_FIELD_NAME
from concrete_model.tests.test_constants import TEST_STATE_DICT
from concrete_model.tests.test_constants import TEST_UNITS


class EntityFieldTest(absltest.TestCase):

  def testEntityFieldBuildsFromDict(self):
    test_entity_field_instance = EntityField.FromDict(
        TEST_ENTITY_FIELD_DICT_WITH_UNITS)

    self.assertEqual(test_entity_field_instance.standard_field_name,
                     TEST_STANDARD_FIELD_NAME)
    self.assertEqual(test_entity_field_instance.raw_field_name,
                     TEST_RAW_FIELD_NAME)
    self.assertIsInstance(test_entity_field_instance.units, Units)
    self.assertEqual(test_entity_field_instance.metadata,
                     {'test': 'test metadata'})

  def testAddState(self):
    test_entity_field_instance = EntityField.FromDict(
        TEST_ENTITY_FIELD_DICT_WITH_NO_UNITS)
    test_state = State.FromDict(TEST_STATE_DICT)

    test_entity_field_instance.states = [test_state]

    self.assertEqual(test_entity_field_instance.states.pop(), test_state)

  def testAddStateRaisesTypeError(self):
    test_entity_field_instance = EntityField.FromDict(
        TEST_ENTITY_FIELD_DICT_WITH_NO_UNITS)

    with self.assertRaises(TypeError):
      test_entity_field_instance.AddState('state_string')

  def testAddUnits(self):
    test_entity_field_instance = EntityField.FromDict(
        TEST_ENTITY_FIELD_DICT_WITH_NO_UNITS)

    test_entity_field_instance.units = TEST_UNITS

    self.assertEqual(test_entity_field_instance.units, TEST_UNITS)

  def testEntityFieldWithStatesRaisesAttributeError(self):
    test_entity_field_instance = EntityField.FromDict(
        TEST_ENTITY_FIELD_DICT_WITH_NO_UNITS)
    test_state = State.FromDict(TEST_STATE_DICT)

    test_entity_field_instance.states = [test_state]

    with self.assertRaises(AttributeError):
      test_entity_field_instance.units = TEST_UNITS

  def testEntityFieldWithUnitsRaisesAttributeError(self):
    test_entity_field_instance = EntityField.FromDict(
        TEST_ENTITY_FIELD_DICT_WITH_UNITS)
    test_state = State.FromDict(TEST_STATE_DICT)

    with self.assertRaises(AttributeError):
      test_entity_field_instance.states = [test_state]


if __name__ == '__main__':
  absltest.main()
