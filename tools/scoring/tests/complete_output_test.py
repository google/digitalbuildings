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
"""Test to detect regressions to the tool's output."""

from absl.testing import absltest

from score import parse_config


class CompleteOutputTest(absltest.TestCase):
  def setUp(self):
    super().setUp()
    ontolgy = '../../ontology/yaml/resources'
    proposed = 'tests/samples/proposed/real_world_proposed.yaml'
    solution = 'tests/samples/solution/real_world_solution.yaml'
    # This circumvents the CLI but it is much more
    # straightforward than invoking via a subprocess
    scorer = parse_config.ParseConfig(ontology=ontolgy,
                                      proposed=proposed,
                                      solution=solution)
    self.output = scorer.execute()

  def testEntityConnectionIdentification(self):
    score = self.output['EntityConnectionIdentification']
    self.assertEqual(
        score,
        '{result_all: -1.00, result_virtual: None, result_reporting: None}')

  def testEntityIdentification(self):
    score = self.output['EntityIdentification']
    self.assertEqual(
        score,
        '{result_all: 0.83, result_virtual: -0.03, result_reporting: 0.99}')

  def testEntityPointIdentification(self):
    # NOTE: this score is known to vary slightly due to the way the matching
    # algorithm works. If the test fails here, try running it again…
    score = self.output['EntityPointIdentification']
    self.assertEqual(
        score,
        '{result_all: 0.82, result_virtual: -0.65, result_reporting: 0.98}')

  def testEntityTypeIdentification(self):
    score = self.output['EntityTypeIdentification']
    # NOTE: this score is known to vary slightly due to the way the matching
    # algorithm works. If the test fails here, try running it again…
    self.assertEqual(
        score,
        '{result_all: -0.70, result_virtual: -0.95, result_reporting: -0.64}')

  def testRawFieldSelection(self):
    score = self.output['RawFieldSelection']
    self.assertEqual(
        score,
        '{result_all: 0.71, result_virtual: None, result_reporting: 0.71}')

  def testStandardFieldNaming(self):
    score = self.output['StandardFieldNaming']
    self.assertEqual(
        score,
        '{result_all: 0.83, result_virtual: None, result_reporting: 0.83}')

  def testStateMapping(self):
    score = self.output['StateMapping']
    self.assertEqual(
        score,
        '{result_all: 0.00, result_virtual: None, result_reporting: 0.00}')

  def testUnitMapping(self):
    score = self.output['UnitMapping']
    self.assertEqual(
        score,
        '{result_all: 0.38, result_virtual: None, result_reporting: 0.38}')


if __name__ == '__main__':
  absltest.main()
