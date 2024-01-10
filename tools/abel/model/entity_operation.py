# Copyright 2023 Google LLC
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
"""File containing EntityOperation class.

EntityOperation class is used to model operations performed on entity
instances.
"""

from typing import Dict, List, Optional

# pylint: disable=g-importing-member
from model.constants import CONDITION
from model.constants import CONDITION_TYPE
from model.constants import DATA_VALIDATION
from model.constants import ONE_OF_LIST
from model.constants import SHOW_CUSTOM_UI
from model.constants import STRICT_VALIDATION
from model.constants import STRING_VALUE
from model.constants import USER_ENTERED_VALUE
from model.constants import VALUES
from model.entity import Entity
from model.entity_enumerations import EntityOperationType
from model.entity_enumerations import EntityUpdateMaskAttribute
from model.guid_to_entity_map import GuidToEntityMap


class EntityOperation(object):
  """Class to define operations on an Entity instance.

  Attributes:
    entity: The Entity instance which an operation is being performed on.
    operation: The EntityOperationType instance defining the type of operation
      being performed.
    update_mask: The EntityUpdateMaskAttribute instance defining what elements
      of an entity are being updated. update_mask must be present if operation
      is UPDATE.
  """

  def __init__(
      self,
      entity: Entity,
      operation: EntityOperationType,
      update_mask: Optional[List[EntityUpdateMaskAttribute]] = None,
  ):
    """Init.

    Args:
      entity: The Entity instance which an operation is being performed on.
      operation: The EntityOperationType instance defining the type of operation
        being performed.
      update_mask: [Optional] The EntityUpdateMaskAttribute instance defining
        what elements of an entity are being updated.
    """
    self.entity = entity
    self.operation = operation
    self.update_mask = update_mask
    if self.operation is EntityOperationType.UPDATE:
      assert self.update_mask is not None, (
          'update_mask must be present if operation is UPDATE for entity:'
          f' {self.entity.bc_guid}'
      )

  def __eq__(self, other) -> bool:
    return (
        self.entity == other.entity
        and self.operation == other.operation
        and self.update_mask == other.update_mask
    )

  def __hash__(self) -> int:
    return hash((self.entity, self.operation, self.update_mask))

  # pylint: disable=unused-argument
  def GetSpreadsheetRowMapping(
      self, guid_to_entity_map: GuidToEntityMap
  ) -> Dict[str, str]:
    """Returns map of entity attributes wih operation by spreadsheet headers."""
    entity_row_map = self.entity.GetSpreadsheetRowMapping(guid_to_entity_map)
    operation_row_map = {
        VALUES: [
            {
                USER_ENTERED_VALUE: {STRING_VALUE: self.entity.etag},
                USER_ENTERED_VALUE: {STRING_VALUE: self.operation.name},
                DATA_VALIDATION: {
                    CONDITION: {
                        CONDITION_TYPE: ONE_OF_LIST,
                        VALUES: [
                            {USER_ENTERED_VALUE: operation.value}
                            for operation in EntityOperationType
                        ],
                    },
                    STRICT_VALIDATION: True,
                    SHOW_CUSTOM_UI: True,
                },
            },
        ]
    }
    return_map = entity_row_map.get(VALUES) + operation_row_map.get(VALUES)
    return {VALUES: return_map}
