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

from guid_generator.guid_generator import GuidGenerator
from guid_generator.tests import test_constants
from validate import instance_parser

_TEST_INSTANCES_PATH = test_constants.TEST_INSTANCES


class GuidGeneratorTest(absltest.TestCase):

  def testGenerateGuidGeneratesGuid(self):
    input_file = os.path.join(_TEST_INSTANCES_PATH, 'GOOD',
                              'building_missing_guid.yaml')

    with open(input_file, 'r', encoding='utf-8') as test_instance:
      test_filenames = [self.create_tempfile(content=test_instance.read())]
      for filename in test_filenames:
        GuidGenerator.GenerateGuids(filename)

      for filename in test_filenames:
        yaml_dict = syaml.load(filename.read_text())
        for i in range(1, len(yaml_dict.values())):
          self.assertIsNotNone(
              yaml_dict.values()[i][instance_parser.ENTITY_CODE_KEY])

  def testGenerateGuidSkipsGoodGuid(self):
    input_file_path = os.path.join(_TEST_INSTANCES_PATH, 'GOOD',
                                   'building_type_keyed_by_guid.yaml')
    with open(input_file_path, 'r', encoding='utf-8') as test_instance:
      test_filenames = [self.create_tempfile(content=test_instance.read())]
      initial_guids = []
      for filename in test_filenames:
        yaml_dict = syaml.load(filename.read_text())
        # this test assumes that entities are keyed by guid
        guids = list(yaml_dict.keys())
        initial_guids.extend(guids)

      for filename in test_filenames:
        GuidGenerator.GenerateGuids(filename.full_path)
      later_guids = []
      for filename in test_filenames:
        yaml_dict = syaml.load(filename.read_text())
        # this is a point test assuming that the entity is keyed by guid
        b_config_dict = dict(yaml_dict)
        b_config_dict.pop(instance_parser._CONFIG_METADATA_KEY, None)
        guids = list(b_config_dict.keys())
        later_guids.extend(guids)

      self.assertEqual(initial_guids, later_guids)
      self.assertEqual(initial_guids[0], 'UK-LON-S2-GUID')

  def testGenerateGuidsSkipsGuidBasedFormat(self):
    input_file_path = os.path.join(_TEST_INSTANCES_PATH, 'GOOD',
                                   'building_config_keyed_by_guid.yaml')
    with open(input_file_path, 'r', encoding='utf-8') as input_file:
      input_file_content = input_file.read()
    test_file = self.create_tempfile(content=input_file_content)

    GuidGenerator.GenerateGuids(test_file.full_path)
    output_file_content = test_file.read_text()

    self.assertEqual(output_file_content, input_file_content)

  def testGenerateGuidsConvertsMixedFormat(self):
    input_file_path = os.path.join(_TEST_INSTANCES_PATH, 'GOOD',
                                   'mixed_building_config.yaml')
    with open(input_file_path, 'r', encoding='utf-8') as input_file:
      input_file_content = input_file.read()
    test_file = self.create_tempfile(content=input_file_content)

    GuidGenerator.GenerateGuids(test_file.full_path)
    output_yaml = syaml.load(test_file.read_text())
    virtual_entity_guid = next(
        key for key, value in output_yaml.items()
        if value.get(instance_parser.ENTITY_CODE_KEY, '') == 'VIRTUAL-ENTITY')

    self.assertIn('BUILDING-GUID', output_yaml)
    self.assertIn('GATEWAY-ENTITY-GUID', output_yaml)
    self.assertNotIn('GATEWAY-ENTITY', output_yaml)
    self.assertNotIn('VIRTUAL-ENTITY', output_yaml)
    self.assertNotIn(instance_parser.ENTITY_GUID_KEY,
                     output_yaml['BUILDING-GUID'])
    self.assertNotIn(instance_parser.ENTITY_GUID_KEY,
                     output_yaml['GATEWAY-ENTITY-GUID'])
    self.assertNotIn(instance_parser.ENTITY_GUID_KEY,
                     output_yaml[virtual_entity_guid])
    self.assertEqual(
        output_yaml['BUILDING-GUID'].get(instance_parser.ENTITY_CODE_KEY),
        'BUILDING')
    self.assertEqual(
        output_yaml['GATEWAY-ENTITY-GUID'].get(instance_parser.ENTITY_CODE_KEY),
        'GATEWAY-ENTITY')
    self.assertEqual(
        output_yaml[virtual_entity_guid].get(instance_parser.ENTITY_CODE_KEY),
        'VIRTUAL-ENTITY')
    self.assertIn(
        'BUILDING-GUID',
        output_yaml['GATEWAY-ENTITY-GUID'][instance_parser.CONNECTIONS_KEY])
    self.assertIn('GATEWAY-ENTITY-GUID',
                  output_yaml[virtual_entity_guid][instance_parser.LINKS_KEY])


if __name__ == '__main__':
  absltest.main()
