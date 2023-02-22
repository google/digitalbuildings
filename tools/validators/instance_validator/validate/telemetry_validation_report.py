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
"""Container for the result of a pubsub message validation."""

from __future__ import annotations

import datetime
from typing import Any, Dict, List, Optional, Tuple

from validate.constants import ENTITY_CODE
from validate.constants import ENTITY_GUID
from validate.constants import ERROR_DEVICES
from validate.constants import EXPECTED_DEVICES
from validate.constants import EXPECTED_POINTS
from validate.constants import EXTRA_DEVICES
from validate.constants import EXTRA_POINTS
from validate.constants import INVALID_DIMENSIONAL_VALUES
from validate.constants import MESSAGE_DESCRIPTION
from validate.constants import MESSAGE_TIMESTAMP
from validate.constants import MESSAGE_VERSION
from validate.constants import MISSING_DEVICES
from validate.constants import MISSING_POINTS
from validate.constants import MISSING_PRESENT_VALUES
from validate.constants import MISSING_TIMESTAMP
from validate.constants import MISSING_VERSION
from validate.constants import REPORT_TIMESTAMP
from validate.constants import TELEMETRY_MESSAGE_ERRORS
from validate.constants import TELEMETRY_MESSAGE_WARNINGS
from validate.constants import TIMESTAMP_FORMAT
from validate.constants import UNMAPPED_STATES


# TODO(b/269321767)
class TelemetryValidationReport(object):
  """Container for a telememtry validation report.

  Attributes:
    timestamp: UTC timestamp for when the report is created.
    version: A pubsub message's UDMI version.
    expected_devices: Dictionary mapping of valid device GUIDs to device codes
      listed in a building configuration.
    extra_devices: Dictionary mapping of valid device GUIDs to device codes
      reported by a pubsub subscription and not contained in a building
      configuration file.
    missing_devices: Dictionary mapping of valid device GUIDs to device codes
      not reported by a pubsub subscription but contained in a building
      configuration file.
    error_devices: List of TelemetryMessageValidationBlock instances for
      telemetry messages that generate validation errors.
  """

  def __init__(
      self,
      expected_devices: Dict[str, str],
      extra_devices: Optional[Dict[str, str]] = None,
      missing_devices: Optional[Dict[str, str]] = None,
      error_devices: Optional[List[TelemetryMessageValidationBlock]] = None,
  ):
    """Init."""
    self._timestamp = datetime.datetime.now(tz=datetime.timezone.utc).strftime(
        TIMESTAMP_FORMAT
    )
    self._expected_devices = expected_devices

    self._extra_devices = {}
    if extra_devices:
      self._extra_devices = extra_devices
    self._missing_devices = {}
    if missing_devices:
      self._missing_devices = missing_devices
    self._error_devices = []
    if error_devices:
      self._error_devices = error_devices

  @property
  def timestamp(self) -> str:
    return self._timestamp

  @property
  def expected_devices(self) -> Dict[str, str]:
    return self._expected_devices

  @property
  def extra_devices(self) -> Dict[str, str]:
    return self._extra_devices

  @property
  def missing_devices(self) -> Dict[str, str]:
    return self._missing_devices

  @property
  def error_devices(self) -> List[TelemetryMessageValidationBlock]:
    return self._error_devices

  def AddExtraDevice(self, guid_to_code_map: Dict[str, str]) -> None:
    """Add a device that exists in telemetry but not in the building config."""
    self._extra_devices.update(guid_to_code_map)

  def AddMissingDevice(self, guid_to_code_map: Dict[str, str]) -> None:
    """Add a device that exists in the building config but not in telemetry."""
    self._missing_devices.update(guid_to_code_map)

  def AddErrorDevice(
      self, validation_block: TelemetryMessageValidationBlock
  ) -> None:
    """Add a telemetry validation block for an entity in the bc."""
    self._error_devices.append(validation_block)

  def GenerateReport(self) -> Dict[str, List[Any]]:
    """Returns json payload representation of validation report."""
    validation_report_dict = {
        REPORT_TIMESTAMP: self._timestamp,
        EXPECTED_DEVICES: self._expected_devices,
        EXTRA_DEVICES: self._extra_devices,
        MISSING_DEVICES: self._missing_devices,
        ERROR_DEVICES: [
            block.CreateJsonReportBlock() for block in self._error_devices
        ],
    }
    return validation_report_dict


