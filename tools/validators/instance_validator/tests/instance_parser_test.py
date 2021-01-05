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

"""Tests tools.validators.instance_validator.instance_parser"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from validate import instance_parser
from absl.testing import absltest
from os import path

_TEST_DIR = path.dirname(path.realpath(__file__))
_TESTCASE_PATH = path.join(_TEST_DIR, 'fake_instances')

class ParserTest(absltest.TestCase):

  def testInstanceValidatorDetectDuplicateKeys(self):
    with self.assertRaises(SystemExit):
      parse = instance_parser.ParseYaml(
          path.join(_TESTCASE_PATH,
                    'BAD',
                    'bad_duplicate_keys.yaml'))
      self.assertIsNone(parse)

  def testInstanceValidatorDetectMissingColon(self):
    with self.assertRaises(SystemExit):
      parse = instance_parser.ParseYaml(
          path.join(_TESTCASE_PATH,
                    'BAD',
                    'bad_missing_colon.yaml'))
      self.assertIsNone(parse)

  def testInstanceValidatorDetectImproperSpacing(self):
    with self.assertRaises(SystemExit):
      parse = instance_parser.ParseYaml(
          path.join(_TESTCASE_PATH,
                    'BAD',
                    'bad_spacing.yaml'))
      self.assertIsNone(parse)

  def testInstanceValidatorDetectImproperTabbing(self):
    with self.assertRaises(SystemExit):
      parse = instance_parser.ParseYaml(
          path.join(_TESTCASE_PATH,
                    'BAD',
                    'bad_tabbing.yaml'))
      self.assertIsNone(parse)

  def testInstanceValidatorParseProperFormat(self):
    parse = instance_parser.ParseYaml(
        path.join(_TESTCASE_PATH,
                  'GOOD',
                  'good_building_type.yaml'))
    self.assertIsNotNone(parse)

  def testInstanceValidatorParseProperConnections(self):
    parse = instance_parser.ParseYaml(
        path.join(_TESTCASE_PATH,
                  'GOOD',
                  'good_building_connections.yaml'))
    self.assertIsNotNone(parse)

  def testInstanceValidatorParseMultipleEntities(self):
    parse = instance_parser.ParseYaml(
        path.join(_TESTCASE_PATH,
                  'GOOD',
                  'good_multi_instances.yaml'))
    self.assertLen(parse.keys(), 3)
    self.assertIn('AHU-11', parse.keys())
    self.assertIn('FCU-1', parse.keys())
    self.assertIn('FCU-10', parse.keys())

  def testInstanceValidatorDetectImproperTranslationCompliance(self):
    with self.assertRaises(SystemExit):
      parse = instance_parser.ParseYaml(
          path.join(_TESTCASE_PATH,
                    'BAD',
                    'bad_translation_compliant.yaml'))
      self.assertIsNone(parse)

  def testInstanceValidatorDetectImproperTranslationKeys(self):
    with self.assertRaises(SystemExit):
      parse = instance_parser.ParseYaml(
          path.join(_TESTCASE_PATH,
                    'BAD',
                    'bad_translation_keys.yaml'))
      self.assertIsNone(parse)

  def testInstanceValidatorDetectImproperUnitsKeys(self):
    with self.assertRaises(SystemExit):
      parse = instance_parser.ParseYaml(
          path.join(_TESTCASE_PATH,
                    'BAD',
                    'bad_translation_units_format.yaml'))
      self.assertIsNone(parse)

if __name__ == '__main__':
  absltest.main()
