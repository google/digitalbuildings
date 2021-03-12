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

"""Tests tools.validators.instance_validator.instance_validator"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from absl.testing import absltest
from validate import handler
from os import path

_TEST_DIR = path.join('third_party/digitalbuildings/tools/validators/instance_validator/', 'tests')
_TESTCASE_PATH = path.join(_TEST_DIR, 'fake_instances')

class HandlerTest(absltest.TestCase):

  def testValidateOneBuildingExist(self):
    try:
      input_file = path.join(_TESTCASE_PATH, 'GOOD', 'good_building_type.yaml')
      args = ['--input', input_file]
      instance_handler = handler.ValidationHelper(args)
      instance_handler.Validate()
    except SyntaxError:
      self.fail('ValidationHelper:Validate raised ExceptionType unexpectedly!')

  def testValidateOneBuildingExistFails(self):
    with self.assertRaises(SyntaxError):
      input_file = path.join(
        _TESTCASE_PATH, 'BAD', 'bad_missing_building.yaml')
      args = ['--input', input_file]
      instance_handler = handler.ValidationHelper(args)
      instance_handler.Validate()

  def testValidateMultipleInputFilesSuccess(self):
    try:
      input_file1 = path.join(_TESTCASE_PATH, 'GOOD', 'good_building_type.yaml')
      input_file2 = path.join(
          _TESTCASE_PATH, 'GOOD', 'good_translation_nobuilding.yaml')
      args = ['-i', input_file1, '-i', input_file2]
      instance_handler = handler.ValidationHelper(args)
      instance_handler.Validate()
    except SyntaxError:
      self.fail('ValidationHelper:Validate unexpectedly raised Exception')

  def testTelemetryArgsBothSetSuccess(self):
    try:
      input_file = path.join(_TESTCASE_PATH, 'GOOD',
                             'good_building_type.yaml')
      args = ['--input', input_file, '--service-account', 'file',
              '--subscription', 'some-subscription']
      handler.ValidationHelper(args)
    except SystemExit:
      self.fail('ValidationHelper:Validate raised ExceptionType unexpectedly!')

  def testTelemetryArgsMissingSubscription(self):
    with self.assertRaises(SystemExit):
      input_file = path.join(_TESTCASE_PATH, 'GOOD',
                             'good_building_type.yaml')
      args = ['--input', input_file, '--service-account', 'file']
      handler.ValidationHelper(args)

  def testTelemetryArgsMissingServiceAccount(self):
    with self.assertRaises(SystemExit):
      input_file = path.join(_TESTCASE_PATH, 'GOOD',
                             'good_building_type.yaml')
      args = ['--input', input_file, '--subscription', 'some-subscription']
      handler.ValidationHelper(args)


if __name__ == '__main__':
  absltest.main()
