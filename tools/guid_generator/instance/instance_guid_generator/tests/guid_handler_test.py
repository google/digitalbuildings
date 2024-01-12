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
"""Tests for entity guid_generator."""

import os

import tempfile
from absl.testing import absltest
import strictyaml as syaml

from instance_guid_generator.guid_handler import GuidGenerator
from instance_guid_generator.tests import test_constants
from validate import instance_parser

# pylint:disable=protected-access
_TEST_INSTANCES_PATH = test_constants.TEST_INSTANCES
_CONFIG_METADATA_KEY = instance_parser._CONFIG_METADATA_KEY
ENTITY_GUID_KEY = instance_parser.ENTITY_GUID_KEY
ENTITY_CODE_KEY = instance_parser.ENTITY_CODE_KEY
LINKS_KEY = instance_parser.LINKS_KEY
CONNECTIONS_KEY = instance_parser.CONNECTIONS_KEY


class GuidGeneratorTest(absltest.TestCase):

  # pylint:disable=line-too-long
  def testGuidGenerator_entitiesKeyedWithGuidKeyedByCode_writesBackEntitiesKeyedByGuidSuccess(
      self,
  ):
    input_file_path = os.path.join(
        _TEST_INSTANCES_PATH, 'GOOD', 'building_config_keyed_by_code.yaml'
    )
    with open(input_file_path, 'r', encoding='utf-8') as input_file:
      input_bc_dict = syaml.load(input_file.read()).data

    with open(input_file_path, 'r', encoding='utf-8') as input_file:
      temp_file_path = os.path.join(tempfile.gettempdir(), 'test_bc.yaml')
      with open(temp_file_path, 'w', encoding='utf-8') as temp_file:
        temp_file.write(input_file.read())
      GuidGenerator.GenerateGuids(os.path.abspath(temp_file_path))

    with open(temp_file_path, 'r', encoding='utf-8') as temp_file:
      output_bc_dict = syaml.load(temp_file.read()).data
    input_bc_dict_guid_code = {
        v.get('guid'): k
        for k, v in input_bc_dict.items()
        if k != _CONFIG_METADATA_KEY
    }
    output_bc_dict_guid_code = {
        k: v.get('code')
        for k, v in output_bc_dict.items()
        if k != _CONFIG_METADATA_KEY
    }
    self.assertEqual(len(input_bc_dict), len(output_bc_dict))
    self.assertEqual(input_bc_dict_guid_code, output_bc_dict_guid_code)

  def testGenerateGuid_entityDoesNotHaveGuid_createsGuidOnEntitySuccess(self):
    input_file = os.path.join(
        _TEST_INSTANCES_PATH, 'GOOD', 'building_missing_guid.yaml'
    )

    with open(input_file, 'r', encoding='utf-8') as input_file:
      temp_filepath = os.path.join(tempfile.gettempdir(), 'test_bc.yaml')
      with open(temp_filepath, 'w', encoding='utf-8') as test_file:
        test_file.write(input_file.read())
    GuidGenerator.GenerateGuids(temp_filepath)

    with open(temp_filepath, 'r', encoding='utf-8') as output_file:
      yaml_dict = syaml.load(output_file.read())
    # get the entity attributes
    output_entity_1 = yaml_dict.values()[1]
    output_entity_2 = yaml_dict.values()[2]
    # entity keyed by guid will not have attribute guid
    self.assertIsNotNone(output_entity_1.get(ENTITY_CODE_KEY))
    self.assertIsNotNone(output_entity_2.get(ENTITY_CODE_KEY))
    self.assertIsNone(output_entity_1.get(ENTITY_GUID_KEY))
    self.assertIsNone(output_entity_2.get(ENTITY_GUID_KEY))

  def testGenerateGuid_guidExistsOnEntity_skipsGuidGenerationSuccess(self):
    input_filepath = os.path.join(
        _TEST_INSTANCES_PATH, 'GOOD', 'building_type_keyed_by_guid.yaml'
    )

    with open(input_filepath, 'r', encoding='utf-8') as input_file:
      temp_filepath = os.path.join(tempfile.gettempdir(), 'test_bc.yaml')
      with open(temp_filepath, 'w', encoding='utf-8') as temp_file:
        temp_file.write(input_file.read())
    with open(temp_filepath, 'r', encoding='utf-8') as input_file:
      yaml_dict = syaml.load(input_file.read())
      # this test assumes that entities are keyed by guid
      initial_guids = list(yaml_dict.keys())
    GuidGenerator.GenerateGuids(os.path.abspath(temp_filepath))

    with open(temp_filepath, 'r', encoding='utf-8') as output_file:
      yaml_dict = syaml.load(output_file.read())
      # this is a point test assuming that the entity is keyed by guid
      b_config_dict = dict(yaml_dict)
      # pylint: disable=protected-access
      b_config_dict.pop(_CONFIG_METADATA_KEY, None)
      later_guids = list(b_config_dict.keys())
    self.assertEqual(initial_guids, later_guids)
    self.assertEqual(initial_guids[0], 'BUILDING-GUID')

  def testGenerateGuids_buildingConfigWithGuidKeyedByGuid_skipsGuidGenerationSuccess(
      self,
  ):
    input_file_path = os.path.join(
        _TEST_INSTANCES_PATH, 'GOOD', 'building_config_keyed_by_guid.yaml'
    )

    with open(input_file_path, 'r', encoding='utf-8') as input_file:
      input_file_content = input_file.read()
      temp_file_name = os.path.join(tempfile.gettempdir(), 'test_bc.yaml')
    with open(temp_file_name, 'w', encoding='utf-8') as temp_file:
      temp_file.write(input_file_content)
    GuidGenerator.GenerateGuids(temp_file_name)

    with open(temp_file_name, 'r', encoding='utf-8') as temp_file:
      output_file_content = temp_file.read()
    self.assertEqual(output_file_content, input_file_content)

  def testGenerateGuids_keyedByGuidOrCode_generatesGuidWithOutputKeyedByGuidSuccess(
      self,
  ):
    input_file_path = os.path.join(
        _TEST_INSTANCES_PATH, 'GOOD', 'mixed_building_config.yaml'
    )

    with open(input_file_path, 'r', encoding='utf-8') as input_file:
      temp_file_name = os.path.join(tempfile.gettempdir(), 'test_bc.yaml')
      with open(temp_file_name, 'w', encoding='utf-8') as temp_file:
        temp_file.write(input_file.read())
    GuidGenerator.GenerateGuids(os.path.abspath(temp_file_name))

    with open(temp_file_name, 'r', encoding='utf-8') as temp_file:
      output_yaml = syaml.load(temp_file.read())
    virtual_entity_guid = next(
        key
        for key, value in output_yaml.items()
        if value.get(instance_parser.ENTITY_CODE_KEY, '')
        == 'VIRTUAL-ENTITY-CODE'
    )
    self.assertIn('BUILDING-GUID', output_yaml)
    self.assertIn('GATEWAY-ENTITY-GUID', output_yaml)
    self.assertNotIn('GATEWAY-ENTITY', output_yaml)
    self.assertNotIn('VIRTUAL-ENTITY', output_yaml)
    self.assertNotIn(ENTITY_GUID_KEY, output_yaml['BUILDING-GUID'])
    self.assertNotIn(ENTITY_GUID_KEY, output_yaml['GATEWAY-ENTITY-GUID'])
    self.assertNotIn(ENTITY_GUID_KEY, output_yaml[virtual_entity_guid])
    self.assertEqual(
        output_yaml['BUILDING-GUID'].get(ENTITY_CODE_KEY), 'US-BLDG-CODE'
    )
    self.assertEqual(
        output_yaml['GATEWAY-ENTITY-GUID'].get(ENTITY_CODE_KEY),
        'GATEWAY-ENTITY-CODE',
    )
    self.assertEqual(
        output_yaml[virtual_entity_guid].get(ENTITY_CODE_KEY),
        'VIRTUAL-ENTITY-CODE',
    )
    self.assertIn(
        'BUILDING-GUID',
        output_yaml['GATEWAY-ENTITY-GUID'][CONNECTIONS_KEY],
    )
    self.assertIn(
        'GATEWAY-ENTITY-GUID',
        output_yaml[virtual_entity_guid][LINKS_KEY],
    )


if __name__ == '__main__':
  absltest.main()
