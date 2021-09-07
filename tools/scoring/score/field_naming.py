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

# Field Naming

# A partial field match is a field mapping that contains either a subset or superset of correct subfields for any particular field.  Theoretically, it is possible to select a subset of subfields that do not combine to meet field construction criteria, however there are a few reasons why discounting these selections is worthwhile:

# Subfield sets that don't make syntactically correct fields are trivially identifiable as invalid

# The required subfields (point/measurement type) of a minimal field are the easiest subfields to identify.

# Limiting results to syntactically valid fields allows building_config to be used without modification.

# Because the exact correct result is known for each raw field in each context, fields can be scored by:
#  (number of correctly identified subfields) - (number of extra result subfields) total solution subfields

# This makes more difficult fields worth more as well, which seems desirable.  Exact matches should also be tracked, and results should be separable between virtual and reporting devices.

# Enumerations

# It is frequently the case that devices have multiple fields that differ only by a trailing enumeration.  As this enumeration is assigned arbitrarily by definition, it should be excluded from scoring.

# Recording vs. Virtual device fields

# Our primary concern is that canonically typed entities are mapped correctly. In the case where a device's points are represented in both a reporting and a virtual device, the virtual device is typically a canonical type and the reporting device is not.  From a scoring perspective, we can ignore the reporting device field in this case and score the mapping of the raw field to the virtual device field, skipping the intermediate name.  In the rare case where both are canonical, we can give the participant the result:actual mapping that makes the best score, however there may be few enough instances of this to simply ignore them in the result.

"""


from score.score import Score

class FieldNaming(Score):
  def __init__(self):
    return False
