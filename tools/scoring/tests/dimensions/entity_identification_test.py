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
  def _prepare_highest_score_argument(self, *, entity_type: str):
    # TODO: move this
    """Prepare argument for direct invocation
    of a dimension for purposes of testing.

      Arguments:
        entity_type: the category of the dimension. (Literal[SIMPLE, COMPLEX])

      Returns:
        The appropriate value for the dimension's singular named argument"""

    universe = BuildUniverse(use_simplified_universe=True)
    reporting_entity_sample = validator.Deserialize(
        ['tests/samples/canonical_entity.yaml'])[0]
    deserialized_files = {
        PROPOSED: reporting_entity_sample,
        SOLUTION: reporting_entity_sample
    }

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
    self.highest_score_argument = self._prepare_highest_score_argument(
        entity_type=COMPLEX)

  def testNoneScore(self):
    """Incomplete data."""
    none_score_argument = {PROPOSED: {}, SOLUTION: {}}
    entity_identification_none_score = EntityIdentification(
        deserialized_files=none_score_argument).evaluate()

    # Directly assigned attributes
    # TODO: add virtual
    self.assertEqual(entity_identification_none_score.correct_reporting, 0)
    self.assertEqual(entity_identification_none_score.correct_ceiling_reporting,
                     0)
    self.assertEqual(entity_identification_none_score.incorrect_reporting, 0)

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
    """Exactly correct."""
    entity_identification_highest_score = EntityIdentification(
        deserialized_files=self.highest_score_argument).evaluate()

    # Directly assigned attributes
    #TODO: add virtual
    self.assertEqual(entity_identification_highest_score.correct_reporting, 1)
    self.assertEqual(
        entity_identification_highest_score.correct_ceiling_reporting, 1)
    self.assertEqual(entity_identification_highest_score.incorrect_reporting, 0)

    # Inherited calculated attributes
    self.assertEqual(entity_identification_highest_score.correct_total(), 1)
    self.assertEqual(entity_identification_highest_score.correct_ceiling(), 1)
    self.assertEqual(entity_identification_highest_score.incorrect_total(), 0)

    # Inherited result properties
    self.assertEqual(entity_identification_highest_score.result_all, 1.0)
    self.assertEqual(entity_identification_highest_score.result_reporting, 1.0)
    self.assertEqual(entity_identification_highest_score.result_virtual, None)

  def testLowestScore(self):
    """Exactly incorrect."""
    lowest_score_argument = {
        PROPOSED: {},
        SOLUTION: self.highest_score_argument[SOLUTION]
    }
    entity_identification_lowest_score = EntityIdentification(
        deserialized_files=lowest_score_argument).evaluate()
    # Directly assigned attributes
    #TODO: add virtual
    self.assertEqual(entity_identification_lowest_score.correct_reporting, 0)
    self.assertEqual(
        entity_identification_lowest_score.correct_ceiling_reporting, 1)
    self.assertEqual(entity_identification_lowest_score.incorrect_reporting, 1)

    # Inherited calculated attributes
    self.assertEqual(entity_identification_lowest_score.correct_total(), 0)
    self.assertEqual(entity_identification_lowest_score.correct_ceiling(), 1)
    self.assertEqual(entity_identification_lowest_score.incorrect_total(), 1)

    # Inherited result properties
    self.assertEqual(entity_identification_lowest_score.result_all, -1.0)
    self.assertEqual(entity_identification_lowest_score.result_reporting, -1.0)
    # TODO
    # self.assertEqual(entity_identification_lowest_score.result_virtual, -1.0)

  def testMiddlingScore(self):
    """50% correct."""
    #TODO
    # middling_score_argument = {
    #     PROPOSED: {},
    #     SOLUTION: {}
    # }
    # entity_identification_middling_score = EntityIdentification(
    #     deserialized_files=middling_score_argument).evaluate()

    # Directly assigned attributes
    #TODO: add virtual
    # self.assertEqual(entity_identification_middling_score.correct_reporting, 1)
    # self.assertEqual(
    #     entity_identification_middling_score.correct_ceiling_reporting, 2)
    # self.assertEqual(entity_identification_middling_score.incorrect_reporting,
    #                  1)

    # Inherited calculated attributes
    # self.assertEqual(entity_identification_middling_score.correct_total(), 0)
    # self.assertEqual(entity_identification_middling_score.correct_ceiling(), 1)
    # self.assertEqual(entity_identification_middling_score.incorrect_total(), 1)

    # Inherited result properties
    # self.assertEqual(entity_identification_middling_score.result_all, 0.0)
    # self.assertEqual(entity_identification_middling_score.result_reporting,
    #                  0.0)
    # self.assertEqual(entity_identification_middling_score.result_virtual,
    #                  0.0)


if __name__ == '__main__':
  absltest.main()
