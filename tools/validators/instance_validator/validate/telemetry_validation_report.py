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
"""Container for the result of a pubsub message validation."""

from __future__ import annotations

import dataclasses
import datetime
from typing import Any, Dict, List, Optional

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
from validate.constants import PRESENT_VALUE_KEY
from validate.constants import REPORT_TIMESTAMP
from validate.constants import TELEMETRY_MESSAGE_ERRORS
from validate.constants import TELEMETRY_MESSAGE_WARNINGS
from validate.constants import TIMESTAMP_FORMAT
from validate.constants import UNMAPPED_STATES


@dataclasses.dataclass
class TelemetryPoint(object):
  """Class to hold telemetry point attributes.

  Attributes:
    point_name: Name of the point.
    present_value: A point's present value which as a string, int, boolean, or
      float.
  """

  point_name: str
  present_value: Any


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
      extra_devices: Dict[str, str],
      missing_devices: Dict[str, str],
      error_devices: List[TelemetryMessageValidationBlock],
  ):
    """Init."""
    self.timestamp = datetime.datetime.now(tz=datetime.timezone.utc).strftime(
        TIMESTAMP_FORMAT
    )
    self.expected_devices = expected_devices
    self.extra_devices = extra_devices
    self.missing_devices = missing_devices
    self.error_devices = error_devices

  def AddExtraDevice(self, code: str) -> None:
    self.extra_devices.append(code)

  def AddMissingDevice(self, code: str) -> None:
    self.missing_devices.append(code)

  def AddErrorDevice(self, code: str) -> None:
    self.error_devices.append(code)

  def GenerateReport(self) -> Dict[str, List[Any]]:
    """Returns json payload representation of validation report."""
    validation_report_dict = {
        REPORT_TIMESTAMP: self.timestamp,
        EXPECTED_DEVICES: self.expected_devices,
        EXTRA_DEVICES: self.extra_devices,
        MISSING_DEVICES: self.missing_devices,
        ERROR_DEVICES: [
            block.CreateJsonReportBlock() for block in self.error_devices
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
      description: Optional[str] = None,
  ):
    """Init."""

    self.guid = guid
    self.code = code
    self.version = version
    self.timestamp = timestamp
    self.expected_points = expected_points
    self.extra_points = []
    self.missing_points = []
    self.missing_present_values = []
    self.unmapped_states = []
    self.invalid_dimensional_values = []
    self.valid = True
    self.description = description

  def AddExtraPoint(self, point: str) -> None:
    self.valid = False
    self.extra_points.append(point)

  def AddMissingPoint(self, point: str) -> None:
    self.valid = False
    self.missing_points.append(point)

  def AddMissingPresentValue(self, point: str) -> None:
    self.valid = False
    self.missing_present_values.append(point)

  def AddUnmappedState(self, state: str, point: str) -> None:
    self.valid = False
    self.unmapped_states.append((point, state))

  def AddInvalidDimensionalValue(self, value: str, point: str) -> None:
    self.valid = False
    self.invalid_dimensional_values.append((point, value))

  def CreateJsonReportBlock(self) -> Dict[str, Any]:
    """Exports a telemetry validation report point(block) as valid json."""

    json_report_block = {
        ENTITY_CODE: self.code,
        ENTITY_GUID: self.guid,
        EXPECTED_POINTS: self._TelemetryPointListToDict(self.expected_points),
        TELEMETRY_MESSAGE_ERRORS: {
            MISSING_POINTS: self._TelemetryPointListToDict(self.missing_points),
            MISSING_PRESENT_VALUES: self._TelemetryPointListToDict(
                self.missing_present_values
            ),
            INVALID_DIMENSIONAL_VALUES: self._TelemetryPointListToDict(
                self.invalid_dimensional_values
            ),
        },
        TELEMETRY_MESSAGE_WARNINGS: {
            EXTRA_POINTS: self._TelemetryPointListToDict(self.extra_points),
            UNMAPPED_STATES: self._TelemetryPointListToDict(
                self.unmapped_states
            ),
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

    if self.description:
      json_report_block.update({MESSAGE_DESCRIPTION: self.description})

    return json_report_block

  def _TelemetryPointListToDict(
      self, point_list: List[TelemetryPoint]
  ) -> Dict[str, Any]:
    """Returns a dictionary representation of a TelemetryPoint instance."""

    point_dictionary = {
        point.point_name: {PRESENT_VALUE_KEY: point.present_value}
        for point in point_list
    }
    return point_dictionary
