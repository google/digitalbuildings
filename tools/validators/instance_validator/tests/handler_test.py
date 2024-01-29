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
"""Tests tools.validators.instance_validator.instance_validator."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import datetime
import os
import re
import shutil
import tempfile
from typing import Dict, List, Tuple
from unittest import mock

from absl.testing import absltest

from tests import test_constants
from validate import entity_instance
from validate import generate_universe
from validate import handler
from validate import instance_parser
from validate import subscriber
from validate import telemetry_validator
from yamlformat.validator import presubmit_validate_types_lib


_TESTCASE_PATH = test_constants.TEST_INSTANCES
_INIT_CFG = instance_parser.ConfigMode.INITIALIZE
_UPDATE_CFG = instance_parser.ConfigMode.UPDATE

_RunValidation = handler.RunValidation
_Deserialize = handler.Deserialize
_RunEntityHelperValidation = handler.EntityHelper.Validate
_CV = entity_instance.CombinationValidator

TEST_DATETIME = datetime.datetime(
    2020, 10, 15, 17, 21, 59, 0, tzinfo=datetime.timezone.utc
)  # 2020-10-15T17:21:59.000Z


def _ParserHelper(testpaths: List[str]) -> instance_parser.InstanceParser:
  parser = instance_parser.InstanceParser()
  for filepath in testpaths:
    parser.AddFile(filepath)
  parser.Finalize()
  return parser


def _Helper(
    testpaths: List[str],
) -> Tuple[
    Dict[str, entity_instance.EntityInstance], instance_parser.EntityOperation
]:
  parser = _ParserHelper(testpaths)
  entities = parser.GetEntities()
  default_operation = handler.GetDefaultOperation(parser.GetConfigMode())
  return entities, default_operation


class HandlerTest(absltest.TestCase):

  def testValidateOneBuildingExist(self):
    try:
      input_file = os.path.join(_TESTCASE_PATH, 'GOOD', 'building_type.yaml')
      _RunValidation([input_file], use_simplified_universe=True)
    except SyntaxError:
      self.fail('ValidationHelper:Validate raised ExceptionType unexpectedly!')

  # pylint:disable=line-too-long
  @mock.patch.object(handler, 'datetime')
  def testFileNameEnumerationHelper_generatesISO8601UTCTimestampEnumeratedFilename_conformsToWindowsLinuxMacOSXSuccess(
      self, mock_datetime
  ):
    mock_datetime.datetime.now.return_value = TEST_DATETIME
    filename = 'test_filename.txt'
    expected_enumerated_filename = '2020_10_15T17_21_59Z_test_filename.txt'
    re_expr = r'^\.|[\\<>:"\/\?]'
    re.compile(re_expr)

    enumerated_filename = handler.FileNameEnumerationHelper(filename)
    matched = re.search(re_expr, enumerated_filename)

    self.assertEqual(enumerated_filename, expected_enumerated_filename)
    self.assertFalse(matched)

  @mock.patch.object(handler, 'datetime')
  def testValidateReportFileNotEmpty(self, mock_datetime):
    mock_datetime.datetime.now.return_value = TEST_DATETIME
    report_directory = ''
    report_size = 0
    try:
      report_directory = tempfile.mkdtemp()
      input_file = os.path.join(_TESTCASE_PATH, 'GOOD', 'building_type.yaml')
      _RunValidation(
          [input_file],
          use_simplified_universe=True,
          gcp_credential_path='fake_credential_path',
          report_directory=report_directory,
      )

      report_size = os.path.getsize(
          os.path.join(
              report_directory,
              handler.FileNameEnumerationHelper(
                  handler.INSTANCE_VALIDATION_FILENAME
              ),
          ),
      )
    except SyntaxError:
      pass
    finally:
      shutil.rmtree(report_directory)

    self.assertGreater(report_size, 0)

  def testValidateOneBuildingExistFails(self):
    """Check that a config without a building is found to be invalid."""
    input_file = os.path.join(_TESTCASE_PATH, 'BAD', 'missing_building.yaml')
    config_universe = generate_universe.BuildUniverse(
        use_simplified_universe=True
    )
    entities, config_mode = _Deserialize([input_file])

    helper = handler.EntityHelper(config_universe)

    with self.assertRaises(SyntaxError):
      helper.Validate(entities, config_mode, is_udmi=True)

  def testValidateMultipleInputFilesSuccess(self):
    try:
      input_file1 = os.path.join(_TESTCASE_PATH, 'GOOD', 'building_type.yaml')
      input_file2 = os.path.join(_TESTCASE_PATH, 'GOOD', 'translation.yaml')
      _RunValidation([input_file1, input_file2], use_simplified_universe=True)
    except SyntaxError:
      self.fail('ValidationHelper:Validate unexpectedly raised Exception')

  @mock.patch.object(telemetry_validator, 'TelemetryValidator')
  @mock.patch.object(subscriber, 'Subscriber')
  def testTelemetryArgsBothSetSuccess(self, mock_subscriber, mock_validator):
    try:
      input_file = os.path.join(_TESTCASE_PATH, 'GOOD', 'building_type.yaml')
      _RunValidation(
          [input_file],
          subscription='a',
          gcp_credential_path='fake_credential_path',
          use_simplified_universe=True,
      )
      mock_subscriber.assert_has_calls([
          mock.call('a'),
          mock.call().Listen(
              mock.ANY, gcp_credential_path='fake_credential_path'
          ),
      ])
      # TODO(berkoben): Make this assert stricter
      mock_validator.assert_has_calls([
          mock.call(mock.ANY, mock.ANY, mock.ANY, mock.ANY),
          mock.call().StartTimer(),
      ])

    except SystemExit:
      self.fail('ValidationHelper:Validate raised ExceptionType unexpectedly!')

  @mock.patch.object(_CV, 'Validate', return_value=True)
  @mock.patch.object(presubmit_validate_types_lib, 'ConfigUniverse')
  def testValidateAcceptsEntitiesWithExpectedTypes(
      self, mock_universe, mock_validator
  ):
    parsed, default_operation = _Helper(
        [os.path.join(_TESTCASE_PATH, 'GOOD', 'translation.yaml')]
    )
    entity_helper = handler.EntityHelper(mock_universe)
    parsed = dict(parsed)
    instances = {}
    for name, ei in parsed.items():
      instances[name] = entity_instance.EntityInstance.FromYaml(
          name, ei, default_operation=default_operation
      )

    valid_entities, all_entities_valid = entity_helper.Validate(
        instances, _INIT_CFG
    )

    self.assertTrue(all_entities_valid)
    self.assertEqual(valid_entities, instances)
    self.assertEqual(mock_validator.call_count, 2)

  def testValidateLinksWithNetworkEntity(self):
    try:
      input_file = os.path.join(_TESTCASE_PATH, 'GOOD', 'links.yaml')
      _RunValidation([input_file], use_simplified_universe=True)
    except SyntaxError:
      self.fail('ValidationHelper:Validate raised ExceptionType unexpectedly!')

  def testValidateAcceptsWithInterdependency(self):
    parsed, default_operation = _Helper(
        [
            os.path.join(
                _TESTCASE_PATH, 'GOOD', 'entity_interdependency_v1_alpha.yaml'
            )
        ]
    )
    config_universe = generate_universe.BuildUniverse(
        use_simplified_universe=True
    )
    entity_helper = handler.EntityHelper(config_universe)
    parsed = dict(parsed)
    instances = {}
    for name, ei in parsed.items():
      instances[name] = entity_instance.EntityInstance.FromYaml(
          name, ei, default_operation=default_operation
      )

    valid_entities, all_entities_valid = entity_helper.Validate(
        instances, _UPDATE_CFG
    )

    self.assertTrue(all_entities_valid)
    self.assertEqual(valid_entities, instances)

  def testGraph_DoesNotAllowDuplicateCloudDeviceId(self):
    # pylint: disable=protected-access
    parsed, default_operation = _Helper(
        [
            os.path.join(
                _TESTCASE_PATH,
                'BAD',
                'entity_identical_cloud_device_ids.yaml',
            )
        ]
    )
    config_universe = generate_universe.BuildUniverse(
        use_simplified_universe=True
    )
    entity_helper = handler.EntityHelper(config_universe)
    parsed = dict(parsed)
    instances = {}
    for name, ei in parsed.items():
      instances[name] = entity_instance.EntityInstance.FromYaml(
          name, ei, default_operation=default_operation
      )

    valid_entities, all_entities_valid = entity_helper.Validate(
        instances, _INIT_CFG
    )
    self.assertFalse(all_entities_valid)
    self.assertLen(valid_entities, 3)
    self.assertFalse(entity_helper._IsDuplicateCDMIds(entities=instances))

  @mock.patch.object(handler, '_ValidateTelemetry')
  def testRunValidation_RunsWithReportDirectory(self, mock_validate_telemetry):
    temp_report_directory = tempfile.mkdtemp()

    try:
      input_file = os.path.join(_TESTCASE_PATH, 'GOOD', 'building_type.yaml')
      _RunValidation(
          [input_file],
          subscription='a',
          gcp_credential_path='fake_credential_path',
          use_simplified_universe=True,
          report_directory=temp_report_directory,
      )

      mock_validate_telemetry.assert_called_once_with(
          subscription='a',
          entities=mock.ANY,
          timeout=600,
          is_udmi=True,
          gcp_credential_path='fake_credential_path',
          report_directory=temp_report_directory,
      )
    except SystemExit:
      self.fail('ValidationHelper:Validate raised ExceptionType unexpectedly!')

  @mock.patch.object(handler, '_ValidateTelemetry')
  def testRunValidation_RunsWithoutReportDirectory(
      self, mock_validate_telemetry
  ):
    try:
      input_file = os.path.join(_TESTCASE_PATH, 'GOOD', 'building_type.yaml')
      _RunValidation(
          [input_file],
          subscription='a',
          gcp_credential_path='fake_credential_path',
          use_simplified_universe=True,
      )

      mock_validate_telemetry.assert_called_once_with(
          subscription='a',
          entities=mock.ANY,
          timeout=mock.ANY,
          is_udmi=True,
          gcp_credential_path='fake_credential_path',
          report_directory=None,
      )
    except SystemExit:
      self.fail('ValidationHelper:Validate raised ExceptionType unexpectedly!')


if __name__ == '__main__':
  absltest.main()
