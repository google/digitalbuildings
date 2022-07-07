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

from model.connection_type import ConnectionType
from model.constants import CONNECTION_TYPE
from model.constants import SOURCE_ENTITY_CODE
from model.constants import SOURCE_ENTITY_GUID
from model.constants import TARGET_ENTITY_CODE
from model.constants import TARGET_ENTITY_GUID
from model.guid_to_entity_map import GuidToEntityMap


class Connection(object):
  """Class to model connections between entities.

  Attributes:
    source_entity_guid: Entity guid for connection source.
    target_entity_guid: Entity guid for connection target.
    connection_type: Instance of ConnectionType class defining the connection
      type between source and target.
    guid_to_entity_map: A global mapping of GUIDs to Entity instances.
  """

  def __init__(self, source_entity_guid: str, target_entity_guid: str,
               connection_type: ConnectionType) -> None:
    """Init.

    Args:
      source_entity_guid: Entity guid for connection source.
      target_entity_guid: Entity guid for connection target.
      connection_type: Type of connection.
    """
    self.source_entity_guid = source_entity_guid
    self.target_entity_guid = target_entity_guid
    self.connection_type = connection_type
    self.guid_to_entity_map = GuidToEntityMap()

  def __str__(self):
    return f'{self.source_entity_guid} - {self.connection_type} - {self.target_entity_guid}'

  def __hash__(self):
    return hash((self.source_entity_guid, self.target_entity_guid,
                 self.connection_type))

  @classmethod
  def FromDict(cls, connection_dict: Dict[str, object]) ->...:
    """Creates a Connection object from mapping of connection attributes to values.

    Args:
      connection_dict: A mapping of attributes to values pertaining to a
        connection.

    Returns:
      An instance of Connection class.
    """
    connection = cls(
        source_entity_guid=connection_dict[SOURCE_ENTITY_GUID],
        target_entity_guid=connection_dict[TARGET_ENTITY_GUID],
        connection_type=ConnectionType[connection_dict[CONNECTION_TYPE]])
    return connection

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

  def GetSpreadsheetRowMapping(self) -> Dict[str, str]:
    """Returns a dictionary of Connection attributes by spreadsheet headers."""
    return {
        SOURCE_ENTITY_CODE:
            self.guid_to_entity_map.GetEntityCodeByGuid(self.source_entity_guid
                                                       ),
        SOURCE_ENTITY_GUID:
            self.source_entity_guid,
        TARGET_ENTITY_CODE:
            self.guid_to_entity_map.GetEntityCodeByGuid(self.target_entity_guid
                                                       ),
        TARGET_ENTITY_GUID:
            self.target_entity_guid,
        CONNECTION_TYPE:
            self.connection_type.name
    }
