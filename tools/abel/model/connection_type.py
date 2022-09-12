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
"""Module for ConnectionType class."""

import enum


class ConnectionType(enum.Enum):
  """Enum class for different connection types."""

  # The type of the connection is not specified.
  TYPE_UNSPECIFIED = 0

  # "Source" physically encapsulates at least part of "Target".
  CONTAINS = 1

  # "Source" determines or affects the internal state of "Target".
  CONTROLS = 2

  # "Source" has some component or part "Target".
  HAS_PART = 3

  # "Source" flows to "Target".
  FEEDS = 4

  # (Mechanical) Function "Source" has an input "Target".
  HAS_INPUT = 5

  # (Mechanical) Function "Source" has an output "Target".
  HAS_OUTPUT = 6

  # "Source" has the detectable range of "Target".
  HAS_RANGE = 7

  # Connection is between two sites.
  SITE = 8
