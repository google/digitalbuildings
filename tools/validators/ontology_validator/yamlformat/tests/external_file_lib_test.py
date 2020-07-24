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

"""Tests corp.bizapps.rews.carson.ontology.validation.external_file_lib."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from absl.testing import absltest

from yamlformat.validator import external_file_lib

DIR_ONE_LEVEL = 'fake_resources/dir1/'
DIR_MULTI_DIR = 'fake_resources/dir2/'

FAN = 'FAN.yaml'
FAN_2 = 'FAN2.yaml'


class ExternalFileLibTest(absltest.TestCase):

  def test_RecursiveDirWalk_oneLevel(self):
    path_parts = external_file_lib.RecursiveDirWalk(DIR_ONE_LEVEL)
    path_parts.sort()

    self.assertLen(path_parts, 2)

    path_part_modified_base = path_parts[0]
    self.assertNotEmpty(path_part_modified_base)
    self.assertEqual(path_part_modified_base.root, DIR_ONE_LEVEL)
    self.assertEqual(path_part_modified_base.relative_path,
                     'entity_types/' + FAN)
    path_part_modified_base = path_parts[1]
    self.assertEqual(path_part_modified_base.root, DIR_ONE_LEVEL)
    self.assertEqual(path_part_modified_base.relative_path,
                     'entity_types/' + FAN_2)

  def test_RecursiveDirWalk_multiLevel(self):
    path_parts = external_file_lib.RecursiveDirWalk(DIR_MULTI_DIR)
    path_parts.sort()

    self.assertLen(path_parts, 4)
    path_part_modified_client_fan = path_parts[0]
    self.assertEqual(path_part_modified_client_fan.root, DIR_MULTI_DIR)
    self.assertEqual(path_part_modified_client_fan.relative_path, FAN_2)

    path_part_modified_client_fan = path_parts[1]
    self.assertEqual(path_part_modified_client_fan.root, DIR_MULTI_DIR)
    self.assertEqual(path_part_modified_client_fan.relative_path,
                     'entity_types/' + FAN)

    path_part_modified_client_fan = path_parts[2]
    self.assertEqual(path_part_modified_client_fan.root, DIR_MULTI_DIR)
    self.assertEqual(path_part_modified_client_fan.relative_path,
                     'entity_types/another_entity_types/' + FAN)

    path_part_modified_client_fan = path_parts[3]
    self.assertEqual(path_part_modified_client_fan.root, DIR_MULTI_DIR)
    self.assertEqual(path_part_modified_client_fan.relative_path,
                     'entity_types/another_entity_types2/' + FAN)

if __name__ == '__main__':
  absltest.main()
