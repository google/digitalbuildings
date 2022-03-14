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
"""Test for configuration file scoring tool "entity identification" dimension (entity_identification.py)."""

from absl.testing import absltest

from score.constants import FileTypes
from score.dimensions.entity_identification import EntityIdentification

PROPOSED, SOLUTION = FileTypes


class EntityIdentificationTest(absltest.TestCase):

  def setUp(self):
    super().setUp()
    # TODO(b/210741084): add real data (append cases to existing tests)
    deserialized_files = {PROPOSED: {}, SOLUTION: {}}
    self.entity_identification = EntityIdentification(
        deserialized_files=deserialized_files)

  def testDirectlyAssignedAttributes(self):
    self.assertEqual(self.entity_identification.correct_reporting, 0)
    self.assertEqual(self.entity_identification.correct_ceiling_reporting, 0)
    self.assertEqual(self.entity_identification.incorrect_reporting, 0)

  def testInheritedCalculatedAttributes(self):
    self.assertEqual(self.entity_identification.correct_total(), 0)
    self.assertEqual(self.entity_identification.correct_ceiling(), 0)
    self.assertEqual(self.entity_identification.incorrect_total(), 0)

  def testInheritedResultProperties(self):
    # These are `None` by virtue of the ceiling being falsy.
    self.assertIsNone(self.entity_identification.result_composite)
    self.assertIsNone(self.entity_identification.result_reporting)
    self.assertIsNone(self.entity_identification.result_virtual)


if __name__ == '__main__':
  absltest.main()
