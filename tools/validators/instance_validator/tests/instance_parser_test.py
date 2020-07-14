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

import os

import instance_parser
from absl.testing import absltest

_TESTCASE_PATH = os.path.join('.', 'tests', 'fake_instances')

class ParserTest(absltest.TestCase):

  def testInstanceValidatorDetectDuplicateKeys(self):
    self.assertIsNone(instance_parser.parse_yaml(os.path.join(
        _TESTCASE_PATH, 'BAD', 'bad_duplicate_keys.yaml')))

  def testInstanceValidatorDetectMissingColon(self):
    self.assertIsNone(instance_parser.parse_yaml(os.path.join(
        _TESTCASE_PATH, 'BAD', 'bad_missing_colon.yaml')))

  def testInstanceValidatorDetectImproperSpacing(self):
    self.assertIsNone(instance_parser.parse_yaml(os.path.join(
        _TESTCASE_PATH, 'BAD', 'bad_spacing.yaml')))

  def testInstanceValidatorDetectImproperTabbing(self):
    self.assertIsNone(instance_parser.parse_yaml(os.path.join(
        _TESTCASE_PATH, 'BAD', 'bad_tabbing.yaml')))

  def testInstanceValidatorParseProperFormat(self):
    parsed_yaml = instance_parser.parse_yaml(os.path.join(
        _TESTCASE_PATH, 'GOOD', 'good_building_type.yaml'))
    self.assertTrue(parsed_yaml.data)

if __name__ == '__main__':
  absltest.main()
