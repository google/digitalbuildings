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
"""Tests for Entity class."""

from absl.testing import absltest

# pylint: disable=g-importing-member
from model.connection import Connection
from model.constants import BC_GUID
from model.constants import CONDITION
from model.constants import CONDITION_TYPE
from model.constants import CONNECTION_TYPE
from model.constants import DATA_VALIDATION
from model.constants import ENTITY_CODE
from model.constants import ETAG
from model.constants import IS_REPORTING_FALSE
from model.constants import IS_REPORTING_TRUE
from model.constants import NAMESPACE
from model.constants import ONE_OF_LIST
from model.constants import SHOW_CUSTOM_UI
from model.constants import SOURCE_ENTITY_GUID
from model.constants import STRICT_VALIDATION
from model.constants import STRING_VALUE
from model.constants import TARGET_ENTITY_GUID
from model.constants import TYPE_NAME
from model.constants import USER_ENTERED_VALUE
from model.constants import VALUES
from model.entity import ReportingEntity
from model.entity import VirtualEntity
from model.entity_enumerations import EntityNamespace
from model.entity_field import DimensionalValueField
from tests.test_constants import TEST_CLOUD_DEVICE_ID
from tests.test_constants import TEST_DIMENSIONAL_VALUE_FIELD_DICT
from tests.test_constants import TEST_ETAG
from tests.test_constants import TEST_NAMESPACE
from tests.test_constants import TEST_REPORTING_ENTITY_CODE
from tests.test_constants import TEST_REPORTING_ENTITY_DICT
from tests.test_constants import TEST_REPORTING_GUID
from tests.test_constants import TEST_TYPE_NAME
from tests.test_constants import TEST_VIRTUAL_ENTITY_CODE
from tests.test_constants import TEST_VIRTUAL_ENTITY_DICT
from tests.test_constants import TEST_VIRTUAL_GUID


