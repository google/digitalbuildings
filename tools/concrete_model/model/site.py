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
"""Module for a site, and all relevant metadata for UDMI site model."""

from typing import Dict, List, Optional

from model.constants import BC_GUID
from model.constants import ENTITY_CODE
from model.constants import SITE_TYPE_NAME
from model.entity import Entity


# TODO(b/218318362) Be able to query an entity belonging to another site.
class Site(object):
  """Data container for a Building Configuration site.

  Within the Concrete Model, A site acts as the root node. While a site is an
  entity, it is aware of all of the nodes under itself since a building contains
  all of its entities.

  Attributes:
    code: A site's human-readable code.
    type_name: A site's standardized DBO entity type id.
    guid: A globally unique identifier(uuid4) for the site.
    entities: A list of GUIDs for entities cointained in a site.
  """

  def __init__(self,
               code: str,
               guid: Optional[str] = None) -> None:
    """Init.

    Args:
      code: Site name.
      guid: UUID4 value for site.
    """
    self.code = code
    self.type_name = SITE_TYPE_NAME
    self._entities = []
    self.guid = guid

  def __str__(self):
    return f'{self.code}'

  @classmethod
  def FromDict(cls, site_dict: Dict[str, object]) ->...:
    site_instance = cls(
        code=site_dict[ENTITY_CODE],
        guid=site_dict[BC_GUID])
    return site_instance

  @property
  def entities(self) -> List[str]:
    """Returns a list of entity guids contained in a site."""
    return self._entities

  @entities.setter
  def entities(self, new_entities: List[Entity]) -> None:
    """Sets the list of entities guids for this site.

    Args:
      new_entities: A list of Entity GUIDs.
    """
    for entity in new_entities:
      self.AddEntity(entity=entity)

  def AddEntity(self, entity: Entity) -> None:
    """Appends an entity GUID to site._entities.

    Args:
      entity: An Entity instance whose guid will be added to self._entities.
    """
    self._entities.append(entity.bc_guid)
