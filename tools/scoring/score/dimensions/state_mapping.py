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

from score.constants import FileTypes
from score.dimensions.dimension import Dimension
from score.types_ import TranslationsDict

PROPOSED, SOLUTION = FileTypes


class StateMapping(Dimension):
  """Quantifies how accurately the proposed file mapped multi-state values for relevant fields."""

  def __init__(self, *, translations: TranslationsDict):
    super().__init__(translations=translations)

    multistate_solutions = (
        field for field in translations[SOLUTION]
        if type(field[1]).__name__ == 'MultiStateValue')
    solution_mappings = set()
    for field in multistate_solutions:
      for kv in field[1].states.items():
        solution_mappings.add((field[0], kv))

    # TODO(b/210741084): clarify this comment and add test case
    # 'if isinstance(kv[1], str)' added 20211102 due to list value in
    # Mapped US-SVL-MP2 proposal
    multistate_proposed = (
        field for field in translations[PROPOSED]
        if type(field[1]).__name__ == 'MultiStateValue')
    proposed_mappings = set()
    for field in multistate_proposed:
      for kv in field[1].states.items():
        if isinstance(kv[1], str):
          proposed_mappings.add((field[0], kv))

    correct_mappings = proposed_mappings.intersection(solution_mappings)

    self.correct_reporting = len(correct_mappings)
    self.correct_ceiling_reporting = len(solution_mappings)
    self.incorrect_reporting = (
        self.correct_ceiling_reporting - self.correct_reporting)
