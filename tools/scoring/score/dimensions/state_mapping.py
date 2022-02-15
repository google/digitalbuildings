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


class StateMapping(Dimension):
  """
  Quantifies how accurately the proposed file
  mapped multi-state values for relevant fields.
  """
  def __init__(self, *, translations: TranslationsDict):
    super().__init__(translations=translations)

    # Combine translations for all devices within the dictionary
    solution_translations = [
        matched_translations[SOLUTION]
        for matched_translations in translations.values()
        if matched_translations[SOLUTION]
    ][0]
    proposed_translations = [
        matched_translations[PROPOSED]
        for matched_translations in translations.values()
        if matched_translations[PROPOSED]
    ][0]

    solution_mappings = set([
        (field[0], kv)
        for field in (field for field in solution_translations
                      if type(field[1]).__name__ == 'MultiStateValue')
        for kv in field[1].states.items()
    ])

    # TODO: clarify this comment and add test case
    # 'if isinstance(kv[1], str)' added 20211102 due to list value in
    # Mapped US-SVL-MP2 proposal
    proposed_mappings = set([
        (field[0], kv)
        for field in (field for field in proposed_translations
                      if type(field[1]).__name__ == 'MultiStateValue')
        for kv in field[1].states.items() if isinstance(kv[1], str)
    ])

    correct_mappings = proposed_mappings.intersection(solution_mappings)

    self.correct_reporting = len(correct_mappings)
    self.correct_ceiling_reporting = len(solution_mappings)
    self.incorrect_reporting = (self.correct_ceiling_reporting -
                                self.correct_reporting)
