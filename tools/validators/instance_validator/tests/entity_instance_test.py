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
from os import path

_TEST_DIR = path.dirname(path.realpath(__file__))
_TESTCASE_PATH = path.join(_TEST_DIR, 'fake_instances')

# generate universe once for all the tests
_UNIVERSE = generate_universe.BuildUniverse()
_UNIVERSE.connections_universe = set(['CONTAINS', 'CONTROLS', 'FEEDS'])

class EntityInstanceTest(absltest.TestCase):


  def testValidateGoodExample(self):
    parsed = instance_parser.parse_yaml(
        path.join(_TESTCASE_PATH,
                  'GOOD',
                  'good_building_type.yaml'))
    parsed = dict(parsed)
    entity_name = list(parsed.keys())[0]

    entity = dict(parsed[entity_name])
    instance = entity_instance.EntityInstance(entity,
                                              _UNIVERSE,
                                              parsed.keys())

    if not instance.IsValidEntityInstance():
      self.fail('exception incorrectly raised')

  def testValidateBadEntityTypeFormat(self):
    parsed = instance_parser.parse_yaml(
        path.join(_TESTCASE_PATH,
                  'BAD',
                  'bad_building_type.yaml'))
    parsed = dict(parsed)
    entity_name = list(parsed.keys())[0]
    entity = dict(parsed[entity_name])

    try:
      entity_instance.EntityInstance(entity, _UNIVERSE, parsed.keys())
    except TypeError as e:
      self.assertEqual(type(e), TypeError)
    else:
      self.fail('{0} was not raised'.format(TypeError))

  def testValidateBadEntityNamespace(self):
    parsed = instance_parser.parse_yaml(
        path.join(_TESTCASE_PATH,
                  'BAD',
                  'bad_building_type_namespace.yaml'))
    parsed = dict(parsed)
    entity_name = list(parsed.keys())[0]
    entity = dict(parsed[entity_name])
    instance = entity_instance.EntityInstance(entity,
                                              _UNIVERSE,
                                              parsed.keys())

    if instance.IsValidEntityInstance():
      self.fail('exception not raised')


  def testValidateRejectsUseOfAbstractType(self):
    parsed = instance_parser.parse_yaml(
        path.join(_TESTCASE_PATH,
                  'BAD',
                  'bad_abstract_type.yaml'))
    parsed = dict(parsed)
    entity_name = list(parsed.keys())[0]

    entity = dict(parsed[entity_name])
    instance = entity_instance.EntityInstance(entity,
                                              _UNIVERSE,
                                              parsed.keys())

    if instance.IsValidEntityInstance():
      self.fail('exception not raised')


  def testValidateBadEntityType(self):
    parsed = instance_parser.parse_yaml(
        path.join(_TESTCASE_PATH,
                  'BAD',
                  'bad_building_type_entity.yaml'))
    parsed = dict(parsed)
    entity_name = list(parsed.keys())[0]

    entity = dict(parsed[entity_name])
    instance = entity_instance.EntityInstance(entity,
                                              _UNIVERSE,
                                              parsed.keys())

    if instance.IsValidEntityInstance():
      self.fail('exception not raised')

  def testValidateCompliantTranslation(self):
    parsed = instance_parser.parse_yaml(
        path.join(_TESTCASE_PATH,
                  'GOOD',
                  'good_translation_compliant.yaml'))
    parsed = dict(parsed)
    entity_name = list(parsed.keys())[0]

    entity = dict(parsed[entity_name])
    instance = entity_instance.EntityInstance(entity,
                                              _UNIVERSE,
                                              parsed.keys())

    if not instance.IsValidEntityInstance():
      self.fail('exception incorrectly raised')

  def testValidateMultipleCompliantTranslation(self):
    parsed = instance_parser.parse_yaml(
        path.join(_TESTCASE_PATH,
                  'GOOD',
                  'good_translation_multiple_compliant.yaml'))
    parsed = dict(parsed)
    entity_name = list(parsed.keys())[0]

    entity = dict(parsed[entity_name])
    instance = entity_instance.EntityInstance(entity,
                                              _UNIVERSE,
                                              parsed.keys())

    if not instance.IsValidEntityInstance():
      self.fail('exception incorrectly raised')


  def testValidateMultipleCompliantTranslationWithFields(self):
    parsed = instance_parser.parse_yaml(
        path.join(_TESTCASE_PATH,
                  'GOOD',
                  'good_building_translation_fields.yaml'))
    parsed = dict(parsed)
    entity_name = list(parsed.keys())[0]

    entity = dict(parsed[entity_name])
    instance = entity_instance.EntityInstance(entity,
                                              _UNIVERSE,
                                              parsed.keys())

    if not instance.IsValidEntityInstance():
      self.fail('exception incorrectly raised')

  def testValidateMultipleCompliantTranslationWithRequiredFieldMissing(self):
    parsed = instance_parser.parse_yaml(
        path.join(_TESTCASE_PATH,
                  'BAD',
                  'bad_translation_with_required_field_missing.yaml'))
    parsed = dict(parsed)
    entity_name = list(parsed.keys())[0]

    entity = dict(parsed[entity_name])
    instance = entity_instance.EntityInstance(entity,
                                              _UNIVERSE,
                                              parsed.keys())

    if instance.IsValidEntityInstance():
      self.fail('exception not raised')

  def testValidateMultipleCompliantTranslationWithNamespaceOtherMultiple(self):
    parsed = instance_parser.parse_yaml(
        path.join(_TESTCASE_PATH, 'GOOD', 'good_translation.yaml'))

    parsed = dict(parsed)
    entity_name_hvac = list(parsed.keys())[0]

    entity_hvac = dict(parsed[entity_name_hvac])
    instance = entity_instance.EntityInstance(entity_hvac
                                              , _UNIVERSE
                                              , parsed.keys())

    if not instance.IsValidEntityInstance():
      self.fail('exception incorrectly raised')

  def testValidateMultipleCompliantTranslationWithNamespaceOther(self):
    parsed = instance_parser.parse_yaml(
        path.join(_TESTCASE_PATH, 'GOOD', 'good_translation.yaml'))

    parsed = dict(parsed)
    entity_name_lighting = list(parsed.keys())[0]

    entity_lighting = dict(parsed[entity_name_lighting])
    instance_lighting = entity_instance.EntityInstance(entity_lighting
                                                       , _UNIVERSE
                                                       , parsed.keys())

    if not instance_lighting.IsValidEntityInstance():
      self.fail('exception incorrectly raised')

  def testValidateMultipleCompliantTranslationWithIdenticalTypes(self):
    parsed = instance_parser.parse_yaml(
        path.join(_TESTCASE_PATH,
                  'GOOD',
                  'good_translation_identical.yaml'))
    parsed = dict(parsed)
    for raw_entity in list(parsed.keys()):
      entity_parsed = dict(parsed[raw_entity])
      entity = entity_instance.EntityInstance(entity_parsed
                                              , _UNIVERSE
                                              , parsed.keys())
      if not entity.IsValidEntityInstance():
        self.fail('exception incorrectly raised')

  def testValidateMultipleCompliantTranslationWithExtraField(self):
    parsed = instance_parser.parse_yaml(
        path.join(_TESTCASE_PATH,
                  'BAD',
                  'bad_translation_with_extra_field.yaml'))
    parsed = dict(parsed)
    entity_name = list(parsed.keys())[0]

    entity = dict(parsed[entity_name])
    instance = entity_instance.EntityInstance(entity
                                              , _UNIVERSE
                                              , parsed.keys())

    if instance.IsValidEntityInstance():
      self.fail('exception not raised')


  def testValidateTranslationUnitValues(self):
    parsed = instance_parser.parse_yaml(
        path.join(_TESTCASE_PATH,
                  'GOOD',
                  'good_translation_unit_values.yaml'))
    parsed = dict(parsed)
    entity_name = list(parsed.keys())[0]

    entity = dict(parsed[entity_name])
    instance = entity_instance.EntityInstance(entity,
                                              _UNIVERSE,
                                              parsed.keys())

    if not instance.IsValidEntityInstance():
      self.fail('exception incorrectly raised')

  def testValidateTranslationStatesAndUnitValues(self):
    parsed = instance_parser.parse_yaml(
        path.join(_TESTCASE_PATH,
                  'GOOD',
                  'good_translation_states_and_unit_values.yaml'))
    parsed = dict(parsed)
    entity_name = list(parsed.keys())[0]

    entity = dict(parsed[entity_name])
    instance = entity_instance.EntityInstance(entity,
                                              _UNIVERSE,
                                              parsed.keys())

    if not instance.IsValidEntityInstance():
      self.fail('exception incorrectly raised')

  def testValidateTranslationUnits(self):
    parsed = instance_parser.parse_yaml(
        path.join(_TESTCASE_PATH,
                  'GOOD',
                  'good_translation_units.yaml'))
    parsed = dict(parsed)
    entity_name = list(parsed.keys())[0]

    entity = dict(parsed[entity_name])
    instance = entity_instance.EntityInstance(entity,
                                              _UNIVERSE,
                                              parsed.keys())

    if not instance.IsValidEntityInstance():
      self.fail('exception incorrectly raised')

  def testValidateTranslationUnitsAndStates(self):
    parsed = instance_parser.parse_yaml(
        path.join(_TESTCASE_PATH,
                  'GOOD',
                  'good_translation_units_and_states.yaml'))
    parsed = dict(parsed)
    entity_name = list(parsed.keys())[0]

    entity = dict(parsed[entity_name])
    instance = entity_instance.EntityInstance(entity,
                                              _UNIVERSE,
                                              parsed.keys())

    if not instance.IsValidEntityInstance():
      self.fail('exception incorrectly raised')

  def testValidateBadTranslationUnitValues(self):
    parsed = instance_parser.parse_yaml(
        path.join(_TESTCASE_PATH,
                  'BAD',
                  'bad_translation_unit_values.yaml'))
    parsed = dict(parsed)
    entity_name = list(parsed.keys())[0]

    entity = dict(parsed[entity_name])
    instance = entity_instance.EntityInstance(entity,
                                              _UNIVERSE,
                                              parsed.keys())

    if instance.IsValidEntityInstance():
      self.fail('exception not raised')

  def testValidateBadTranslationStates(self):
    parsed = instance_parser.parse_yaml(
        path.join(_TESTCASE_PATH,
                  'BAD',
                  'bad_translation_states.yaml'))
    parsed = dict(parsed)
    entity_name = list(parsed.keys())[0]

    entity = dict(parsed[entity_name])
    instance = entity_instance.EntityInstance(entity,
                                              _UNIVERSE,
                                              parsed.keys())

    if instance.IsValidEntityInstance():
      self.fail('exception not raised')

  def testValidateBadLinkFields(self):
    parsed = instance_parser.parse_yaml(
        path.join(_TESTCASE_PATH,
                  'BAD',
                  'bad_building_links_fields.yaml'))
    entity_instances = {}
    parsed = dict(parsed)
    for raw_entity in list(parsed.keys()):
      entity_parsed = dict(parsed[raw_entity])
      entity = entity_instance.EntityInstance(entity_parsed
                                              , _UNIVERSE
                                              , parsed.keys())
      entity_instances[raw_entity] = entity

    if entity_instances.get('ENTITY-NAME')\
        .IsValidEntityInstance(entity_instances):
      self.fail('exception not raised')

  def testValidateBadLinkEntityName(self):
    parsed = instance_parser.parse_yaml(
        path.join(_TESTCASE_PATH,
                  'BAD',
                  'bad_building_links_entity_name.yaml'))
    entity_instances = {}
    parsed = dict(parsed)
    for raw_entity in list(parsed.keys()):
      entity_parsed = dict(parsed[raw_entity])
      entity = entity_instance.EntityInstance(entity_parsed
                                              , _UNIVERSE
                                              , parsed.keys())
      entity_instances[raw_entity] = entity

    if entity_instances.get('ENTITY-NAME')\
        .IsValidEntityInstance(entity_instances):
      self.fail('exception not raised')

  def testValidateBadLinkWrongField(self):
    parsed = instance_parser.parse_yaml(
        path.join(_TESTCASE_PATH,
                  'BAD',
                  'bad_links_wrong_link.yaml'))
    entity_instances = {}
    parsed = dict(parsed)
    for raw_entity in list(parsed.keys()):
      entity_parsed = dict(parsed[raw_entity])
      entity = entity_instance.EntityInstance(entity_parsed
                                              , _UNIVERSE
                                              , parsed.keys())
      entity_instances[raw_entity] = entity

    if entity_instances.get('ENTITY-NAME')\
        .IsValidEntityInstance(entity_instances):
      self.fail('exception not raised')


  def testValidateBadLinkMissingField(self):
    parsed = instance_parser.parse_yaml(
        path.join(_TESTCASE_PATH,
                  'BAD',
                  'bad_links_missing_field.yaml'))
    entity_instances = {}
    parsed = dict(parsed)
    for raw_entity in list(parsed.keys()):
      entity_parsed = dict(parsed[raw_entity])
      entity = entity_instance.EntityInstance(entity_parsed
                                              , _UNIVERSE
                                              , parsed.keys())
      entity_instances[raw_entity] = entity

    if entity_instances.get('ENTITY-NAME')\
        .IsValidEntityInstance(entity_instances):
      self.fail('exception not raised')

  def testValidateGoodLinkEntityName(self):
    parsed = instance_parser.parse_yaml(
        path.join(_TESTCASE_PATH,
                  'GOOD',
                  'good_links.yaml'))
    entity_instances = {}
    parsed = dict(parsed)
    for raw_entity in list(parsed.keys()):
      entity_parsed = dict(parsed[raw_entity])
      entity = entity_instance.EntityInstance(entity_parsed
                                              , _UNIVERSE
                                              , parsed.keys())
      entity_instances[raw_entity] = entity

    for _, instance in entity_instances.items():
      if not instance.IsValidEntityInstance(entity_instances):
        self.fail('exception incorrectly raised')


  def testValidateStates(self):
    parsed = instance_parser.parse_yaml(
        path.join(_TESTCASE_PATH,
                  'GOOD',
                  'good_translation_states.yaml'))
    parsed = dict(parsed)
    for raw_entity in list(parsed.keys()):
      entity_parsed = dict(parsed[raw_entity])
      entity = entity_instance.EntityInstance(entity_parsed
                                              , _UNIVERSE
                                              , parsed.keys())
      if not entity.IsValidEntityInstance():
        self.fail('exception incorrectly raised')


  def testGoodConnections(self):
    parsed = instance_parser.parse_yaml(
        path.join(_TESTCASE_PATH,
                  'GOOD',
                  'good_building_connections.yaml'))
    parsed = dict(parsed)
    entity_name = list(parsed.keys())[0]
    entity = dict(parsed[entity_name])

    if 'connections' not in entity.keys():
      self.fail('entity does not have connections when expected')
    if _UNIVERSE.connections_universe is None:
      self.fail('universe does not valid connections universe')

    instance = entity_instance.EntityInstance(entity,
                                              _UNIVERSE,
                                              parsed.keys())

    if not instance.IsValidEntityInstance():
      self.fail('exception incorrectly raised')

  def testBadConnections(self):
    parsed = instance_parser.parse_yaml(
        path.join(_TESTCASE_PATH,
                  'BAD',
                  'bad_building_connections.yaml'))
    parsed = dict(parsed)
    entity_name = list(parsed.keys())[0]

    entity = dict(parsed[entity_name])
    instance = entity_instance.EntityInstance(entity,
                                              _UNIVERSE,
                                              parsed.keys())

    if instance.IsValidEntityInstance():
      self.fail('exception not raised')

if __name__ == '__main__':
  absltest.main()
