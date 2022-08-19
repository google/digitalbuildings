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
"""Tests tools.validators.instance_validator.instance_parser."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from os import path

from absl.testing import absltest
import strictyaml as syaml

from tests import test_constants
from validate import handler
from validate import instance_parser


_TESTCASE_PATH = test_constants.TEST_INSTANCES


def _ParserHelper(testpaths):
  parser = instance_parser.InstanceParser()
  for filepath in testpaths:
    parser.AddFile(filepath)
  parser.Finalize()
  return parser


def _Helper(testpaths):
  return _ParserHelper(testpaths).GetEntities()


class ParserTest(absltest.TestCase):

  def testFunction_EnumToRegex_Success(self):
    expected = syaml.Regex('^(ADD) | (UPDATE)$')
    actual = instance_parser.EnumToRegex(
        instance_parser.EntityOperation,
        [instance_parser.EntityOperation.DELETE])
    self.assertEqual(str(expected), str(actual))

  def testInstanceValidator_DetectDuplicateKeys_Fails(self):
    with self.assertRaises(SystemExit):
      parser = _Helper(
          [path.join(_TESTCASE_PATH, 'BAD', 'duplicate_keys.yaml')])
      del parser

  def testInstanceValidator_DetectMissingColon_Fails(self):
    with self.assertRaises(SystemExit):
      parser = _Helper([path.join(_TESTCASE_PATH, 'BAD', 'missing_colon.yaml')])
      del parser

  def testInstanceValidator_DetectImproperSpacing_Fails(self):
    with self.assertRaises(SystemExit):
      parser = _Helper([path.join(_TESTCASE_PATH, 'BAD', 'spacing.yaml')])
      del parser

  def testInstanceValidator_DetectImproperTabbing_Fails(self):
    with self.assertRaises(SystemExit):
      parser = _Helper([path.join(_TESTCASE_PATH, 'BAD', 'tabbing.yaml')])
      del parser

  def testInstanceValidator_ParseProperFormat_Success(self):
    parser = _Helper([path.join(_TESTCASE_PATH, 'GOOD', 'building_type.yaml')])
    del parser

  def testInstanceValidator_ParseProperConnections_Success(self):
    parser = _Helper(
        [path.join(_TESTCASE_PATH, 'GOOD', 'building_connections.yaml')])
    del parser

  def testInstanceValidator_ParseProperConnectionList_Success(self):
    parser = _Helper(
        [path.join(_TESTCASE_PATH, 'GOOD', 'building_connection_list.yaml')])
    del parser

  def testInstanceValidator_ParseMultipleEntities_Success(self):
    parser = _Helper(
        [path.join(_TESTCASE_PATH, 'GOOD', 'multi_instances.yaml')])

    self.assertLen(parser.keys(), 3)
    self.assertIn('AHU-11-GUID', parser.keys())
    self.assertIn('FCU-1-GUID', parser.keys())
    self.assertIn('FCU-10-GUID', parser.keys())

  def testInstanceValidator_DetectImproperTranslationCompliance(self):
    with self.assertRaises(SystemExit):
      parser = _Helper(
          [path.join(_TESTCASE_PATH, 'BAD', 'translation_compliant.yaml')])
      del parser

  def testInstanceValidator_DetectImproperTranslationKeys(self):
    with self.assertRaises(SystemExit):
      parser = _Helper(
          [path.join(_TESTCASE_PATH, 'BAD', 'translation_keys.yaml')])
      del parser

  def testInstanceValidator_DetectImproperUnitsKeys(self):
    with self.assertRaises(SystemExit):
      parser = _Helper(
          [path.join(_TESTCASE_PATH, 'BAD', 'translation_units_format.yaml')])
      del parser

  def testInstanceValidator_CloudDeviceIdNotSetWithTranslation(self):
    with self.assertRaises(KeyError):
      parser = _Helper([
          path.join(_TESTCASE_PATH, 'BAD',
                    'translation_no_cloud_device_id.yaml')
      ])
      del parser

  def testInstanceValidator_DetectDuplicateEntityKeys(self):
    with self.assertRaises(SystemExit):
      parser = _Helper([path.join(_TESTCASE_PATH, 'BAD', 'duplicate_key.yaml')])
      del parser

  def testInstanceValidator_DetectDuplicateMetadata(self):
    with self.assertRaises(SystemExit):
      parser = _Helper(
          [path.join(_TESTCASE_PATH, 'BAD', 'duplicate_metadata.yaml')])
      del parser

  def testInstanceValidator_RejectsOperationOnInitialize(self):
    with self.assertRaises(SystemExit):
      parser = _Helper(
          [path.join(_TESTCASE_PATH, 'BAD', 'entity_operation.yaml')])
      del parser

  def testInstanceValidator_RejectsMaskOnInitialize(self):
    with self.assertRaises(SystemExit):
      parser = _Helper([path.join(_TESTCASE_PATH, 'BAD', 'entity_mask.yaml')])
      del parser

  def testInstanceValidator_RejectsMaskOnAdd(self):
    with self.assertRaises(SystemExit):
      parser = _Helper(
          [path.join(_TESTCASE_PATH, 'BAD', 'entity_add_mask.yaml')])
      del parser

  def testInstanceValidator_RejectsUpdateWithoutEtag(self):
    with self.assertRaises(SystemExit):
      parser = _Helper([path.join(_TESTCASE_PATH, 'BAD', 'entity_etag.yaml')])
      del parser

  def testInstanceValidator_ReadsMetadata_Success(self):
    parser = _ParserHelper(
        [path.join(_TESTCASE_PATH, 'GOOD', 'with_metadata.yaml')])
    self.assertLen(parser.GetEntities().keys(), 2)
    self.assertEqual(parser.GetConfigMode(), instance_parser.ConfigMode.UPDATE)

  def testInstanceValidator_ReadsMetadataAtEnd_Success(self):
    parser = _ParserHelper(
        [path.join(_TESTCASE_PATH, 'GOOD', 'with_metadata_at_end.yaml')])
    self.assertLen(parser.GetEntities().keys(), 2)
    self.assertEqual(parser.GetConfigMode(), instance_parser.ConfigMode.UPDATE)

  def testInstanceValidator_HandlesUpdateMode_Success(self):
    parser = _ParserHelper([
        path.join(_TESTCASE_PATH, 'GOOD',
                  'update_change_subset_of_entities.yaml')
    ])
    self.assertLen(parser.GetEntities().keys(), 4)

  def testInstanceValidator_RejectsUpdateMaskWithoutUpdateMode_Fails(self):
    with self.assertRaises(SystemExit):
      parser = _Helper([
          path.join(_TESTCASE_PATH, 'BAD',
                    'update_with_incorrect_metadata.yaml')
      ])
      del parser

  def testInstanceValidator_UsesDefaultMode_Success(self):
    parser = _ParserHelper(
        [path.join(_TESTCASE_PATH, 'GOOD', 'building_type.yaml')])
    self.assertEqual(parser.GetConfigMode(),
                     instance_parser.ConfigMode.Default())

  def testInstanceValidator_InvalidConfigModeExport_RaisesKeyError(self):
    with self.assertRaises(KeyError):
      parser = _ParserHelper(
          [path.join(_TESTCASE_PATH, 'BAD', 'configmode.yaml')])
      del parser

  def testEntityBlock_NewFormatSingleton_Success(self):
    parser = _ParserHelper(
        [path.join(_TESTCASE_PATH, 'GOOD', 'new_format_singleton.yaml')])
    self.assertEqual(
        list(parser.GetEntities().keys()).pop(),
        '9a86a19b-b687-4db1-888e-2cf34d04b74c')

  def testEntityBlock_CodeWithSpace_Success(self):
    parser = _ParserHelper(
        [path.join(_TESTCASE_PATH, 'GOOD', 'code_with_spaces.yaml')])
    self.assertEqual(
        list(parser.GetEntities().keys()).pop(), 'SDC_EXT 2-1 / Rm 2D2-GUID')

  def testEntityBlock_ValidUpdateMaskValueTypes_Success(self):
    parser = _ParserHelper(
        [path.join(_TESTCASE_PATH, 'GOOD', 'update_mask.yaml')])
    self.assertLen(parser.GetEntities().keys(), 1)

  def testEntityBlock_InvalidUpdateMaskInconsistentTypes_Fails(self):
    with self.assertRaises(SystemExit):
      parser = _Helper(
          [path.join(_TESTCASE_PATH, 'BAD', 'update_mask_value.yaml')])
      del parser

  def testEntityBlock_ValidUpdateMaskValue_Success(self):
    parser = _ParserHelper(
        [path.join(_TESTCASE_PATH, 'GOOD', 'update_mask.yaml')])
    expected = {
        'SDC_EXT-17-GUID': {
            'type': 'HVAC/SDC_EXT',
            'code': 'SDC_EXT-17',
            'cloud_device_id': 'foobar',
            'etag': 'a56789',
            'update_mask': ['translation', 'connection'],
            'translation': {
                'shade_extent_percentage_command': {
                    'present_value':
                        'points.shade_extent_percentage_command.present_value',
                    'units': {
                        'key': 'points.shade_extent_percentage_command.units',
                        'values': {
                            'percent': '%',
                            'type': 'HVAC/SDC_EXT'
                        }
                    }
                }
            }
        }
    }

    self.assertLen(parser.GetEntities().keys(), 1)
    self.assertEqual(parser.GetEntities(), expected)

  def testGoodEntity_DefaultExportOperationParses_Success(self):
    parser = _ParserHelper(
        [path.join(_TESTCASE_PATH, 'GOOD', 'entity_export_operation.yaml')])

    parsed = parser.GetEntities()
    _, entity = next(iter(parsed.items()))
    entity_operation = entity.get(instance_parser.ENTITY_OPERATION_KEY, None)
    default_operation = handler.GetDefaultOperation(parser.GetConfigMode())

    self.assertIsNone(entity_operation)
    self.assertLen(parser.GetEntities().keys(), 1)
    self.assertEqual(default_operation, instance_parser.EntityOperation.EXPORT)

  def testEntityBlock_InvalidExportOperation_Fails(self):
    with self.assertRaises(SystemExit):
      parser = _Helper(
          [path.join(_TESTCASE_PATH, 'BAD', 'entity_export_operation.yaml')])
      del parser

  def testEntityBlock_InvalidUpdateMaskAndOperation_Fails(self):
    with self.assertRaises(SystemExit):
      parser = _Helper(
          [path.join(_TESTCASE_PATH, 'BAD', 'update_mask_operation.yaml')])
      del parser

def testGoodBuildingConfig_EntityWithId_Success(self):
  parser = _ParserHelper(
      [path.join(_TESTCASE_PATH, 'GOOD', 'bc_entity_with_id.yaml')])

  parsed = parser.GetEntities()
  _, entity = next(next(iter(parsed.items())))

  self.assertLen(parser.GetEntities().keys(), 2)
  self.assertEqual(entity.get(instance_parser.ENTITY_ID_KEY),
      "deprecated-but-doesn't-break")

if __name__ == '__main__':
  absltest.main()
