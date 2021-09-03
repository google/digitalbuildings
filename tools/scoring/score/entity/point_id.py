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


# Entity Point Identification

# For each entity we care that all of its points are identified successfully.  While applying a point to a reporting device should be trivial once the point is identified and named, it is more difficult for virtual devices, and therefore worth scoring.
#
# Procedurally, scoring is accomplished by first building a multi-mapping between solution devices or device groups (for virtual devices) and result devices.  Starting with the best possible match in the group, devices are scored and removed from the global set until all solution devices have been processed.
#  (number of correctly mapped fields) - (number of incorrect or extra fields) total fields in all devices

# Results can be viewed separately for reporting and virtual devices.

from score.score import Score


class PointId(Score):
    def __init__(self):
        return False
