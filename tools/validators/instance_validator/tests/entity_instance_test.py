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

"""Tests for entity_instance.py"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from validate import generate_universe
from validate import entity_instance
from validate import instance_parser
from absl.testing import absltest

import os

_TESTCASE_PATH = os.path.join('.', 'tests', 'fake_instances')

class EntityInstanceTest(absltest.TestCase):

  def setUp(self):
    temp_universe = generate_universe.BuildUniverse()
    temp_universe.connections_universe = set(['CONTAINS', 'CONTROLS', 'FEEDS'])
    self.universe = temp_universe

  def testValidateGoodExample(self):
    parsed = instance_parser.parse_yaml(
        os.path.join(_TESTCASE_PATH,
                     'GOOD',
                     'good_building_type.yaml'))
    parsed = dict(parsed)
    entity_name = list(parsed.keys())[0]

    entity = dict(parsed[entity_name])
    instance = entity_instance.EntityInstance(entity,
                                              self.universe,
                                              parsed.keys())

    if not instance.IsValidEntityInstance():
      self.fail('exception incorrectly raised')

  def testValidateBadEntityTypeFormat(self):
    parsed = instance_parser.parse_yaml(
        os.path.join(_TESTCASE_PATH,
                     'BAD',
                     'bad_building_type.yaml'))
    parsed = dict(parsed)
    entity_name = list(parsed.keys())[0]

    entity = dict(parsed[entity_name])
    instance = entity_instance.EntityInstance(entity,
                                              self.universe,
                                              parsed.keys())

    if instance.IsValidEntityInstance():
      self.fail('exception not raised')

  def testValidateBadEntityNamespace(self):
    parsed = instance_parser.parse_yaml(
        os.path.join(_TESTCASE_PATH,
                     'BAD',
                     'bad_building_type_namespace.yaml'))
    parsed = dict(parsed)
    entity_name = list(parsed.keys())[0]

    entity = dict(parsed[entity_name])
    instance = entity_instance.EntityInstance(entity,
                                              self.universe,
                                              parsed.keys())

    if instance.IsValidEntityInstance():
      self.fail('exception not raised')

  def testValidateBadEntityType(self):
    parsed = instance_parser.parse_yaml(
        os.path.join(_TESTCASE_PATH,
                     'BAD',
                     'bad_building_type_entity.yaml'))
    parsed = dict(parsed)
    entity_name = list(parsed.keys())[0]

    entity = dict(parsed[entity_name])
    instance = entity_instance.EntityInstance(entity,
                                              self.universe,
                                              parsed.keys())

    if instance.IsValidEntityInstance():
      self.fail('exception not raised')

  def testValidateCompliantTranslation(self):
    parsed = instance_parser.parse_yaml(
        os.path.join(_TESTCASE_PATH,
                     'GOOD',
                     'good_translation_compliant.yaml'))
    parsed = dict(parsed)
    entity_name = list(parsed.keys())[0]

    entity = dict(parsed[entity_name])
    instance = entity_instance.EntityInstance(entity,
                                              self.universe,
                                              parsed.keys())

    if not instance.IsValidEntityInstance():
      self.fail('exception incorrectly raised')

  def testValidateMultipleCompliantTranslation(self):
    parsed = instance_parser.parse_yaml(
        os.path.join(_TESTCASE_PATH,
                     'GOOD',
                     'good_translation_multiple_compliant.yaml'))
    parsed = dict(parsed)
    entity_name = list(parsed.keys())[0]

    entity = dict(parsed[entity_name])
    instance = entity_instance.EntityInstance(entity,
                                              self.universe,
                                              parsed.keys())

    if not instance.IsValidEntityInstance():
      self.fail('exception incorrectly raised')

  def testValidateTranslationUnitValues(self):
    parsed = instance_parser.parse_yaml(
        os.path.join(_TESTCASE_PATH,
                     'GOOD',
                     'good_translation_unit_values.yaml'))
    parsed = dict(parsed)
    entity_name = list(parsed.keys())[0]

    entity = dict(parsed[entity_name])
    instance = entity_instance.EntityInstance(entity,
                                              self.universe,
                                              parsed.keys())

    if not instance.IsValidEntityInstance():
      self.fail('exception incorrectly raised')

  def testValidateTranslationStates(self):
    parsed = instance_parser.parse_yaml(
        os.path.join(_TESTCASE_PATH,
                     'GOOD',
                     'good_translation_states.yaml'))
    parsed = dict(parsed)
    entity_name = list(parsed.keys())[0]

    entity = dict(parsed[entity_name])
    instance = entity_instance.EntityInstance(entity,
                                              self.universe,
                                              parsed.keys())

    if not instance.IsValidEntityInstance():
      self.fail('exception incorrectly raised')

  def testValidateTranslationStatesAndUnitValues(self):
    parsed = instance_parser.parse_yaml(
        os.path.join(_TESTCASE_PATH,
                     'GOOD',
                     'good_translation_states_and_unit_values.yaml'))
    parsed = dict(parsed)
    entity_name = list(parsed.keys())[0]

    entity = dict(parsed[entity_name])
    instance = entity_instance.EntityInstance(entity,
                                              self.universe,
                                              parsed.keys())

    if not instance.IsValidEntityInstance():
      self.fail('exception incorrectly raised')

  def testValidateTranslationUnits(self):
    parsed = instance_parser.parse_yaml(
        os.path.join(_TESTCASE_PATH,
                     'GOOD',
                     'good_translation_units.yaml'))
    parsed = dict(parsed)
    entity_name = list(parsed.keys())[0]

    entity = dict(parsed[entity_name])
    instance = entity_instance.EntityInstance(entity,
                                              self.universe,
                                              parsed.keys())

    if not instance.IsValidEntityInstance():
      self.fail('exception incorrectly raised')

  def testValidateTranslationUnitsAndStates(self):
    parsed = instance_parser.parse_yaml(
        os.path.join(_TESTCASE_PATH,
                     'GOOD',
                     'good_translation_units_and_states.yaml'))
    parsed = dict(parsed)
    entity_name = list(parsed.keys())[0]

    entity = dict(parsed[entity_name])
    instance = entity_instance.EntityInstance(entity,
                                              self.universe,
                                              parsed.keys())

    if not instance.IsValidEntityInstance():
      self.fail('exception incorrectly raised')

  def testValidateBadTranslationUnitValues(self):
    parsed = instance_parser.parse_yaml(
        os.path.join(_TESTCASE_PATH,
                     'BAD',
                     'bad_translation_unit_values.yaml'))
    parsed = dict(parsed)
    entity_name = list(parsed.keys())[0]

    entity = dict(parsed[entity_name])
    instance = entity_instance.EntityInstance(entity,
                                              self.universe,
                                              parsed.keys())

    if instance.IsValidEntityInstance():
      self.fail('exception not raised')

  def testValidateBadTranslationStates(self):
    parsed = instance_parser.parse_yaml(
        os.path.join(_TESTCASE_PATH,
                     'BAD',
                     'bad_translation_states.yaml'))
    parsed = dict(parsed)
    entity_name = list(parsed.keys())[0]

    entity = dict(parsed[entity_name])
    instance = entity_instance.EntityInstance(entity,
                                              self.universe,
                                              parsed.keys())

    if instance.IsValidEntityInstance():
      self.fail('exception not raised')

  def testValidateBadLinkFields(self):
    parsed = instance_parser.parse_yaml(
        os.path.join(_TESTCASE_PATH,
                     'BAD',
                     'bad_building_links_fields.yaml'))
    parsed = dict(parsed)
    entity_name = list(parsed.keys())[0]

    entity = dict(parsed[entity_name])
    instance = entity_instance.EntityInstance(entity,
                                              self.universe,
                                              parsed.keys())

    if instance.IsValidEntityInstance():
      self.fail('exception not raised')

  def testValidateBadLinkEntityName(self):
    parsed = instance_parser.parse_yaml(
        os.path.join(_TESTCASE_PATH,
                     'BAD',
                     'bad_building_links_entity_name.yaml'))
    parsed = dict(parsed)
    entity_name = list(parsed.keys())[0]

    entity = dict(parsed[entity_name])
    instance = entity_instance.EntityInstance(entity,
                                              self.universe,
                                              parsed.keys())

    if instance.IsValidEntityInstance():
      self.fail('exception not raised')

  def testValidateLinks(self):
    parsed = instance_parser.parse_yaml(
        os.path.join(_TESTCASE_PATH,
                     'GOOD',
                     'good_building_links.yaml'))
    parsed = dict(parsed)
    entity_name = list(parsed.keys())[0]

    entity = dict(parsed[entity_name])
    instance = entity_instance.EntityInstance(entity,
                                              self.universe,
                                              parsed.keys())

    if not instance.IsValidEntityInstance():
      self.fail('exception incorrectly raised')

  def testGoodConnections(self):
    parsed = instance_parser.parse_yaml(
        os.path.join(_TESTCASE_PATH,
                     'GOOD',
                     'good_building_connections.yaml'))
    parsed = dict(parsed)
    entity_name = list(parsed.keys())[0]
    entity = dict(parsed[entity_name])

    if 'connections' not in entity.keys():
      self.fail('entity does not have connections when expected')
    if self.universe.connections_universe is None:
      self.fail('universe does not valid connections universe')

    instance = entity_instance.EntityInstance(entity,
                                              self.universe,
                                              parsed.keys())

    if not instance.IsValidEntityInstance():
      self.fail('exception incorrectly raised')

  def testBadConnections(self):
    parsed = instance_parser.parse_yaml(
        os.path.join(_TESTCASE_PATH,
                     'BAD',
                     'bad_building_connections.yaml'))
    parsed = dict(parsed)
    entity_name = list(parsed.keys())[0]

    entity = dict(parsed[entity_name])
    instance = entity_instance.EntityInstance(entity,
                                              self.universe,
                                              parsed.keys())

    if instance.IsValidEntityInstance():
      self.fail('exception not raised')

if __name__ == '__main__':
  absltest.main()
