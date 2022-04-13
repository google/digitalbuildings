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
"""Core component."""

from score.dimensions.dimension import Dimension
from score.constants import FileTypes, DimensionCategories

PROPOSED, SOLUTION = FileTypes


class UnitMapping(Dimension):
  """Quantifies how accurately the proposed file
  mapped dimensional units for relevant fields."""

  # SIMPLE category indicates this dimension receives translations
  # rather than `deserialized_files` to do its calculations
  category = DimensionCategories.SIMPLE

  def _fetch_mappings(self, translations):
    return set([(field[0], kv)
                for field in (field for field in translations
                              if type(field[1]).__name__ == 'DimensionalValue')
                for kv in field[1].unit_mappings.items()])

  def evaluate(self):
    """Calculates and assigns properties necessary for generating a score."""

    proposed_translations, solution_translations = map(
        self._condense_translations, (PROPOSED, SOLUTION))

    proposed_mappings, solution_mappings = map(
        self._fetch_mappings, (proposed_translations, solution_translations))

    correct_mappings = proposed_mappings.intersection(solution_mappings)

    self.correct_reporting = len(correct_mappings)
    self.correct_ceiling_reporting = len(solution_mappings)
    self.incorrect_reporting = (self.correct_ceiling_reporting -
                                self.correct_reporting)

    return self
