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
from tools.scoring.score.parse_config import ParseConfig

from tools.validators.ontology_validator.yamlformat.validator.presubmit_validate_types_lib import ConfigUniverse
from tools.validators.instance_validator.validate.entity_instance import EntityInstance
from typing import Dict


class ParseConfigTest(absltest.TestCase):
  def setUp(self):
    super().setUp()
    self.ontology = 'foo',
    self.solution = 'bar',
    self.proposed = 'baz'
    self.parse = ParseConfig(
        ontology=self.ontology, solution=self.olution, proposed=self.proposed)

  def testInitialize(self):
    self.assertEqual(self.parse.args.ontology, self.ontology)
    self.assertEqual(self.parse.args.solution, self.solution)
    self.assertEqual(self.parse.args.proposed, self.proposed)
    self.assertFalse(self.parse.args.verbose, self.verbose)

    self.assertEqual(type(self.parse.universe), ConfigUniverse)

    self.assertEqual(
        type(self.parse.parsed.proposed),
        Dict[str, EntityInstance])
    self.assertEqual(
        type(self.parse.parsed.solution),
        Dict[str, EntityInstance])

    self.assertEqual(type(self.parse.parsed.scores), dict)


if __name__ == '__main__':
  absltest.main()
