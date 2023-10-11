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
"""Mapping of guids to Entity instances."""
import uuid
from typing import Dict

GUID_MAP_SHARDS = 64

class GuidToEntityMap(object):
  """Container for mapping of Entity instances by entity guids.

  Attributes: guid_to_entity_map: Mapping of entity guids
  to Entity instances.
  """

  def _submap(self, key: uuid.UUID) -> dict[uuid.UUID, object]:
    shard = key.int % GUID_MAP_SHARDS
    return self._shards[shard]

  def __init__(self):
    """Init."""
    self._shards = [{} for i in range(0, GUID_MAP_SHARDS)]
    self._guid_code_map = None

  def AddSite(self, site: ...) -> None:
    """Adds a site by guid to the mapping.

    Adding a site to the guid to entity instance map is necessary because
    connections may reference a site by guid or code. Sites are handled
    separately than entities in the model_builder module, and therefore need to
    be added to the map separately.

    Args:
      site: Site instance to be added as a value to the map.

    Raises:
      AttributeError: When site guid attribute is None.
      KeyError: When site guid already maps to another site in the model.
    """
    if not site.guid:
      raise AttributeError(f'{site.code}: guid missing')

    shard = self._submap(site.guid)
    if site.guid not in shard:
      shard[site.guid] = site
    else:
      raise KeyError(
          f'{site.guid} maps to {shard[site.guid]}')
    self._guid_code_map = None

  def AddEntity(self, entity: ...) -> None:
    """Adds an entity by guid to the mapping.

    This method does not generate a guid for an entity and will throw an
    exception if the entity's guid attribute is empty.

    Args:
      entity: Entity instance to be added as a value.

    Raises:
      AttributeError: When entity has an empty guid attribute.
      KeyError: When a GUID already maps to another Entity in the model.
    """
    if entity is None:
      raise ValueError('Cannot add None values to the guid to entity map.')
    if not entity.bc_guid:
      raise AttributeError(f'{entity.code}: guid missing')
    shard = self._submap(entity.bc_guid)
    if entity.bc_guid not in shard:
      shard[entity.bc_guid] = entity
      self._guid_code_map = None
    else:
      raise KeyError(
          f'{entity.bc_guid} maps to {shard[entity.bc_guid]}'
      )

  def GetEntityByGuid(self, guid: uuid.UUID) ->...:
    """Gets an Entity instance mapped to the input guid.

    Args:
      guid: A guid key.

    Returns:
      The Entity instance keyed by guid.

    Raises:
      KeyError: When guid is not a valid key in the map.
    """
    entity = self._submap(guid).get(guid)
    if entity is None:
      raise KeyError(f'{guid} is not a valid guid in the guid to entity map')
    return entity

  def GetEntityCodeByGuid(self, guid: uuid.UUID) -> str:
    """Gets an entity code mapped by guid.

    Args:
      guid: A guid key.

    Returns:
      A human-readable code from the entity instance mapped by guid.
    """
    return self.GetEntityByGuid(guid).code

  def _GuidCodeMap(self) -> dict[str, uuid.UUID]:
    if self._guid_code_map is not None:
      return self._guid_code_map
    guid_by_code = {}
    for shard in self._shards:
      for guid, entity in shard.items():
        guid_by_code[entity.code] = guid
    return guid_by_code

  def GetEntityGuidByCode(self, code: str) -> uuid.UUID:
    """Returns entity code mapped by guid in the guid to entity mapping.

    Args:
      code: A non-duplicate entity code.

    Returns:
      The guid associated with an entity code.

    Raises:
      AttributeError: If code is not an entity code contained in
      self._guid_to_entity_map
    """
    guid_by_code = self._GuidCodeMap()
    guid = guid_by_code.get(code)
    if not guid:
      raise AttributeError(f'{code} is not a valid entity code.')
    else:
      return guid

  def RemoveEntity(self, guid: uuid.UUID) -> None:
    """Removes a guid and entity pair from guid to entity mapping.

    Args:
      guid: A guid key.

    Returns:
      The removed Entity instance.
    """

    self._submap(guid).pop(guid)
    self._guid_code_map = None

  def UpdateEntityMapping(self, guid: uuid.UUID, entity: ...) -> None:
    """Maps existing guid key to new Entity instance.

    Args:
      guid: Guid key already mapped in self._guid_to_entity_map.
      entity: An Entity instance.

    Raises:
      KeyError: When guid is not a valid key in the guid to entity map.
      ValueError: When entity is not an Entity instance.
    """
    shard = self._submap(guid)
    if not shard.get(guid):
      raise KeyError(f'{guid} is not a valid guid in the guid to entity map')
    elif not entity:
      raise ValueError(f'{guid} cannot map to object of type None')
    shard[guid] = entity
    self._guid_code_map = None

  def GetGuidToEntityMap(self) -> Dict[uuid.UUID, object]:
    """Returns mapping of guids to Entity instances."""
    full_map = {}
    for shard in self._shards:
      full_map.update(shard)
    return full_map

  def Clear(self) -> None:
    """Clears global guid mapping.

    Adding for testing purposes.
    """
    for shard in self._shards:
      shard.clear()
    self._guid_code_map = None
