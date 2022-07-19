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
"""Test for configuration file scoring tool "state mapping" dimension (state_mapping.py)."""

from absl.testing import absltest

from score.constants import FileTypes
from score.dimensions.state_mapping import StateMapping

PROPOSED, SOLUTION = FileTypes


class StateMappingTest(absltest.TestCase):

  def setUp(self):
    super().setUp()
    # TODO(b/210741084): add real data (append cases to existing tests)
    translations = {PROPOSED: [], SOLUTION: []}
    self.state_mapping = StateMapping(translations=translations)

  def testDirectlyAssignedAttributes(self):
    self.assertEqual(self.state_mapping.correct_reporting, 0)
    self.assertEqual(self.state_mapping.correct_ceiling_reporting, 0)
    self.assertEqual(self.state_mapping.incorrect_reporting, 0)

  def testInheritedCalculatedAttributes(self):
    self.assertEqual(self.state_mapping.correct_total(), 0)
    self.assertEqual(self.state_mapping.correct_ceiling(), 0)
    self.assertEqual(self.state_mapping.incorrect_total(), 0)

  def testInheritedResultProperties(self):
    # These are `None` by virtue of the ceiling being falsy.
    self.assertIsNone(self.state_mapping.result_composite)
    self.assertIsNone(self.state_mapping.result_reporting)
    self.assertIsNone(self.state_mapping.result_virtual)


if __name__ == '__main__':
  absltest.main()
