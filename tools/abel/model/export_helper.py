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
"""Helper module for exporting a valid Building Configuration or spreadsheet."""

from typing import Any, Dict, List

from googleapiclient.discovery import Resource
from googleapiclient.errors import HttpError
from strictyaml import as_document

from model.constants import BODY_VALUE_RANGE_KEY
from model.constants import CONFIG_CLOUD_DEVICE_ID
from model.constants import CONFIG_CODE
from model.constants import CONFIG_CONNECTIONS
from model.constants import CONFIG_INITIALIZE
from model.constants import CONFIG_LINKS
from model.constants import CONFIG_METADATA
from model.constants import CONFIG_OPERATION
from model.constants import CONFIG_STATES
from model.constants import CONFIG_TRANSLATION
from model.constants import CONFIG_TYPE
from model.constants import CONFIG_UNITS
from model.constants import CONFIG_UNITS_KEY
from model.constants import CONFIG_UNITS_PRESENT_VALUE
from model.constants import CONFIG_UNITS_VALUES
from model.constants import UTF_8
from model.constants import VALUE_INPUT_OPTION_RAW
from model.constants import WRITE
from model.entity import Entity
from model.entity import ReportingEntity
from model.entity import VirtualEntity
from model.entity_field import EntityField
from model.guid_to_entity_map import GuidToEntityMap
from model.model_builder import ModelBuilder
from model.model_error import SpreadsheetAuthorizationError


class GoogleSheetExport(object):
  """Class to help write ABEL data types to a Google Sheets spreadsheet.

  Attributes:
    guid_to_entity_map: A global mapping of GUIDs to Entity instances.
  """

  def __init__(self):
    """Init."""
    self.guid_to_entity_map = GuidToEntityMap()

  def WriteAllSheets(self, spreadsheet_range: List[str], spreadsheet_id: str,
                     model_dict: Dict[str, Dict[str, str]],
                     google_sheets_service: Resource) -> str:
    """Translates an ABEL concrete model into a Google Sheets spreadsheet.

    Args:
      spreadsheet_range: A list of table names.
      spreadsheet_id: Google spreadsheet ID.
      model_dict: Dictionary of internal ABEL model elements to translate to a
        spreadsheet.
      google_sheets_service: A Google Python API Client discovery Resource
        instance with methods for interacting with the Google Sheets service.

    Returns:
      Id of the updated spreadsheet.

    Raises:
      SpreadsheetAuthorizationError: When the Google Sheets API request fails.
    """
    sheet = google_sheets_service.spreadsheets()
    for named_range in spreadsheet_range:
      body_value_range = {BODY_VALUE_RANGE_KEY: model_dict[named_range]}
      try:
        sheet.values().update(
            spreadsheetId=spreadsheet_id,
            range=named_range,
            valueInputOption=VALUE_INPUT_OPTION_RAW,
            body=body_value_range).execute()
      except HttpError as http_error:
        raise SpreadsheetAuthorizationError(
            spreadsheet_id=spreadsheet_id,
            resp=http_error.resp,
            content=http_error.content) from http_error
    return spreadsheet_id


