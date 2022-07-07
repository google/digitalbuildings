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
"""Global mapping of guids to Entity instances."""


class GuidToEntityMap(object):
  """Class to store and manage accessibility to a global mapping of entity guids to Entity instances.

  Attributes: guid_to_entity_map(class variable): Global mapping of entity guids
  to Entity instances.
  """
  _guid_to_entity_map = {}

  def __init__(self):
    """Init."""

  def AddSite(self, site: ...) -> None:
    """Adds a site by guid to the global map.

    Adding a site to the global guid to entity instance map is necessary because
    connections may reference a site by guid or code. Sites are handled
    separately than entities in the model_builder module, and therefore need to
    be added to the global map separately.

    Args:
      site: Site instance to be added as a value to the global map.

    Raises:
      AttributeError: When site guid attribute is None.
      KeyError: When site guid already maps to another site in the model.
    """
    if not site.guid:
      raise AttributeError(f'{site.code}: guid missing')
    if site.guid not in self._guid_to_entity_map.keys():
      self._guid_to_entity_map[site.guid] = site
    else:
      raise KeyError(
          f'{site.guid} maps to {self._guid_to_entity_map[site.guid]}')

  def AddEntity(self, entity: ...) -> None:
    """Adds an entity by guid to the global map.

    This method does not generate a guid for an entity and will throw an
    exception if the entity's guid attribute is empty.

    Args:
      entity: Entity instance to be added as a value.

    Raises:
      AttributeError: When entity has an empty guid attribute.
      KeyError: When a GUID already maps to another Entity in the model.
    """
    if not entity.bc_guid:
      raise AttributeError(f'{entity.code}: guid missing')
    if entity.bc_guid not in self._guid_to_entity_map.keys():
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
      KeyError: When guid is not a valid key in the global map.
    """
    try:
      return self._guid_to_entity_map.get(guid)
    except KeyError:
      raise KeyError(f'{guid} is not a valid guid key.') from None

  def GetEntityCodeByGuid(self, guid: str) -> str:
    """Gets an entity code mapped by guid.

    Args:
      guid: A guid key.

    Returns:
      A human-readable code from the entity instance mapped by guid.

    Raises:
      KeyError: When guid is not a valid key in the global map.
    """
    try:
      return self._guid_to_entity_map.get(guid).code
    except KeyError:
      raise KeyError(f'{guid} is not a valid guid key.') from None

  def GetEntityGuidByCode(self, code: str) -> str:
    """Returns an entity code mapped to by a guid in the global guid to entity mapping.

    Args:
      code: A non-duplicate entity code.

    Returns:
      The guid associated with an entity code.
    """
    guid_by_code = {
        entity.code: guid for guid, entity in self._guid_to_entity_map.items()
    }
    return guid_by_code[code]

  def RemoveEntity(self, guid: str) -> None:
    """Removes a guid to Entity mapping.

    Args:
      guid: A guid key.
    """
    self._guid_to_entity_map.pop(guid)

  def UpdateEntityMapping(self, guid: str, entity: ...) -> None:
    """Maps existing guid key to new Entity instance.

    Args:
      guid: Guid key already mapped in self._guid_to_entity_map.
      entity: An Entity instance.

    Raises:
      KeyError: When guid is not a valid key in the global map.
    """
    try:
      self._guid_to_entity_map[guid] = entity
    except KeyError:
      raise KeyError(f'{guid} is not a valid guid key.') from None

  def Clear(self) -> None:
    """Clears global guid mapping.

    Adding for testing purposes.
    """
    self._guid_to_entity_map.clear()
