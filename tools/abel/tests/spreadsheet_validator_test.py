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
import tempfile

from absl.testing import absltest

from model.constants import BC_GUID
from model.constants import CONNECTION_TYPE
from model.constants import CONNECTIONS
from model.constants import ENTITIES
from model.constants import ENTITY_CODE
from model.constants import ENTITY_FIELDS
from model.constants import FACILITIES_NAMESPACE
from model.constants import FACILTITIES_ENTITY_CODE_REGEX
from model.constants import IS_REPORTING
from model.constants import METADATA
from model.constants import NAMESPACE
from model.constants import RAW_FIELD_NAME
from model.constants import RAW_STATE
from model.constants import RAW_UNIT_PATH
from model.constants import RAW_UNIT_VALUE
from model.constants import REPORTING_ENTITY_CODE
from model.constants import REPORTING_ENTITY_FIELD_NAME
from model.constants import REPORTING_ENTITY_GUID
from model.constants import SOURCE_ENTITY_CODE
from model.constants import SOURCE_ENTITY_GUID
from model.constants import STANDARD_FIELD_NAME
from model.constants import STANDARD_STATE
from model.constants import STANDARD_UNIT_VALUE
from model.constants import STATES
from model.constants import TARGET_ENTITY_CODE
from model.constants import TARGET_ENTITY_GUID
from model.constants import TYPE_NAME
from tests.test_constants import TEST_NAMESPACE
from tests.test_constants import TEST_REPORTING_ENTITY_CODE
from tests.test_constants import TEST_REPORTING_ENTITY_DICT
from tests.test_constants import TEST_REPORTING_GUID
from tests.test_constants import TEST_SPREADSHEET
from validators.spreadsheet_error import ConnectionDependencyError
from validators.spreadsheet_error import CrossSheetDependencyError
from validators.spreadsheet_error import InvalidNamingError
from validators.spreadsheet_error import MissingSpreadsheetValueError
from validators.spreadsheet_error import SpreadsheetHeaderError
from validators.spreadsheet_validator import SpreadsheetValidator

_TEST_VALIDATOR_LOG_PATH = os.path.join(tempfile.gettempdir(),
                                        'test_model_validation_out.log')


