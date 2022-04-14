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
"entity connection identification" dimension."""

from absl.testing import absltest

from score.dimensions.entity_connection_identification import EntityConnectionIdentification
from score.constants import FileTypes, DimensionCategories

from tests.helper import TestHelper

PROPOSED, SOLUTION = FileTypes


class EntityConnectionIdentificationTest(absltest.TestCase):
  def setUp(self):
    super().setUp()
    featureful_file_path = (
        'tests/samples/proposed/entity_connection_identification.yaml')
    self.highest_score_argument = TestHelper.prepare_dimension_argument(
        dimension=EntityConnectionIdentification,
        proposed_path=featureful_file_path,
        solution_path=featureful_file_path)

    empty_file_path = 'tests/samples/empty.yaml'
    self.none_score_argument = TestHelper.prepare_dimension_argument(
        dimension=EntityConnectionIdentification,
        proposed_path=empty_file_path,
        solution_path=empty_file_path)

    no_contains_file_path = 'tests/samples/proposed/entity_connection_identification_no_contains.yaml'  # pylint: disable=line-too-long

    self.middling_score_argument = TestHelper.prepare_dimension_argument(
        dimension=EntityConnectionIdentification,
        proposed_path=no_contains_file_path,
        solution_path=featureful_file_path)

  def testCategoryAttribute_COMPLEX(self):
    self.assertEqual(EntityConnectionIdentification.category,
                     DimensionCategories.COMPLEX)

  def testEvaluate_ScoreNone(self):
    """When ceiling==0, the resulting score is None. The ceiling is 0
    because the solution does not contain any entities."""
    none_score_expected = EntityConnectionIdentification(
        deserialized_files=self.none_score_argument).evaluate()

    # Directly assigned attributes

    # Reporting and virtual entities are not evaluated separately,
    # thus these values are not overridden by the child class
    self.assertEqual(none_score_expected.correct_reporting, None)
    self.assertEqual(none_score_expected.correct_ceiling_reporting, None)
    self.assertEqual(none_score_expected.incorrect_reporting, None)

    self.assertEqual(none_score_expected.correct_virtual, None)
    self.assertEqual(none_score_expected.correct_ceiling_virtual, None)
    self.assertEqual(none_score_expected.incorrect_virtual, None)

    # These are set to allow for an "all" score to be calculated
    # in the absence of "reporting" and "virtual" components
    self.assertEqual(none_score_expected.correct_total_override, 0)
    self.assertEqual(none_score_expected.correct_ceiling_override, 0)
    self.assertEqual(none_score_expected.incorrect_total_override, 0)

    # Inherited calculated attributes
    self.assertEqual(none_score_expected.correct_total(), 0)
    self.assertEqual(none_score_expected.correct_ceiling(), 0)
    self.assertEqual(none_score_expected.incorrect_total(), 0)

    # Inherited result properties. These are `None` by virtue of the ceiling
    # being falsy: that is to say, there was nothing to score against.
    self.assertEqual(none_score_expected.result_all, None)
    self.assertEqual(none_score_expected.result_reporting, None)
    self.assertEqual(none_score_expected.result_virtual, None)

  def testEvaluate_ScoreHighestPossible(self):
    """When correct==ceiling, the resulting score is 1.0. All entities
    correspond because the proposal is the same as the solution."""
    highest_score_expected = EntityConnectionIdentification(
        deserialized_files=self.highest_score_argument).evaluate()

    # Directly assigned attributes

    # Reporting and virtual entities are not evaluated separately,
    # thus these values are not overridden by the child class
    self.assertEqual(highest_score_expected.correct_reporting, None)
    self.assertEqual(highest_score_expected.correct_ceiling_reporting, None)
    self.assertEqual(highest_score_expected.incorrect_reporting, None)

    self.assertEqual(highest_score_expected.correct_virtual, None)
    self.assertEqual(highest_score_expected.correct_ceiling_virtual, None)
    self.assertEqual(highest_score_expected.incorrect_virtual, None)

    # These are set to allow for an "all" score to be calculated
    # in the absence of "reporting" and "virtual" components
    self.assertEqual(highest_score_expected.correct_total_override, 6)
    self.assertEqual(highest_score_expected.correct_ceiling_override, 6)
    self.assertEqual(highest_score_expected.incorrect_total_override, 0)

    # Inherited calculated attributes
    self.assertEqual(highest_score_expected.correct_total(), 6)
    self.assertEqual(highest_score_expected.correct_ceiling(), 6)
    self.assertEqual(highest_score_expected.incorrect_total(), 0)

    # Inherited result properties
    self.assertEqual(highest_score_expected.result_all, 1.0)
    self.assertEqual(highest_score_expected.result_reporting, None)
    self.assertEqual(highest_score_expected.result_virtual, None)

  def testEvaluate_ScoreLowestPossible(self):
    """When correct==0, the resulting score is -1.0. No entities
    correspond because the proposal does not contain any entities."""
    lowest_score_argument = {
        PROPOSED:
        self.none_score_argument[PROPOSED],  # Empty, i.e. nothing correct
        SOLUTION: self.highest_score_argument[SOLUTION]
    }
    lowest_score_expected = EntityConnectionIdentification(
        deserialized_files=lowest_score_argument).evaluate()

    # Directly assigned attributes

    # Reporting and virtual entities are not evaluated separately,
    # thus these values are not overridden by the child class
    self.assertEqual(lowest_score_expected.correct_reporting, None)
    self.assertEqual(lowest_score_expected.correct_ceiling_reporting, None)
    self.assertEqual(lowest_score_expected.incorrect_reporting, None)

    self.assertEqual(lowest_score_expected.correct_virtual, None)
    self.assertEqual(lowest_score_expected.correct_ceiling_virtual, None)
    self.assertEqual(lowest_score_expected.incorrect_virtual, None)

    # These are set to allow for an "all" score to be calculated
    # in the absence of "reporting" and "virtual" components
    self.assertEqual(lowest_score_expected.correct_total_override, 0)
    self.assertEqual(lowest_score_expected.correct_ceiling_override, 6)
    self.assertEqual(lowest_score_expected.incorrect_total_override, 6)

    # Inherited calculated attributes
    self.assertEqual(lowest_score_expected.correct_total(), 0)
    self.assertEqual(lowest_score_expected.correct_ceiling(), 6)
    self.assertEqual(lowest_score_expected.incorrect_total(), 6)

    # Inherited result properties
    self.assertEqual(lowest_score_expected.result_all, -1.0)
    self.assertEqual(lowest_score_expected.result_reporting, None)
    self.assertEqual(lowest_score_expected.result_virtual, None)

  def testEvaluate_ScoreMiddling(self):
    """When correct is half of the ceiling, the resulting score is 0.0. In this
    case, reporting entities scored 1.0 and virtual entities scored -1.0; the
    result for all entities is 0.0."""
    middling_score_expected = EntityConnectionIdentification(
        deserialized_files=self.middling_score_argument).evaluate()

    # Directly assigned attributes

    # Reporting and virtual entities are not evaluated separately,
    # thus these values are not overridden by the child class
    self.assertEqual(middling_score_expected.correct_reporting, None)
    self.assertEqual(middling_score_expected.correct_ceiling_reporting, None)
    self.assertEqual(middling_score_expected.incorrect_reporting, None)

    self.assertEqual(middling_score_expected.correct_virtual, None)
    self.assertEqual(middling_score_expected.correct_ceiling_virtual, None)
    self.assertEqual(middling_score_expected.incorrect_virtual, None)

    # These are set to allow for an "all" score to be calculated
    # in the absence of "reporting" and "virtual" components
    self.assertEqual(middling_score_expected.correct_total_override, 3)
    self.assertEqual(middling_score_expected.correct_ceiling_override, 6)
    self.assertEqual(middling_score_expected.incorrect_total_override, 3)

    # Inherited calculated attributes
    self.assertEqual(middling_score_expected.correct_total(), 3)
    self.assertEqual(middling_score_expected.correct_ceiling(), 6)
    self.assertEqual(middling_score_expected.incorrect_total(), 3)

    # Inherited result properties
    self.assertEqual(middling_score_expected.result_all, 0.0)
    self.assertEqual(middling_score_expected.result_reporting, None)
    self.assertEqual(middling_score_expected.result_virtual, None)


if __name__ == '__main__':
  absltest.main()
