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
""" Core component """

from score.dimensions.dimension import Dimension
from score.constants import FileTypes

PROPOSED, SOLUTION = FileTypes


class RawFieldSelection(Dimension):
  """
  Quantifies whether the correct raw fields
  (e.g. "points.chilled_water_flowrate_sensor.present_value")
  were mapped (versus ignored) in the proposed file.
  """
  def _fetch_raw_field_names(self, translations):
    return set([
        translation.raw_field_name
        for standard_field_name, translation in translations
    ])

  def evaluate(self):
    proposed_condensed = self._condense_translations(PROPOSED)
    solution_condensed = self._condense_translations(SOLUTION)

    # Account for empty list
    proposed_translations = proposed_condensed and proposed_condensed[0]
    solution_translations = solution_condensed and solution_condensed[0]

    proposed_fields = self._fetch_raw_field_names(proposed_translations)
    solution_fields = self._fetch_raw_field_names(solution_translations)

    correct_fields = proposed_fields.intersection(solution_fields)
    incorrect_fields = proposed_fields.difference(solution_fields)

    self.correct_reporting = len(correct_fields)
    self.correct_ceiling_reporting = len(set(solution_translations))
    self.incorrect_reporting = len(incorrect_fields)

    return self
