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
"""Tests tools.validators.instance_validator.message_filters"""

from __future__ import absolute_import
from absl.testing import absltest
from validate import message_filters

class MessageFilterTests(absltest.TestCase):
  """Tests"""

  def testTelemetryWithEmptyMessage(self):
    self.assertFalse(message_filters.Udmi.telemetry({}))

  def testTelemetryWithStateMessage(self):
    attrs = {'subFolder': 'update', 'subType': 'state'}
    self.assertFalse(message_filters.Udmi.telemetry(attrs))

  def testTelemetryWithTelemetry(self):
    attrs = {'subFolder': 'pointset'}
    self.assertTrue(message_filters.Udmi.telemetry(attrs))

  def testTelemetryWithStatePointset(self):
    attrs = {'subFolder': 'pointset', 'subType': 'state'}
    self.assertFalse(message_filters.Udmi.telemetry(attrs))

if __name__ == '__main__':
  absltest.main()
