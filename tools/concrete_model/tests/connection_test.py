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
"""Tests for Connection class."""

from absl.testing import absltest

from model.connection import Connection
from model.connection_type import ConnectionType


class ConnectionTest(absltest.TestCase):

  def setUp(self):
    super().setUp()
    self.source_entity_guid = '1234'
    self.target_entity_guid = '5678'
    self.valid_connection_type = ConnectionType.FEEDS

  def testConnectionInitsFromDict(self):
    """Tests that a Connection instance is correctly initialized using the FromDict() class method."""
    test_connection_dict = {
        'source_entity_guid': self.source_entity_guid,
        'target_entity_guid': self.target_entity_guid,
        'connection_type': self.valid_connection_type
    }
    test_connection_instance = Connection.FromDict(test_connection_dict)

    self.assertIsInstance(test_connection_instance, Connection)
    self.assertEqual(self.valid_connection_type,
                     test_connection_instance.connection_type)
    self.assertEqual(self.source_entity_guid,
                     test_connection_instance.source_entity_guid)
    self.assertEqual(self.target_entity_guid,
                     test_connection_instance.target_entity_guid)

  def testInvalidConnectionTypeRaisesTypeError(self):
    """Test that a type error is raised when connection type is not passed in as a ConnectionType instance."""
    test_connection_dict = {
        'source_entity_guid': self.source_entity_guid,
        'target_entity_guid': self.target_entity_guid,
        'connection_type': 'FEEDS'
    }

    with self.assertRaises(TypeError):
      Connection.FromDict(test_connection_dict)

if __name__ == '__main__':
  absltest.main()
