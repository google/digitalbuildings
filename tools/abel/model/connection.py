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
"""Module for concrete model connections."""

from typing import Dict

# pylint: disable=g-importing-member
from model.connection_type import ConnectionType
from model.constants import CONDITION
from model.constants import CONDITION_TYPE
from model.constants import CONNECTION_TYPE
from model.constants import DATA_VALIDATION
from model.constants import ONE_OF_LIST
from model.constants import SHOW_CUSTOM_UI
from model.constants import SOURCE_ENTITY_GUID
from model.constants import STRICT_VALIDATION
from model.constants import STRING_VALUE
from model.constants import TARGET_ENTITY_GUID
from model.constants import USER_ENTERED_VALUE
from model.constants import VALUES
from model.guid_to_entity_map import GuidToEntityMap


class Connection(object):
  """Class to model connections between entities.

  Attributes:
    source_entity_guid: Entity guid for connection source.
    target_entity_guid: Entity guid for connection target.
    connection_type: Instance of ConnectionType class defining the connection
      type between source and target.
  """

  def __init__(
      self,
      source_entity_guid: str,
      target_entity_guid: str,
      connection_type: ConnectionType,
  ) -> None:
    """Init.

    Args:
      source_entity_guid: Entity guid for connection source.
      target_entity_guid: Entity guid for connection target.
      connection_type: Type of connection.
    """
    self.source_entity_guid = source_entity_guid
    self.target_entity_guid = target_entity_guid
    self.connection_type = connection_type

  def __repr__(self):
    return (
        f'{self.source_entity_guid} - {self.connection_type.value} -'
        f' {self.target_entity_guid}'
    )

  def __hash__(self):
    return hash(
        (self.source_entity_guid, self.target_entity_guid, self.connection_type)
    )

  def __eq__(self, other) -> bool:
    if not isinstance(other, Connection):
      raise TypeError(f'{other} must be an instance of Connection')
    return (
        self.source_entity_guid == other.source_entity_guid
        and self.target_entity_guid == other.target_entity_guid
        and self.connection_type == other.connection_type
    )

  @classmethod
  def FromDict(cls, connection_dict: Dict[str, object]) -> ...:
    """Creates Connection instance from map of connection values by names.

    Args:
      connection_dict: A mapping of attributes to values pertaining to a
        connection.

    Returns:
      An instance of Connection class.
    """
    return cls(
        source_entity_guid=connection_dict[SOURCE_ENTITY_GUID],
        target_entity_guid=connection_dict[TARGET_ENTITY_GUID],
        connection_type=ConnectionType[connection_dict[CONNECTION_TYPE]],
    )

  @property
  def connection_type(self) -> ConnectionType:
    """Returns the connections type as an enum."""
    return self._connection_type

  @connection_type.setter
  def connection_type(self, value: ConnectionType) -> None:
    """Validates connection_type is an instance of ConnectionType enum and sets.

    Args:
      value: An instance of ConnectionType class to be set.
    """
    if not isinstance(value, ConnectionType):
      raise TypeError(f'{value} must be an instance of ConnectionType enum')
    self._connection_type = value

  def GetSpreadsheetRowMapping(
      self, guid_to_entity_map: GuidToEntityMap
  ) -> Dict[str, str]:
    """Returns a dictionary of Connection attributes by spreadsheet headers."""
    return {
        VALUES: [
            {
                USER_ENTERED_VALUE: {
                    STRING_VALUE: guid_to_entity_map.GetEntityCodeByGuid(
                        self.source_entity_guid
                    )
                }
            },
            {USER_ENTERED_VALUE: {STRING_VALUE: self.source_entity_guid}},
            {
                USER_ENTERED_VALUE: {STRING_VALUE: self.connection_type.name},
                DATA_VALIDATION: {
                    CONDITION: {
                        CONDITION_TYPE: ONE_OF_LIST,
                        VALUES: [
                            {USER_ENTERED_VALUE: namespace.value}
                            for namespace in ConnectionType
                        ],
                    },
                    STRICT_VALIDATION: True,
                    SHOW_CUSTOM_UI: True,
                },
            },
            {
                USER_ENTERED_VALUE: {
                    STRING_VALUE: guid_to_entity_map.GetEntityCodeByGuid(
                        self.target_entity_guid
                    )
                }
            },
            {USER_ENTERED_VALUE: {STRING_VALUE: self.target_entity_guid}},
        ]
    }
