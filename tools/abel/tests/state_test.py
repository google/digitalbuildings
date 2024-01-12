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
"""Tests for States class."""

from absl.testing import absltest

# pylint: disable=g-importing-member
from model.constants import RAW_STATE
from model.constants import REPORTING_ENTITY_FIELD_NAME
from model.constants import REPORTING_ENTITY_GUID
from model.constants import STANDARD_STATE
from model.state import State


_TEST_STATE_DICT = {
    REPORTING_ENTITY_GUID: 'test_guid',
    REPORTING_ENTITY_FIELD_NAME: 'discharge_fan_run_command',
    STANDARD_STATE: 'ON',
    RAW_STATE: 'TRUE',
}


class StatesTest(absltest.TestCase):

  def setUp(self):
    super().setUp()
    self.test_state = State.FromDict(_TEST_STATE_DICT)

  def testFromDict(self):
    self.assertEqual(
        self.test_state.reporting_entity_guid,
        _TEST_STATE_DICT[REPORTING_ENTITY_GUID],
    )
    self.assertEqual(
        self.test_state.std_field_name,
        _TEST_STATE_DICT[REPORTING_ENTITY_FIELD_NAME],
    )
    self.assertEqual(
        self.test_state.standard_state, _TEST_STATE_DICT[STANDARD_STATE]
    )
    self.assertEqual(self.test_state.raw_state, _TEST_STATE_DICT[RAW_STATE])

  def testStateRepr(self):
    expected_representation = (
        'TRUE: ON for test_guid: discharge_fan_run_command'
    )

    self.assertEqual(str(self.test_state), expected_representation)


if __name__ == '__main__':
  absltest.main()
