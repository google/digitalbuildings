# Copyright 2021 Google LLC
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
from absl.testing import absltest
import argparse

from yamlformat import arg_parser

class ArgParserTest(absltest.TestCase):

  def setUp(self):
    self.parser = arg_parser.CreateParser()

  def testParserIsParser(self):
    self.assertEqual(type(self.parser), argparse.ArgumentParser)

  def testInputArgsExist(self):
    parsed = self.parser.parse_args([
        '--original',
        './my/path/to/foo',
        '--interactive',
        'False'
    ])
    self.assertEqual(parsed.original, './my/path/to/foo')
    self.assertEqual(parsed.modified_types_filepath, None)
    self.assertFalse(eval(parsed.interactive))

  def testOriginalArgIsRequired(self):
    with self.assertRaises(SystemExit):
      self.parser.parse_args(['-m', './test/path'])

  def testInteractiveIsTrue(self):
    parsed = self.parser.parse_args([
        '--original',
        './my/path/to/foo',
        '--interactive',
        'True'
    ])
    self.assertEqual(parsed.original, './my/path/to/foo')
    self.assertEqual(parsed.modified_types_filepath, None)
    self.assertTrue(eval(parsed.interactive))

  def testNoInteractiveFlag(self):
    parsed = self.parser.parse_args([
        '--original',
        './my/path/to/foo'
    ])
    self.assertEqual(parsed.original, './my/path/to/foo')
    self.assertEqual(parsed.modified_types_filepath, None)
    self.assertFalse(eval(parsed.interactive))

if __name__ == '__main__':
  absltest.main()
