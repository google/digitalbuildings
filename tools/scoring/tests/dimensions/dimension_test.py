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
core functionality unit base class (dimension.py)."""

from absl.testing import absltest

from score.dimensions.dimension import Dimension


class DimensionTest(absltest.TestCase):
  def setUp(self):
    super().setUp()
    self.dimension = Dimension(translations='translations')
    self.dimension.correct_virtual = 1
    self.dimension.correct_reporting = 1
    self.dimension.correct_ceiling_virtual = 2
    self.dimension.correct_ceiling_reporting = 2
    self.dimension.incorrect_virtual = 1
    self.dimension.incorrect_reporting = 1

    self.dimension_none = Dimension(deserialized_files='deserialized files')
    self.dimension_none.correct_virtual = 0
    self.dimension_none.correct_reporting = 0
    self.dimension_none.correct_ceiling_virtual = 0
    self.dimension_none.correct_ceiling_reporting = 0
    self.dimension_none.incorrect_virtual = 0
    self.dimension_none.incorrect_reporting = 0

  def testArgumentAttributes(self):
    self.assertEqual(self.dimension.translations, 'translations')
    self.assertEqual(self.dimension.deserialized_files, None)

    self.assertEqual(self.dimension_none.translations, None)
    self.assertEqual(self.dimension_none.deserialized_files,
                     'deserialized files')

  def testArgumentExclusivity(self):
    with self.assertRaises(Exception) as not_enough:
      Dimension()
    self.assertEqual(
        not_enough.exception.args[0],
        '`translations` xor `deserialized_files` argument is required')

    with self.assertRaises(Exception) as too_many:
      Dimension(translations='translations',
                deserialized_files='deserialized files')
    self.assertEqual(
        too_many.exception.args[0],
        '`translations` or `deserialized_files` argument must be exclusive')

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
