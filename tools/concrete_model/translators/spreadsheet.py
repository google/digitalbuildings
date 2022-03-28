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
"""Module for representing Concrete Model spreadsheets and translating them into dataclasses."""

import dataclasses
from typing import List, Dict, Optional

from model.telemetry_format import TelemetryFormat


@dataclasses.dataclass(frozen=True)
class SpreadsheetEntityField():
  """Represents a single row in a Concrete Model Entity Fields table."""

  site_name: str
  entity_name: str
  field_name: str
  bc_units: str
  udmi_units: Optional[str]
  bc_telemetry: str
  bc_initial_value: str
  udmi_telemetry_format: TelemetryFormat
  bc_device_id: int
  bc_object_type: str
  bc_object_id: str
  bc_object_name: str
  udmi_ref: Optional[str] = None
  udmi_writeable: Optional[bool] = None
  udmi_baseline_value: Optional[int] = None
  udmi_baseline_tolerance: Optional[int] = None
  udmi_baseline_state: Optional[str] = None
  udmi_cov_increment: Optional[int] = None
  context: Optional[Dict[str, str]] = None


@dataclasses.dataclass(frozen=True)
class SpreadsheetEntity():
  """Represents a single row in a Concrete Model Entities table."""

  site_name: str
  code: str
  udmi_physical_asset_name: str
  bc_guid: str
  udmi_guid: str
  cloud_device_id: str
  namespace: str
  general_type: str
  entity_type: Optional[str] = None
  udmi_system_location_section: Optional[str] = None
  udmi_system_location_x: Optional[int] = None
  udmi_system_location_y: Optional[int] = None
  udmi_system_location_z: Optional[int] = None
  context: Optional[Dict[str, str]] = None


@dataclasses.dataclass(frozen=True)
class SpreadsheetSite():
  """Represents a single row in a Concrete Model Sites table."""

  name: str
  guid: str = None


@dataclasses.dataclass(frozen=True)
class SpreadsheetConnection():
  """Represents a single row in a Concrete Model Connections table."""

  source_site: str
  source_entity_code: str
  target_site: str
  target_entity_code: str
  connection_type: str


@dataclasses.dataclass(frozen=True)
class SpreadsheetState():
  """Represents a single row in a Concrete Model States table."""

  site_name: str
  entity_name: str
  field_name: str
  payload_state: str
  standard_state: str


class Spreadsheet():
  """A collection of spreadsheet entry tables corresponding to concrete model spreadsheet tables.

  Attributes:
    entity_field_entries: A list of SpreadsheetEntityField instances.
    entity_entries: A list of SpreadsheetEntity instances.
    site_entries: A list of SpreadsheetSite instances.
    connection_entries: A list of SpreadsheetConnection instances.
    state_entries: A list of SpreadsheetState instances.
  """

  def __init__(self) -> None:
    """Initializes a Spreadsheet object."""
    self._entity_field_entries: List[SpreadsheetEntityField] = []
    self._entity_entries: List[SpreadsheetEntity] = []
    self._site_entries: List[SpreadsheetSite] = []
    self._connection_entries: List[SpreadsheetConnection] = []
    self._state_entries: List[SpreadsheetState] = []

  @classmethod
  def FromFile(cls, file_path: str) ->...:
    """Parses a loadsheet excel file into a Loadsheet instance.

    Args:
      file_path: A loadsheet's file path.

    Returns:
      A Spreadsheet instance.
    """

  @property
  def entityfields(self) -> List[SpreadsheetEntityField]:
    """Collection of entity field entries."""
    return self._entity_field_entries

  @property
  def entities(self) -> List[SpreadsheetEntity]:
    """Collection of entity entries."""
    return self._entity_entries

  @property
  def sites(self) -> List[SpreadsheetSite]:
    """Collection of site entries."""
    return self._site_entries

  @property
  def connections(self) -> List[SpreadsheetConnection]:
    """Collection of connection entries."""
    return self._connection_entries

  @property
  def states(self) -> List[SpreadsheetState]:
    """Collection of state entries."""
    return self._state_entries

  def AddEntity(self, entity: SpreadsheetEntity) -> None:
    """Adds a SpreadsheetEntity instance to a Spreadsheet instance.

    Args:
      entity: A SpreadsheetEntity instance.
    """

  def AddEntityField(self, field: SpreadsheetEntityField) -> None:
    """Adds a SpreadsheetEntityField instance to a spreadsheet instance.

    Args:
      field: A SpreadsheetEntityField instance.
    """

  def AddSite(self, site: SpreadsheetSite) -> None:
    """Adds a SpreadsheetSite instance to a Spreadsheet instance.

    Args:
      site: A SpreadsheetSite instance.
    """

  def AddConnection(self, connection: SpreadsheetConnection) -> None:
    """Adds a SpreadsheetConnection instance to a Spreadsheet instance.

    Args:
      connection: A SpreadsheetConnection instance.
    """

  def AddState(self, state: SpreadsheetState) -> None:
    """Adds a SpreadsheetState instance to a Spreadsheet instance.

    Args:
      state: A SpreadsheetState instance.
    """
