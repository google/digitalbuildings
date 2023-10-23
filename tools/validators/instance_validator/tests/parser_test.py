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
"""Tests tools.validators.instance_validator.instance_parser."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os.path
import yaml
from os import path

from absl.testing import absltest

from tests import test_constants
from validate import handler
from validate import parser as p
from validate import enumerations


# _TESTCASE_PATH = test_constants.TEST_INSTANCES

class ParserTest(absltest.TestCase):
  def setUp(self):
    self.parser = p.Parser(schema_folder='../schemas')
  def testGetDefaultEntityOperation(self):
    pass

  def testDeserializeGoodBuildingConfig(self):
    pass

  def testDeserialize_DuplicateKeys_Fails(self):
    bad_testcase_path = [os.path.join(os.path.abspath('./fake_instances'), 'BAD', 'duplicate_keys.yaml')]

    entities, config_mode = self.parser.Deserialize(yaml_files=bad_testcase_path)

    self.assertEqual(config_mode, enumerations.ConfigMode.EXPORT)
    self.assertLen(entities, 0)

  def testDeserialize_NoConfigModeRaisesKeyError(self):
    bad_testcase_path = [os.path.join(os.path.abspath('./fake_instances'), 'BAD', 'no_config_metadata.yaml')]

    with self.assertRaises(KeyError):
      self.parser.Deserialize(yaml_files=bad_testcase_path)

  def testDeserialize_MissingColon_Fails(self):
    bad_testcase_path = [os.path.join(os.path.abspath('./fake_instances'), 'BAD', 'missing_colon.yaml')]

    with self.assertRaises(yaml.scanner.ScannerError):
      self.parser.Deserialize(yaml_files=bad_testcase_path)

  def testDeserialize_BadSpacing_Fails(self):
    bad_testcase_path = [os.path.join(os.path.abspath('./fake_instances'), 'BAD', 'spacing.yaml')]

    with self.assertRaises(yaml.scanner.ScannerError):
      self.parser.Deserialize(yaml_files=bad_testcase_path)

  def testDeserialize_BadSpacing_Fails(self):
    bad_testcase_path = [os.path.join(os.path.abspath('./fake_instances'), 'BAD', 'tabbing.yaml')]

    with self.assertRaises(yaml.parser.ParserError):
      self.parser.Deserialize(yaml_files=bad_testcase_path)

  def testDeserialize_BuildingConnections_Success(self):
    good_testcase_path = [os.path.join(os.path.abspath('./fake_instances'), 'GOOD', 'building_connections.yaml')]

    entities, config_mode = self.parser.Deserialize(yaml_files=good_testcase_path)

    self.assertEqual(config_mode, enumerations.ConfigMode.INITIALIZE)
    self.assertLen(entities, 1)
    self.assertIn('US-SEA-BLDG1-GUID', entities)







if __name__ == '__main__':
  absltest.main()