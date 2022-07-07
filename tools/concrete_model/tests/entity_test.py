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
"""Tests for Entity class."""

from absl.testing import absltest

from model.connection import Connection
from model.constants import BC_GUID
from model.constants import CLOUD_DEVICE_ID
from model.constants import CONNECTION_TYPE
from model.constants import ENTITY_CODE
from model.constants import ETAG
from model.constants import IS_REPORTING
from model.constants import METADATA
from model.constants import NAMESPACE
from model.constants import SOURCE_ENTITY_GUID
from model.constants import TARGET_ENTITY_GUID
from model.constants import TYPE_NAME
from model.entity import ReportingEntity
from model.entity import VirtualEntity
from model.entity_field import EntityField
from google3.third_party.digitalbuildings.tools.concrete_model.tests.test_constants import TEST_CLOUD_DEVICE_ID
from google3.third_party.digitalbuildings.tools.concrete_model.tests.test_constants import TEST_ENTITY_FIELD_DICT_WITH_UNITS
from google3.third_party.digitalbuildings.tools.concrete_model.tests.test_constants import TEST_NAMESPACE
from google3.third_party.digitalbuildings.tools.concrete_model.tests.test_constants import TEST_REPORTING_ENTITY_CODE
from google3.third_party.digitalbuildings.tools.concrete_model.tests.test_constants import TEST_REPORTING_ENTITY_DICT
from google3.third_party.digitalbuildings.tools.concrete_model.tests.test_constants import TEST_REPORTING_GUID
from google3.third_party.digitalbuildings.tools.concrete_model.tests.test_constants import TEST_TYPE_NAME
from google3.third_party.digitalbuildings.tools.concrete_model.tests.test_constants import TEST_VIRTUAL_ENTITY_CODE
from google3.third_party.digitalbuildings.tools.concrete_model.tests.test_constants import TEST_VIRTUAL_ENTITY_DICT
from google3.third_party.digitalbuildings.tools.concrete_model.tests.test_constants import TEST_VIRTUAL_GUID


class EntityTest(absltest.TestCase):

  def testVirtualEntityInstantiatesFromDict(self):

    test_virtual_entity = VirtualEntity.FromDict(TEST_VIRTUAL_ENTITY_DICT)

    self.assertEqual(test_virtual_entity.code, TEST_VIRTUAL_ENTITY_CODE)
    self.assertEqual(test_virtual_entity.bc_guid, TEST_VIRTUAL_GUID)
    self.assertEqual(test_virtual_entity.namespace, TEST_NAMESPACE)
    self.assertEqual(test_virtual_entity.type_name, TEST_TYPE_NAME)
    self.assertEqual(test_virtual_entity.metadata, {'test': 'test metadata'})

  def testReportingEntityInstantiatesFromDict(self):

    test_reporting_entity = ReportingEntity.FromDict(TEST_REPORTING_ENTITY_DICT)

    self.assertEqual(test_reporting_entity.code, TEST_REPORTING_ENTITY_CODE)
    self.assertEqual(test_reporting_entity.bc_guid, TEST_REPORTING_GUID)
    self.assertEqual(test_reporting_entity.namespace, TEST_NAMESPACE)
    self.assertEqual(test_reporting_entity.type_name, TEST_TYPE_NAME)
    self.assertEqual(test_reporting_entity.cloud_device_id,
                     TEST_CLOUD_DEVICE_ID)
    self.assertEqual(test_reporting_entity.metadata, {'test': 'test metadata'})

  def testEntityEquality(self):
    test_entity_1 = VirtualEntity.FromDict(TEST_VIRTUAL_ENTITY_DICT)
    test_entity_2 = VirtualEntity.FromDict(TEST_VIRTUAL_ENTITY_DICT)

    self.assertEqual(test_entity_1, test_entity_2)

  def testEntityInequality(self):
    test_virtual_entity_dict_2 = {
        ENTITY_CODE: 'CHWS-2',
        BC_GUID: None,
        ETAG: '7654321',
        NAMESPACE: TEST_NAMESPACE,
        TYPE_NAME: None,
        METADATA + '.test': 'test metadata'
    }

    test_entity_1 = VirtualEntity.FromDict(TEST_VIRTUAL_ENTITY_DICT)
    test_entity_2 = VirtualEntity.FromDict(test_virtual_entity_dict_2)

    self.assertNotEqual(test_entity_1, test_entity_2)

  # TODO(b/228974634) Write tests once Entity dependencies are merged.
  def testAddConnection(self):
    test_connection = Connection.FromDict({
        SOURCE_ENTITY_GUID: 'source_guid',
        TARGET_ENTITY_GUID: TEST_REPORTING_GUID,
        CONNECTION_TYPE: 'CONTROLS'
    })
    test_entity = ReportingEntity.FromDict(TEST_REPORTING_ENTITY_DICT)

    test_entity.connections = [test_connection]

    self.assertEqual(test_entity.connections.pop(), test_connection)

  def testAddTranslation(self):
    test_field = EntityField.FromDict(TEST_ENTITY_FIELD_DICT_WITH_UNITS)
    test_reporting_entity = ReportingEntity.FromDict(TEST_REPORTING_ENTITY_DICT)

    test_reporting_entity.translations = [test_field]

  def testAddLink(self):
    test_field = EntityField.FromDict(TEST_ENTITY_FIELD_DICT_WITH_UNITS)
    test_virtual_entity = VirtualEntity.FromDict(TEST_VIRTUAL_ENTITY_DICT)

    test_virtual_entity.links = [test_field]

  def testVirtualGetSpreadsheetRowMapping(self):
    test_virtual_entity = VirtualEntity.FromDict(TEST_VIRTUAL_ENTITY_DICT)
    expected_row_mapping = {
        ENTITY_CODE: TEST_VIRTUAL_ENTITY_CODE,
        BC_GUID: TEST_VIRTUAL_GUID,
        IS_REPORTING: False,
        CLOUD_DEVICE_ID: None,
        ETAG: None,
        NAMESPACE: TEST_NAMESPACE,
        TYPE_NAME: TEST_TYPE_NAME
    }

    row_mapping = test_virtual_entity.GetSpreadsheetRowMapping()

    self.assertEqual(expected_row_mapping, row_mapping)


if __name__ == '__main__':
  absltest.main()
