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
from score.types_ import TranslationsDict
from score.constants import FileTypes

PROPOSED, SOLUTION = FileTypes


class UnitMapping(Dimension):
  """
  Quantifies how accurately the proposed file
  mapped dimensional units for relevant fields.
  """
  def __init__(self, *, translations: TranslationsDict):
    super().__init__(translations=translations)

    solution_mappings = set([
        (field[0], kv)
        for field in (field for field in translations[SOLUTION]
                      if type(field[1]).__name__ == 'DimensionalValue')
        for kv in field[1].unit_mappings.items()
    ])

    proposed_mappings = set([
        (field[0], kv)
        for field in (field for field in translations[PROPOSED]
                      if type(field[1]).__name__ == 'DimensionalValue')
        for kv in field[1].unit_mappings.items()
    ])

    correct_mappings = proposed_mappings.intersection(solution_mappings)

    self.correct_reporting = len(correct_mappings)
    self.correct_ceiling_reporting = len(solution_mappings)
    self.incorrect_reporting = (self.correct_ceiling_reporting -
                                self.correct_reporting)
