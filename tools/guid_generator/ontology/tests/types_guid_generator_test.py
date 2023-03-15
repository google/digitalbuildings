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

"""Tests for types_guid_generator."""

import os

import tempfile
from absl.testing import absltest
import strictyaml as syaml

from google3.third_party.digitalbuildings.tools.guid_generator.ontology.tests import test_constants
from google3.third_party.digitalbuildings.tools.guid_generator.ontology.types_guid_generator import GenerateGuids

_TEST_INSTANCES_PATH = test_constants.TEST_INSTANCES


class TypesGuidGeneratorTest(absltest.TestCase):

  def testTypesGuidGenerator_allTypesHaveGuids_outputFileUnchangedSuccess(self):
    input_file_path = os.path.join(_TEST_INSTANCES_PATH,
                                   'entity_types_with_guids.yaml')
    temp_dir = tempfile.mkdtemp(suffix='entity_types')
    temp_file_path = os.path.join(temp_dir, 'test.yaml')

    with open(input_file_path, encoding='utf-8') as input_file, open(
        temp_file_path, 'w', encoding='utf-8') as temp_file:
      input_file_content = input_file.read()
      temp_file.write(input_file_content)
    GenerateGuids(os.path.abspath(temp_file_path))

    with open(temp_file_path, encoding='utf-8') as temp_file:
      output_file_content = temp_file.read()
    self.assertEqual(input_file_content, output_file_content)

  def testTypesGuidGenerator_generatesGuidsWhenMissing_success(self):
    input_file_path = os.path.join(_TEST_INSTANCES_PATH,
                                   'entity_types_with_missing_guids.yaml')
    temp_dir = tempfile.mkdtemp(suffix='entity_types')
    temp_file_path = os.path.join(temp_dir, 'test.yaml')

    with open(input_file_path, encoding='utf-8') as input_file, open(
        temp_file_path, 'w', encoding='utf-8') as temp_file:
      temp_file.write(input_file.read())
    GenerateGuids(os.path.abspath(temp_file_path))

    with open(temp_file_path, encoding='utf-8') as temp_file:
      yaml_dict = syaml.load(temp_file.read())
    type_content_1 = yaml_dict.values()[0]
    type_content_2 = yaml_dict.values()[1]
    type_content_3 = yaml_dict.values()[2]
    self.assertIsNotNone(type_content_1.get('guid'))
    self.assertIsNotNone(type_content_2.get('guid'))
    self.assertIsNotNone(type_content_3.get('guid'))

if __name__ == '__main__':
  absltest.main()
