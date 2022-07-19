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
"""Module for EntityField units."""

from typing import Dict

from google3.third_party.digitalbuildings.tools.concrete_model.model.constants import RAW_UNIT_PATH
from google3.third_party.digitalbuildings.tools.concrete_model.model.constants import RAW_UNIT_VALUE
from google3.third_party.digitalbuildings.tools.concrete_model.model.constants import STANDARD_UNIT_VALUE


class Units(object):
  """Data container class for an Entity Field's Units.

  Attributes:
    raw_unit_path: Bacnet device path to a data point's units.
    standard_to_raw_unit_map: A mapping of standard units names to bacnet device
      data units.
  """

  def __init__(self, raw_unit_path: str,
               standard_to_raw_unit_map: Dict[str, str]) -> None:
    """Init.

    Args:
      raw_unit_path: Bacnet device path to a data point's units.
      standard_to_raw_unit_map: A mapping of standard units names to bacnet
        device data units.
    """
    self.raw_unit_path = raw_unit_path
    self.standard_to_raw_unit_map = standard_to_raw_unit_map

  def GetSpreadsheetRowMapping(self) -> Dict[str, str]:
    """Returns a dictionary of EntityField attributes by spreadsheet headers.

    Corresponds to a single row in a concrete model spreadsheet.
    """
    spreadsheet_row_mapping = {RAW_UNIT_PATH: self.raw_unit_path}
    standard_to_raw_unit_map = self.standard_to_raw_unit_map
    for standard_unit_value, raw_unit_value in standard_to_raw_unit_map.items():
      spreadsheet_row_mapping.update({
          STANDARD_UNIT_VALUE: standard_unit_value,
          RAW_UNIT_VALUE: raw_unit_value
      })
    return spreadsheet_row_mapping
