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
"""Module for concrete model entities."""

import abc
from typing import Dict, List, Optional

from google3.third_party.digitalbuildings.tools.concrete_model.model.connection import Connection
from google3.third_party.digitalbuildings.tools.concrete_model.model.constants import BC_GUID
from google3.third_party.digitalbuildings.tools.concrete_model.model.constants import CLOUD_DEVICE_ID
from google3.third_party.digitalbuildings.tools.concrete_model.model.constants import ENTITY_CODE
from google3.third_party.digitalbuildings.tools.concrete_model.model.constants import ETAG
from google3.third_party.digitalbuildings.tools.concrete_model.model.constants import IS_REPORTING
from google3.third_party.digitalbuildings.tools.concrete_model.model.constants import METADATA
from google3.third_party.digitalbuildings.tools.concrete_model.model.constants import NAMESPACE
from google3.third_party.digitalbuildings.tools.concrete_model.model.constants import TYPE_NAME
from google3.third_party.digitalbuildings.tools.concrete_model.model.entity_field import EntityField


class Entity(object):
  """Base class to model concrete entities within a building.

  Attributes:
    code: Human readable name of an entity.
    etag: Hash used for entity versioning.
    namespace: DBO namespace for an entity e.g. HVAC.
    connections: List of Connection class instances.
    type_name: A DBO type name for this entity.
    bc_guid: UUID4 value for an entity.
    metadata: Contextual metadata coming from a physical device. e.g. {
        location: '/Sif-Solo/Site 1 - Sif/Charleston Road North/B13 - 1875
          Charleston/Roof',
        control_programs: ['Trane AC-1', '1875 Charleston'],
        device_id: 'DEV:2809009',
        model_label: blank,
        manufacturer_label: blank }
  """

  def __init__(self,
               code: str,
               namespace: str,
               etag: Optional[str] = None,
               type_name: Optional[str] = None,
               bc_guid: Optional[str] = None,
               metadata: Optional[Dict[str, str]] = None):
    """Init.

    Args:
      code: The entity's name.
      namespace: An entity's DBO namespace e.g. HVAC.
      etag: [Optional] Hash used for entity versioning.
      type_name: [Optional] An entity's DBO type name.
      bc_guid: [Optional] UUID4 value for an entity.
      metadata: [Optional] Contextual metadata about an entity.
    """

    self.code = code
    self.bc_guid = bc_guid
    self.etag = etag
    self.namespace = namespace
    self._connections = []
    self.type_name = type_name
    self.metadata = metadata

  def __hash__(self):
    return hash((self.code, self.etag, self.bc_guid))

  def __repr__(self) -> str:
    return f'{self.code}'

  @property
  def connections(self) -> List[Connection]:
    """Returns a list of Connection instances related to an entity."""
    return self._connections

  @connections.setter
  def connections(self, new_connections: List[Connection]) -> None:
    """Sets new_connections as self._connections.

    Args:
      new_connections: A list of Connection instances
    """
    self._connections.clear()
    for connection in new_connections:
      self.AddConnection(connection)

  def AddConnection(self, new_connection: Connection) -> None:
    """Adds a new entity connection to self._connections.

    Args:
      new_connection: Connection instance being added to an entity

    Raises:
      TypeError: If new_connection is not a Connection instance.
      AttributeError: If new_connection.target_entity_guid does not equal the
      entity's guid.

    """
    if not isinstance(new_connection, Connection):
      raise TypeError(
          f'{new_connection} cannot be added as a connection to an entity.')
    if new_connection.target_entity_guid != self.bc_guid:
      raise AttributeError(
          f'{new_connection.target_entity_guid} does not equal {self.bc_guid}')
    self.connections.append(new_connection)

  @abc.abstractmethod
  def GetSpreadsheetRowMapping(self):
    """Returns a dictionary of entity attributes by spreadsheet headers."""


