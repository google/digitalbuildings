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

"""Tests for generate_universe.py"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from validate import generate_universe
from absl.testing import absltest
from os import path

_DEFAULT_ONTOLOGY_LOCATION = path.join('..', '..', '..',
                                       'ontology', 'yaml', 'resources')
_BAD_MODIFIED_ONTOLOGY = path.join('.', 'fake_bad_modified_ontology')

class GenerateUniverseTest(absltest.TestCase):

  def setUp(self):
    self.universe = generate_universe.BuildUniverse()

  def testCanGenerateUniverse(self):
    self.assertTrue(self.universe)

  def testModifiedTypesFilepathWorks(self):
    test_universe = generate_universe.BuildUniverse(_DEFAULT_ONTOLOGY_LOCATION)
    self.assertTrue(test_universe)

  def testCatchInvalidModifiedOntology(self):
    self.assertRaises(Exception,
                      generate_universe.BuildUniverse(_BAD_MODIFIED_ONTOLOGY))

if __name__ == '__main__':
  absltest.main()
