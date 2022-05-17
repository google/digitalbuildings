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

import re as regex

PROPOSED, SOLUTION = FileTypes


class StandardFieldNaming(Dimension):
  """Quantifies whether the correct standard field names
  (e.g. "chilled_water_flowrate_sensor")
  were selected in the proposed file."""

  # SIMPLE category indicates this dimension receives `translations`
  # rather than `deserialized_files` to do its calculations
  category = DimensionCategories.SIMPLE

  def _split_subfields(self, field):
    return set(
        filter(lambda subfield: not bool(regex.match('[0-9]+', subfield)),
               field.split('_')))

  def evaluate(self):
    """Calculates and assigns properties necessary for generating a score."""
    correct_subfields = []
    correct_ceiling: int = 0
    incorrect_subfields = []

    for entity_translations in self.translations.values():
      for solution_field, solution_value in entity_translations[SOLUTION]:
        solution_subfields = self._split_subfields(solution_field)
        correct_ceiling += len(solution_subfields)

        proposed_subfields = set()

        for proposed_field, proposed_value in entity_translations[PROPOSED]:
          if proposed_value.raw_field_name == solution_value.raw_field_name:
            proposed_subfields = self._split_subfields(proposed_field)

        correct_subfields.extend(
            proposed_subfields.intersection(solution_subfields))
        incorrect_subfields.extend(
            solution_subfields.difference(proposed_subfields))

    self.correct_reporting = len(correct_subfields)
    self.correct_ceiling_reporting = correct_ceiling
    self.incorrect_reporting = len(incorrect_subfields)

    return self
