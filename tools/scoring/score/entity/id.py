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

# Entities

# There are three aspects of entities that we're concerned with:

# What entities exist

# Were their points identified properly

# Was their type assigned accurately

# While success at each of these likely correlates with success at the other
# two.  For example,  it may be possible to infer that an entity should exist
# and be a certain type without being able to explicitly identify the points
# that map to it.  As a result, we'd like to score them all separately.

# Entity Identification

# List all the canonically typed devices that exist in the solution
#   Identify reporting devices by cloud_device_id
#   Identify virtual devices by parent devices
#       Note: there may be more than one device with each ancestry
#   For each solution device or group, identify result devices that have the
# same identifier
#   Allow only one mapping from the result for each device in the solution

# The score is:
#  (number of correctly paired devices) - (number of unpaired result devices)
# total devices

# Again, reporting and virtual device results should be separable

"""

from score.score import Score


class EntityId(Score):

  def __init__(self):
    return False
