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
"""Helper module for concrete model construction."""

from typing import Dict, List, Optional

# pylint: disable=g-importing-member
from model.connection import Connection as ABELConnection
from model.constants import ALL_CONNECTION_HEADERS
from model.constants import ALL_ENTITY_HEADERS
from model.constants import ALL_FIELD_HEADERS
from model.constants import ALL_SITE_HEADERS
from model.constants import ALL_STATE_HEADERS
from model.constants import BACKGROUND_COLOR_STYLE
from model.constants import CONNECTIONS
from model.constants import DATA
from model.constants import ENTITIES
from model.constants import ENTITY_FIELDS
from model.constants import FROZEN_ROW_COUNT
from model.constants import GRID_PROPERTIES
from model.constants import PROPERTIES
from model.constants import RGB_COLOR
from model.constants import ROW_DATA
from model.constants import SHEETS
from model.constants import SITES
from model.constants import STATES
from model.constants import STRING_VALUE
from model.constants import TEXT_FORMAT
from model.constants import TITLE
from model.constants import USER_ENTERED_FORMAT
from model.constants import USER_ENTERED_VALUE
from model.constants import VALUES
from model.entity import Entity
from model.entity import ReportingEntity
from model.entity import VirtualEntity
from model.entity_field import MultistateValueField
from model.entity_operation import EntityOperation
from model.from_building_config import AddReportingEntitiesFromEntityInstance
from model.from_building_config import EntityInstanceToEntity
from model.from_spreadsheet import LoadConnectionsFromSpreadsheet
from model.from_spreadsheet import LoadFieldsFromSpreadsheet
from model.from_spreadsheet import LoadOperationsFromSpreadsheet
from model.from_spreadsheet import LoadStatesFromSpreadsheet
from model.guid_to_entity_map import GuidToEntityMap
from model.site import Site
from model.state import State
from validate.entity_instance import EntityInstance
from validate.field_translation import FieldTranslation


