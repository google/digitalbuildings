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

from model.entity import ReportingEntity
from model.entity import VirtualEntity
from model.guid_to_entity_map import GuidToEntityMap
from model.site import Site
from abel.tests.test_constants import TEST_REPORTING_ENTITY_DICT
from abel.tests.test_constants import TEST_REPORTING_GUID
from abel.tests.test_constants import TEST_SITE_DICT
from abel.tests.test_constants import TEST_SITE_DICT_NO_GUID
from abel.tests.test_constants import TEST_VIRTUAL_ENTITY_DICT

_TEST_REPORTING_ENTITY = ReportingEntity.FromDict(TEST_REPORTING_ENTITY_DICT)
_TEST_VIRTUAL_ENTITY = VirtualEntity.FromDict(TEST_VIRTUAL_ENTITY_DICT)
_TEST_SITE = Site.FromDict(TEST_SITE_DICT)


class GuidToEntityMapTest(absltest.TestCase):

  def setUp(self):
    super().setUp()
    self.guid_to_entity_map = GuidToEntityMap()
    self.guid_to_entity_map.Clear()

  def testAddSite(self):
    self.guid_to_entity_map.AddSite(_TEST_SITE)
    test_site = self.guid_to_entity_map.GetEntityByGuid('test_site_guid')

    self.assertEqual(test_site, _TEST_SITE)

  def testAddSiteRaisesKeyError(self):
    self.guid_to_entity_map.AddSite(_TEST_SITE)

    with self.assertRaises(KeyError):
      self.guid_to_entity_map.AddSite(_TEST_SITE)

  def testAddSiteRaisesAttributeError(self):
    test_site_no_guid = Site.FromDict(TEST_SITE_DICT_NO_GUID)

    with self.assertRaises(AttributeError):
      self.guid_to_entity_map.AddSite(test_site_no_guid)

  def testAddEntity(self):
    self.guid_to_entity_map.AddEntity(_TEST_REPORTING_ENTITY)

    self.assertEqual(
        self.guid_to_entity_map.GetEntityByGuid(_TEST_REPORTING_ENTITY.bc_guid),
        _TEST_REPORTING_ENTITY)
    with self.assertRaises(ValueError):
      self.guid_to_entity_map.AddEntity(None)

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
      self.guid_to_entity_map.GetEntityByGuid('bad_guid')

  def testRemoveEntity(self):
    self.guid_to_entity_map.AddEntity(_TEST_REPORTING_ENTITY)
    self.guid_to_entity_map.AddEntity(_TEST_VIRTUAL_ENTITY)

    removed_entity = self.guid_to_entity_map.RemoveEntity(
        _TEST_REPORTING_ENTITY.bc_guid)

    self.assertEqual(removed_entity, _TEST_REPORTING_ENTITY)

  def testUpdateEntityMapping(self):
    self.guid_to_entity_map.AddEntity(_TEST_REPORTING_ENTITY)
    _TEST_VIRTUAL_ENTITY.guid = _TEST_REPORTING_ENTITY.bc_guid

    self.guid_to_entity_map.UpdateEntityMapping(_TEST_REPORTING_ENTITY.bc_guid,
                                                _TEST_VIRTUAL_ENTITY)

    self.assertEqual(
        self.guid_to_entity_map.GetEntityByGuid(_TEST_REPORTING_ENTITY.bc_guid),
        _TEST_VIRTUAL_ENTITY)
    with self.assertRaises(ValueError):
      self.guid_to_entity_map.UpdateEntityMapping(
          _TEST_REPORTING_ENTITY.bc_guid, None)

  def testMultipleInstancesUseSameMap(self):
    self.guid_to_entity_map.AddEntity(_TEST_REPORTING_ENTITY)

    guid_to_entity_map_2 = GuidToEntityMap()

    self.assertEqual(
        guid_to_entity_map_2.GetEntityByGuid(_TEST_REPORTING_ENTITY.bc_guid),
        _TEST_REPORTING_ENTITY)

  def testGetEntityGuidByCode(self):
    self.guid_to_entity_map.AddEntity(_TEST_REPORTING_ENTITY)

    self.assertEqual(
        self.guid_to_entity_map.GetEntityGuidByCode(
            _TEST_REPORTING_ENTITY.code), _TEST_REPORTING_ENTITY.bc_guid)
    with self.assertRaises(AttributeError):
      self.guid_to_entity_map.GetEntityGuidByCode('bad_code')

  def testGetEntityCodeByGuid(self):
    self.guid_to_entity_map.AddEntity(_TEST_REPORTING_ENTITY)

    self.assertEqual(
        self.guid_to_entity_map.GetEntityCodeByGuid(
            _TEST_REPORTING_ENTITY.bc_guid), _TEST_REPORTING_ENTITY.code)
    with self.assertRaises(KeyError):
      self.guid_to_entity_map.GetEntityCodeByGuid('bad_guid')

  def testGetEntityByGuid(self):
    self.guid_to_entity_map.AddEntity(_TEST_REPORTING_ENTITY)

    self.assertEqual(
        self.guid_to_entity_map.GetEntityByGuid(_TEST_REPORTING_ENTITY.bc_guid),
        _TEST_REPORTING_ENTITY)

  def testClear(self):
    self.guid_to_entity_map.Clear()

    self.assertEmpty(self.guid_to_entity_map.GetGuidToEntityMap())

if __name__ == '__main__':
  absltest.main()

