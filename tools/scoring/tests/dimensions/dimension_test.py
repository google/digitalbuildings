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
core functionality parent class (dimension.py)."""

from absl.testing import absltest

from score.dimensions.dimension import Dimension
from astroid import MANAGER

MANAGER.astroid_cache.clear()


class DimensionTest(absltest.TestCase):
  def setUp(self):
    super().setUp()
    # TODO: set these attributes separately from instantiation
    # as the signature requirements evolve w/ further implementation
    self.dimension = Dimension(1, 1, 2, 2, 1, 1)

    self.dimension_none = Dimension(0, 0, 0, 0, 0, 0)

  def testCorrect(self):
    self.assertEqual(self.dimension.correct(), 2)

  def testCorrectCeiling(self):
    self.assertEqual(self.dimension.correct_ceiling(), 4)

  def testIncorrect(self):
    self.assertEqual(self.dimension.incorrect(), 2)

  def testResultComposite(self):
    self.assertEqual(self.dimension.result_composite, 0.0)
    self.assertEqual(self.dimension_none.result_composite, None)

  def testResultVirtual(self):
    self.assertEqual(self.dimension.result_virtual, 0.0)
    self.assertEqual(self.dimension_none.result_virtual, None)

  def testResultReporting(self):
    self.assertEqual(self.dimension.result_reporting, 0.0)
    self.assertEqual(self.dimension_none.result_reporting, None)

  def testStr(self):
    self.assertEqual(
        self.dimension.__str__(),
        '{result_composite: 0.0, result_virtual: 0.0, result_reporting: 0.0}')


if __name__ == '__main__':
  absltest.main()
