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

from typing import Dict, Optional, List

from model.entity_field import EntityField
from model.entity_type import EntityType


class Entity(object):
  """Class to represent entities within the concrete model.

  Attributes:
    name: Human readable name of an entity.
    guid: UUID4 value for an entity.
    cloud_device_id: IoT application device id.
    type_name: Instance of EntityType class.
    fields: Mapping of standard field names to EntityField instances.
    is_reporting: if an entity maps 1:1 to a reporting device, it is a reporting
      entity.
    metadata: Contextual metadata coming from a physical device. i.e.
      {
        location: '/Sif-Solo/Site 1 - Sif/Charleston Road North/B13 - 1875
          Charleston/Roof',
        control_programs: ['Trane AC-1', '1875 Charleston'],
        device_id: 'DEV:2809009'
      }
  """

  def __init__(self,
               name: str,
               cloud_device_id: Optional[str],
               type_name: EntityType,
               fields: List[EntityField],
               is_reporting: bool,
               guid: Optional[str] = None,
               metadata: Optional[Dict[str, str]] = None):
    """Init.

    Args:
      name: the entity's name.
      cloud_device_id: Device id iot core or any iot application.
      type_name: DBO entity type stored in EntityType instance.
      fields: List of standard field names.
      is_reporting: if an entity maps 1:1 to a reporting device, it is a
        reporting entity.
      guid: [Optional] Universally Unique identification code for an entity.
      metadata: Contextual metadata about an entity.
    """

    self.name = name
    self._guid = guid
    self.cloud_device_id = cloud_device_id
    self.type_name = type_name
    self._fields = fields
    self.is_reporting = is_reporting
    self.metadata = metadata

  @classmethod
  def FromDict(cls, entity_dict: Dict[str, object]):
    """class method to create an instance of Entity from mapping of entity attributes to values.

    Args:
      entity_dict: dictionary mapping field attributes to values from a
        loadsheet or building configuration.

    Returns:
      An instance of Entity class.
    """

  @property
  def fields(self) -> Dict[str, EntityField]:
    """Returns a mapping of standard field names to EntityField instances associated with self."""
    return self._fields

  @fields.setter
  def fields(self, new_fields: Dict[str, EntityField]) -> None:
    """Validates that each value of new_fields is an instance of EntityField class and sets.

    Arguments:
      new_fields: A mapping of standard field names to EntityField instances.
    """

  @property
  def guid(self) -> str:
    """Returns the GUID associated with self."""
    return self._guid

  @guid.setter
  def guid(self, guid: Optional[str] = None) -> None:
    """If guid argument is none, generate a new guid for set or just set if none.

    Args:
      guid: [Optional] A UUID string.
    """