class BuildingConfigExport(object):
  """Class to translate an ABEL model into a Building Configuration.

  Attributes:
    model: The ABEL model graph.
    guid_to_entity_map: A global mapping of GUIDs to Entity instances.
  """

  def __init__(self, model_builder: ModelBuilder):
    """Init.

    Args:
      model_builder: Instance of ModelBuilder class to be translated into a
        Building Configuration file.
    """
    self.model = model_builder
    self.guid_to_entity_map = GuidToEntityMap()

  # TODO(b/233756557) Allow user to set config_metadata operation.
  def ExportBuildingConfiguration(self, filepath: str) -> Dict[str, Any]:
    """Exports an ABEL concrete model graph to a Building Config file.

    Args:
      filepath: Absolute export path for a Building Config.

    Returns:
      A dictionary model of the exported building config.

    Raises:
      PermissionError: When ABEL is denied access to filepath.
    """
    site = self.model.site
    entity_yaml_dict = {CONFIG_METADATA: {CONFIG_OPERATION: CONFIG_INITIALIZE}}
    for entity_guid in site.entities:
      entity = self.guid_to_entity_map.GetEntityByGuid(entity_guid)
      if isinstance(entity, ReportingEntity):
        entity_yaml_dict.update({
            entity.bc_guid: self._GetReportingEntityBuildingConfigBlock(entity)
        })
      elif isinstance(entity, VirtualEntity):
        entity_yaml_dict.update(
            {entity.bc_guid: self._GetVirtualEntityBuildingConfigBlock(entity)})

    entity_yaml_dict.update({
        site.guid: {
            CONFIG_CODE: site.code,
            CONFIG_TYPE: site.namespace + '/' + site.type_name
        }
    })
    try:
      with open(filepath, WRITE, encoding=UTF_8) as file:
        for key, value in entity_yaml_dict.items():
          file.write(as_document({key: value}).as_yaml())
          file.write('\n')
    except PermissionError:
      print(f'Permission denied when writing to {filepath}')
    return entity_yaml_dict

  def _GetReportingEntityBuildingConfigBlock(
      self, entity: ReportingEntity) -> Dict[str, object]:
    """Returns a Building Config formatted reporting entity block dictionary.

    Args:
      entity: A ReportingEntity instance.

    Returns:
      A dicitionary in Building Config format ready to be parsed into yaml.
    """
    reporting_entity_yaml = {
        CONFIG_CLOUD_DEVICE_ID: entity.cloud_device_id,
        CONFIG_CODE: entity.code,
    }
    reporting_entity_yaml.update(self._GetConnections(entity=entity))
    if entity.translations:
      reporting_entity_yaml[CONFIG_TRANSLATION] = {}
      for field in entity.translations:
        if field.reporting_entity_field_name:
          reporting_entity_yaml[CONFIG_TRANSLATION].update(
              {field.reporting_entity_field_name: self._TranslateField(field)})
        else:
          reporting_entity_yaml[CONFIG_TRANSLATION].update(
              {field.standard_field_name: self._TranslateField(field)})
    reporting_entity_yaml.update(
        {CONFIG_TYPE: entity.namespace + '/' + str(entity.type_name)})
    return reporting_entity_yaml

  def _GetVirtualEntityBuildingConfigBlock(
      self, entity: VirtualEntity) -> Dict[str, object]:
    """Returns a Building Config formatted virtual entity block dictionary.

    Args:
      entity: A VirutalEntity instance.

    Returns:
      A dicitionary formatted for Building Config ready to be parsed into yaml.
    """
    virtual_entity_yaml = {CONFIG_CODE: entity.code}
    virtual_entity_yaml.update(self._GetConnections(entity=entity))
    if entity.links:
      virtual_entity_yaml.update({CONFIG_LINKS: self._SortLinks(entity)})
    virtual_entity_yaml.update(
        {CONFIG_TYPE: entity.namespace + '/' + str(entity.type_name)})
    return virtual_entity_yaml

  def _GetConnections(self, entity: Entity) -> Dict[str, List[str]]:
    if entity.connections:
      return {
          CONFIG_CONNECTIONS: {
              c.source_entity_guid: [c.connection_type.name]
              for c in entity.connections
          }
      }
    return {}

  def _SortLinks(self, entity: VirtualEntity) -> Dict[str, object]:
    """Sorts an entity's links by guid and returns a Building Config compliant mapping.

    Args:
      entity: A VirtualEntity instance

    Returns:
      A dictionary of lists keyed by reporting entity guids. Each list is a
      dictionary of reporting entity fields mapped by virtual entity fields.
    """
    link_map = {}
    if entity.links:
      for field in entity.links:
        if field.reporting_entity_guid not in link_map.keys():
          link_map[field.reporting_entity_guid] = {
              field.standard_field_name: field.reporting_entity_field_name
          }
        else:
          link_map[field.reporting_entity_guid].update(
              {field.standard_field_name: field.reporting_entity_field_name})
    return link_map

  def _TranslateField(self, field: EntityField) -> Dict[str, object]:
    """Returns a Building Configuration compliant translation mapping.

    Args:
      field: An EntityField instance.

    Returns:
      A translation mapping.
    """
    return_dict = {CONFIG_UNITS_PRESENT_VALUE: field.raw_field_name}
    if field.units:
      return_dict[CONFIG_UNITS] = {
          CONFIG_UNITS_KEY: field.units.raw_unit_path,
          CONFIG_UNITS_VALUES: {
              standard_unit: raw_unit for standard_unit, raw_unit in
              field.units.standard_to_raw_unit_map.items()
          }
      }
    elif field.states:
      return_dict[CONFIG_STATES] = {
          state.standard_state: state.raw_state for state in field.states
      }
    return return_dict
