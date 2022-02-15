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
"""Module for concrete model units."""

from typing import Dict


class Units(object):
  """Class for concrete model states.

  Attributes:
    raw_unit_path: the units path in the payload device.
    standard_to_raw_unit_map: A mapping DBO
      unit to raw unit value.
  """

  def __init__(self,
               raw_unit_path: str,
               standard_to_raw_unit_map: Dict[str, str]) -> None:
    """Init.

    Args:
      raw_unit_path: the units path in the payload device.
      standard_to_raw_unit_map: A mapping DBO
        unit to raw unit value.
    """
    self.raw_unit_path = raw_unit_path
    self.standard_to_raw_unit_map = standard_to_raw_unit_map

  def AddUnit(self, raw_unit_path: str,
              dbo_to_raw_unit_map: Dict[str, str]) -> None:
    """Adds a new unit to self.standard_to_raw_unit_map.

    Args:
      raw_unit_path: a devices path to a unit value. i.e.
        pointset.points.supply_fan_speed_percentage_command.units
      dbo_to_raw_unit_map: A mapping of standard unit name to raw units from
        payload device.
    """
