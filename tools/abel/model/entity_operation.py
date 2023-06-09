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
from typing import List, Optional

from model.entity import Entity
from model.entity_enumerations import EntityOperationType
from model.entity_enumerations import EntityUpdateMaskAttribute


class EntityOperation(object):
  """Class to define operations on an Entity instance.

  Attributes:
    entity: The Entity instance which an operation is being performed on.
    operation_type: The EntityOperationType instance defining the type of
      operation being performed.
    update_mask: An optional list of EntityUpdateMaskAttribute instances 
      defining what elements of an entity are being updated. update_mask must
      be present if operation type is UPDATE.
  """

  def __init__(
      self,
      entity: Entity,
      operation_type: EntityOperationType,
      update_mask: Optional[List[EntityUpdateMaskAttribute]] = None,
  ):
    """Init.

    Args:
      entity: The Entity instance which an operation is being performed on.
      operation_type: The EntityOperationType instance defining the type of
        operation being performed.
      update_mask: [Optional] An optional list of EntityUpdateMaskAttribute
        instances defining what elements of an entity are being updated.
    """
    self.entity = entity
    self.operation_type = operation_type
    self.update_mask = update_mask
    if self.operation is EntityOperationType.UPDATE:
      assert self.update_mask is not None, (
          'update_mask must be present if operation is UPDATE for entity:'
          f' {self.entity.bc_guid}'
      )
