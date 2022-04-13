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
"state mapping" dimension."""

from absl.testing import absltest

from score.dimensions.state_mapping import StateMapping
from score.constants import FileTypes, DimensionCategories

from tests.helper import TestHelper

PROPOSED, SOLUTION = FileTypes


class StateMappingTest(absltest.TestCase):
  def setUp(self):
    super().setUp()
    one_entity_file_path = (
        'tests/samples/proposed/state_mapping_one_entity.yaml')
    self.highest_score_argument = TestHelper.prepare_dimension_argument(
        dimension=StateMapping,
        proposed_path=one_entity_file_path,
        solution_path=one_entity_file_path)

    empty_file_path = 'tests/samples/empty.yaml'
    self.none_score_argument = TestHelper.prepare_dimension_argument(
        dimension=StateMapping,
        proposed_path=empty_file_path,
        solution_path=empty_file_path)

    self.lowest_score_argument = TestHelper.prepare_dimension_argument(
        dimension=StateMapping,
        proposed_path=empty_file_path,
        solution_path=one_entity_file_path)

    two_entities_file_path = (
        'tests/samples/proposed/state_mapping_two_entities.yaml')
    self.middling_score_argument = TestHelper.prepare_dimension_argument(
        dimension=StateMapping,
        proposed_path=one_entity_file_path,
        solution_path=two_entities_file_path)

  def testCategoryAttribute_SIMPLE(self):
    self.assertEqual(StateMapping.category, DimensionCategories.SIMPLE)

  def testEvaluate_ScoreNone(self):
    """When ceiling==0, the resulting score is None. The ceiling is 0
    because the solution does not contain any entities."""
    none_score_expected = StateMapping(
        translations=self.none_score_argument).evaluate()

    # Directly assigned attributes
    self.assertEqual(none_score_expected.correct_reporting, 0)
    self.assertEqual(none_score_expected.correct_ceiling_reporting, 0)
    self.assertEqual(none_score_expected.incorrect_reporting, 0)

    # Inherited calculated attributes
    self.assertEqual(none_score_expected.correct_total(), 0)
    self.assertEqual(none_score_expected.correct_ceiling(), 0)
    self.assertEqual(none_score_expected.incorrect_total(), 0)

    # Inherited result properties. These are `None` by virtue of the ceiling
    # being falsy: that is to say, there was nothing to score against.
    self.assertEqual(none_score_expected.result_all, None)
    self.assertEqual(none_score_expected.result_reporting, None)
    # "Simple" dimensions don't operate on virtual entities
    self.assertEqual(none_score_expected.result_virtual, None)

  def testEvaluate_ScoreHighestPossible(self):
    """When correct==ceiling, the resulting score is 1.0. All entities
    correspond because the proposal is the same as the solution."""
    highest_score_expected = StateMapping(
        translations=self.highest_score_argument).evaluate()

    # Directly assigned attributes
    self.assertEqual(highest_score_expected.correct_reporting, 2)
    self.assertEqual(highest_score_expected.correct_ceiling_reporting, 2)
    self.assertEqual(highest_score_expected.incorrect_reporting, 0)

    # Inherited calculated attributes
    self.assertEqual(highest_score_expected.correct_total(), 2)
    self.assertEqual(highest_score_expected.correct_ceiling(), 2)
    self.assertEqual(highest_score_expected.incorrect_total(), 0)

    # Inherited result properties
    self.assertEqual(highest_score_expected.result_all, 1.0)
    self.assertEqual(highest_score_expected.result_reporting, 1.0)
    # "Simple" dimensions don't operate on virtual entities
    self.assertEqual(highest_score_expected.result_virtual, None)

  def testEvaluate_ScoreLowestPossible(self):
    """When correct==0, the resulting score is -1.0. No entities
    correspond because the proposal does not contain any entities."""
    lowest_score_expected = StateMapping(
        translations=self.lowest_score_argument).evaluate()

    # Directly assigned attributes
    self.assertEqual(lowest_score_expected.correct_reporting, 0)
    self.assertEqual(lowest_score_expected.correct_ceiling_reporting, 2)
    self.assertEqual(lowest_score_expected.incorrect_reporting, 2)

    # Inherited calculated attributes
    self.assertEqual(lowest_score_expected.correct_total(), 0)
    self.assertEqual(lowest_score_expected.correct_ceiling(), 2)
    self.assertEqual(lowest_score_expected.incorrect_total(), 2)

    # Inherited result properties
    self.assertEqual(lowest_score_expected.result_all, -1.0)
    self.assertEqual(lowest_score_expected.result_reporting, -1.0)
    # "Simple" dimensions don't operate on virtual entities
    self.assertEqual(lowest_score_expected.result_virtual, None)

  def testEvaluate_ScoreMiddling(self):
    """When correct is half of the ceiling, the resulting score is 0.0."""
    middling_score_expected = StateMapping(
        translations=self.middling_score_argument).evaluate()

    # Directly assigned attributes
    self.assertEqual(middling_score_expected.correct_reporting, 2)
    self.assertEqual(middling_score_expected.correct_ceiling_reporting, 4)
    self.assertEqual(middling_score_expected.incorrect_reporting, 2)

    # Inherited calculated attributes
    self.assertEqual(middling_score_expected.correct_total(), 2)
    self.assertEqual(middling_score_expected.correct_ceiling(), 4)
    self.assertEqual(middling_score_expected.incorrect_total(), 2)

    # Inherited result properties
    self.assertEqual(middling_score_expected.result_all, 0.0)
    self.assertEqual(middling_score_expected.result_reporting, 0.0)
    # "Simple" dimensions don't operate on virtual entities
    self.assertEqual(middling_score_expected.result_virtual, None)


if __name__ == '__main__':
  absltest.main()
