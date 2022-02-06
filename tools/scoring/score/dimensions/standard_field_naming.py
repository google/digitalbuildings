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

import re as regex

PROPOSED, SOLUTION = FileTypes


class StandardFieldNaming(Dimension):
  """
  Quantifies whether the correct standard field names
  (e.g. "chilled_water_flowrate_sensor")
  were selected in the proposed file.
  """
  def __init__(self, *, translations: TranslationsDict):
    super().__init__(translations=translations)

    correct_subfields = []
    correct_ceiling: int = 0
    incorrect_subfields = []

    for s_field, s_value in translations[SOLUTION]:
      s_subs = set(
          filter(lambda subfield: not bool(regex.match('[0-9]+', subfield)),
                 s_field.split('_')))
      correct_ceiling += len(s_subs)

      for p_field, p_value in translations[PROPOSED]:
        if p_value.raw_field_name == s_value.raw_field_name:
          p_subs = set(
              filter(lambda subfield: not bool(regex.match('[0-9]+', subfield)),
                     p_field.split('_')))

          correct_subs = p_subs.intersection(s_subs)
          incorrect_subs = p_subs.difference(s_subs)

          correct_subfields += correct_subs
          incorrect_subfields += incorrect_subs

    self.correct_reporting = len(correct_subfields)
    self.correct_ceiling_reporting = correct_ceiling
    self.incorrect_reporting = len(incorrect_subfields)
