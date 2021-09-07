# Copyright 2021 Google LLC
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
"""

# Unit Mappings

# Dimensional fields should have correct mappings for their units of measure or
# states to standard DBO values.  In practical terms, identification of the
# units field for any known field will be trivial in the data participants
# receive.  We will therefore assume it is correct and not score it.

# What we can score is the Key:value mapping of native unit names to canonical
# names.  This may be done for each dimensional field in the solution set
# field-by-field basis (though it is somewhat redundant in practical terms).
# Scoring will be:
#  (number of correctly defined Key:value pairs) - (number of incorrectly
# defined key:value pairs) total key:value pairs

# This score should be calculated independently overall and for fields that
# were correctly identified as important.

"""

from score.score import Score


class UnitMapping(Score):

  def __init__(self):
    return False
