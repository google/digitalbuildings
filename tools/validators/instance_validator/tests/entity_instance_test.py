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
from absl.testing import absltest

import instance_parser
import os

_TESTCASE_PATH = os.path.join('.', 'tests', 'fake_instances')

class EntityInstanceTest(absltest.TestCase):

  def setUp(self):
    self.universe = generate_universe.BuildUniverse()

  def testValidateGoodExample(self):
    parsed, err = instance_parser.parse_yaml(
        os.path.join(_TESTCASE_PATH,
                     'GOOD',
                     'good_building_type.yaml'))
    parsed = dict(parsed)
    entity_name = list(parsed.keys())[0]

    entity = dict(parsed[entity_name])
    instance = entity_instance.EntityInstance(entity, self.universe)

    self.assertIsNone(err)
    if not instance.IsValidEntityInstance():
      self.fail('exception incorrectly raised')

  def testValidateBadEntityTypeFormat(self):
    parsed, err = instance_parser.parse_yaml(
        os.path.join(_TESTCASE_PATH,
                     'BAD',
                     'bad_building_type.yaml'))
    parsed = dict(parsed)
    entity_name = list(parsed.keys())[0]

    self.assertIsNone(err)
    entity = dict(parsed[entity_name])
    instance = entity_instance.EntityInstance(entity, self.universe)

    if instance.IsValidEntityInstance():
      self.fail('exception not raised')

  def testValidateBadEntityNamespace(self):
    parsed, err = instance_parser.parse_yaml(
        os.path.join(_TESTCASE_PATH,
                     'BAD',
                     'bad_building_type_namespace.yaml'))
    parsed = dict(parsed)
    entity_name = list(parsed.keys())[0]

    self.assertIsNone(err)
    entity = dict(parsed[entity_name])
    instance = entity_instance.EntityInstance(entity, self.universe)

    if instance.IsValidEntityInstance():
      self.fail('exception not raised')

  def testValidateBadEntityType(self):
    parsed, err = instance_parser.parse_yaml(
        os.path.join(_TESTCASE_PATH,
                     'BAD',
                     'bad_building_type_entity.yaml'))
    parsed = dict(parsed)
    entity_name = list(parsed.keys())[0]

    self.assertIsNone(err)
    entity = dict(parsed[entity_name])
    instance = entity_instance.EntityInstance(entity, self.universe)

    if instance.IsValidEntityInstance():
      self.fail('exception not raised')

  def testValidateCompliantTranslation(self):
    parsed, err = instance_parser.parse_yaml(
        os.path.join(_TESTCASE_PATH,
                     'GOOD',
                     'good_translation_compliant.yaml'))
    parsed = dict(parsed)
    entity_name = list(parsed.keys())[0]

    self.assertIsNone(err)
    entity = dict(parsed[entity_name])
    instance = entity_instance.EntityInstance(entity, self.universe)

    if not instance.IsValidEntityInstance():
      self.fail('exception incorrectly raised')

  def testValidateMultipleCompliantTranslation(self):
    parsed, err = instance_parser.parse_yaml(
        os.path.join(_TESTCASE_PATH,
                     'GOOD',
                     'good_translation_multiple_compliant.yaml'))
    parsed = dict(parsed)
    entity_name = list(parsed.keys())[0]

    self.assertIsNone(err)
    entity = dict(parsed[entity_name])
    instance = entity_instance.EntityInstance(entity, self.universe)

    if not instance.IsValidEntityInstance():
      self.fail('exception incorrectly raised')

  def testValidateTranslationUnitValues(self):
    parsed, err = instance_parser.parse_yaml(
        os.path.join(_TESTCASE_PATH,
                     'GOOD',
                     'good_translation_unit_values.yaml'))
    parsed = dict(parsed)
    entity_name = list(parsed.keys())[0]

    self.assertIsNone(err)
    entity = dict(parsed[entity_name])
    instance = entity_instance.EntityInstance(entity, self.universe)

    if not instance.IsValidEntityInstance():
      self.fail('exception incorrectly raised')

  def testValidateTranslationStates(self):
    parsed, err = instance_parser.parse_yaml(
        os.path.join(_TESTCASE_PATH,
                     'GOOD',
                     'good_translation_states.yaml'))
    parsed = dict(parsed)
    entity_name = list(parsed.keys())[0]

    self.assertIsNone(err)
    entity = dict(parsed[entity_name])
    instance = entity_instance.EntityInstance(entity, self.universe)

    if not instance.IsValidEntityInstance():
      self.fail('exception incorrectly raised')

  def testValidateTranslationStatesAndUnitValues(self):
    parsed, err = instance_parser.parse_yaml(
        os.path.join(_TESTCASE_PATH,
                     'GOOD',
                     'good_translation_states_and_unit_values.yaml'))
    parsed = dict(parsed)
    entity_name = list(parsed.keys())[0]

    self.assertIsNone(err)
    entity = dict(parsed[entity_name])
    instance = entity_instance.EntityInstance(entity, self.universe)

    if not instance.IsValidEntityInstance():
      self.fail('exception incorrectly raised')

  def testValidateTranslationUnits(self):
    parsed, err = instance_parser.parse_yaml(
        os.path.join(_TESTCASE_PATH,
                     'GOOD',
                     'good_translation_units.yaml'))
    parsed = dict(parsed)
    entity_name = list(parsed.keys())[0]

    self.assertIsNone(err)
    entity = dict(parsed[entity_name])
    instance = entity_instance.EntityInstance(entity, self.universe)

    if not instance.IsValidEntityInstance():
      self.fail('exception incorrectly raised')

  def testValidateTranslationUnitsAndStates(self):
    parsed, err = instance_parser.parse_yaml(
        os.path.join(_TESTCASE_PATH,
                     'GOOD',
                     'good_translation_units_and_states.yaml'))
    parsed = dict(parsed)
    entity_name = list(parsed.keys())[0]

    self.assertIsNone(err)
    entity = dict(parsed[entity_name])
    instance = entity_instance.EntityInstance(entity, self.universe)

    if not instance.IsValidEntityInstance():
      self.fail('exception incorrectly raised')

  def testValidateBadTranslationUnitValues(self):
    parsed, err = instance_parser.parse_yaml(
        os.path.join(_TESTCASE_PATH,
                     'BAD',
                     'bad_translation_unit_values.yaml'))
    parsed = dict(parsed)
    entity_name = list(parsed.keys())[0]

    self.assertIsNone(err)
    entity = dict(parsed[entity_name])
    instance = entity_instance.EntityInstance(entity, self.universe)

    if instance.IsValidEntityInstance():
      self.fail('exception not raised')

  def testValidateBadTranslationStates(self):
    parsed, err = instance_parser.parse_yaml(
        os.path.join(_TESTCASE_PATH,
                     'BAD',
                     'bad_translation_states.yaml'))
    parsed = dict(parsed)
    entity_name = list(parsed.keys())[0]

    self.assertIsNone(err)
    entity = dict(parsed[entity_name])
    instance = entity_instance.EntityInstance(entity, self.universe)

    if instance.IsValidEntityInstance():
      self.fail('exception not raised')

if __name__ == '__main__':
  absltest.main()
