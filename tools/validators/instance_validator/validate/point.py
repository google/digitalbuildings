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

"""Data point in a telemetry message."""

class Point(object):
  """A point from a pubsub telemetry message.

  Args:
    point_name: name of the point
    value: value of the point
  """

  def __init__(self, point_name, value):
    super().__init__()
    self.point_name = point_name
    self.present_value = self._ValueToString(value)

  def _ValueToString(self, value):
    """This is needed to allow parsing of values (bool and multi-states)."""
    if isinstance(value, bool):
      return str(value).lower()

    if isinstance(value, (int, float)):
      return str(value)

