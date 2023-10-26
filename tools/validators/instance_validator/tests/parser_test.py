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

import jsonschema
import yaml
from os import path

from absl.testing import absltest

from tests import test_constants
from validate import handler
from validate import parser as p
from validate import enumerations
import uuid


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

  # NOT WORKING
  def testDeserialize_BuildingConnections_Success(self):
    good_testcase_path = [os.path.join(os.path.abspath('./fake_instances'), 'GOOD', 'building_connections.yaml')]

    entities, config_mode = self.parser.Deserialize(yaml_files=good_testcase_path)

    self.assertEqual(config_mode, enumerations.ConfigMode.INITIALIZE)
    self.assertLen(entities, 1)
    self.assertIn(uuid.UUID('3cf600dc-0e48-40ad-9807-ba98018e9946'), entities)

  def testDeserialize_ParseConnectionList_Succeeds(self):
    good_testcase_path = [os.path.join(os.path.abspath('./fake_instances'), 'GOOD', 'building_connection_list.yaml')]

    entities, config_mode = self.parser.Deserialize(yaml_files=good_testcase_path)

    self.assertEqual(config_mode, enumerations.ConfigMode.INITIALIZE)
    self.assertLen(entities, 1)
    self.assertIn(uuid.UUID('3cf600dc-0e48-40ad-9807-ba98018e9946'), entities)

  def testDeserialize_ParseMultipleEntities_Success(self):
    good_testcase_path = [os.path.join(os.path.abspath('./fake_instances'), 'GOOD', 'multi_instances.yaml')]

    entities, config_mode = self.parser.Deserialize(yaml_files=good_testcase_path)

    self.assertEqual(config_mode, enumerations.ConfigMode.INITIALIZE)
    self.assertLen(entities, 3)
    self.assertIn(uuid.UUID('37bc3537-9c19-42f9-968e-893d2ce1c6b6'), entities)
    self.assertIn(uuid.UUID('71965f14-9690-4218-9c9e-cb9550b8a07f'), entities)
    self.assertIn(uuid.UUID('2778562f-8600-4c55-bb36-0802cdf63956'), entities)

  def testDeserialize_BadTranslation_Fails(self):
    bad_testcase_path = [os.path.join(os.path.abspath('./fake_instances'), 'BAD', 'translation_compliant.yaml')]

    entities, config_mode = self.parser.Deserialize(yaml_files=bad_testcase_path)

    self.assertLen(entities, 0)

  def testDeserialize_BadTranslationKeys_Fails(self):
    bad_testcase_path = [os.path.join(os.path.abspath('./fake_instances'), 'BAD', 'translation_keys.yaml')]

    entities, config_mode = self.parser.Deserialize(yaml_files=bad_testcase_path)

    self.assertLen(entities, 0)

  def testDeserialize_BadTranslationUnits_Fails(self):
    bad_testcase_path = [os.path.join(os.path.abspath('./fake_instances'), 'BAD', 'translation_units_format.yaml')]

    entities, config_mode = self.parser.Deserialize(yaml_files=bad_testcase_path)

    self.assertLen(entities, 0)

  def testDeserialize_BadTranslationNoCDID_Fails(self):
    bad_testcase_path = [os.path.join(os.path.abspath('./fake_instances'), 'BAD', 'translation_missing_cloud_device_id.yaml')]

    entities, config_mode = self.parser.Deserialize(yaml_files=bad_testcase_path)

    self.assertLen(entities, 1)
    self.assertIn(uuid.UUID('135d08f4-8df0-46ae-86cb-16b953870aeb'), entities)
    self.assertNotIn(uuid.UUID('eb15ee68-795f-430a-bb1f-8e70eaf2e66a'), entities)

  def testDeserializer_UpdateMaskWithoutUpdateOperation_Fails(self):
    bad_testcase_path = [
      os.path.join(os.path.abspath('./fake_instances'), 'BAD', 'update_mask_value.yaml')]

    entities, config_mode = self.parser.Deserialize(yaml_files=bad_testcase_path)

    self.assertLen(entities, 0)

  def testDeserializer_UpdateMaskDependency_Success(self):
    good_testcase_path = [
      os.path.join(os.path.abspath('./fake_instances'), 'GOOD', 'update_mask.yaml')]

    entities, config_mode = self.parser.Deserialize(yaml_files=good_testcase_path)

    self.assertEqual(config_mode, enumerations.ConfigMode.UPDATE)
    self.assertLen(entities, 1)
    self.assertIn(uuid.UUID('71965f14-9690-4218-9c9e-cb9550b8a07f'), entities)

  def testDeserialize_DefaultExportOperationForUpdateMode_Success(self):
    good_testcase_path = [
      os.path.join(os.path.abspath('./fake_instances'), 'GOOD', 'entity_export_operation.yaml')]

    entities, config_mode = self.parser.Deserialize(yaml_files=good_testcase_path)

    self.assertEqual(config_mode, enumerations.ConfigMode.UPDATE)
    self.assertEqual(self.parser.GetDefaultEntityOperation(), enumerations.EntityOperation.EXPORT)
    self.assertLen(entities, 1)
    self.assertIn(uuid.UUID('71965f14-9690-4218-9c9e-cb9550b8a07f'), entities)

  def testDeserialize_ExportEntityMissingEtag_Fails(self):
    bad_testcase_path = [
      os.path.join(os.path.abspath('./fake_instances'), 'BAD', 'entity_export_operation.yaml')]

    entities, config_mode = self.parser.Deserialize(yaml_files=bad_testcase_path)

    self.assertEqual(config_mode, enumerations.ConfigMode.EXPORT)
    self.assertLen(entities, 0)


if __name__ == '__main__':
  absltest.main()