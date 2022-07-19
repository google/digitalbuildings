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
"""Tests for spreadsheet_validator."""

import copy
import os
import pathlib as pl

from absl.testing import absltest

from model.constants import BC_GUID
from model.constants import CONNECTION_TYPE
from model.constants import CONNECTIONS
from model.constants import ENTITIES
from model.constants import ENTITY_CODE
from model.constants import IS_REPORTING
from model.constants import METADATA
from model.constants import NAMESPACE
from model.constants import SOURCE_ENTITY_CODE
from model.constants import SOURCE_ENTITY_GUID
from model.constants import TARGET_ENTITY_CODE
from model.constants import TARGET_ENTITY_GUID
from model.constants import TYPE_NAME
from concrete_model.tests.test_constants import TEST_NAMESPACE
from concrete_model.tests.test_constants import TEST_REPORTING_ENTITY_CODE
from concrete_model.tests.test_constants import TEST_REPORTING_ENTITY_DICT
from concrete_model.tests.test_constants import TEST_SPREADSHEET
from validators.spreadsheet_validator import SpreadsheetValidator

_TEST_VALIDATOR_LOG_PATH = os.path.join(
    os.path.expanduser('~'), 'code/test_model_validation_out.log')


class SpreadsheetValidatorTest(absltest.TestCase):

  def setUp(self):
    super().setUp()
    self.validator = SpreadsheetValidator(filepath=_TEST_VALIDATOR_LOG_PATH)
    self.test_spreadsheet = copy.deepcopy(TEST_SPREADSHEET)

  def testValidate(self):
    validator_result = self.validator.Validate(self.test_spreadsheet)

    self.assertTrue(validator_result)

  def testValidateContainsLogsMissingSpreadsheetValueError(self):
    test_virtual_entity_dict = {
        ENTITY_CODE: None,
        BC_GUID: None,
        NAMESPACE: TEST_NAMESPACE,
        TYPE_NAME: None,
        IS_REPORTING: 'FASLE',
        METADATA + '.test': 'test metadata'
    }
    self.test_spreadsheet[ENTITIES].append(test_virtual_entity_dict)

    validator_results = self.validator.Validate(self.test_spreadsheet)

    self.assertFalse(validator_results)

  def testInsufficientHeadersCreatesErrors(self):
    test_virtual_entity_dict_missing_type_name_header = {
        ENTITY_CODE: None,
        BC_GUID: None,
        NAMESPACE: TEST_NAMESPACE,
        IS_REPORTING: 'FALSE',
        METADATA + '.test': 'test metadata'
    }
    self.test_spreadsheet[ENTITIES] = [
        test_virtual_entity_dict_missing_type_name_header
    ]

    validator_results = self.validator.Validate(self.test_spreadsheet)

    self.assertFalse(validator_results)

  def testConnectionToBuildingIsValid(self):
    test_connection_to_building = {
        SOURCE_ENTITY_CODE: 'UK-LON-S2',
        SOURCE_ENTITY_GUID: None,
        TARGET_ENTITY_CODE: TEST_REPORTING_ENTITY_CODE,
        TARGET_ENTITY_GUID: None,
        CONNECTION_TYPE: 'CONTAINS'
    }
    self.test_spreadsheet[CONNECTIONS].append(test_connection_to_building)

    validator_results = self.validator.Validate(self.test_spreadsheet)

    self.assertTrue(validator_results)

  def testDuplicateEntityCodes(self):
    test_entity_with_duplicate_code = TEST_REPORTING_ENTITY_DICT.copy()
    self.test_spreadsheet[ENTITIES].append(test_entity_with_duplicate_code)

    validator_results = self.validator.Validate(self.test_spreadsheet)

    self.assertFalse(validator_results)

  def testCreatesLogFile(self):
    log_path = '/build/work/e1cb3532038491632c91c4936844ac13345a/google3/tmp/code/test_model_validation_out.log'
    self.assertIsNotNone(pl.Path(log_path).resolve().is_file())

if __name__ == '__main__':
  absltest.main()
