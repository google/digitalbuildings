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

from model.states import States


class StatesTest(absltest.TestCase):

  def setUp(self):
    """Set up for StatesTest."""
    super().setUp()
    self.test_state_map = {
        'OPEN': ['1'],
    }
    self.multistate = States(self.test_state_map)

  def testAddState(self):
    self.multistate.AddState(standard_state='CLOSED', raw_states=['2', '3'])

    self.assertEqual(
        self.multistate.standard_to_raw_state_map['CLOSED'], ['2', '3'])

if __name__ == '__main__':
  absltest.main()
