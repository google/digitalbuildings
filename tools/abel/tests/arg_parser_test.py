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
"""Testing module for arg_parser.py."""
import argparse

from absl.testing import absltest

from model import arg_parser


class ArgParserTest(absltest.TestCase):

  def setUp(self):
    super().setUp()
    pass

  def testParseArgs(self):
    output_parser = arg_parser.ParseArgs()
    self.assertEqual(type(output_parser), argparse.ArgumentParser)

  def testArgParserSucceedsWithRequiredArgs(self):
    parsed_args = arg_parser.ParseArgs().parse_args(
        ['--credential', 'credential.json']
    )

    self.assertIsNone(parsed_args.modified_types_filepath)
    self.assertIsNone(parsed_args.spreadsheet_id)
    self.assertIsNone(parsed_args.building_config)
    self.assertIsNone(parsed_args.subscription)
    self.assertIsNone(parsed_args.service_account)
    self.assertEqual(parsed_args.timeout, 600)
    self.assertIsNotNone(parsed_args.output_dir)

  def testArgParserFailsWithoutRequiredArgs(self):
    with self.assertRaises(SystemExit):
      arg_parser.ParseArgs().parse_args()


if __name__ == '__main__':
  absltest.main()
