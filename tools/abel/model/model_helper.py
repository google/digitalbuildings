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
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either exintess or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Module to help perform operations on an ABEL model instance or instances."""

from typing import List

from model import entity as entity_lib
from model import entity_enumerations
from model import entity_field as ef
from model import entity_operation
from model import model_builder as mb
from validate import field_translation as ft


def _GetLinkScore(
    current_links: List[ft.FieldTranslation],
    updated_links: List[ft.FieldTranslation],
) -> float:
  """Function to help determine how similar two virtual entities' links are.

  Args:
    current_links: A list of FieldTranslation instances which are links for a
      current entity.
    updated_links: An entity instance from an updated building config. This
      updated entity is the same as the entity which contains current_links.

  Returns:
    A score within range [0, 1] modeling the similarity between two lists of
    linked field translations.
  """
  current_link_set = set(current_links)
  updated_link_set = set(updated_links)
  link_score = len(updated_link_set.intersection(current_link_set)) / len(
      current_link_set
  )
  return link_score


def DetermineReportingEntityUpdateMask(
    current_model, updated_model, current_entity, updated_entity
):
  """Returns a list with EntityUpdateMaskAttribute for a reporting entity.

  Args:
    current_model: Model instance parsed from a building config exported from DB
      API.
    updated_model: Model instance parsed from an updated building config.
    current_entity: An Entity instance from a building config exported from DB
      API.
    updated_entity: An Entity instance from an updated building config.
  """
  update_mask = []
  if updated_entity.code != current_entity.code:
    update_mask.append(entity_enumerations.EntityUpdateMaskAttribute.CODE)
  if updated_entity.type_name != current_entity.type_name:
    update_mask.append(entity_enumerations.EntityUpdateMaskAttribute.TYPE)
  if set(updated_entity.connections).difference(
      set(current_entity.connections)
  ):
    update_mask.append(
        entity_enumerations.EntityUpdateMaskAttribute.CONNECTIONS
    )
  if set(updated_entity.translations).intersection(
      set(current_entity.translations)
  ) != set(current_entity.translations):
    update_mask.append(
        entity_enumerations.EntityUpdateMaskAttribute.TRANSLATION
    )
  else:
    for updated_field in updated_entity.translations:
      curent_translations = {
          field.std_field_name: field for field in current_entity.translations
      }
      current_field = curent_translations.get(updated_field.std_field_name)
      if isinstance(current_field, ef.DimensionalValueField) and isinstance(
          updated_field, ef.DimensionalValueField
      ):
        # Unit mapping could change
        if current_field.units != updated_field.units:
          update_mask.append(
              entity_enumerations.EntityUpdateMaskAttribute.TRANSLATION
          )
      elif isinstance(current_field, ef.MultistateValueField) and isinstance(
          updated_field, ef.MultistateValueField
      ):
        # state mappings could change
        current_states = current_model.GetStates(
            current_field.reporting_entity_guid, current_field.std_field_name
        )
        updated_states = updated_model.GetStates(
            updated_field.reporting_entity_guid, updated_field.std_field_name
        )

        if sorted(
            current_states, key=lambda state: state.reporting_entity_guid
        ) != sorted(
            updated_states, key=lambda state: state.reporting_entity_guid
        ):
          update_mask.append(
              entity_enumerations.EntityUpdateMaskAttribute.TRANSLATION
          )

      elif isinstance(current_field, ef.MissingField) and not isinstance(
          updated_field, ef.MissingField
      ):
        # field was missing and now is not missing
        update_mask.append(
            entity_enumerations.EntityUpdateMaskAttribute.TRANSLATION
        )
      elif not isinstance(current_field, ef.MissingField) and isinstance(
          updated_field, ef.MissingField
      ):
        # field was being reported but is now missing
        update_mask.append(
            entity_enumerations.EntityUpdateMaskAttribute.TRANSLATION
        )
  return update_mask


def DetermineVirtualEntityUpdateMask(current_entity, updated_entity):
  """Returns a list with EntityUpdateMaskAttribute for a virtual entity.

  Args:
    current_entity: An Entity instance from a building config exported from DB
      API.
    updated_entity: An Entity instance from an updated building config.
  """
  update_mask = []
  if updated_entity.code != current_entity.code:
    update_mask.append(entity_enumerations.EntityUpdateMaskAttribute.CODE)
  if updated_entity.type_name != current_entity.type_name:
    update_mask.append(entity_enumerations.EntityUpdateMaskAttribute.TYPE)
  if set(updated_entity.connections).difference(
      set(current_entity.connections)
  ):
    update_mask.append(
        entity_enumerations.EntityUpdateMaskAttribute.CONNECTIONS
    )
  # Facilities entities don't have links but are virtual so do the following
  # check to ensure a division by zero error is not thrown.
  if (
      current_entity.links
      and updated_entity.links
      and (
          _GetLinkScore(
              current_links=current_entity.links,
              updated_links=updated_entity.links,
          )
          < 0.9
      )
  ):
    update_mask.append(entity_enumerations.EntityUpdateMaskAttribute.LINKS)
  return update_mask


def DetermineEntityOperations(
    current_model: mb.Model, updated_model: mb.Model
) -> List[entity_operation.EntityOperation]:
  """Function to determine entity operations between two model instances.

  Args:
    current_model: Model instance parsed from a building config exported from DB
      API.
    updated_model: Model instance parsed from an updated building config.

  Returns:
    A list of Entity operation instances containing the updated entity and the
    operation which is being performed on it.
  """
  operations = []
  for import_entity in updated_model.entities:
    if import_entity.bc_guid not in set(
        entity.bc_guid for entity in current_model.entities
    ):
      operations.append(
          entity_operation.EntityOperation(
              import_entity,
              operation=entity_enumerations.EntityOperationType.ADD,
          )
      )
      continue

    export_entity = current_model.GetEntity(import_entity.bc_guid)
    if isinstance(import_entity, entity_lib.VirtualEntity) and isinstance(
        export_entity, entity_lib.VirtualEntity
    ):
      update_mask = DetermineVirtualEntityUpdateMask(
          export_entity, import_entity
      )
    elif isinstance(import_entity, entity_lib.ReportingEntity) and isinstance(
        export_entity, entity_lib.ReportingEntity
    ):
      update_mask = DetermineReportingEntityUpdateMask(
          current_model, updated_model, export_entity, import_entity
      )
    else:
      raise TypeError(
          f'GUID: {import_entity.bc_guid} Maps to both a reporting entity and'
          ' a virtual entity.'
      )
    if update_mask:
      operations.append(
          entity_operation.EntityOperation(
              import_entity,
              operation=entity_enumerations.EntityOperationType.UPDATE,
              update_mask=update_mask,
          )
      )

  return operations


def ReconcileOperations(
    model_operations: List[entity_operation.EntityOperation],
    generated_operations: List[entity_operation.EntityOperation],
) -> List[entity_operation.EntityOperation]:
  """Function to reconcile two lists of entity operations.

  Two lists of operations will be generated for a set of entities. One is parsed
  from a spreadsheet/building config. The other is generated by comparing two
  models. Two operation types that cannot be generated computationally are
  DELETE and EXPORT. These two types will come from either a spreadsheet or
  building config.

  All operations take precedence over EXPORT and DELETE takes precedence over
  all operations.

  Args:
    model_operations: List of EntityOperation instances manually imported from a
      spreadsheet or building config.
    generated_operations: List of Entityoperation instances generated
      automatically from comparing two model instances.

  Returns:
     A list of EntityOperation instances.
  """
  return_operations = []
  generated_operation_map = {
      operation.entity.bc_guid: operation for operation in generated_operations
  }
  for model_operation in model_operations:
    generated_operation = generated_operation_map.get(
        model_operation.entity.bc_guid
    )
    if not generated_operation:
      return_operations.append(model_operation)
    elif (
        model_operation.operation
        == entity_enumerations.EntityOperationType.DELETE
    ):
      return_operations.append(model_operation)
    elif (
        model_operation.operation
        == entity_enumerations.EntityOperationType.EXPORT
        and generated_operation.operation
        != entity_enumerations.EntityOperationType.EXPORT
    ):
      return_operations.append(generated_operation)
    else:
      return_operations.append(generated_operation)
  return return_operations


def Split(
    model: mb.Model,
    operations: List[entity_operation.EntityOperation],
    namespace: entity_enumerations.EntityNamespace,
) -> mb.Model:
  """Method to split a model on namespace.

  A model is split on a namesapce such that the resulting subset contains only
  entities in the desired namesapce AND dependencies for those entities. e.g.
  facilities entities like floors and rooms.

  Args:
    model: A Model instance to be split.
    operations: List of EntityOperation instances for a Model instance.
    namespace: An EntityNamespace enumeration.

  Returns:
    A Model instance containing the subset of entities.
  """

  def GetConnectionDependencies(entity, dependencies, split_entities):
    """Helper method to recursively get connection dependencies.

    Args:
      entity: Entity instance.
      dependencies: ...
      split_entities: Entities who already have been visited.

    Returns:
      A list of entities connected to entity.
    """
    split_entities.append(entity)
    if not entity.connections and entity not in split_entities:
      dependencies.append(entity)
      return dependencies
    else:
      for connection in entity.connections:
        entity = model.GetEntity(connection.source_entity_guid)
        if entity not in split_entities:
          dependencies += GetConnectionDependencies(
              entity, dependencies, split_entities
          )
          dependencies.append(entity)
      return dependencies

  def GetLinkDependencies(entity, all_entities) -> List[entity_lib.Entity]:
    """Helper method to iteratively get link dependencies.

    Args:
      entity: An Entity instance.
      all_entities: List of Entity Instances which are already dependencies for
        other entities.

    Returns:
      Dependencies for entity.
    """
    dependencies = []
    if isinstance(entity, entity_lib.VirtualEntity) and entity.links:
      for link in entity.links:
        entity = model.GetEntity(link.reporting_entity_guid)
        if entity not in all_entities and entity not in dependencies:
          dependencies.append(entity)
    return dependencies

  all_entities = []
  for e in [
      operation.entity
      for operation in operations
      if operation.entity.namespace == namespace
  ]:
    all_entities += GetConnectionDependencies(e, [], all_entities)
    all_entities += GetLinkDependencies(e, all_entities)
  split_operations = [
      operation for operation in operations if operation.entity in all_entities
  ]
  return (
      mb.Model.Builder.FromEntities(model.site, all_entities),
      split_operations,
  )
