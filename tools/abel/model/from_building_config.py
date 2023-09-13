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
"""Helper module for model_builder class."""

from typing import List, Tuple

# pylint: disable=g-importing-member
from model.connection import Connection as ABELConnection
from model.constants import CONNECTION_TYPE
from model.constants import SOURCE_ENTITY_GUID
from model.constants import TARGET_ENTITY_GUID
from model.entity import Entity
from model.entity import ReportingEntity
from model.entity import VirtualEntity
from model.entity_enumerations import EntityOperationType
from model.entity_enumerations import EntityUpdateMaskAttribute
from model.entity_field import DimensionalValueField
from model.entity_field import MissingField
from model.entity_field import MultistateValueField
from model.entity_operation import EntityOperation
from model.state import State
from model.units import Units
from validate.connection import Connection as IVConnection
from validate.entity_instance import EntityInstance
from validate.field_translation import DimensionalValue
from validate.field_translation import FieldTranslation
from validate.field_translation import MultiStateValue
from validate.field_translation import UndefinedField as IVUndefinedField
from validate.link import Link


def EntityInstanceToEntity(
    entity_instance: EntityInstance,
) -> Tuple[Entity, List[FieldTranslation], List[State], List[ABELConnection]]:
  """Maps EntityInstance attributes to an ABEL Entity instance.

  Args:
    entity_instance: An Instance Validator EntityInstance.

  Returns:
    entity: List of ABEL entity instances
    fields: List of ABEL field instances
    states: List of ABEL state instances
    connections: List of ABEL connection instances
  """
  fields = []
  states = []
  connections = []
  entity_operation = None

  if not entity_instance.cloud_device_id:
    entity = VirtualEntity(
        code=entity_instance.code,
        namespace=entity_instance.namespace,
        etag=entity_instance.etag,
        type_name=entity_instance.type_name,
        bc_guid=entity_instance.guid,
    )
  else:
    entity = ReportingEntity(
        code=entity_instance.code,
        namespace=entity_instance.namespace,
        cloud_device_id=entity_instance.cloud_device_id,
        etag=entity_instance.etag,
        type_name=entity_instance.type_name,
        bc_guid=entity_instance.guid,
    )
    if entity_instance.translation:
      for field in entity_instance.translation.values():
        if isinstance(field, DimensionalValue):
          fields.append(
              _DimensionalValueToDimensionalValueField(
                  reporting_entity_guid=entity_instance.guid, field=field
              )
          )
        elif isinstance(field, MultiStateValue):
          this_field, this_states = _MultistateValueToMultistateValueField(
              reporting_entity_guid=entity_instance.guid, field=field
          )
          fields.append(this_field)
          states.extend(this_states)
        elif isinstance(field, IVUndefinedField):
          fields.append(
              _UndefinedFieldToUndefinedField(
                  reporting_entity_guid=entity_instance.guid, field=field
              )
          )

  if entity_instance.connections:
    for connection in entity_instance.connections:
      connections.append(
          _TranslateConnectionsToABEL(entity_instance.guid, connection)
      )
  if entity_instance.operation:
    operation = EntityOperationType(entity_instance.operation.value)
    entity_operation = EntityOperation(operation=operation, entity=entity)
    if entity_instance.update_mask:
      entity_operation.update_mask = [
          EntityUpdateMaskAttribute(mask_element)
          for mask_element in entity_instance.update_mask
      ]

  return entity, fields, states, connections, entity_operation


def _DimensionalValueToDimensionalValueField(
    reporting_entity_guid: str, field: DimensionalValue
) -> DimensionalValueField:
  """Maps DimensionalValue attributes to ABEL DimensionalValueField instance.

  Args:
    reporting_entity_guid: Parent reporting entity guid.
    field: An Instance Validator DimensionalValue instance.

  Returns:
    DimensionalValueField instance with units populated
  """
  dimensional_value_field = DimensionalValueField(
      std_field_name=field.std_field_name,
      raw_field_name=field.raw_field_name,
      entity_guid=reporting_entity_guid,
      reporting_entity_guid=reporting_entity_guid,
  )

  dimensional_value_field.units = Units(
      raw_unit_path=field.unit_field_name,
      standard_to_raw_unit_map=field.unit_mapping,
  )

  return dimensional_value_field


