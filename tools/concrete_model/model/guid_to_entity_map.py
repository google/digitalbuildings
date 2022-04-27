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

from model.entity import Entity


class GuidToEntityMap(object):
  """Class to store and manage accessibility to a global mapping of entity guids to Entity instances.

  Attributes:
    guid_to_entity_map(class variable): Global mapping of entity guids to Entity
      instances.
  """
  _guid_to_entity_map = {}

  def __init__(self):
    """Init."""

  def AddEntity(self, entity: Entity) -> None:
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
    mapped_entity = self._guid_to_entity_map[entity.bc_guid]
    if not mapped_entity:
      self._guid_to_entity_map[entity.bc_guid] = entity
    else:
      raise KeyError(f'{entity.bc_guid} already maps to {mapped_entity}')

  def GetEntityByGuid(self, guid: str) ->...:
    """Gets and Entity instance mapped to the input guid.

    Args:
      guid: A guid key.

    Returns:
      The Entity instance keyed by guid.
    """
    try:
      return self._guid_to_entity_map.get(guid)
    except KeyError:
      raise KeyError(f'{guid} is not a valid guid key!') from None

  def RemoveEntity(self, guid: str) ->...:
    """Removes a guid to Entity mapping.

    Args:
      guid: A guid key.

    Returns:
      The removed Entity instance.
    """
    self._guid_to_entity_map.pop(guid)

  def UpdateEntityMapping(self, guid: str, entity: ...) -> None:
    """Maps existing guid key to new Entity instance.

    Args:
      guid: Guid key already mapped in self._guid_to_entity_map.
      entity: An Entity instance.
    """
    try:
      self._guid_to_entity_map[guid] = entity
    except KeyError:
      raise KeyError(f'{guid} is not a valid guid key!') from None
