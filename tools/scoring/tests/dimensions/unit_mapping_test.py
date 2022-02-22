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
"""Test for configuration file scoring tool
"unit mapping" dimension (unit_mapping.py)."""

from absl.testing import absltest

from score.dimensions.unit_mapping import UnitMapping
from score.constants import FileTypes

PROPOSED, SOLUTION = FileTypes


class UnitMappingTest(absltest.TestCase):
  def setUp(self):
    super().setUp()
    # TODO: add real data (append cases to existing tests)
    translations = {PROPOSED: [], SOLUTION: []}
    self.unit_mapping = UnitMapping(translations=translations)

  def testDirectlyAssignedAttributes(self):
    self.assertEqual(self.unit_mapping.correct_reporting, 0)
    self.assertEqual(self.unit_mapping.correct_ceiling_reporting, 0)
    self.assertEqual(self.unit_mapping.incorrect_reporting, 0)

  def testInheritedCalculatedAttributes(self):
    self.assertEqual(self.unit_mapping.correct_total(), 0)
    self.assertEqual(self.unit_mapping.correct_ceiling(), 0)
    self.assertEqual(self.unit_mapping.incorrect_total(), 0)

  def testInheritedResultProperties(self):
    # These are `None` by virtue of the ceiling being falsy.
    self.assertEqual(self.unit_mapping.result_composite, None)
    self.assertEqual(self.unit_mapping.result_reporting, None)
    self.assertEqual(self.unit_mapping.result_virtual, None)


if __name__ == '__main__':
  absltest.main()
