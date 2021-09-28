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

  def test_EnumToRegex(self):
    expected = syaml.Regex('^(ADD) | (UPDATE)$')
    actual = instance_parser.EnumToRegex(
        instance_parser.EntityOperation,
        [instance_parser.EntityOperation.DELETE])
    self.assertEqual(str(expected), str(actual))

  def testInstanceValidatorDetectDuplicateKeys(self):
    with self.assertRaises(SystemExit):
      parse = _Helper(
          [path.join(_TESTCASE_PATH, 'BAD', 'bad_duplicate_keys.yaml')])
      self.assertIsNone(parse)

  def testInstanceValidatorDetectMissingColon(self):
    with self.assertRaises(SystemExit):
      parse = _Helper(
          [path.join(_TESTCASE_PATH, 'BAD', 'bad_missing_colon.yaml')])
      self.assertIsNone(parse)

  def testInstanceValidatorDetectImproperSpacing(self):
    with self.assertRaises(SystemExit):
      parse = _Helper([path.join(_TESTCASE_PATH, 'BAD', 'bad_spacing.yaml')])
      self.assertIsNone(parse)

  def testInstanceValidatorDetectImproperTabbing(self):
    with self.assertRaises(SystemExit):
      parse = _Helper([path.join(_TESTCASE_PATH, 'BAD', 'bad_tabbing.yaml')])
      self.assertIsNone(parse)

  def testInstanceValidatorParseProperFormat(self):
    parse = _Helper(
        [path.join(_TESTCASE_PATH, 'GOOD', 'good_building_type.yaml')])
    self.assertIsNotNone(parse)

  def testInstanceValidatorParseProperConnections(self):
    parse = _Helper(
        [path.join(_TESTCASE_PATH, 'GOOD', 'good_building_connections.yaml')])
    self.assertIsNotNone(parse)

  def testInstanceValidatorParseMultipleEntities(self):
    parse = _Helper(
        [path.join(_TESTCASE_PATH, 'GOOD', 'good_multi_instances.yaml')])
    self.assertLen(parse.keys(), 3)
    self.assertIn('AHU-11', parse.keys())
    self.assertIn('FCU-1', parse.keys())
    self.assertIn('FCU-10', parse.keys())

  def testInstanceValidatorDetectImproperTranslationCompliance(self):
    with self.assertRaises(SystemExit):
      parse = _Helper(
          [path.join(_TESTCASE_PATH, 'BAD', 'bad_translation_compliant.yaml')])
      del parse

  def testInstanceValidatorDetectImproperTranslationKeys(self):
    with self.assertRaises(SystemExit):
      parse = _Helper(
          [path.join(_TESTCASE_PATH, 'BAD', 'bad_translation_keys.yaml')])
      del parse

  def testInstanceValidatorDetectImproperUnitsKeys(self):
    with self.assertRaises(SystemExit):
      parse = _Helper([
          path.join(_TESTCASE_PATH, 'BAD', 'bad_translation_units_format.yaml')
      ])
      del parse

  def testInstanceValidatorCloudDeviceIdNotSetWithTranslation(self):
    with self.assertRaises(KeyError):
      parse = _Helper([
          path.join(_TESTCASE_PATH, 'BAD',
                    'bad_translation_no_cloud_device_id.yaml')
      ])
      del parse

  def testInstanceValidatorDetectDuplicateEntityKeys(self):
    with self.assertRaises(SystemExit):
      parse = _Helper(
          [path.join(_TESTCASE_PATH, 'BAD', 'bad_duplicate_key.yaml')])
      del parse

  def testInstanceValidatorDetectDuplicateMetadata(self):
    with self.assertRaises(SystemExit):
      parse = _Helper(
          [path.join(_TESTCASE_PATH, 'BAD', 'bad_duplicate_metadata.yaml')])
      del parse

  def testInstanceValidatorRejectsOperationOnInitialize(self):
    with self.assertRaises(SystemExit):
      parse = _Helper(
          [path.join(_TESTCASE_PATH, 'BAD', 'bad_entity_operation.yaml')])
      del parse

  def testInstanceValidatorRejectsMaskOnInitialize(self):
    with self.assertRaises(SystemExit):
      parse = _Helper(
          [path.join(_TESTCASE_PATH, 'BAD', 'bad_entity_mask.yaml')])
      del parse

  def testInstanceValidatorRejectsMaskOnAdd(self):
    with self.assertRaises(SystemExit):
      parse = _Helper(
          [path.join(_TESTCASE_PATH, 'BAD', 'bad_entity_add_mask.yaml')])
      del parse

  def testInstanceValidatorRejectsUpdateWithoutEtag(self):
    with self.assertRaises(SystemExit):
      parse = _Helper(
          [path.join(_TESTCASE_PATH, 'BAD', 'bad_entity_etag.yaml')])
      del parse

  def testInstanceValidatorReadsMetadata(self):
    parser = _ParserHelper(
        [path.join(_TESTCASE_PATH, 'GOOD', 'good_with_metadata.yaml')])
    self.assertLen(parser.GetEntities().keys(), 2)
    self.assertEqual(parser.GetConfigMode(), instance_parser.ConfigMode.UPDATE)

  def testInstanceValidatorReadsMetadataAtEnd(self):
    parser = _ParserHelper(
        [path.join(_TESTCASE_PATH, 'GOOD', 'good_with_metadata_at_end.yaml')])
    self.assertLen(parser.GetEntities().keys(), 2)
    self.assertEqual(parser.GetConfigMode(), instance_parser.ConfigMode.UPDATE)

  def testInstanceValidatorHandlesUpdateMode(self):
    parser = _ParserHelper(
        [path.join(_TESTCASE_PATH, 'GOOD', 'good_update_with_metadata.yaml')])
    self.assertLen(parser.GetEntities().keys(), 4)

  def testInstanceValidatorUsesDefaultMode(self):
    parser = _ParserHelper(
        [path.join(_TESTCASE_PATH, 'GOOD', 'good_building_type.yaml')])
    self.assertEqual(parser.GetConfigMode(),
                     instance_parser.ConfigMode.Default())

  def testInstanceRejectsExportMode(self):
    with self.assertRaises(KeyError):
      parser = _ParserHelper(
          [path.join(_TESTCASE_PATH, 'BAD', 'bad_configmode.yaml')])
      del parser

if __name__ == '__main__':
  absltest.main()