class SpreadsheetValidatorTest(absltest.TestCase):

  def setUp(self):
    super().setUp()
    self.validator = SpreadsheetValidator(filepath=_TEST_VALIDATOR_LOG_PATH)
    self.test_spreadsheet = copy.deepcopy(TEST_SPREADSHEET)

  def testValidate(self):
    is_valid = self.validator.Validate(self.test_spreadsheet)

    self.assertTrue(is_valid)
    self.assertEmpty(self.validator.validation_errors)

  def testBadFieldNameDependencyLogsError(self):
    bad_test_state = {
        ENTITY_CODE: TEST_REPORTING_ENTITY_CODE,
        BC_GUID: TEST_REPORTING_GUID,
        REPORTING_ENTITY_FIELD_NAME: 'not a valid field name',
        STANDARD_STATE: 'ON',
        RAW_STATE: 'TRUE'
    }
    self.test_spreadsheet[STATES].append(bad_test_state)

    is_valid = self.validator.Validate(self.test_spreadsheet)

    self.assertFalse(is_valid)
    self.assertIsInstance(self.validator.validation_errors.pop(),
                          CrossSheetDependencyError)

  def testBadEntityCodeDependencyLogsError(self):
    bad_test_field = {
        STANDARD_FIELD_NAME: 'test_field_name',
        RAW_FIELD_NAME: 'pointset.raw_field_name',
        ENTITY_CODE: 'Not a valid entity code',
        REPORTING_ENTITY_FIELD_NAME: 'test_resporting_field_name',
        REPORTING_ENTITY_CODE: TEST_REPORTING_ENTITY_CODE,
        REPORTING_ENTITY_GUID: TEST_REPORTING_GUID,
        BC_GUID: TEST_REPORTING_GUID,
        RAW_UNIT_PATH: 'no-units',
        STANDARD_UNIT_VALUE: 'no-units',
        RAW_UNIT_VALUE: 'no-units',
        METADATA + '.test': 'test metadata'
    }
    self.test_spreadsheet[ENTITY_FIELDS].append(bad_test_field)

    is_valid = self.validator.Validate(self.test_spreadsheet)
    validation_error = self.validator.validation_errors.pop()

    self.assertFalse(is_valid)
    self.assertEmpty(self.validator.validation_errors)
    self.assertIsInstance(validation_error, CrossSheetDependencyError)
    self.assertEqual(validation_error.column, ENTITY_CODE)
    self.assertEqual(validation_error.table, ENTITY_FIELDS)
    self.assertEqual(validation_error.target_table, ENTITIES)

  def testEmptySpreadsheetRaisesException(self):
    with self.assertRaises(ValueError):
      self.validator.Validate({})

  def testSpreadsheetWithoutBuildingIsNotValid(self):
    blank_spreadsheet = {
        'Site': [],
        'Entities': [],
        'Entity Fields': [],
        'States': [],
        'Connections': []
    }

    is_valid = self.validator.Validate(blank_spreadsheet)
    validation_error = self.validator.validation_errors.pop()

    self.assertFalse(is_valid)
    self.assertEmpty(self.validator.validation_errors)
    self.assertIsInstance(validation_error, MissingSpreadsheetValueError)
    self.assertEqual(validation_error.message,
                     'Please provide a building code and guid.')

  def testValidateLogsMissingSpreadsheetValueError(self):
    test_virtual_entity_dict = {
        ENTITY_CODE: None,
        BC_GUID: None,
        NAMESPACE: TEST_NAMESPACE,
        TYPE_NAME: 'test_type',
        IS_REPORTING: 'FASLE',
        METADATA + '.test': 'test metadata'
    }
    self.test_spreadsheet[ENTITIES].append(test_virtual_entity_dict)

    is_valid = self.validator.Validate(self.test_spreadsheet)
    validation_error = self.validator.validation_errors.pop()

    self.assertFalse(is_valid)
    # Validation errors should be empty after one error is popped.
    self.assertEmpty(self.validator.validation_errors)
    self.assertIsInstance(validation_error, MissingSpreadsheetValueError)
    # Error is thrown on empty entity code.
    self.assertEqual(validation_error.column, ENTITY_CODE)

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

    is_valid = self.validator.Validate(self.test_spreadsheet)

    self.assertFalse(is_valid)
    self.assertIsInstance(self.validator.validation_errors.pop(),
                          SpreadsheetHeaderError)

  def testConnectionToBuildingIsValid(self):
    test_connection_to_building = {
        SOURCE_ENTITY_CODE: 'UK-LON-S2',
        SOURCE_ENTITY_GUID: None,
        TARGET_ENTITY_CODE: TEST_REPORTING_ENTITY_CODE,
        TARGET_ENTITY_GUID: None,
        CONNECTION_TYPE: 'CONTAINS'
    }
    self.test_spreadsheet[CONNECTIONS].append(test_connection_to_building)

    is_valid = self.validator.Validate(self.test_spreadsheet)

    self.assertTrue(is_valid)
    self.assertEmpty(self.validator.validation_errors)

  def testInvalidConnectionDependencyLogsError(self):
    test_connection_to_building = {
        SOURCE_ENTITY_CODE: 'UK-LON-X1',
        SOURCE_ENTITY_GUID: None,
        TARGET_ENTITY_CODE: TEST_REPORTING_ENTITY_CODE,
        TARGET_ENTITY_GUID: None,
        CONNECTION_TYPE: 'CONTAINS'
    }
    self.test_spreadsheet[CONNECTIONS].append(test_connection_to_building)

    is_valid = self.validator.Validate(self.test_spreadsheet)

    self.assertFalse(is_valid)
    self.assertIsInstance(self.validator.validation_errors.pop(),
                          ConnectionDependencyError)

  def testDuplicateEntityCodes(self):
    test_entity_with_duplicate_code = TEST_REPORTING_ENTITY_DICT.copy()
    self.test_spreadsheet[ENTITIES].append(test_entity_with_duplicate_code)

    validator_results = self.validator.Validate(self.test_spreadsheet)

    self.assertFalse(validator_results)

  def testFacilitiesEntityMissingGuid(self):
    facilities_entity_no_guid = {
        ENTITY_CODE: 'US-SEA-BUILD1-1',
        BC_GUID: None,
        NAMESPACE: 'FACILITIES',
        IS_REPORTING: 'FALSE',
        METADATA + '.test': 'test metadata'
    }
    facilities_entity_with_guid = {
        ENTITY_CODE: 'US-SEA-BUILD2-1',
        BC_GUID: 'a_guid',
        NAMESPACE: 'FACILITIES',
        IS_REPORTING: 'FALSE',
        METADATA + '.test': 'test metadata'
    }
    self.test_spreadsheet[ENTITIES].append(facilities_entity_no_guid)

    no_guid_validator_results = self.validator.ValidateFacilitiesEntities(
        sheet=[facilities_entity_no_guid])
    with_guid_validator_results = self.validator.ValidateFacilitiesEntities(
        sheet=[facilities_entity_with_guid])
    is_valid = self.validator.Validate(self.test_spreadsheet)

    self.assertLen(no_guid_validator_results, 1)
    self.assertIsInstance(no_guid_validator_results.pop(),
                          MissingSpreadsheetValueError)
    self.assertEmpty(with_guid_validator_results)
    self.assertFalse(is_valid)

  # pylint: disable=line-too-long
  def testFacilititesEntityWithInvalidCode(self):
    facilities_entity_with_bad_code = {
        ENTITY_CODE: 'bad_entity_code',
        BC_GUID: 'a_guid',
        TYPE_NAME: 'FLOOR',
        NAMESPACE: FACILITIES_NAMESPACE,
        IS_REPORTING: 'FALSE',
        METADATA + '.test': 'test metadata'
    }
    self.test_spreadsheet[ENTITIES].append(facilities_entity_with_bad_code)

    invalid_name_validator_results = self.validator.ValidateFacilitiesEntities(
        sheet=self.test_spreadsheet[ENTITIES])
    error_message = f'Table: {ENTITIES}, Row: 2, Column: {ENTITY_CODE}, Message: , entity name: bad_entity_code must follow naming pattern: {FACILTITIES_ENTITY_CODE_REGEX}'

    self.assertLen(invalid_name_validator_results, 1)
    invalid_name_error = invalid_name_validator_results.pop()
    self.assertIsInstance(invalid_name_error, InvalidNamingError)
    self.assertEqual(error_message, invalid_name_error.GetErrorMessage())

  # pylint: disable=line-too-long
  def testCreatesLogFile(self):
    log_path = '/build/work/e1cb3532038491632c91c4936844ac13345a/google3/tmp/code/test_model_validation_out.log'
    self.assertIsNotNone(pl.Path(log_path).resolve().is_file())


if __name__ == '__main__':
  absltest.main()