class Model(object):
  """ABEL Concrete Model graph.

  ABEL parses a concrete model spreadsheet into a set of standard Python
  dictionaries mapping spreadsheet headers to values. This module takes in those
  dictionaries and parses their data into ABEL model elements.

  Attributes:
    fields: A list of FieldTranslation instances.
    entities: A list Entity instances.
    site: A list of Site instances.
    states: A list of State instances.
    connections: A list of Connection instances.
    guid_to_entity_map: A mapping of GUIDs to Entity instances.
  """

  class Builder(object):
    """Builder for ABEL Concrete Model graph."""

    def __init__(self, site: Site):
      self.site = site
      self.fields: List[FieldTranslation] = []
      self.entities: List[Entity] = []
      self.states: List[State] = []
      self.connections: List[ABELConnection] = []
      self.guid_to_entity_map = GuidToEntityMap()
      self.guid_to_entity_map.AddSite(site)

    @classmethod
    def FromSpreadsheet(cls, spreadsheet_dict: Dict[str, object]) -> ...:
      """Converts a Spreadsheet instance into fields, entities, and sites.

      Args:
        spreadsheet_dict: A mapping of spreadsheet names to Lists of
          dictionaries representing cells in a row keyed by column headers.

      Returns:
        An instance of Model class and a list of EntityOperation intances
        operating on Entity instances in a Model.
      """
      # Currently only supports one site per ABEL instance.
      site = Site.FromDict(spreadsheet_dict[SITES][0])
      model_builder = cls(site)

      entity_operations = LoadOperationsFromSpreadsheet(
          spreadsheet_dict[ENTITIES], model_builder.guid_to_entity_map
      )
      model_builder.entities = [
          operation.entity for operation in entity_operations
      ]
      model_builder.fields = LoadFieldsFromSpreadsheet(
          spreadsheet_dict[ENTITY_FIELDS], model_builder.guid_to_entity_map
      )
      model_builder.states = LoadStatesFromSpreadsheet(
          spreadsheet_dict[STATES], model_builder.guid_to_entity_map
      )
      model_builder.connections = LoadConnectionsFromSpreadsheet(
          spreadsheet_dict[CONNECTIONS], model_builder.guid_to_entity_map
      )
      return model_builder, entity_operations

    @classmethod
    def FromBuildingConfig(
        cls, site: Site, building_config_dict: Dict[str, EntityInstance]
    ) -> ...:
      """Converts a yaml document into fields, entities, and sites.

      Iterates through the dictionary returned by Instance validator
      deserialization. Iterates a second time and fills Reporting entity code,
      guid and field name values for a field.

      Args:
        site: A site instance stripped from a building config.
        building_config_dict: A dictionary mapping of Instance Validator
          EntityInstance objects by guid.

      Returns:
        A Model instance and a list of EntityOperation instances operating on
        Entity instances  in a model.
      """
      model_builder = cls(site)
      entities = []
      fields = []
      states = []
      connections = []
      operations = []

      for entity_instance in building_config_dict.values():
        this_entity, this_fields, this_states, this_connections, operation = (
            EntityInstanceToEntity(entity_instance)
        )
        model_builder.guid_to_entity_map.AddEntity(this_entity)
        entities.append(this_entity)
        fields.extend(this_fields)
        states.extend(this_states)
        connections.extend(this_connections)
        operations.append(operation)

      for entity_instance in building_config_dict.values():
        AddReportingEntitiesFromEntityInstance(entity_instance, fields)

      model_builder.entities = entities
      model_builder.fields = fields
      model_builder.states = states
      model_builder.connections = connections

      return model_builder, operations

    def Build(self) -> ...:
      """Connects ABEL graph with Guids as edges.

      Guids are used as edges between entities, translations and reporting
      entities, and links and virtual entities. Reporting field names are used
      at edges between states and MultiStateValue fields.

      Returns:
        built Model instance
      """
      self.site.entities = self.entities
      # For each entity, Add connections where entity is the source
      for guid in self.site.entities:
        entity = self.guid_to_entity_map.GetEntityByGuid(guid)
        for connection in self.connections:
          if connection.target_entity_guid == guid:
            entity.AddConnection(connection)
        # For each field in the model
        for field in self.fields:
          # For each state in the model
          for state in self.states:
            # Create edges between states and their corresponding Multi-state
            # value field in stances.
            if state.reporting_entity_guid == guid:
              if state.std_field_name in (
                  field.reporting_entity_field_name,
                  field.std_field_name,
              ):
                if isinstance(field, MultistateValueField):
                  field.AddState(state)
          # Link field to entity if entity is virtual
          if isinstance(entity, VirtualEntity):
            if field.entity_guid == guid:
              entity.AddLink(field)
          # Add field as a translation to entity if entity is reporting.
          elif isinstance(entity, ReportingEntity):
            if guid in (field.entity_guid, field.reporting_entity_guid):
              entity.AddTranslation(field)
      return Model(self)

  def __init__(self, builder: Builder):
    self._site = builder.site
    self._fields = builder.fields
    self._entities = builder.entities
    self._states = builder.states
    self._connections = builder.connections
    self._guid_to_entity_map = builder.guid_to_entity_map

  @property
  def site(self) -> Site:
    return self._site

  @property
  def fields(self) -> List[FieldTranslation]:
    return self._fields

  @property
  def entities(self) -> List[VirtualEntity]:
    return self._entities

  @property
  def states(self) -> List[State]:
    return self._states

  @property
  def connections(self) -> List[ABELConnection]:
    return self._connections

  @property
  def guid_to_entity_map(self) -> GuidToEntityMap:
    return self._guid_to_entity_map

  def GetEntity(self, entity_guid: str) -> Entity:
    return self.guid_to_entity_map.GetEntityByGuid(entity_guid)

  def ToModelDictionary(
      self, operations: Optional[List[EntityOperation]] = None
  ) -> Dict[str, List[List[str]]]:
    """Converts a model into a dictionary for parsing into a spreadsheet.

    Converts model site, entities, fields, states, and connections into a
    dictionary to fill a spreadsheet. Since this method is used to export a
    concrete model into a spreadsheet, abel_elements are internal ABEL model
    instances constructed from a parsed Building config.

    Args:
      operations: List of EntityOperation instances.

    Returns:
      A python dictionary of model values.
    """

    if operations:
      entities = operations
    else:
      entities = self.entities

    spreadsheet_range = {
        SITES: (ALL_SITE_HEADERS, [self.site]),
        ENTITIES: (ALL_ENTITY_HEADERS, entities),
        ENTITY_FIELDS: (ALL_FIELD_HEADERS, self.fields),
        STATES: (ALL_STATE_HEADERS, self.states),
        CONNECTIONS: (ALL_CONNECTION_HEADERS, self.connections),
    }
    title = (
        f'{self.site.code}'
        '{datetime.datetime.strftime(datetime.datetime.now(),' 
        ' "%Y-%m-%d %H:%M")}'
    )
    spreadsheet_model = {PROPERTIES: {TITLE: title}, SHEETS: []}
    # pylint: disable = g-complex-comprehension
    for sheet_name, (headers, abel_element_list) in spreadsheet_range.items():
      header_row = {
          VALUES: [
              {
                  USER_ENTERED_VALUE: {STRING_VALUE: header},
                  USER_ENTERED_FORMAT: {
                      BACKGROUND_COLOR_STYLE: {
                          RGB_COLOR: {
                              'red': 227,
                              'green': 82,
                              'blue': 125,
                          }
                      },
                      TEXT_FORMAT: {'bold': True},
                  },
              }
              for header in headers
          ]
      }
      sheet_model = {
          PROPERTIES: {
              TITLE: sheet_name,
              GRID_PROPERTIES: {FROZEN_ROW_COUNT: 1},
          },
          DATA: {ROW_DATA: [header_row]},
      }
      if abel_element_list:
        for abel_element in abel_element_list:
          try:
            sheet_model.get(DATA).get(ROW_DATA).append(
                abel_element.GetSpreadsheetRowMapping(self.guid_to_entity_map)
            )
          except AttributeError as err:
            print(f'sheet_name: {sheet_name}')
            print(f'{abel_element} contains missing attributes.')
            print(err)
      spreadsheet_model.get(SHEETS).append(sheet_model)
    return spreadsheet_model
