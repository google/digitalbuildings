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
"""Test for configuration file scoring tool outputs (result.py)."""

from absl.testing import absltest

from score.dimensions.result import Result


class ResultTest(absltest.TestCase):
  def setUp(self):
    super().setUp()
    self.result = Result(correct_virtual=1,
                         correct_reporting=1,
                         correct_ceiling_virtual=2,
                         correct_ceiling_reporting=2,
                         incorrect_virtual=1,
                         incorrect_reporting=1)
    self.result_none = Result(correct_virtual=0,
                              correct_reporting=0,
                              correct_ceiling_virtual=0,
                              correct_ceiling_reporting=0,
                              incorrect_virtual=0,
                              incorrect_reporting=0)

  def testCorrect(self):
    self.assertEqual(classmethod(self.result.correct()), 2)

  def testCorrectCeiling(self):
    self.assertEqual(classmethod(self.result.correct_ceiling()), 4)

  def testIncorrect(self):
    self.assertEqual(classmethod(self.result.incorrect()), 2)

  def testResultComposite(self):
    self.assertEqual(self.result.result_composite, 0.0)
    self.assertEqual(self.result_none.result_composite, None)

  def testResultVirtual(self):
    self.assertEqual(self.result.result_virtual, 0.0)
    self.assertEqual(self.result_none.result_virtual, None)

  def testResultReporting(self):
    self.assertEqual(self.result.result_reporting, 0.0)
    self.assertEqual(self.result_none.result_reporting, None)


if __name__ == '__main__':
  absltest.main()
