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
"""Test for configuration file parser (parse_config.py)."""

from absl.testing import absltest
from unittest.mock import patch

from score.parse_config import ParseConfig
from yamlformat.validator.presubmit_validate_types_lib import ConfigUniverse


class ParseConfigTest(absltest.TestCase):
  def setUp(self):
    super().setUp()
    self.ontology = '../../../ontology/yaml/resources'
    self.solution = 'samples/solution/building_config_example.yaml'
    self.proposed = 'samples/proposed/building_config_example.yaml'
    self.parse = ParseConfig(ontology=self.ontology,
                             solution=self.solution,
                             proposed=self.proposed)

  def testInitialize(self):
    self.assertEqual(self.parse.args['ontology'], self.ontology)
    self.assertEqual(self.parse.args['solution'], self.solution)
    self.assertEqual(self.parse.args['proposed'], self.proposed)
    self.assertFalse(self.parse.args['verbose'])

    self.assertEqual(type(self.parse.universe), ConfigUniverse)

    self.assertEqual(type(self.parse.parsed['proposed']),
                     dict)  # Dict[str, EntityInstance]
    self.assertEqual(type(self.parse.parsed['solution']),
                     dict)  # Dict[str, EntityInstance]

    self.assertEqual(type(self.parse.scores), dict)

  @patch('builtins.print')
  def testAppendTypes(self, mock_print):
    self.parse.append_types()
    self.assertEqual(mock_print.call_count, 4)


if __name__ == '__main__':
  absltest.main()
