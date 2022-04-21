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
"""Test for command line interface and entry point."""

import argparse
from absl.testing import absltest

import scorer


class CliTest(absltest.TestCase):
  def setUp(self):
    super().setUp()
    self.cli = scorer.parse_args()

  def testCliIsParser(self):
    self.assertEqual(type(self.cli), argparse.ArgumentParser)

  def testVerboseInputArgsExist(self):
    parsed = self.cli.parse_args([
        '--modified-ontology-types', 'path/to/ontology/yaml/resources',
        '--solution', 'path/to/solution/file.yaml', '--proposed',
        'path/to/proposed/file.yaml', '--verbose', 'True'
    ])
    self.assertEqual(parsed.ontology, 'path/to/ontology/yaml/resources')
    self.assertEqual(parsed.solution, 'path/to/solution/file.yaml')
    self.assertEqual(parsed.proposed, 'path/to/proposed/file.yaml')
    self.assertTrue(parsed.verbose)

  def testConciseInputArgsExist(self):
    parsed = self.cli.parse_args([
        '-m', 'path/to/ontology/yaml/resources', '-sol',
        'path/to/solution/file.yaml', '-prop', 'path/to/proposed/file.yaml',
        '-v', 'True'
    ])
    self.assertEqual(parsed.ontology, 'path/to/ontology/yaml/resources')
    self.assertEqual(parsed.solution, 'path/to/solution/file.yaml')
    self.assertEqual(parsed.proposed, 'path/to/proposed/file.yaml')
    self.assertTrue(parsed.verbose)

  def testSolutionArgIsRequired(self):
    with self.assertRaises(SystemExit):
      self.cli.parse_args(['--proposed', 'path/to/proposed/file.yaml'])

  def testProposedArgIsRequired(self):
    with self.assertRaises(SystemExit):
      self.cli.parse_args(['--solution', 'path/to/solution/file.yaml'])

  def testOntologyArgDefaultsPath(self):
    parsed = self.cli.parse_args([
        '--solution', 'path/to/solution/file.yaml', '--proposed',
        'path/to/proposed/file.yaml'
    ])
    self.assertEqual(parsed.ontology, 'ontology/yaml/resources')

  def testVerboseArgIsTrue(self):
    parsed = self.cli.parse_args([
        '--solution', 'path/to/solution/file.yaml', '--proposed',
        'path/to/proposed/file.yaml', '--verbose', 'True'
    ])
    self.assertTrue(parsed.verbose)

    parsed = self.cli.parse_args([
        '--solution', 'path/to/solution/file.yaml', '--proposed',
        'path/to/proposed/file.yaml', '--verbose', 'true'
    ])
    self.assertTrue(parsed.verbose)

    parsed = self.cli.parse_args([
        '--solution', 'path/to/solution/file.yaml', '--proposed',
        'path/to/proposed/file.yaml', '--verbose', 'yes'
    ])
    self.assertTrue(parsed.verbose)

    parsed = self.cli.parse_args([
        '--solution', 'path/to/solution/file.yaml', '--proposed',
        'path/to/proposed/file.yaml', '--verbose', '1'
    ])
    self.assertTrue(parsed.verbose)

  def testVerboseArgDefaultsFalse(self):
    parsed = self.cli.parse_args([
        '--solution',
        'path/to/solution/file.yaml',
        '--proposed',
        'path/to/proposed/file.yaml',
    ])
    self.assertFalse(parsed.verbose)


if __name__ == '__main__':
  absltest.main()
