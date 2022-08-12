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

import tempfile
from absl.testing import absltest
import strictyaml as syaml

from guid_handler import GuidGenerator
from tests import test_constants
from validate import instance_parser

_TEST_INSTANCES_PATH = test_constants.TEST_INSTANCES


class GuidGeneratorTest(absltest.TestCase):

  def testGenerateGuidGeneratesGuid(self):
    input_file = os.path.join(_TEST_INSTANCES_PATH, 'GOOD',
                              'building_missing_guid.yaml')

    with open(input_file, 'r', encoding='utf-8') as test_instance:
      temp_file = os.path.join(tempfile.gettempdir(), 'test_bc.yaml')
      with open(temp_file, 'w', encoding='utf-8') as test_file:
        test_file.write(test_instance.read())
      test_filenames = [temp_file]
      for filename in test_filenames:
        GuidGenerator.GenerateGuids(filename)

      for filename in test_filenames:
        with open(filename, 'r', encoding='utf-8') as file:
          yaml_dict = syaml.load(file.read())
          for i in range(1, len(yaml_dict.values())):
            self.assertIsNotNone(
                yaml_dict.values()[i][instance_parser.ENTITY_CODE_KEY])

  def testGenerateGuidSkipsGoodGuid(self):
    input_file = os.path.join(_TEST_INSTANCES_PATH, 'GOOD',
                                   'building_type_keyed_by_guid.yaml')
    with open(input_file, 'r', encoding='utf-8') as test_instance:
      temp_file = os.path.join(tempfile.gettempdir(), 'test_bc.yaml')
      with open(temp_file, 'w', encoding='utf-8') as test_file:
        test_file.write(test_instance.read())
      test_filenames = [temp_file]
      initial_guids = []
      for filename in test_filenames:
        with open(filename, 'r', encoding = 'utf-8') as file:
          yaml_dict = syaml.load(file.read())
          # this test assumes that entities are keyed by guid
          guids = list(yaml_dict.keys())
          initial_guids.extend(guids)

      for filename in test_filenames:
        GuidGenerator.GenerateGuids(os.path.abspath(filename))
      later_guids = []
      for filename in test_filenames:
        with open(filename, 'r', encoding='utf-8') as file:
          yaml_dict = syaml.load(file.read())
          # this is a point test assuming that the entity is keyed by guid
          b_config_dict = dict(yaml_dict)
          # pylint: disable=protected-access
          b_config_dict.pop(instance_parser._CONFIG_METADATA_KEY, None)
          guids = list(b_config_dict.keys())
          later_guids.extend(guids)

      self.assertEqual(initial_guids, later_guids)
      self.assertEqual(initial_guids[0], 'UK-LON-S2-GUID')

  def testGenerateGuidsSkipsGuidBasedFormat(self):
    input_file_content = ''
    output_file_content = ''
    input_file_path = os.path.join(_TEST_INSTANCES_PATH, 'GOOD',
                                   'building_config_keyed_by_guid.yaml')
    with open(input_file_path, 'r', encoding='utf-8') as input_file:
      input_file_content = input_file.read()
      temp_file_name = os.path.join(tempfile.gettempdir(), 'test_bc.yaml')
      with open(temp_file_name, 'w', encoding='utf-8') as temp_file:
        temp_file.write(input_file_content)

      GuidGenerator.GenerateGuids(temp_file_name)
      with open(temp_file_name, 'r', encoding='utf-8') as temp_file:
        output_file_content = temp_file.read()

    self.assertEqual(output_file_content, input_file_content)

  def testGenerateGuidsConvertsMixedFormat(self):
    input_file_path = os.path.join(_TEST_INSTANCES_PATH, 'GOOD',
                                   'mixed_building_config.yaml')
    with open(input_file_path, 'r', encoding='utf-8') as input_file:
      temp_file_name = os.path.join(tempfile.gettempdir(), 'test_bc.yaml')
      with open(temp_file_name, 'w', encoding='utf-8') as temp_file:
        temp_file.write(input_file.read())

    GuidGenerator.GenerateGuids(os.path.abspath(temp_file_name))
    with open(temp_file_name, 'r', encoding='utf-8') as temp_file:
      output_yaml = syaml.load(temp_file.read())
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
