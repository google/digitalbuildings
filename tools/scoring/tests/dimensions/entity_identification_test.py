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
"entity identification" dimension (entity_identification.py)."""

from absl.testing import absltest

from score.dimensions.entity_identification import EntityIdentification
from score.constants import FileTypes, DimensionCategories
from score.parse_config import ParseConfig

from validate import handler as validator
from validate.generate_universe import BuildUniverse

PROPOSED, SOLUTION = FileTypes
SIMPLE, COMPLEX = DimensionCategories


class EntityIdentificationTest(absltest.TestCase):
  def _prepare_dimension_argument(self, *, entity_type, proposed_path,
                                  solution_path):
    """Prepare argument for direct invocation of a dimension for purposes of
    testing (i.e. mimic parse_config.py).

    NOTE: this uses the simplified universe. If the test data references types
    which are not contained therein, results will differ from those which use
    the full universe because entities with missing types are skipped!

      Arguments:
        entity_type: the category of the dimension. (Literal[SIMPLE, COMPLEX])
        proposed_path: the path to the proposed YAML file
        solution_path: the path to the solution YAML file

      Returns:
        The appropriate value for the dimension's singular named argument"""

    universe = BuildUniverse(use_simplified_universe=True)
    proposed_config = validator.Deserialize([proposed_path])[0]
    solution_config = validator.Deserialize([solution_path])[0]
    deserialized_files = {PROPOSED: proposed_config, SOLUTION: solution_config}

    deserialized_files_appended = ParseConfig.append_types(
        universe=universe, deserialized_files=deserialized_files)

    if entity_type == SIMPLE:
      matches = ParseConfig.match_reporting_entities(
          proposed_entities=deserialized_files_appended[PROPOSED],
          solution_entities=deserialized_files_appended[SOLUTION])

      translations = ParseConfig.retrieve_reporting_translations(
          matches=matches,
          proposed_entities=deserialized_files_appended[PROPOSED],
          solution_entities=deserialized_files_appended[SOLUTION])

      return translations
    elif entity_type == COMPLEX:
      return deserialized_files_appended

  def setUp(self):
    super().setUp()
    featureful_file_path = (
        'tests/samples/proposed/entity_identification_virtual.yaml')
    self.highest_score_argument = self._prepare_dimension_argument(
        entity_type=COMPLEX,
        proposed_path=featureful_file_path,
        solution_path=featureful_file_path)

    empty_file_path = 'tests/samples/empty.yaml'
    self.none_score_argument = self._prepare_dimension_argument(
        entity_type=COMPLEX,
        proposed_path=empty_file_path,
        solution_path=empty_file_path)

    reporting_entity_file_path = (
        'tests/samples/proposed/entity_identification_reporting.yaml')
    self.middling_score_argument = self._prepare_dimension_argument(
        entity_type=COMPLEX,
        proposed_path=reporting_entity_file_path,
        solution_path=featureful_file_path)

  def testEntityIdentificationNoneScoreWithEmptyFile(self):
    """When ceiling==0, the resulting score is None."""
    none_score_expected = EntityIdentification(
        deserialized_files=self.none_score_argument).evaluate()

    # Directly assigned attributes
    self.assertEqual(none_score_expected.correct_reporting, 0)
    self.assertEqual(none_score_expected.correct_ceiling_reporting, 0)
    self.assertEqual(none_score_expected.incorrect_reporting, 0)

    self.assertEqual(none_score_expected.correct_virtual, 0)
    self.assertEqual(none_score_expected.correct_ceiling_virtual, 0)
    self.assertEqual(none_score_expected.incorrect_virtual, 0)

    # Inherited calculated attributes
    self.assertEqual(none_score_expected.correct_total(), 0)
    self.assertEqual(none_score_expected.correct_ceiling(), 0)
    self.assertEqual(none_score_expected.incorrect_total(), 0)

    # Inherited result properties. These are `None` by virtue of the ceiling
    # being falsy: that is to say, there was nothing to score against.
    self.assertEqual(none_score_expected.result_all, None)
    self.assertEqual(none_score_expected.result_reporting, None)
    self.assertEqual(none_score_expected.result_virtual, None)

  def testEntityIdentificationHighestPossibleScore(self):
    """When correct==ceiling, the resulting score is 1.0."""
    highest_score_expected = EntityIdentification(
        deserialized_files=self.highest_score_argument).evaluate()

    # Directly assigned attributes
    self.assertEqual(highest_score_expected.correct_reporting, 1)
    self.assertEqual(highest_score_expected.correct_ceiling_reporting, 1)
    self.assertEqual(highest_score_expected.incorrect_reporting, 0)

    self.assertEqual(highest_score_expected.correct_virtual, 1)
    self.assertEqual(highest_score_expected.correct_ceiling_virtual, 1)
    self.assertEqual(highest_score_expected.incorrect_virtual, 0)

    # Inherited calculated attributes
    self.assertEqual(highest_score_expected.correct_total(), 2)
    self.assertEqual(highest_score_expected.correct_ceiling(), 2)
    self.assertEqual(highest_score_expected.incorrect_total(), 0)

    # Inherited result properties
    self.assertEqual(highest_score_expected.result_all, 1.0)
    self.assertEqual(highest_score_expected.result_reporting, 1.0)
    self.assertEqual(highest_score_expected.result_virtual, 1.0)

  def testEntityIdentificationLowestPossibleScore(self):
    """When correct==0, the resulting score is -1.0."""
    lowest_score_argument = {
        PROPOSED:
        self.none_score_argument[PROPOSED],  # Empty, i.e. nothing correct
        SOLUTION: self.highest_score_argument[SOLUTION]
    }
    lowest_score_expected = EntityIdentification(
        deserialized_files=lowest_score_argument).evaluate()
    # Directly assigned attributes
    self.assertEqual(lowest_score_expected.correct_reporting, 0)
    self.assertEqual(lowest_score_expected.correct_ceiling_reporting, 1)
    self.assertEqual(lowest_score_expected.incorrect_reporting, 1)

    self.assertEqual(lowest_score_expected.correct_virtual, 0)
    self.assertEqual(lowest_score_expected.correct_ceiling_virtual, 1)
    self.assertEqual(lowest_score_expected.incorrect_virtual, 1)

    # Inherited calculated attributes
    self.assertEqual(lowest_score_expected.correct_total(), 0)
    self.assertEqual(lowest_score_expected.correct_ceiling(), 2)
    self.assertEqual(lowest_score_expected.incorrect_total(), 2)

    # Inherited result properties
    self.assertEqual(lowest_score_expected.result_all, -1.0)
    self.assertEqual(lowest_score_expected.result_reporting, -1.0)
    self.assertEqual(lowest_score_expected.result_virtual, -1.0)

  def testEntityIdentificationMiddlingScore(self):
    """When correct is half of the ceiling, the resulting score is 0.0."""
    middling_score_expected = EntityIdentification(
        deserialized_files=self.middling_score_argument).evaluate()

    # Directly assigned attributes
    self.assertEqual(middling_score_expected.correct_reporting, 1)
    self.assertEqual(middling_score_expected.correct_ceiling_reporting, 1)
    self.assertEqual(middling_score_expected.incorrect_reporting, 0)

    self.assertEqual(middling_score_expected.correct_virtual, 0)
    self.assertEqual(middling_score_expected.correct_ceiling_virtual, 1)
    self.assertEqual(middling_score_expected.incorrect_virtual, 1)

    # Inherited calculated attributes
    self.assertEqual(middling_score_expected.correct_total(), 1)
    self.assertEqual(middling_score_expected.correct_ceiling(), 2)
    self.assertEqual(middling_score_expected.incorrect_total(), 1)

    # Inherited result properties
    self.assertEqual(middling_score_expected.result_all, 0.0)
    self.assertEqual(middling_score_expected.result_reporting, 1.0)
    self.assertEqual(middling_score_expected.result_virtual, -1.0)


if __name__ == '__main__':
  absltest.main()
