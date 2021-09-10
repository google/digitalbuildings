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
""" Criteria upon which proposed solutions are scored. """

from enum import Enum, unique


@unique
class _Entity(Enum):
  CONNECTION_IDENTIFICATION = 'connection_identification'
  IDENTIFICATION = 'identification'
  POINT_IDENTIFICATION = 'point_identification'
  TYPE_IDENTIFICATION = 'type_identification'


@unique
class Dimension(Enum):
  UNIT_MAPPING = 'unit_mapping'
  STATE_MAPPING = 'state_mapping'
  FIELD_SELECTION = 'field_selection'
  FIELD_NAMING = 'field_naming'
  ENTITY = _Entity
