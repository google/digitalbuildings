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
from score.constants import FileTypes, DimensionCategories

from yamlformat.validator.presubmit_validate_types_lib import ConfigUniverse

from validate import handler as validator
from validate.field_translation import NonDimensionalValue

from typing import Any, NamedTuple

PROPOSED, SOLUTION = FileTypes
SIMPLE, COMPLEX = DimensionCategories


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
    self.assertEqual(self.parse.args[SOLUTION], self.solution)
    self.assertEqual(self.parse.args[PROPOSED], self.proposed)
    self.assertFalse(self.parse.args['verbose'])

    self.assertEqual(type(self.parse.universe), ConfigUniverse)

    self.assertEqual(type(self.parse.deserialized_files[PROPOSED]),
                     dict)  # DeserializedFile
    self.assertEqual(type(self.parse.deserialized_files[SOLUTION]),
                     dict)  # DeserializedFile

    self.assertEqual(type(self.parse.results), dict)

  @patch('builtins.print')
  def testAppendTypes(self, mock_print):
    self.assertFalse(
        hasattr(
            list(self.parse.deserialized_files[PROPOSED].values())[0], 'type'))
    deserialized_files_appended = self.parse._append_types(  # pylint: disable=protected-access
        universe=self.parse.universe,
        deserialized_files=self.parse.deserialized_files)
    self.assertEqual(mock_print.call_count, 4)
    calls = [
        call(f'{PROPOSED} translations absent: 0 (from 0 links)'),
        call(f'{PROPOSED} types absent: 0 (0 instances)'),
        call(f'{SOLUTION} translations absent: 0 (from 0 links)'),
        call(f'{SOLUTION} types absent: 0 (0 instances)')
    ]
    mock_print.assert_has_calls(calls)
    self.assertTrue(
        hasattr(
            list(deserialized_files_appended[PROPOSED].values())[0], 'type'))  # pylint: disable=unsubscriptable-object

  def testMatchReportingEntities(self):
    proposed_entities = validator.Deserialize(
        ['tests/samples/proposed/match_reporting_entities.yaml'])[0]
    solution_entities = validator.Deserialize(
        ['tests/samples/solution/match_reporting_entities.yaml'])[0]

    matches = parse_config.ParseConfig._match_reporting_entities(  # pylint: disable=protected-access
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

    matches = parse_config.ParseConfig._match_reporting_entities(  # pylint: disable=protected-access
        proposed_entities=proposed_entities,
        solution_entities=solution_entities)

    translations = parse_config.ParseConfig._retrieve_reporting_translations(  # pylint: disable=protected-access
        matches=matches,
        proposed_entities=proposed_entities,
        solution_entities=solution_entities)

    self.assertEqual(type(translations), dict)  # TranslationsDict
    self.assertEqual(len(translations.items()), len(matches))

    cdid = '2599571827844401'

    self.assertEqual(type(translations[cdid]), dict)

    self.assertTrue(f'{PROPOSED}' in translations[cdid])
    self.assertEqual(type(translations[cdid][f'{PROPOSED}']), list)
    self.assertEqual(len(translations[cdid][f'{PROPOSED}']), 1)
    self.assertEqual(type(translations[cdid][f'{PROPOSED}'][0]), tuple)
    self.assertEqual(translations[cdid][f'{PROPOSED}'][0][0], 'wrong')
    self.assertEqual(type(translations[cdid][f'{PROPOSED}'][0][1]),
                     NonDimensionalValue)

    self.assertTrue(f'{SOLUTION}' in translations[cdid])
    self.assertEqual(type(translations[cdid][f'{SOLUTION}']), list)
    self.assertEqual(len(translations[cdid][f'{SOLUTION}']), 1)
    self.assertEqual(type(translations[cdid][f'{SOLUTION}'][0]), tuple)
    self.assertEqual(translations[cdid][f'{SOLUTION}'][0][0], 'target')
    self.assertEqual(type(translations[cdid][f'{SOLUTION}'][0][1]),
                     NonDimensionalValue)

  def testAggregateResults(self):
    class _MockDimensionComplex(NamedTuple):
      deserialized_files: Any

      def evaluate(self):
        return f'called with {self.deserialized_files}'

    class _MockDimensionSimple(NamedTuple):
      translations: Any

      def evaluate(self):
        return f'called with {self.translations}'

    results = parse_config.ParseConfig._aggregate_results(  # pylint: disable=protected-access
        dimensions={
            f'{SIMPLE}': [_MockDimensionSimple],
            f'{COMPLEX}': [_MockDimensionComplex]
        },
        translations='argument for simple dimensions',
        deserialized_files='argument for complex dimensions')

    self.assertEqual(type(results), dict)
    self.assertEqual(results['_MockDimensionSimple'],
                     'called with argument for simple dimensions')
    self.assertEqual(results['_MockDimensionComplex'],
                     'called with argument for complex dimensions')


if __name__ == '__main__':
  absltest.main()