class VirtualEntity(Entity):
  """Class to model virtual entities within a building.

  Attributes:
    links: List of EntityField instances mapping to this virtual entity.
  """

  def __init__(self,
               code: str,
               namespace: str,
               etag: Optional[str] = None,
               type_name: Optional[str] = None,
               bc_guid: Optional[str] = None,
               metadata: Optional[Dict[str, str]] = None):
    """Init.

    Args:
      code: The entity's name.
      namespace: An entity's DBO namespace i.e. HVAC.
      etag: [Optional] Hash used for entity versioning.
      type_name: [Optional] An entity's DBO type name.
      bc_guid: [Optional] UUID4 value for an entity.
      metadata: [Optional] Contextual metadata about an entity.
    """

    super().__init__(code, namespace, etag, type_name, bc_guid, metadata)
    self._links = []

  def __eq__(self, other: ...) -> bool:
    if not isinstance(other, Entity):
      raise TypeError(f'{str(other)} must be an Entity instance')
    return (self.code, self.bc_guid) == (other.code, other.bc_guid)

  @classmethod
  def FromDict(cls, entity_dict: Dict[str, str]) ->...:
    """Class method to create an Entity instance from a mapping of entity attributes to values.

    Args:
      entity_dict: Dictionary mapping entity attributes to values from a
        spreadsheet or building configuration.

    Returns:
      An instance of Entity class.
    """
    # TODO(b/228973208) Add support for key errors for keys not in entity_dict.
    virtual_entity_instance = cls(
        code=entity_dict[ENTITY_CODE],
        bc_guid=entity_dict[BC_GUID],
        namespace=entity_dict[NAMESPACE],
        type_name=entity_dict[TYPE_NAME],
    )
    if ETAG in entity_dict.keys():
      virtual_entity_instance.etag = entity_dict[ETAG]
    # Merge all metadata cells in a row into one dictionary
    virtual_entity_instance.metadata = {
        k[len(METADATA) + 1:]: v
        for k, v in entity_dict.items()
        if k[:len(METADATA)] == METADATA
    }
    return virtual_entity_instance

  @property
  def links(self) -> List[EntityField]:
    """Returns a list of linked EntityField instances."""
    return self._links

  @links.setter
  def links(self, new_links: List[EntityField]) -> None:
    """Sets new_links as self._links.

    Args:
      new_links: A list of EntityField instances.
    """
    self._links.clear()
    for link in new_links:
      self.AddLink(new_link=link)

  def AddLink(self, new_link: EntityField) -> None:
    """Adds a new link to self._links."""
    if not isinstance(new_link, EntityField):
      raise TypeError(f'{str(new_link)} must be an EntityField instance.')
    self._links.append(new_link)

  def GetSpreadsheetRowMapping(self) -> Dict[str, str]:
    """Returns a dictionary of  virtual entity attributes by spreadsheet headers."""
    return {
        ENTITY_CODE: self.code,
        BC_GUID: self.bc_guid,
        IS_REPORTING: False,
        CLOUD_DEVICE_ID: None,
        ETAG: self.etag,
        NAMESPACE: self.namespace,
        TYPE_NAME: self.type_name
    }


class ReportingEntity(Entity):
  """Class to model reporting entities within a building.

  Attributes:
    cloud_device_id: Unique numeric ID for cloud iot service.
    translations: List of EntityField instances modeling datapoints on a
      reporting entity/device.
  """

  def __init__(self,
               code: str,
               namespace: str,
               cloud_device_id: Optional[str] = None,
               etag: Optional[str] = None,
               type_name: Optional[str] = None,
               bc_guid: Optional[str] = None,
               metadata: Optional[Dict[str, str]] = None):
    """Init.

    Args:
      code: The entity's name.
      namespace: An entity's DBO namespace i.e. HVAC.
      cloud_device_id: [Optional] Unique numeric ID for cloud iot service.
      etag: [Optional] Hash used for entity versioning.
      type_name: [Optional] An entity's DBO type name.
      bc_guid: [Optional] UUID4 value for an entity.
      metadata: [Optional] Contextual metadata about an entity.
    """

    super().__init__(code, namespace, etag, type_name, bc_guid, metadata)
    self.cloud_device_id = cloud_device_id
    self._translations = []

  def __eq__(self, other: ...) -> bool:
    if not isinstance(other, Entity):
      raise TypeError(f'{str(other)} must be an Entity instance')
    return (self.code, self.cloud_device_id,
            self.bc_guid) == (other.code, other.cloud_device_id, other.bc_guid)

  @classmethod
  def FromDict(cls, entity_dict: Dict[str, str]) ->...:
    """Class method to create a ReportingEntity instance from a mapping of entity attributes to values.

    Args:
      entity_dict: Dictionary mapping entity attributes to values from a
        spreadsheet or building configuration.

    Returns:
      An instance of Entity class.
    """
    # TODO(b/228973208) Add support for key errors for keys not in entity_dict.
    reporting_entity_instance = cls(
        code=entity_dict[ENTITY_CODE],
        bc_guid=entity_dict[BC_GUID],
        namespace=entity_dict[NAMESPACE],
        type_name=entity_dict[TYPE_NAME],
        cloud_device_id=entity_dict[CLOUD_DEVICE_ID])
    if ETAG in entity_dict.keys():
      reporting_entity_instance.etag = entity_dict[ETAG]
    reporting_entity_instance.metadata = {
        k[len(METADATA) + 1:]: v
        for k, v in entity_dict.items()
        if k[:len(METADATA)] == METADATA
    }
    return reporting_entity_instance

  @property
  def translations(self) -> List[EntityField]:
    """Returns a list of EntityField instances associated with a reporting entity."""
    return self._translations

  @translations.setter
  def translations(self, new_translations: List[EntityField]) -> None:
    """Sets the EntityField instances for this reporting entity.

    Args:
      new_translations: List of EntityField instances.
    """
    self._translations.clear()
    for translation in new_translations:
      self.AddTranslation(new_translation=translation)

  def AddTranslation(self, new_translation: EntityField) -> None:
    """Adds an EntityField instance to self._translations."""
    if not isinstance(new_translation, EntityField):
      raise TypeError(
          f'{str(new_translation)} must be an EntityField instance.')
    self._translations.append(new_translation)

  def GetSpreadsheetRowMapping(self) -> Dict[str, str]:
    """Returns a dictionary of virtual entity attributes by spreadsheet headers."""
    return {
        ENTITY_CODE: self.code,
        BC_GUID: self.bc_guid,
        IS_REPORTING: True,
        CLOUD_DEVICE_ID: self.cloud_device_id,
        ETAG: self.etag,
        NAMESPACE: self.namespace,
        TYPE_NAME: self.type_name
    }
