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
"""Tests for google3.corp.bizapps.rews.carson.ontology.validation.base_lib."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from absl.testing import absltest
from yamlformat.validator import base_lib


class BaseLibTest(absltest.TestCase):

  def testHasDeprecatedType(self):
    hdt = base_lib.HasDeprecatedType
    self.assertTrue(hdt(['DEPRECATED']))
    self.assertTrue(hdt(['/DEPRECATED']))
    self.assertTrue(hdt(['HVAC/DEPRECATED']))
    self.assertTrue(hdt(['INCOMPLETE']))
    self.assertTrue(hdt(['/INCOMPLETE']))
    self.assertTrue(hdt(['HVAC/INCOMPLETE']))
    self.assertFalse(hdt(['OTHER_TYPE']))

  def testGetEquipmentClass(self):
    eq = base_lib.GetEquipmentClass
    self.assertEqual(eq('FCU_RH_1'), 'FCU')
    self.assertEqual(eq('FCU_RH'), 'FCU')
    self.assertEqual(eq('FCU'), 'FCU')
    self.assertEqual(eq('HVAC/FCU'), 'FCU')
    self.assertEqual(eq('/FCU'), 'FCU')
    self.assertIsNone(eq('123'))

  def testComponentTypeFromString(self):
    self.assertEqual(
        base_lib.ComponentType.FromString('fields'),
        base_lib.ComponentType.FIELD)

  def testComponentTypeFromStringBadValue(self):
    with self.assertRaises(LookupError):
      base_lib.ComponentType.FromString('bad')

  def testGetTreeLocation(self):
    testpath = 'HVAC/fields'

    folderpath, component = base_lib.GetTreeLocation(testpath)

    self.assertEqual(folderpath, 'HVAC/fields')
    self.assertEqual(base_lib.ComponentType.FIELD, component)

  def testGetTreeLocationGlobal(self):
    testpath = 'fields'

    folderpath, component = base_lib.GetTreeLocation(testpath)

    self.assertEqual(folderpath, 'fields')
    self.assertEqual(base_lib.ComponentType.FIELD, component)

  def testGetTreeLocationWithSubdirs(self):
    testpath = 'HVAC/fields/subdir1/subdir2'

    folderpath, component = base_lib.GetTreeLocation(testpath)

    self.assertEqual(folderpath, 'HVAC/fields')
    self.assertEqual(base_lib.ComponentType.FIELD, component)

  def testGetTreeLocationWithBadSubdirs(self):
    testpath = 'HVAC/bad/fields'
    with self.assertRaises(ValueError):
      _, _ = base_lib.GetTreeLocation(testpath)

  def testGetTreeLocationWithBadParentDirs(self):
    testpath = 'bad/HVAC/fields'
    with self.assertRaises(ValueError):
      _, _ = base_lib.GetTreeLocation(testpath)

if __name__ == '__main__':
  absltest.main()
