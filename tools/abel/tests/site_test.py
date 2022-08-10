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
"""Tests for Site class."""


from absl.testing import absltest

from model.constants import BC_GUID
from model.constants import BUILDING_CODE
from model.constants import CLOUD_DEVICE_ID
from model.constants import ENTITY_CODE
from model.constants import METADATA
from model.constants import NAMESPACE
from model.constants import TYPE_NAME
from model.entity import ReportingEntity
from model.site import Site
from abel.tests.test_constants import TEST_CLOUD_DEVICE_ID
from abel.tests.test_constants import TEST_NAMESPACE
from abel.tests.test_constants import TEST_REPORTING_ENTITY_CODE
from abel.tests.test_constants import TEST_REPORTING_GUID
from abel.tests.test_constants import TEST_TYPE_NAME

_TEST_REPORTING_ENTITY_DICT = {
    ENTITY_CODE: TEST_REPORTING_ENTITY_CODE,
    BC_GUID: TEST_REPORTING_GUID,
    NAMESPACE: TEST_NAMESPACE,
    CLOUD_DEVICE_ID: TEST_CLOUD_DEVICE_ID,
    TYPE_NAME: TEST_TYPE_NAME,
    METADATA + '.test': 'test metadata'
}
_TEST_SITE_DICT = {
    BUILDING_CODE: 'UK-LON-S2',
    BC_GUID: 'test_site_guid',
}
_TEST_REPORTING_ENTITY = ReportingEntity.FromDict(_TEST_REPORTING_ENTITY_DICT)


class SiteTest(absltest.TestCase):

  def testSiteInitializesFromDict(self):
    test_site = Site.FromDict(_TEST_SITE_DICT)

    self.assertEqual(test_site.code, 'UK-LON-S2')
    self.assertEqual(test_site.guid, 'test_site_guid')

  def testSiteAddsEntity(self):
    test_site = Site.FromDict(_TEST_SITE_DICT)

    test_site.AddEntity(_TEST_REPORTING_ENTITY)

    self.assertEqual(test_site.entities, [_TEST_REPORTING_ENTITY.bc_guid])

if __name__ == '__main__':
  absltest.main()
