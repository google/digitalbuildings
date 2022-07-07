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
"""Tests for GuidToEntityMap class."""

from absl.testing import absltest

from model.constants import BC_GUID
from model.constants import CLOUD_DEVICE_ID
from model.constants import ENTITY_CODE
from model.constants import METADATA
from model.constants import NAMESPACE
from model.constants import TYPE_NAME
from model.entity import ReportingEntity
from model.entity import VirtualEntity
from model.guid_to_entity_map import GuidToEntityMap
from model.site import Site
from google3.third_party.digitalbuildings.tools.concrete_model.tests.test_constants import TEST_CLOUD_DEVICE_ID
from google3.third_party.digitalbuildings.tools.concrete_model.tests.test_constants import TEST_NAMESPACE
from google3.third_party.digitalbuildings.tools.concrete_model.tests.test_constants import TEST_REPORTING_ENTITY_CODE
from google3.third_party.digitalbuildings.tools.concrete_model.tests.test_constants import TEST_REPORTING_GUID
from google3.third_party.digitalbuildings.tools.concrete_model.tests.test_constants import TEST_SITE_DICT
from google3.third_party.digitalbuildings.tools.concrete_model.tests.test_constants import TEST_TYPE_NAME
from google3.third_party.digitalbuildings.tools.concrete_model.tests.test_constants import TEST_VIRTUAL_GUID

_TEST_REPORTING_ENTITY_DICT = {
    ENTITY_CODE: TEST_REPORTING_ENTITY_CODE,
    BC_GUID: TEST_REPORTING_GUID,
    NAMESPACE: TEST_NAMESPACE,
    CLOUD_DEVICE_ID: TEST_CLOUD_DEVICE_ID,
    TYPE_NAME: TEST_TYPE_NAME,
    METADATA + '.test': 'test metadata'
}
_TEST_VIRTUAL_ENTITY_DICT = {
    ENTITY_CODE: 'CHWS-2',
    BC_GUID: TEST_VIRTUAL_GUID,
    NAMESPACE: TEST_NAMESPACE,
    TYPE_NAME: None,
    METADATA + '.test': 'test metadata'
}
_TEST_REPORTING_ENTITY = ReportingEntity.FromDict(_TEST_REPORTING_ENTITY_DICT)
_TEST_VIRTUAL_ENTITY = VirtualEntity.FromDict(_TEST_VIRTUAL_ENTITY_DICT)
_TEST_SITE = Site.FromDict(TEST_SITE_DICT)


class GuidToEntityMapTest(absltest.TestCase):

  def setUp(self):
    super().setUp()
    self.guid_to_entity_map = GuidToEntityMap()

  def testAddSite(self):
    self.guid_to_entity_map.AddSite(_TEST_SITE)

    self.assertEqual(
        self.guid_to_entity_map.GetEntityByGuid('test_site_guid'), _TEST_SITE)
    with self.assertRaises(KeyError):
      self.guid_to_entity_map.AddSite(_TEST_SITE)

  def testAddSiteRaisesAttributeError(self):
    _TEST_SITE.guid = None

    with self.assertRaises(AttributeError):
      self.guid_to_entity_map.AddSite(_TEST_SITE)

  def testAddEntity(self):
    self.guid_to_entity_map.AddEntity(_TEST_REPORTING_ENTITY)

    self.assertEqual(
        self.guid_to_entity_map.GetEntityByGuid(_TEST_REPORTING_ENTITY.guid),
        _TEST_REPORTING_ENTITY)

  def testAddEntityRaisesAttributeError(self):
    _TEST_REPORTING_ENTITY.bc_guid = None

    with self.assertRaises(AttributeError):
      self.guid_to_entity_map.AddEntity(_TEST_REPORTING_ENTITY)

    _TEST_REPORTING_ENTITY.bc_guid = TEST_REPORTING_GUID

  def testAddEntityRaisesKeyError(self):
    self.guid_to_entity_map.AddEntity(_TEST_REPORTING_ENTITY)

    with self.assertRaises(KeyError):
      self.guid_to_entity_map.AddEntity(_TEST_REPORTING_ENTITY)

  def testGetEntityByGuidRaisesKeyError(self):

    with self.assertRaises(KeyError):
      self.guid_to_entity_map.GetEntityByGuid(_TEST_VIRTUAL_ENTITY.guid)

  def testRemoveEntity(self):
    self.guid_to_entity_map.AddEntity(_TEST_REPORTING_ENTITY)
    self.guid_to_entity_map.AddEntity(_TEST_VIRTUAL_ENTITY)

    removed_entity = self.guid_to_entity_map.RemoveEntity(
        _TEST_REPORTING_ENTITY.guid)

    self.assertEqual(removed_entity, _TEST_REPORTING_ENTITY)

  def testUpdateEntityMapping(self):
    self.guid_to_entity_map.AddEntity(_TEST_REPORTING_ENTITY)
    _TEST_VIRTUAL_ENTITY.guid = _TEST_REPORTING_ENTITY.guid

    self.guid_to_entity_map.UpdateEntityMapping(_TEST_REPORTING_ENTITY.guid,
                                                _TEST_VIRTUAL_ENTITY)

    self.assertEqual(
        self.guid_to_entity_map.GetEntityByGuid(_TEST_REPORTING_ENTITY.guid),
        _TEST_VIRTUAL_ENTITY)

  def testMultipleInstancesUseSameMap(self):
    self.guid_to_entity_map.AddEntity(_TEST_REPORTING_ENTITY)

    guid_to_entity_map_2 = GuidToEntityMap()

    self.assertEqual(
        guid_to_entity_map_2.GetEntityByGuid(_TEST_REPORTING_ENTITY.guid),
        _TEST_REPORTING_ENTITY)

  def testGetEntityGuidByCode(self):
    self.guid_to_entity_map.AddEntity(_TEST_REPORTING_ENTITY)

    self.assertEqual(
        self.guid_to_entity_map.GetEntityGuidByCode(
            _TEST_REPORTING_ENTITY.code), _TEST_REPORTING_ENTITY.guid)
    with self.assertRaises(KeyError):
      self.guid_to_entity_map.GetEntityByGuid('bad_code')

  def testGetEntityCodeByGuid(self):
    self.guid_to_entity_map.AddEntity(_TEST_REPORTING_ENTITY)

    self.assertEqual(
        self.guid_to_entity_map.GetEntityCodeByGuid(
            _TEST_REPORTING_ENTITY.bc_guid), _TEST_REPORTING_ENTITY.code)
    with self.assertRaises(KeyError):
      self.guid_to_entity_map.GetEntityByGuid('bad_guid')

  def testGetEntityByGuid(self):
    self.guid_to_entity_map.AddEntity(_TEST_REPORTING_ENTITY)

    self.assertEqual(
        self.guid_to_entity_map.GetEntityByGuid(_TEST_REPORTING_ENTITY.bc_guid),
        _TEST_REPORTING_ENTITY)
    with self.assertRaises(KeyError):
      self.guid_to_entity_map.GetEntityByGuid('bad_guid')
