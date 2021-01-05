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

"""Container for a telemetry validation error."""

class TelemetryWarning(object):
  """Container for a telemetry validation warning.

  Args:
    entity: name of the entity with the warning
    point: name of the point with the warning (can be None)
    message: specific warning message
  """

  def __init__(self, entity, point, message):
    super().__init__()
    self.entity = entity
    self.point = point
    self.message = message

  def __eq__(self, other):
    if not isinstance(other, TelemetryWarning):
      return NotImplemented
    return (self.entity == other.entity and
            self.point == other.point and
            self.message == other.message)

  def GetPrintableMessage(self):
    """Returns a human-readable message that explains this warning."""

    msg = '- entity [{0}]'.format(self.entity)
    if self.point:
      msg += ', point [{0}]'.format(self.point)
    msg += ': {0}\n'.format(self.message)
    return msg
