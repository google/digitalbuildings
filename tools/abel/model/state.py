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
"""Module for concrete model states."""

from typing import Dict

# pylint: disable=g-importing-member
from model.constants import RAW_STATE
from model.constants import REPORTING_ENTITY_FIELD_NAME
from model.constants import REPORTING_ENTITY_GUID
from model.constants import STANDARD_STATE
from model.constants import STRING_VALUE
from model.constants import USER_ENTERED_VALUE
from model.constants import VALUES
from model.guid_to_entity_map import GuidToEntityMap


class State(object):
  """Class for concrete model states.

  Attributes:
    reporting_entity_guid: UUID4 id of the parent reporting entity for a field.
    std_field_name: Standardized field name for an EntityField
    standard_state: Standardized state name.
    raw_state: Raw state name coming from bacnet payload device.
    guid_to_entity_map: Global entity by guid mapping.
  """

  def __init__(
      self,
      reporting_entity_guid: str,
      std_field_name: str,
      standard_state: str,
      raw_state: str,
  ):
    """Init.

    Args:
      reporting_entity_guid: UUID4 id of the parent entity for a field.
      std_field_name: Standardized field name for an EntityField
      standard_state: Standardized state name.
      raw_state: Raw state name coming from bacnet payload device.
    """
    self.reporting_entity_guid = reporting_entity_guid
    self.std_field_name = std_field_name
    self.standard_state = standard_state
    self.raw_state = raw_state

  def __repr__(self) -> str:
    return (
        f'{self.raw_state}: {self.standard_state} for'
        f' {self.reporting_entity_guid}: {self.std_field_name}'
    )

  def __eq__(self, other: ...) -> bool:
    if not isinstance(other, State):
      raise TypeError('Other object must be a state instance.')
    return (
        self.reporting_entity_guid == other.reporting_entity_guid
        and self.std_field_name == other.std_field_name
        and self.standard_state == other.standard_state
        and self.raw_state == other.raw_state
    )

  @classmethod
  def FromDict(cls, states_dict: Dict[str, str]) -> ...:
    return cls(
        reporting_entity_guid=states_dict[REPORTING_ENTITY_GUID],
        std_field_name=states_dict[REPORTING_ENTITY_FIELD_NAME],
        standard_state=states_dict[STANDARD_STATE],
        raw_state=states_dict[RAW_STATE],
    )

  def GetSpreadsheetRowMapping(
      self, guid_to_entity_map: GuidToEntityMap
  ) -> Dict[str, str]:
    """Returns a dictionary of State attributes by spreadsheet headers."""
    return {
        VALUES: [
            {
                USER_ENTERED_VALUE: {
                    STRING_VALUE: guid_to_entity_map.GetEntityCodeByGuid(
                        self.reporting_entity_guid
                    )
                }
            },
            {USER_ENTERED_VALUE: {STRING_VALUE: self.reporting_entity_guid}},
            {USER_ENTERED_VALUE: {STRING_VALUE: self.std_field_name}},
            {USER_ENTERED_VALUE: {STRING_VALUE: self.standard_state}},
            {USER_ENTERED_VALUE: {STRING_VALUE: self.raw_state}},
        ]
    }
