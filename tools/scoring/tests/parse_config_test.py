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

from validate.field_translation import NonDimensionalValue


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

    self.assertEqual(type(self.parse.deserialized_files['proposed']),
                     dict)  # Dict[str, EntityInstance]
    self.assertEqual(type(self.parse.deserialized_files['solution']),
                     dict)  # Dict[str, EntityInstance]

    self.assertEqual(type(self.parse.results), dict)

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
    proposed_entities = validator.Deserialize(
        ['tests/samples/proposed/match_reporting_entities.yaml'])[0]
    solution_entities = validator.Deserialize(
        ['tests/samples/solution/match_reporting_entities.yaml'])[0]

    matches = parse_config.ParseConfig.match_reporting_entities(
        proposed_entities=proposed_entities,
        solution_entities=solution_entities)

    self.assertEqual(len(proposed_entities), 4)
    self.assertEqual(len(solution_entities), 4)
    self.assertEqual(len(matches), 1)
    self.assertEqual(matches[0], '2599571827844401')  # Yes, it's a string

  def testRetrieveReportingTranslations(self):
    proposed_entities = validator.Deserialize(
        ['tests/samples/proposed/retrieve_reporting_translations.yaml'])[0]
    solution_entities = validator.Deserialize(
        ['tests/samples/solution/retrieve_reporting_translations.yaml'])[0]

    matches = parse_config.ParseConfig.match_reporting_entities(
        proposed_entities=proposed_entities,
        solution_entities=solution_entities)

    translations = parse_config.ParseConfig.retrieve_reporting_translations(
        matches=matches,
        proposed_entities=proposed_entities,
        solution_entities=solution_entities)

    self.assertEqual(type(translations), dict)
    self.assertEqual(len(translations.items()), len(matches))

    cdid = '2599571827844401'

    self.assertEqual(type(translations[cdid]), dict)

    self.assertTrue('proposed_translations' in translations[cdid])
    self.assertEqual(type(translations[cdid]['proposed_translations']), list)
    self.assertEqual(len(translations[cdid]['proposed_translations']), 1)
    self.assertEqual(type(translations[cdid]['proposed_translations'][0]),
                     tuple)
    self.assertEqual(translations[cdid]['proposed_translations'][0][0], 'wrong')
    self.assertEqual(type(translations[cdid]['proposed_translations'][0][1]),
                     NonDimensionalValue)

    self.assertTrue('solution_translations' in translations[cdid])
    self.assertEqual(type(translations[cdid]['solution_translations']), list)
    self.assertEqual(len(translations[cdid]['solution_translations']), 1)
    self.assertEqual(type(translations[cdid]['solution_translations'][0]),
                     tuple)
    self.assertEqual(translations[cdid]['solution_translations'][0][0],
                     'target')
    self.assertEqual(type(translations[cdid]['solution_translations'][0][1]),
                     NonDimensionalValue)

  def testAggregateResultsNonDbo(self):
    mock_dimension = lambda *, translations: f'called with {translations}'
    results = parse_config.ParseConfig.aggregate_results_nondbo(
        dimensions=[mock_dimension], translations='arbitrary')

    self.assertEqual(type(results), dict)
    self.assertEqual(results['<lambda>'], 'called with arbitrary')

  def testAggregateResultsDbo(self):
    mock_dbo_dimension = (
        lambda *, proposed_entities, solution_entities:
        f'called with {proposed_entities} {solution_entities}')
    results_dbo = parse_config.ParseConfig.aggregate_results_dbo(
        dbo_dimensions=[mock_dbo_dimension],
        proposed_entities='arbitrary',
        solution_entities='arguments')

    self.assertEqual(type(results_dbo), dict)
    self.assertEqual(results_dbo['<lambda>'], 'called with arbitrary arguments')


if __name__ == '__main__':
  absltest.main()