class TelemetryMessageValidationBlock(object):
  """A container for telemetry validation result from pubsub message by entity.

  Attributes:
    guid: Entity guid of the of the device whose pubsub message is being
      validated.
    code: Entity code of the of the device whose pubsub message is being
      validated.
    timestamp: UTC timestamp for when oubsub message is received.
    version: GCP pubsub API version.
    expected_points: Dictionary of expected points.
    extra_points: Set of points found in telemetry that is not captured in the
      building config.
    missing_points: Set of points found in the building config that is not
      captured in the telemetry stream.
    missing_present_values: Points in a pubsub message which are missing the
      present_value field.
    unmapped_states: Point states received in a pubsub but not present in a
      building config file.
    invalid_dimensional_values: Points whose dimensional value is not of the
      correct type.
    valid: Boolean indicator of whether a pubsub message is valid and conforms
      to a building config translation.
    description: [Optional] Description of what makes the device invalid. Good
      for errors or warnings that may not fall under one of the above
      categories.
  """

  def __init__(
      self,
      guid: str,
      code: str,
      expected_points: list[str],
      timestamp: Optional[datetime.datetime] = None,
      version: Optional[str] = None,
      description: Optional[str] = '',
  ):
    """Init."""

    self.guid = guid
    self.code = code
    self.version = version
    self.timestamp = timestamp
    self._expected_points = expected_points
    self._extra_points = []
    self._missing_points = []
    self._missing_present_values = []
    self._unmapped_states = []
    self._invalid_dimensional_values = []
    self._valid = True
    self._description = description

  @property
  def expected_points(self) -> list[str]:
    return self._expected_points

  @property
  def valid(self) -> bool:
    return self._valid

  @property
  def description(self) -> str:
    return self._description

  @property
  def extra_points(self) -> list[str]:
    return self._extra_points

  @property
  def missing_points(self) -> list[str]:
    return self._missing_points

  @property
  def missing_present_values(self) -> list[str]:
    return self._missing_present_values

  @property
  def unmapped_states(self) -> list[Tuple[str, str]]:
    return self._unmapped_states

  @property
  def invalid_dimensional_values(self) -> list[Tuple[str, str]]:
    return self._invalid_dimensional_values

  def AddDescription(self, description: str) -> None:
    self._valid = False
    self._description += description

  def AddExtraPoint(self, point: str) -> None:
    """Add a point that exists in the telemetry message but not in the building config."""
    self._valid = False
    self._extra_points.append(point)

  def AddMissingPoint(self, point: str) -> None:
    """Add a point that exists in the building config but not in the telemetry message."""
    self._valid = False
    self._missing_points.append(point)

  def AddMissingPresentValue(self, point: str) -> None:
    """Add a point that is missing the present_value field."""
    self._valid = False
    self._missing_present_values.append(point)

  def AddUnmappedState(self, state: str, point: str) -> None:
    """Add a state that exists in the telemetry message but does not map to a standard state."""
    self._valid = False
    self._unmapped_states.append((point, state))

  def AddInvalidDimensionalValue(self, value: str, point: str) -> None:
    """Add a point whose dimensional value is not of the correct type."""
    self._valid = False
    self._invalid_dimensional_values.append((point, value))

  def CreateJsonReportBlock(self) -> Dict[str, Any]:
    """Exports a telemetry validation report point(block) as valid json."""

    json_report_block = {
        ENTITY_CODE: self.code,
        ENTITY_GUID: self.guid,
        EXPECTED_POINTS: self._expected_points,
        TELEMETRY_MESSAGE_ERRORS: {
            MISSING_POINTS: self._missing_points,
            MISSING_PRESENT_VALUES: self._missing_present_values,
            INVALID_DIMENSIONAL_VALUES: _TelemetryPointListToDict(
                self._invalid_dimensional_values
            ),
        },
        TELEMETRY_MESSAGE_WARNINGS: {
            EXTRA_POINTS: self._extra_points,
            UNMAPPED_STATES: _TelemetryPointListToDict(self._unmapped_states),
        },
    }

    if not self.timestamp:
      json_report_block.update({MESSAGE_TIMESTAMP: MISSING_TIMESTAMP})
    else:
      json_report_block.update({MESSAGE_TIMESTAMP: self.timestamp})

    if not self.version:
      json_report_block.update({MESSAGE_VERSION: MISSING_VERSION})
    else:
      json_report_block.update({MESSAGE_VERSION: self.version})

    if self._description:
      json_report_block.update({MESSAGE_DESCRIPTION: self._description})

    return json_report_block


def _TelemetryPointListToDict(
    point_tuple_list: List[Tuple[str, str]]
) -> Dict[str, str]:
  """Returns a dictionary representation of a tuple of point and value."""

  point_dictionary = {point: value for point, value in point_tuple_list}
  return point_dictionary
