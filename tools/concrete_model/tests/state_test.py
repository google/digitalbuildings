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

from google3.third_party.digitalbuildings.tools.concrete_model.model.constants import BC_GUID
from google3.third_party.digitalbuildings.tools.concrete_model.model.constants import RAW_STATE
from google3.third_party.digitalbuildings.tools.concrete_model.model.constants import STANDARD_FIELD_NAME
from google3.third_party.digitalbuildings.tools.concrete_model.model.constants import STANDARD_STATE
from google3.third_party.digitalbuildings.tools.concrete_model.model.state import State

_TEST_STATE_DICT = {
    BC_GUID: 'test_guid',
    STANDARD_FIELD_NAME: 'discharge_fan_run_command',
    STANDARD_STATE: 'ON',
    RAW_STATE: 'TRUE'
}


class StatesTest(absltest.TestCase):

  def testFromDict(self):
    test_state = State.FromDict(_TEST_STATE_DICT)

    self.assertEqual(test_state.entity_guid, _TEST_STATE_DICT[BC_GUID])
    self.assertEqual(test_state.standard_field_name,
                     _TEST_STATE_DICT[STANDARD_FIELD_NAME])
    self.assertEqual(test_state.standard_state,
                     _TEST_STATE_DICT[STANDARD_STATE])
    self.assertEqual(test_state.raw_state, _TEST_STATE_DICT[RAW_STATE])

if __name__ == '__main__':
  absltest.main()
