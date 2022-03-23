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

import copy

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

    deserialized_files_appended = ParseConfig._append_types(  # pylint: disable=protected-access
        universe=universe,
        deserialized_files=deserialized_files)

    if entity_type == SIMPLE:
      matches = ParseConfig._match_reporting_entities(  # pylint: disable=protected-access
          proposed_entities=deserialized_files_appended[PROPOSED],
          solution_entities=deserialized_files_appended[SOLUTION])

      translations = ParseConfig._retrieve_reporting_translations(  # pylint: disable=protected-access
          matches=matches,
          proposed_entities=deserialized_files_appended[PROPOSED],
          solution_entities=deserialized_files_appended[SOLUTION])

      return translations
    elif entity_type == COMPLEX:
      return deserialized_files_appended

  def setUp(self):
    super().setUp()
    path = 'tests/samples/virtual_entity.yaml'
    self.highest_score_argument = self._prepare_dimension_argument(
        entity_type=COMPLEX, proposed_path=path, solution_path=path)

  def testNoneScore(self):
    """When ceiling==0, the resulting score is None."""
    none_score_argument = {PROPOSED: {}, SOLUTION: {}}
    entity_identification_none_score = EntityIdentification(
        deserialized_files=none_score_argument).evaluate()

    # Directly assigned attributes
    self.assertEqual(entity_identification_none_score.correct_reporting, 0)
    self.assertEqual(entity_identification_none_score.correct_ceiling_reporting,
                     0)
    self.assertEqual(entity_identification_none_score.incorrect_reporting, 0)

    self.assertEqual(entity_identification_none_score.correct_virtual, 0)
    self.assertEqual(entity_identification_none_score.correct_ceiling_virtual,
                     0)
    self.assertEqual(entity_identification_none_score.incorrect_virtual, 0)

    # Inherited calculated attributes
    self.assertEqual(entity_identification_none_score.correct_total(), 0)
    self.assertEqual(entity_identification_none_score.correct_ceiling(), 0)
    self.assertEqual(entity_identification_none_score.incorrect_total(), 0)

    # Inherited result properties. These are `None` by virtue of the ceiling
    # being falsy: that is to say, there was nothing to score against.
    self.assertEqual(entity_identification_none_score.result_all, None)
    self.assertEqual(entity_identification_none_score.result_reporting, None)
    self.assertEqual(entity_identification_none_score.result_virtual, None)

  def testHighestScore(self):
    """When correct==ceiling, the resulting score is 1.0."""
    entity_identification_highest_score = EntityIdentification(
        deserialized_files=self.highest_score_argument).evaluate()

    # Directly assigned attributes
    self.assertEqual(entity_identification_highest_score.correct_reporting, 1)
    self.assertEqual(
        entity_identification_highest_score.correct_ceiling_reporting, 1)
    self.assertEqual(entity_identification_highest_score.incorrect_reporting, 0)

    self.assertEqual(entity_identification_highest_score.correct_virtual, 1)
    self.assertEqual(
        entity_identification_highest_score.correct_ceiling_virtual, 1)
    self.assertEqual(entity_identification_highest_score.incorrect_virtual, 0)

    # Inherited calculated attributes
    self.assertEqual(entity_identification_highest_score.correct_total(), 2)
    self.assertEqual(entity_identification_highest_score.correct_ceiling(), 2)
    self.assertEqual(entity_identification_highest_score.incorrect_total(), 0)

    # Inherited result properties
    self.assertEqual(entity_identification_highest_score.result_all, 1.0)
    self.assertEqual(entity_identification_highest_score.result_reporting, 1.0)
    self.assertEqual(entity_identification_highest_score.result_virtual, 1.0)

  def testLowestScore(self):
    """When correct==0, the resulting score is -1.0."""
    lowest_score_argument = {
        PROPOSED: {},
        SOLUTION: self.highest_score_argument[SOLUTION]
    }
    entity_identification_lowest_score = EntityIdentification(
        deserialized_files=lowest_score_argument).evaluate()
    # Directly assigned attributes
    self.assertEqual(entity_identification_lowest_score.correct_reporting, 0)
    self.assertEqual(
        entity_identification_lowest_score.correct_ceiling_reporting, 1)
    self.assertEqual(entity_identification_lowest_score.incorrect_reporting, 1)

    self.assertEqual(entity_identification_lowest_score.correct_virtual, 0)
    self.assertEqual(entity_identification_lowest_score.correct_ceiling_virtual,
                     1)
    self.assertEqual(entity_identification_lowest_score.incorrect_virtual, 1)

    # Inherited calculated attributes
    self.assertEqual(entity_identification_lowest_score.correct_total(), 0)
    self.assertEqual(entity_identification_lowest_score.correct_ceiling(), 2)
    self.assertEqual(entity_identification_lowest_score.incorrect_total(), 2)

    # Inherited result properties
    self.assertEqual(entity_identification_lowest_score.result_all, -1.0)
    self.assertEqual(entity_identification_lowest_score.result_reporting, -1.0)
    self.assertEqual(entity_identification_lowest_score.result_virtual, -1.0)

  def testMiddlingScore(self):
    """When correct is half of the ceiling, the resulting score is 0.0."""
    # To create the proposed file, clone the solution file and remove the
    # virtual entity, which comprises 50% of the dictionary
    proposed = copy.deepcopy(self.highest_score_argument[SOLUTION])
    proposed.pop('daf3048f-2118-4afc-a5f0-8b4ce0c25fef')
    middling_score_argument = {
        PROPOSED: proposed,
        SOLUTION: self.highest_score_argument[SOLUTION]
    }
    entity_identification_middling_score = EntityIdentification(
        deserialized_files=middling_score_argument).evaluate()

    # Directly assigned attributes
    self.assertEqual(entity_identification_middling_score.correct_reporting, 1)
    self.assertEqual(
        entity_identification_middling_score.correct_ceiling_reporting, 1)
    self.assertEqual(entity_identification_middling_score.incorrect_reporting,
                     0)

    self.assertEqual(entity_identification_middling_score.correct_virtual, 0)
    self.assertEqual(
        entity_identification_middling_score.correct_ceiling_virtual, 1)
    self.assertEqual(entity_identification_middling_score.incorrect_virtual, 1)

    # Inherited calculated attributes
    self.assertEqual(entity_identification_middling_score.correct_total(), 1)
    self.assertEqual(entity_identification_middling_score.correct_ceiling(), 2)
    self.assertEqual(entity_identification_middling_score.incorrect_total(), 1)

    # Inherited result properties
    self.assertEqual(entity_identification_middling_score.result_all, 0.0)
    self.assertEqual(entity_identification_middling_score.result_reporting, 1.0)
    self.assertEqual(entity_identification_middling_score.result_virtual, -1.0)


if __name__ == '__main__':
  absltest.main()
