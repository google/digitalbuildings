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
from unittest.mock import call, patch

from score import parse_config
from yamlformat.validator.presubmit_validate_types_lib import ConfigUniverse

from validate import handler as validator
from validate.entity_instance import EntityInstance


class ParseConfigTest(absltest.TestCase):
  def setUp(self):
    super().setUp()
    self.ontology = '../../ontology/yaml/resources'
    self.solution = 'tests/samples/solution/building_config_example.yaml'
    self.proposed = 'tests/samples/proposed/building_config_example.yaml'
    self.parse = parse_config.ParseConfig(ontology=self.ontology,
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
    calls = [
        call('proposed translations absent: 0 (from 0 links)'),
        call('proposed types absent: 0 (0 instances)'),
        call('solution translations absent: 0 (from 0 links)'),
        call('solution types absent: 0 (0 instances)')
    ]
    mock_print.assert_has_calls(calls)

  def testMatchReportingEntities(self):
    proposed = validator.Deserialize(
        ['tests/samples/proposed/match_reporting_entities.yaml'])[0]
    solution = validator.Deserialize(
        ['tests/samples/files/solution/match_reporting_entities.yaml'])[0]

    matches = parse_config.ParseConfig.match_reporting_entities(
        proposed=proposed, solution=solution)

    self.assertEqual(len(proposed), 4)
    self.assertEqual(len(solution), 4)
    self.assertEqual(len(matches),
                     2)  # number of valid reporting entities in solution
    self.assertTrue(isinstance(
        matches[0], tuple))  #Tuple[Optional[EntityInstance], EntityInstance]
    self.assertEqual(matches[0][0].cloud_device_id,
                     '2599571827844401')  # Yes, it's a string
    self.assertEqual(matches[0][0].cloud_device_id,
                     matches[0][1].cloud_device_id)
    self.assertTrue(matches[1][0] is None)
    self.assertTrue(isinstance(matches[1][1], EntityInstance))


if __name__ == '__main__':
  absltest.main()
