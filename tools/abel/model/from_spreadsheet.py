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
"""Helper module for model model_builder class."""

from typing import Dict, List, Tuple
import uuid

from model.connection import Connection as ABELConnection
from model.constants import BC_GUID
from model.constants import ENTITY_CODE
from model.constants import IS_REPORTING
from model.constants import MISSING
from model.constants import MISSING_TRUE
from model.constants import RAW_UNIT_PATH
from model.constants import REPORTING_ENTITY_CODE
from model.constants import REPORTING_ENTITY_GUID
from model.constants import SOURCE_ENTITY_CODE
from model.constants import SOURCE_ENTITY_GUID
from model.constants import TARGET_ENTITY_CODE
from model.constants import TARGET_ENTITY_GUID
from model.entity import Entity
from model.entity import ReportingEntity
from model.entity import VirtualEntity
from model.entity_field import DimensionalValueField
from model.entity_field import MissingField
from model.entity_field import MultistateValueField
from model.guid_to_entity_map import GuidToEntityMap
from model.state import State
from validate.field_translation import FieldTranslation


def LoadEntitiesFromSpreadsheet(
    entity_entries: List[Dict[str, str]]
) -> Tuple[GuidToEntityMap, List[Entity]]:
  """Loads a list of entity maps into Entity instances.

  Args:
    entity_entries: A list of Python Dictionaries mapping entity attributes
      names to attribute values from Entity spreadsheet.

  Returns:
    guid_to_entity_map: guid to ABEL entity instance map.
  """
  guid_to_entity_map = GuidToEntityMap()

  for entity_entry in entity_entries:
    if entity_entry[IS_REPORTING].upper() == 'TRUE':
      new_entity = ReportingEntity.FromDict(entity_entry)
    else:
      new_entity = VirtualEntity.FromDict(entity_entry)
    if not new_entity.bc_guid:
      new_entity.bc_guid = str(uuid.uuid4())
    guid_to_entity_map.AddEntity(new_entity)

  return guid_to_entity_map


def LoadFieldsFromSpreadsheet(
    entity_field_entries: List[Dict[str, str]],
    guid_to_entity_map: GuidToEntityMap,
) -> List[FieldTranslation]:
  """Loads list of entity field maps into FieldTranslation instances.

  Once the entity field mapping is loaded into an FieldTranslation instance,
  it
  is then added to the ABEL internal model.

  Args:
    entity_field_entries: A list of python dictionaries mapping entity field
      attribute names to values from Fields spreadsheet.
    guid_to_entity_map: Map keyed by guid and values are either Reporting or
      Virtual Entity instances.

  Returns:
    fields: list of field translation instances.
  """
  fields = []
  for entity_field_entry in entity_field_entries:
    entity_field_entry[BC_GUID] = guid_to_entity_map.GetEntityGuidByCode(
        entity_field_entry[ENTITY_CODE]
    )
    if entity_field_entry[REPORTING_ENTITY_CODE]:
      entity_field_entry[REPORTING_ENTITY_GUID] = (
          guid_to_entity_map.GetEntityGuidByCode(
              entity_field_entry[REPORTING_ENTITY_CODE]
          )
      )
    if entity_field_entry[MISSING].upper() == MISSING_TRUE:
      fields.append(MissingField.FromDict(entity_field_entry))
    elif entity_field_entry[RAW_UNIT_PATH]:
      fields.append(DimensionalValueField.FromDict(entity_field_entry))
    else:
      fields.append(MultistateValueField.FromDict(entity_field_entry))

  return fields


def LoadStatesFromSpreadsheet(
    state_entries: List[Dict[str, str]], guid_to_entity_map: GuidToEntityMap
) -> List[State]:
  """Loads a list of state dictionary mappings into State instances.

  Args:
    state_entries: A list of python dictionaries mapping state attribute names
      to values from States spreadsheet.
    guid_to_entity_map: Map keyed by guid and values are either Reporting or
      Virtual Entity instances.

  Returns:
    states: List of State instances
  """
  states = []

  for state_entry in state_entries:
    state_entry[BC_GUID] = guid_to_entity_map.GetEntityGuidByCode(
        state_entry[REPORTING_ENTITY_CODE]
    )
    states.append(State.FromDict(state_entry))

  return states


def LoadConnectionsFromSpreadsheet(
    connection_entries: List[Dict[str, str]],
    guid_to_entity_map: GuidToEntityMap,
) -> List[ABELConnection]:
  """Loads a list of connection dictionary mappings into Connection instances.

  Args:
    connection_entries: A list of python dictionaries mapping connection
      attribute names to values from the Connections spreadsheet.
    guid_to_entity_map: Map keyed by guid and values are either Reporting or
      Virtual Entity instances.

  Returns:
    connections: List of ABELConnection instances
  """
  connections = []

  for connection_entry in connection_entries:
    connection_entry[SOURCE_ENTITY_GUID] = (
        guid_to_entity_map.GetEntityGuidByCode(
            connection_entry[SOURCE_ENTITY_CODE]
        )
    )
    connection_entry[TARGET_ENTITY_GUID] = (
        guid_to_entity_map.GetEntityGuidByCode(
            connection_entry[TARGET_ENTITY_CODE]
        )
    )
    connections.append(ABELConnection.FromDict(connection_entry))

  return connections
