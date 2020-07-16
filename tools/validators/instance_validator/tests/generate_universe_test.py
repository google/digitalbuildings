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

from universe_generation import generate_universe
from absl.testing import absltest

class GenerateUniverseTest(absltest.TestCase):

  def setUp(self):
    self.config = generate_universe.build_config()

  def testCanGenerateConfig(self):
    self.assertTrue(self.config)

  def testCanGenerateStateUniverse(self):
    state_universe = generate_universe.build_state_universe(self.config)
    self.assertTrue(state_universe)

  def testCanGenerateSubfieldUniverse(self):
    subfield_universe = generate_universe.build_subfield_universe(self.config)
    self.assertTrue(subfield_universe)

  def testCanGenerateUnitUniverse(self):
    subfield_universe = generate_universe.build_subfield_universe(self.config)
    unit_universe = generate_universe.build_unit_universe(self.config,
                                                          subfield_universe)
    self.assertTrue(unit_universe)

  def testCanGenerateFieldUniverse(self):
    config = generate_universe.build_config()
    subfield_universe = generate_universe.build_subfield_universe(config)
    state_universe = generate_universe.build_state_universe(config)
    field_universe = generate_universe.build_field_universe(config,
                                                            subfield_universe,
                                                            state_universe)
    self.assertTrue(field_universe)

  def testCanGenerateTypeUniverse(self):
    subfield_universe = generate_universe.build_subfield_universe(self.config)
    state_universe = generate_universe.build_state_universe(self.config)
    field_universe = generate_universe.build_field_universe(self.config,
                                                            subfield_universe,
                                                            state_universe)
    type_universe = generate_universe.build_type_universe(self.config,
                                                          field_universe)
    self.assertTrue(type_universe)

  def testCanGenerateUniverse(self):
    universe = generate_universe.build_universe()
    self.assertTrue(universe)

  def testCanParseUniverse(self):
    universe = generate_universe.build_universe()
    parsed_univ = generate_universe.parse_universe(universe)
    fields, subfields_map, states_map, units_map, entities_map = parsed_univ
    self.assertTrue(fields)
    self.assertTrue(subfields_map)
    self.assertTrue(states_map)
    self.assertTrue(units_map)
    self.assertTrue(entities_map)

if __name__ == '__main__':
  absltest.main()
