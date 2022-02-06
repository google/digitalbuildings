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


class RawFieldSelection(Dimension):
  """
  Quantifies whether the correct raw fields (e.g. "exhaust_air_damper_command)
  were mapped (versus ignored) in the proposed file.
  """
  def __init__(self, *, translations: TranslationsDict):
    super().__init__(translations=translations)

    solution_fields = set(
        map(lambda item: item[1].raw_field_name, translations[SOLUTION]))
    proposed_fields = set(
        map(lambda item: item[1].raw_field_name, translations[PROPOSED]))

    correct_fields = proposed_fields.intersection(solution_fields)
    incorrect_fields = proposed_fields.difference(solution_fields)

    self.correct_reporting = len(correct_fields)
    self.correct_ceiling_reporting = len(set(translations[SOLUTION]))
    self.incorrect_reporting = len(incorrect_fields)
