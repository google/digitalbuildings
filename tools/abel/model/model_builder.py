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
"""Helper module for concrete model construction."""

from typing import Dict, List
import uuid

from model.connection import Connection as ABELConnection
from model.constants import ALL_CONNECTION_HEADERS
from model.constants import ALL_ENTITY_HEADERS
from model.constants import ALL_FIELD_HEADERS
from model.constants import ALL_SITE_HEADERS
from model.constants import ALL_STATE_HEADERS
from model.constants import BC_GUID
from model.constants import CONNECTION_TYPE
from model.constants import CONNECTIONS
from model.constants import ENTITIES
from model.constants import ENTITY_CODE
from model.constants import ENTITY_FIELDS
from model.constants import IS_REPORTING
from model.constants import REPORTING_ENTITY_CODE
from model.constants import REPORTING_ENTITY_GUID
from model.constants import SITES
from model.constants import SOURCE_ENTITY_CODE
from model.constants import SOURCE_ENTITY_GUID
from model.constants import STATES
from model.constants import TARGET_ENTITY_CODE
from model.constants import TARGET_ENTITY_GUID
from model.entity import Entity
from model.entity import ReportingEntity
from model.entity import VirtualEntity
from model.entity_field import EntityField
from model.guid_to_entity_map import GuidToEntityMap
from model.site import Site
from model.state import State
from model.units import Units
from validate.connection import Connection as IVConnection
from validate.entity_instance import EntityInstance
from validate.field_translation import DimensionalValue
from validate.field_translation import MultiStateValue
from validate.link import Link