def _MultistateValueToMultistateValueField(
    reporting_entity_guid: str, field: MultiStateValue
) -> Tuple[MultistateValueField, List[State]]:
  """Maps MultiStateValue attributes to ABEL MultistateValueField instances.

  Args:
    reporting_entity_guid: Parent reporting entity guid.
    field: An Instance Validator MultiStateValue instance.

  Returns:
    MultistateValueField instance and list of State instances
  """
  to_return_field = MultistateValueField(
      std_field_name=field.std_field_name,
      raw_field_name=field.raw_field_name,
      entity_guid=reporting_entity_guid,
      reporting_entity_guid=reporting_entity_guid,
  )
  to_return_states = _TranslateStatesToABEL(
      entity_guid=reporting_entity_guid, field=field
  )

  return to_return_field, to_return_states


def _TranslateStatesToABEL(
    entity_guid: str, field: MultiStateValue
) -> List[State]:
  """Maps MultiStateValue state attributes to ABEL State instance.

  Args:
    entity_guid: Parent entity guid.
    field: An Instance Validator MultistateValue instance.  Returns List of
      State instances

  Returns:
    List of ABEL state instances
  """

  states = []
  for std_state_value, raw_state_value in field.states.items():
    states.append(
        State(
            std_field_name=field.std_field_name,
            reporting_entity_guid=entity_guid,
            standard_state=std_state_value,
            raw_state=raw_state_value,
        )
    )
  return states


def _UndefinedFieldToUndefinedField(
    reporting_entity_guid: str, field: IVUndefinedField
) -> MissingField:
  """Maps IV UndefinedField attributes to ABEL UndefinedField instances.

  Args:
    reporting_entity_guid: Parent reporting entity guid.
    field: An Instance Validator UndefinedField instance.

  Returns:
    MissingField instance
  """
  return MissingField(
      std_field_name=field.std_field_name,
      entity_guid=reporting_entity_guid,
      reporting_entity_guid=reporting_entity_guid,
  )


def _TranslateConnectionsToABEL(
    entity_guid: str, connection: IVConnection
) -> ABELConnection:
  """Maps Instance Validator Connection attributes to ABEL Connection object.

  Args:
    entity_guid: Parent entity guid.
    connection: Instance Validator Connection instance.

  Returns:
    ABELConnection instance
  """
  return ABELConnection.FromDict({
      SOURCE_ENTITY_GUID: connection.source,
      CONNECTION_TYPE: connection.ctype,
      TARGET_ENTITY_GUID: entity_guid,
  })


def AddReportingEntitiesFromEntityInstance(
    entity_instance: EntityInstance, fields: List[FieldTranslation]
) -> None:
  """Adds link attributes to FieldTranslation children for all virtual entities.

  Determines if an entity has links, and calls this method to fill in
  entity_guid, reporting_entity_field_name, and std_field_name for a field.

  Args:
    entity_instance: An EntityInstance instance from Instance Validator
      deserialization.
    fields: List of all building config FieldTranslations
  """
  if entity_instance.links:
    for link in entity_instance.links:
      _AddReportingEntitiesFromLinks(
          link=link, entity_instance=entity_instance, fields=fields
      )


def _AddReportingEntitiesFromLinks(
    link: Link, entity_instance: EntityInstance, fields: List[FieldTranslation]
) -> None:
  """Add reporting entity code, guid and field name to a FieldTranslation child.

  For each link, iterate through this model's fields and if the links source
  guid equals the field's reporting_entity_guid and the field's standard field
  name is the link's mapped field, then add this virtual entity as the
  entity_guid for a field.

  Args:
    link: An Instance Validator Link instance.
    entity_instance: An EntityInstance from Instance Validator deserialization.
    fields: List of all building config fields
  """
  for source_field, target_field in link.field_map.items():
    for field in fields:
      if (
          link.source == field.reporting_entity_guid
          and field.std_field_name == target_field
      ):
        field.entity_guid = entity_instance.guid
        field.reporting_entity_field_name = target_field
        field.std_field_name = source_field
