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
