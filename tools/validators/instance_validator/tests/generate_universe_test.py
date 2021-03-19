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
"""Tests for generate_universe.py."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from os import path

from absl.testing import absltest

from validate import generate_universe

_IVAL_DIR = path.dirname(path.realpath(__file__))
_TEST_DIR = _IVAL_DIR
_RESOURCES = path.join('..', '..', '..', '..', 'ontology', 'yaml', 'resources')
_DEFAULT_ONTOLOGY_LOCATION = path.abspath(path.join(_TEST_DIR, _RESOURCES))
_BAD_MODIFIED_ONTOLOGY = path.join(_TEST_DIR, 'fake_resources', 'BAD',
                                   'BAD_FORMAT')
_NONEXISTENT_LOCATION = path.join(_TEST_DIR, 'nonexistent')
_EMPTY_FOLDER = path.join(_TEST_DIR, 'fake_resources', 'BAD', 'BAD_EMPTY')


class GenerateUniverseTest(absltest.TestCase):

  def testCanGenerateUniverse(self):
    universe = generate_universe.BuildUniverse(_DEFAULT_ONTOLOGY_LOCATION)
    self.assertTrue(universe)

  def testCatchInvalidModifiedOntology(self):
    with self.assertRaises(Exception) as context:
      generate_universe.BuildUniverse(_BAD_MODIFIED_ONTOLOGY)
    self.assertIn('no longer valid', str(context.exception))

  def testModifiedTypesCatchesNonexistent(self):
    self.assertRaises(Exception,
                      generate_universe.BuildUniverse(_NONEXISTENT_LOCATION))

  def testModifiedTypesCatchesEmpty(self):
    self.assertRaises(Exception, generate_universe.BuildUniverse(_EMPTY_FOLDER))


if __name__ == '__main__':
  absltest.main()
