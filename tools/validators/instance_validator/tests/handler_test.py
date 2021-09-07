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
"""Tests tools.validators.instance_validator.instance_validator."""


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from os import path
from typing import Dict, List
from unittest import mock

from absl.testing import absltest

from tests import test_constants
from validate import entity_instance
from validate import handler
from validate import instance_parser
from validate import subscriber
from validate import telemetry_validator
from yamlformat.validator import presubmit_validate_types_lib

_TESTCASE_PATH = test_constants.TEST_INSTANCES
_INIT_CFG = instance_parser.ConfigMode.INITIALIZE

_RunValidation = handler.RunValidation
_RunEntityHelperValidation = handler.EntityHelper.Validate
_CV = entity_instance.CombinationValidator


def _ParserHelper(testpaths: List[str]) -> instance_parser.InstanceParser:
  parser = instance_parser.InstanceParser()
  for filepath in testpaths:
    parser.AddFile(filepath)
  parser.Finalize()
  return parser


def _Helper(testpaths: List[str]) -> Dict[str, entity_instance.EntityInstance]:
  return _ParserHelper(testpaths).GetEntities()


class HandlerTest(absltest.TestCase):

  def testValidateOneBuildingExist(self):
    try:
      input_file = path.join(_TESTCASE_PATH, 'GOOD', 'good_building_type.yaml')
      _RunValidation([input_file])
    except SyntaxError:
      self.fail('ValidationHelper:Validate raised ExceptionType unexpectedly!')

  def testValidateOneBuildingExistFails(self):
    with self.assertRaises(SyntaxError):
      input_file = path.join(_TESTCASE_PATH, 'BAD', 'bad_missing_building.yaml')
      _RunValidation([input_file])

  def testValidateMultipleInputFilesSuccess(self):
    try:
      input_file1 = path.join(_TESTCASE_PATH, 'GOOD', 'good_building_type.yaml')
      input_file2 = path.join(_TESTCASE_PATH, 'GOOD',
                              'good_translation_nobuilding.yaml')
      _RunValidation([input_file1, input_file2])
    except SyntaxError:
      self.fail('ValidationHelper:Validate unexpectedly raised Exception')

  @mock.patch.object(telemetry_validator, 'TelemetryValidator')
  @mock.patch.object(subscriber, 'Subscriber')
  def testTelemetryArgsBothSetSuccess(self, mock_subscriber, mock_validator):
    try:
      input_file = path.join(_TESTCASE_PATH, 'GOOD', 'good_building_type.yaml')
      _RunValidation([input_file], subscription='a', service_account='file')
      mock_subscriber.assert_has_calls(
          [mock.call('a', 'file'),
           mock.call().Listen(mock.ANY)])
      # TODO(berkoben): Make this assert stricter
      mock_validator.assert_has_calls(
          [mock.call(mock.ANY, mock.ANY, mock.ANY),
           mock.call().StartTimer()])

    except SystemExit:
      self.fail('ValidationHelper:Validate raised ExceptionType unexpectedly!')

  def testTelemetryArgsMissingSubscription(self):
    with self.assertRaises(SystemExit):
      input_file = path.join(_TESTCASE_PATH, 'GOOD', 'good_building_type.yaml')
      _RunValidation([input_file], service_account='file')

  def testTelemetryArgsMissingServiceAccount(self):
    with self.assertRaises(SystemExit):
      input_file = path.join(_TESTCASE_PATH, 'GOOD', 'good_building_type.yaml')
      _RunValidation([input_file], subscription='a')

  @mock.patch.object(_CV, 'Validate', return_value=True)
  @mock.patch.object(presubmit_validate_types_lib, 'ConfigUniverse')
  def testValidateAcceptsEntitiesWithExpectedTypes(self, mock_universe,
                                                   mock_validator):
    parsed = _Helper(
        [path.join(_TESTCASE_PATH, 'GOOD', 'good_translation.yaml')])
    entity_helper = handler.EntityHelper(mock_universe)
    parsed = dict(parsed)
    instances = {}
    for name, ei in parsed.items():
      instances[name] = entity_instance.EntityInstance.FromYaml(ei)

    valid_entities = entity_helper.Validate(instances, _INIT_CFG)

    self.assertEqual(valid_entities, instances)
    self.assertEqual(mock_validator.call_count, 2)


if __name__ == '__main__':
  absltest.main()
