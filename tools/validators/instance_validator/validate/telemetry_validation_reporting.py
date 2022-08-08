# Copyright 2020 Google LLC
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
"""Container for a telemetry validation report point: warning or error."""

import enum


class TelemetryReportPointType(enum.Enum):
  WARNING = 'WARNING'
  ERROR = 'ERROR'

  def __str__(self):
    return self.value


class TelemetryReportPoint(object):
  """Container for a telemetry validation point."""

  def __init__(self, entity, point, error_message, report_type):
    """Init.

    Args:
      entity: name of the entity with the error
      point: name of the point with the error (can be None)
      error_message: specific error message
      report_type: TelemetryReportyPointType WARNING or ERROR
    """
    super().__init__()
    self.entity = entity
    self.point = point
    self.error_message = error_message
    self._report_type = report_type

  # this should be immutable after instantiation; as it doesn't make sense to
  # reclassify a TelemetryReportPoint designation in this context
  @property
  def report_type(self):
    return self._report_type

  def __eq__(self, other):
    if not isinstance(
        other, TelemetryReportPoint) or other.report_type != self.report_type:
      return NotImplemented

    return (self.entity == other.entity and self.point == other.point and
            self.error_message == other.error_message)

  def GetPrintableErrorMessage(self):
    """Returns a human-readable error_message."""
    msg = f'- entity [{self.entity}]'
    if self.point:
      msg += f', point [{self.point}]'
    msg += f': {self.error_message}\n'

    return msg
