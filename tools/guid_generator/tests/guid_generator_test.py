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
"""Tests for guid_generator."""

import os

from absl.testing import absltest
import strictyaml as syaml

from guid_generator import guid_generator
from tests import test_constants
from validate import instance_parser

_TESTCASE_PATH = test_constants.TEST_INSTANCES


class GuidGeneratorTest(absltest.TestCase):

  @classmethod
  def setUpClass(cls):
    super(cls, GuidGeneratorTest).setUpClass()
    cls.test_generator = guid_generator.GuidGenerator()

  def testGenerateGuidGeneratesGuid(self):
    input_file = os.path.join(_TESTCASE_PATH, 'GOOD',
                              'good_building_missing_guid.yaml')

    with open(input_file, 'r', encoding='utf-8') as test_instance:
      test_filenames = [self.create_tempfile(content=test_instance.read())]
      for filename in test_filenames:
        self.test_generator.GenerateGuids(filename)

      for filename in test_filenames:
        yaml_dict = syaml.load(filename.read_text())
        for i in range(1, len(yaml_dict.values())):
          self.assertIsNotNone(
              yaml_dict.values()[i][instance_parser.ENTITY_GUID_KEY])

  def testGenerateGuidSkipsGoodGuid(self):
    input_file = os.path.join(_TESTCASE_PATH, 'GOOD', 'good_building_type.yaml')
    with open(input_file, 'r', encoding='utf-8') as test_instance:
      test_filenames = [self.create_tempfile(content=test_instance.read())]
      initial_guids = []
      for filename in test_filenames:
        yaml_dict = syaml.load(filename.read_text())
        for value in yaml_dict.values():
          initial_guids.append(value[instance_parser.ENTITY_GUID_KEY])

      for filename in test_filenames:
        self.test_generator.GenerateGuids(filename.full_path)
      later_guids = []
      for filename in test_filenames:
        yaml_dict = syaml.load(filename.read_text())
        # Starting at the second element to skip over config metadata block
        for i in range(1, len(yaml_dict.values())):
          later_guids.append(
              yaml_dict.values()[i][instance_parser.ENTITY_GUID_KEY])

      self.assertEqual(initial_guids, later_guids)
      self.assertEqual(initial_guids[0], '12345')


if __name__ == '__main__':
  absltest.main()