# pylint: disable=unnecessary-dunder-call
class EntityTest(absltest.TestCase):

  def testVirtualEntityInstantiatesFromDict(self):
    test_virtual_entity = VirtualEntity.FromDict(TEST_VIRTUAL_ENTITY_DICT)

    self.assertEqual(test_virtual_entity.code, TEST_VIRTUAL_ENTITY_CODE)
    self.assertEqual(test_virtual_entity.bc_guid, TEST_VIRTUAL_GUID)
    self.assertEqual(test_virtual_entity.namespace, TEST_NAMESPACE)
    self.assertEqual(test_virtual_entity.type_name, TEST_TYPE_NAME)

  def testReportingEntityInstantiatesFromDict(self):
    test_reporting_entity = ReportingEntity.FromDict(TEST_REPORTING_ENTITY_DICT)

    self.assertEqual(test_reporting_entity.code, TEST_REPORTING_ENTITY_CODE)
    self.assertEqual(test_reporting_entity.bc_guid, TEST_REPORTING_GUID)
    self.assertEqual(test_reporting_entity.namespace, TEST_NAMESPACE)
    self.assertEqual(test_reporting_entity.type_name, TEST_TYPE_NAME)
    self.assertEqual(
        test_reporting_entity.cloud_device_id, TEST_CLOUD_DEVICE_ID
    )

  def testVirtualEntityEquality(self):
    test_entity_1 = VirtualEntity.FromDict(TEST_VIRTUAL_ENTITY_DICT)
    test_entity_2 = VirtualEntity.FromDict(TEST_VIRTUAL_ENTITY_DICT)

    self.assertEqual(test_entity_1, test_entity_2)

  def testVirtualEntityInequality(self):
    test_virtual_entity_dict_2 = {
        ENTITY_CODE: 'CHWS-2',
        BC_GUID: None,
        ETAG: '7654321',
        NAMESPACE: TEST_NAMESPACE,
        TYPE_NAME: None,
    }
    test_entity_1 = VirtualEntity.FromDict(TEST_VIRTUAL_ENTITY_DICT)
    test_entity_2 = VirtualEntity.FromDict(test_virtual_entity_dict_2)

    self.assertNotEqual(test_entity_1, test_entity_2)
    self.assertNotEqual(test_entity_1, 'not_an_entity')

  def testReportingEntityEquality(self):
    test_reporting_entity_1 = ReportingEntity.FromDict(
        TEST_REPORTING_ENTITY_DICT
    )
    test_reporting_entity_2 = ReportingEntity.FromDict(
        TEST_REPORTING_ENTITY_DICT
    )

    self.assertEqual(test_reporting_entity_1, test_reporting_entity_2)

  def testReportingEntityInequality(self):
    test_reporting_entity_1 = ReportingEntity.FromDict(
        TEST_REPORTING_ENTITY_DICT
    )
    test_reporting_entity_2 = ReportingEntity.FromDict(
        TEST_REPORTING_ENTITY_DICT
    )
    test_reporting_entity_2.etag = 'not_an_etag'

    self.assertNotEqual(test_reporting_entity_1, test_reporting_entity_2)
    self.assertNotEqual(test_reporting_entity_1, 'not_an_entity')

  def testAddConnection(self):
    test_connection = Connection.FromDict({
        SOURCE_ENTITY_GUID: 'source_guid',
        TARGET_ENTITY_GUID: TEST_REPORTING_GUID,
        CONNECTION_TYPE: 'CONTROLS',
    })
    test_entity = ReportingEntity.FromDict(TEST_REPORTING_ENTITY_DICT)

    test_entity.AddConnection(test_connection)

    self.assertEqual(test_entity.connections.pop(), test_connection)

  def testAddConnectionRaisesTypeError(self):
    test_entity = ReportingEntity.FromDict(TEST_REPORTING_ENTITY_DICT)

    with self.assertRaises(TypeError):
      test_entity.AddConnection('Not a connection instance.')

  def testAddConnectionRaisesAttributeError(self):
    test_entity = ReportingEntity.FromDict(TEST_REPORTING_ENTITY_DICT)
    bad_connection_dict = {
        SOURCE_ENTITY_GUID: 'source_entity_guid',
        TARGET_ENTITY_GUID: 'bad_target_entity_guid',
        CONNECTION_TYPE: 'FEEDS',
    }
    bad_connection = Connection.FromDict(bad_connection_dict)

    with self.assertRaises(AttributeError):
      test_entity.AddConnection(bad_connection)

  def testAddTranslation(self):
    test_field = DimensionalValueField.FromDict(
        TEST_DIMENSIONAL_VALUE_FIELD_DICT
    )
    test_reporting_entity = ReportingEntity.FromDict(TEST_REPORTING_ENTITY_DICT)

    test_reporting_entity.AddTranslation(test_field)

    self.assertIn(test_field, test_reporting_entity.translations)

  def testAddTranslationRaisesTypeError(self):
    test_reporting_entity = ReportingEntity.FromDict(TEST_REPORTING_ENTITY_DICT)

    with self.assertRaises(TypeError):
      test_reporting_entity.AddTranslation('not an entity field')

  def testAddLink(self):
    test_field = DimensionalValueField.FromDict(
        TEST_DIMENSIONAL_VALUE_FIELD_DICT
    )
    test_virtual_entity = VirtualEntity.FromDict(TEST_VIRTUAL_ENTITY_DICT)

    test_virtual_entity.AddLink(test_field)

    self.assertIn(test_field, test_virtual_entity.links)

  def testAddLinkRaisesTypeError(self):
    test_virtual_entity = VirtualEntity.FromDict(TEST_VIRTUAL_ENTITY_DICT)

    with self.assertRaises(TypeError):
      test_virtual_entity.AddLink('not an entity field')

  def testVirtualGetSpreadsheetRowMapping(self):
    test_virtual_entity = VirtualEntity.FromDict(TEST_VIRTUAL_ENTITY_DICT)
    expected_row_mapping = {
        VALUES: [
            {USER_ENTERED_VALUE: {STRING_VALUE: TEST_VIRTUAL_ENTITY_CODE}},
            {USER_ENTERED_VALUE: {STRING_VALUE: TEST_VIRTUAL_GUID}},
            {USER_ENTERED_VALUE: {STRING_VALUE: TEST_ETAG}},
            {
                USER_ENTERED_VALUE: {STRING_VALUE: IS_REPORTING_FALSE},
                DATA_VALIDATION: {
                    CONDITION: {
                        CONDITION_TYPE: ONE_OF_LIST,
                        VALUES: [
                            {USER_ENTERED_VALUE: IS_REPORTING_TRUE},
                            {USER_ENTERED_VALUE: IS_REPORTING_FALSE},
                        ],
                    },
                    STRICT_VALIDATION: True,
                    SHOW_CUSTOM_UI: True,
                },
            },
            {USER_ENTERED_VALUE: {STRING_VALUE: None}},
            {
                USER_ENTERED_VALUE: {STRING_VALUE: TEST_NAMESPACE},
                DATA_VALIDATION: {
                    CONDITION: {
                        CONDITION_TYPE: ONE_OF_LIST,
                        VALUES: [
                            {USER_ENTERED_VALUE: namespace.value}
                            for namespace in EntityNamespace
                        ],
                    },
                    STRICT_VALIDATION: True,
                    SHOW_CUSTOM_UI: True,
                },
            },
            {USER_ENTERED_VALUE: {STRING_VALUE: TEST_TYPE_NAME}},
        ]
    }

    row_mapping = test_virtual_entity.GetSpreadsheetRowMapping()

    self.assertEqual(expected_row_mapping, row_mapping)

  def testRepr(self):
    test_virtual_entity = VirtualEntity.FromDict(TEST_VIRTUAL_ENTITY_DICT)

    self.assertEqual(
        str(test_virtual_entity),
        f'{test_virtual_entity.bc_guid}: {test_virtual_entity.code}',
    )


if __name__ == '__main__':
  absltest.main()
