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

from typing import Dict


class GuidToEntityMap(object):
  """Container for mapping of Entity instances by entity guids.

  Attributes: guid_to_entity_map(class variable): Mapping of entity guids
  to Entity instances.
  """

  def __init__(self):
    """Init."""
    self._guid_to_entity_map = {}

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
    elif site.guid not in self._guid_to_entity_map:
      self._guid_to_entity_map.update({site.guid: site})
    else:
      raise KeyError(
          f'{site.guid} maps to {self._guid_to_entity_map[site.guid]}')

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
    if entity.bc_guid not in self._guid_to_entity_map:
      self._guid_to_entity_map[entity.bc_guid] = entity
    else:
      raise KeyError(
          f'{entity.bc_guid} maps to {self._guid_to_entity_map[entity.bc_guid]}'
      )

  def GetEntityByGuid(self, guid: str) ->...:
    """Gets an Entity instance mapped to the input guid.

    Args:
      guid: A guid key.

    Returns:
      The Entity instance keyed by guid.

    Raises:
      KeyError: When guid is not a valid key in the map.
    """
    entity = self._guid_to_entity_map.get(guid)
    if entity is None:
      raise KeyError(f'{guid} is not a valid guid in the guid to entity map')
    return entity

  def GetEntityCodeByGuid(self, guid: str) -> str:
    """Gets an entity code mapped by guid.

    Args:
      guid: A guid key.

    Returns:
      A human-readable code from the entity instance mapped by guid.
    """
    return self.GetEntityByGuid(guid).code

  def GetEntityGuidByCode(self, code: str) -> str:
    """Returns entity code mapped by guid in the guid to entity mapping.

    Args:
      code: A non-duplicate entity code.

    Returns:
      The guid associated with an entity code.

    Raises:
      AttributeError: If code is not an entity code contained in
      self._guid_to_entity_map
    """
    guid_by_code = {
        entity.code: guid for guid, entity in self._guid_to_entity_map.items()
    }
    guid = guid_by_code.get(code)
    if not guid:
      raise AttributeError(f'{code} is not a valid entity code.')
    else:
      return guid

  def RemoveEntity(self, guid: str) -> None:
    """Removes a guid and entity pair from guid to entity mapping.

    Args:
      guid: A guid key.

    Returns:
      The removed Entity instance.
    """

    return self._guid_to_entity_map.pop(guid)

  def UpdateEntityMapping(self, guid: str, entity: ...) -> None:
    """Maps existing guid key to new Entity instance.

    Args:
      guid: Guid key already mapped in self._guid_to_entity_map.
      entity: An Entity instance.

    Raises:
      KeyError: When guid is not a valid key in the guid to entity map.
      ValueError: When entity is not an Entity instance.
    """
    if not self._guid_to_entity_map.get(guid):
      raise KeyError(f'{guid} is not a valid guid in the guid to entity map')
    elif not entity:
      raise ValueError(f'{guid} cannot map to object of type None')
    self._guid_to_entity_map.update({guid: entity})

  def GetGuidToEntityMap(self) -> Dict[str, object]:
    """Returns mapping of guids to Entity instances."""
    return self._guid_to_entity_map

  def Clear(self) -> None:
    """Clears global guid mapping.

    Adding for testing purposes.
    """
    self._guid_to_entity_map.clear()