class ModelBuilder(object):
  """Class to build an ABEL Concrete Model graph.

  ABEL parses a concrete model spreadsheet into a set of standard Python
  dictionaries mapping spreadsheet headers to values. This module takes in those
  dictionaries and parses their data into ABEL model elements.

  Attributes:
    fields: A list of EntityField instances.
    entities: A list Entity instances.
    site: A list of Site instances.
    states: A list of State instances.
    connections: A list of Connection instances.
    guid_to_entity_map: A global mapping of GUIDs to Entity instances.
  """

  def __init__(self, site: Site):
    self.site = site
    self.fields: List[EntityField] = []
    self.entities: List[Entity] = []
    self.states: List[State] = []
    self.connections: List[ABELConnection] = []
    self.guid_to_entity_map = GuidToEntityMap()

  @classmethod
  def FromSpreadsheet(cls, spreadsheet_dict: Dict[str, object]) ->...:
    """Converts a Spreadsheet instance into fields, entities, and sites.

    Args:
      spreadsheet_dict: A mapping of spreadsheet names to Lists of dictionaries
        representing cells in a row keyed by column headers.

    Returns:
      An instance of ModelBuilder.
    """
    # Currently only supports one site per ABEL instance.
    site = Site.FromDict(spreadsheet_dict[SITES][0])
    model_builder = cls(site)
    model_builder.guid_to_entity_map.AddSite(site)
    model_builder.LoadEntities(spreadsheet_dict[ENTITIES])
    model_builder.LoadEntityFields(spreadsheet_dict[ENTITY_FIELDS])
    model_builder.LoadStates(spreadsheet_dict[STATES])
    model_builder.LoadConnections(spreadsheet_dict[CONNECTIONS])
    return model_builder

  @classmethod
  def FromBuildingConfig(cls, site: Site,
                         building_config_dict: Dict[str, EntityInstance]) ->...:
    """Converts a yaml document into fields, entities, and sites.

    Iterates through the dictionary returned by Instance validator
    deserialization. Iterates a second time and fills Reporting entity code,
    guid and field name values for a field.

    Args:
      site: A site instance stripped from a building config.
      building_config_dict: A dictionary mapping of Instance Validator
        EntityInstance objects by guid.

    Returns:
      A ModelBuilder instance.
    """
    model_builder = cls(site)
    model_builder.guid_to_entity_map.AddSite(site)
    for entity_instance in building_config_dict.values():
      model_builder.EntityInstanceToEntity(entity_instance)

    for entity_instance in building_config_dict.values():
      model_builder.AddReportingEntitiesFromEntityInstance(entity_instance)
    return model_builder

  # TODO(b/234630862) Refactor Build method for readability.
  def Build(self) -> None:
    """Connects all entities to a site, fields to entities, and entities to entities based on attributes."""
    self.site.entities = self.entities
    for guid in self.site.entities:
      entity = self.guid_to_entity_map.GetEntityByGuid(guid)
      for connection in self.connections:
        if connection.target_entity_guid == guid:
          entity.AddConnection(connection)
      for field in self.fields:
        for state in self.states:
          if state.standard_field_name == field.standard_field_name and state.entity_guid == guid:
            field.AddState(state)
        if isinstance(entity, VirtualEntity):
          if field.entity_guid == guid:
            entity.AddLink(field)
        elif isinstance(entity, ReportingEntity):
          if field.entity_guid == guid or field.reporting_entity_guid == guid:
            entity.AddTranslation(field)

  def LoadEntities(self, entity_entries: List[Dict[str, str]]) -> None:
    """Loads a list of entity dictionary mappings into Entity instances and adds to the model.

    Args:
      entity_entries: A list of Python Dictionaries mapping entity attributes
        names to attribute values.
    """
    for entity_entry in entity_entries:
      if entity_entry[IS_REPORTING].upper() == 'TRUE':
        new_entity = ReportingEntity.FromDict(entity_entry)
      else:
        new_entity = VirtualEntity.FromDict(entity_entry)
      if not new_entity.bc_guid:
        new_entity.bc_guid = str(uuid.uuid4())
      self.guid_to_entity_map.AddEntity(new_entity)
      self.entities.append(new_entity)

  def LoadEntityFields(self, entity_field_entries: List[Dict[str,
                                                             str]]) -> None:
    """Loads a list of entity field dictionary mappings into EntityField instances and adds to the model.

    Args:
      entity_field_entries: A list of python dictionaries mapping entity field
        attribute names to values.
    """
    for entity_field_entry in entity_field_entries:
      entity_field_entry[BC_GUID] = self.guid_to_entity_map.GetEntityGuidByCode(
          entity_field_entry[ENTITY_CODE])
      if entity_field_entry[REPORTING_ENTITY_CODE]:
        entity_field_entry[
            REPORTING_ENTITY_GUID] = self.guid_to_entity_map.GetEntityGuidByCode(
                entity_field_entry[REPORTING_ENTITY_CODE])
      self.fields.append(EntityField.FromDict(entity_field_entry))

  def LoadStates(self, state_entries: List[Dict[str, str]]) -> None:
    """Loads a list of state dictionary mappings into State instances and adds to the model.

    Args:
      state_entries: A list of python dictionaries mapping state attribute names
        to values.
    """
    for state_entry in state_entries:
      state_entry[BC_GUID] = self.guid_to_entity_map.GetEntityGuidByCode(
          state_entry[ENTITY_CODE])
      self.states.append(State.FromDict(state_entry))

  def LoadConnections(self, connection_entries: List[Dict[str, str]]) -> None:
    """Loads a list of connection dictionary mappings into Connection instances and adds to the model.

    Args:
      connection_entries: A list of python dictionaries mapping connection
        attribute names to values.
    """
    for connection_entry in connection_entries:
      connection_entry[
          SOURCE_ENTITY_GUID] = self.guid_to_entity_map.GetEntityGuidByCode(
              connection_entry[SOURCE_ENTITY_CODE])
      connection_entry[
          TARGET_ENTITY_GUID] = self.guid_to_entity_map.GetEntityGuidByCode(
              connection_entry[TARGET_ENTITY_CODE])
      self.connections.append(ABELConnection.FromDict(connection_entry))

  def EntityInstanceToEntity(self, entity_instance: EntityInstance) -> None:
    """Maps EntityInstance attributes to an ABEL Entity instance and adds to the model.

    Args:
      entity_instance: An Instance Validator EntityInstance.
    """
    if not entity_instance.cloud_device_id:
      entity = VirtualEntity(
          code=entity_instance.code,
          namespace=entity_instance.namespace,
          etag=entity_instance.etag,
          type_name=entity_instance.type_name,
          bc_guid=entity_instance.guid)
    else:
      entity = ReportingEntity(
          code=entity_instance.code,
          namespace=entity_instance.namespace,
          cloud_device_id=entity_instance.cloud_device_id,
          etag=entity_instance.etag,
          type_name=entity_instance.type_name,
          bc_guid=entity_instance.guid)

      for field in entity_instance.translation.values():
        if isinstance(field, DimensionalValue):
          self._DimensionalValueToEntityField(
              reporting_entity_guid=entity_instance.guid, field=field)
        elif isinstance(field, MultiStateValue):
          self._MultistateValueToEntityField(
              reporting_entity_guid=entity_instance.guid, field=field)

    self.entities.append(entity)
    self.guid_to_entity_map.AddEntity(entity)

    if entity_instance.connections:
      for connection in entity_instance.connections:
        self._TranslateConnectionsToABEL(entity_instance.guid, connection)

  def _DimensionalValueToEntityField(self, reporting_entity_guid: str,
                                     field: DimensionalValue) -> None:
    """Maps DimensionalValue attributes to ABEL EntityField instances and adds to the model.

    Args:
      reporting_entity_guid: Parent reporting entity guid.
      field: An Instance Validator DimensionalValue instance.
    """
    entity_field = EntityField(
        standard_field_name=field.std_field_name,
        raw_field_name=field.raw_field_name,
        entity_guid=reporting_entity_guid,
        reporting_entity_guid=reporting_entity_guid)

    entity_field.units = Units(
        raw_unit_path=field.unit_field_name,
        standard_to_raw_unit_map=field.unit_mappings)

    self.fields.append(entity_field)

  def _MultistateValueToEntityField(self, reporting_entity_guid: str,
                                    field: MultiStateValue) -> None:
    """Maps MultiStateValue attributes to ABEL EntityField instances.

    Args:
      reporting_entity_guid: Parent reporting entity guid.
      field: An Instance Validator MultiStateValue instance.
    """
    self.fields.append(
        EntityField(
            standard_field_name=field.std_field_name,
            raw_field_name=field.raw_field_name,
            entity_guid=reporting_entity_guid,
            reporting_entity_guid=reporting_entity_guid))
    self._TranslateStatesToABEL(entity_guid=reporting_entity_guid, field=field)

  def _TranslateStatesToABEL(self, entity_guid: str,
                             field: MultiStateValue) -> None:
    """Maps MultiStateValue state attributes to ABEL State instance.

    Args:
      entity_guid: Parent entity guid.
      field: An Instance Validator MultistateValue instance.
    """
    for std_state_value, raw_state_value in field.states.items():
      self.states.append(
          State(
              standard_field_name=field.std_field_name,
              entity_guid=entity_guid,
              standard_state=std_state_value,
              raw_state=raw_state_value))

  def _TranslateConnectionsToABEL(self, entity_guid: str,
                                  connection: IVConnection) -> None:
    """Maps Instance Validator Connection attributes to ABEL Connection object.

    Args:
      entity_guid: Parent entity guid.
      connection: Instance Validator Connection instance.
    """
    self.connections.append(
        ABELConnection.FromDict({
            SOURCE_ENTITY_GUID: connection.source,
            CONNECTION_TYPE: connection.ctype,
            TARGET_ENTITY_GUID: entity_guid
        }))

  def ToModelDictionary(self) -> Dict[str, List[List[str]]]:
    """Converts a model into a dictionary for parsing into a spreadsheet.

    Converts model site, entities, fields, states, and connections into a
    dictionary to fill a spreadsheet. Since this method is used to export a
    concrete model into a spreadsheet, abel_elements are internal ABEL model
    instances constructed from a parsed Building config.

    Returns:
      A python dictionary of model values.
    """
    spreadsheet_dictionary = {}
    spreadsheet_range = {
        SITES: (ALL_SITE_HEADERS, [self.site]),
        ENTITIES: (ALL_ENTITY_HEADERS, self.entities),
        ENTITY_FIELDS: (ALL_FIELD_HEADERS, self.fields),
        STATES: (ALL_STATE_HEADERS, self.states),
        CONNECTIONS: (ALL_CONNECTION_HEADERS, self.connections)
    }
    for sheet_name, (headers, abel_element_list) in spreadsheet_range.items():
      if abel_element_list:
        rows = []
        for abel_element in abel_element_list:
          try:
            rows.append(list(abel_element.GetSpreadsheetRowMapping().values()))
          except AttributeError as err:
            print(f'sheet_name: {sheet_name}')
            print(f'{abel_element} contains missing attributes.')
            print(err)
        spreadsheet_dictionary[sheet_name] = [headers] + rows
      else:
        spreadsheet_dictionary[sheet_name] = []
    return spreadsheet_dictionary

  def AddReportingEntitiesFromEntityInstance(
      self, entity_instance: EntityInstance) -> None:
    """Adds link attributes to EntityField instances for all virtual entities.

    Determines if an entity has links, and calls this method to fill in
    entity_guid, reporting_entity_field_name, and standard_field_name for a
    field.

    Args:
      entity_instance: An EntityInstance instance from Instance Validator
        deserialization.
    """
    if entity_instance.links:
      for link in entity_instance.links:
        self._AddReportingEntitiesFromLinks(
            link=link, entity_instance=entity_instance)

  def _AddReportingEntitiesFromLinks(self, link: Link,
                                     entity_instance: EntityInstance) -> None:
    """Adds reporting entity code, guid and field name to an EntityField instance.

    For each link, iterate through this model's fields and if the links source
    guid equals the field's reporting_entity_guid and the field's standard field
    name is the link's mapped field, then add this virtual entity as the
    entity_guid for a field.

    Args:
      link: An Instance Validator Link instance.
      entity_instance: An EntityInstance from Instance Validator
        deserialization.
    """
    for source_field, target_field in link.field_map.items():
      for field in self.fields:
        if link.source == field.reporting_entity_guid and field.standard_field_name == target_field:
          field.entity_guid = entity_instance.guid
          field.reporting_entity_field_name = target_field
          field.standard_field_name = source_field
