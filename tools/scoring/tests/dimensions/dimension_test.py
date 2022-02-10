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
"""Test for configuration file scoring tool
core component base class (dimension.py)."""

from absl.testing import absltest

from validate import handler as validator
from validate.generate_universe import BuildUniverse
from validate.entity_instance import EntityInstance
from score.dimensions.dimension import Dimension

import copy


def canonical_entity() -> EntityInstance:
  entity = list(
      validator.Deserialize(['tests/samples/canonical_entity.yaml'
                             ])[0].values())[0]
  # Append the type to be checked by entity_is_canonical()
  entity.type = BuildUniverse(use_simplified_universe=True).GetEntityType(
      entity.namespace, entity.type_name)
  return entity


def noncanonical_entity() -> EntityInstance:
  entity = list(
      validator.Deserialize(['tests/samples/noncanonical_entity.yaml'
                             ])[0].values())[0]
  # Append the type to be checked by entity_is_canonical()
  entity.type = BuildUniverse(use_simplified_universe=True).GetEntityType(
      entity.namespace, entity.type_name)
  return entity


class DimensionTest(absltest.TestCase):
  def setUp(self):
    super().setUp()
    self.dimension = Dimension(translations='translations')
    self.dimension.correct_virtual = 1
    self.dimension.correct_reporting = 1
    self.dimension.correct_ceiling_virtual = 2
    self.dimension.correct_ceiling_reporting = 2
    self.dimension.incorrect_virtual = 1
    self.dimension.incorrect_reporting = 1

    self.dimension_none = Dimension(deserialized_files='deserialized files')
    self.dimension_none.correct_virtual = 0
    self.dimension_none.correct_reporting = 0
    self.dimension_none.correct_ceiling_virtual = 0
    self.dimension_none.correct_ceiling_reporting = 0
    self.dimension_none.incorrect_virtual = 0
    self.dimension_none.incorrect_reporting = 0

    self.entities = {
        'canonical_type_appended':
        canonical_entity(),
        'noncanonical_type_appended':
        noncanonical_entity(),
        'reporting':
        list(
            validator.Deserialize(['tests/samples/reporting_entity.yaml'
                                   ])[0].values())[0],
        'virtual':
        list(
            validator.Deserialize(['tests/samples/virtual_entity.yaml'
                                   ])[0].values())[0],
    }

  def testArgumentAttributes(self):
    self.assertEqual(self.dimension.translations, 'translations')
    self.assertEqual(self.dimension.deserialized_files, None)

    self.assertEqual(self.dimension_none.translations, None)
    self.assertEqual(self.dimension_none.deserialized_files,
                     'deserialized files')

  def testArgumentExclusivity(self):
    with self.assertRaises(Exception) as not_enough:
      Dimension()
    self.assertEqual(
        not_enough.exception.args[0],
        '`translations` xor `deserialized_files` argument is required')

    with self.assertRaises(Exception) as too_many:
      Dimension(translations='translations',
                deserialized_files='deserialized files')
    self.assertEqual(
        too_many.exception.args[0],
        '`translations` or `deserialized_files` argument must be exclusive')

  def testCorrectTotal(self):
    self.assertEqual(self.dimension.correct_total(), 2)
    self.assertEqual(self.dimension_none.correct_total(), 0)

  def testCorrectCeiling(self):
    self.assertEqual(self.dimension.correct_ceiling(), 4)
    self.assertEqual(self.dimension_none.correct_total(), 0)

  def testIncorrectTotal(self):
    self.assertEqual(self.dimension.incorrect_total(), 2)
    self.assertEqual(self.dimension_none.correct_total(), 0)

  def testResultComposite(self):
    self.assertEqual(self.dimension.result_composite, 0.0)
    self.assertEqual(self.dimension_none.result_composite, None)

  def testResultVirtual(self):
    self.assertEqual(self.dimension.result_virtual, 0.0)
    self.assertEqual(self.dimension_none.result_virtual, None)

  def testResultReporting(self):
    self.assertEqual(self.dimension.result_reporting, 0.0)
    self.assertEqual(self.dimension_none.result_reporting, None)

  def testEntityIsCanonical(self):
    self.assertTrue(
        Dimension.entity_is_canonical(
            entity=self.entities['canonical_type_appended']))
    self.assertFalse(
        Dimension.entity_is_canonical(
            entity=self.entities['noncanonical_type_appended']))
    # This entity has had a type of `None` appended, thus it returns false.
    reporting_type_none = copy.copy(self.entities['reporting'])
    reporting_type_none.type = None
    self.assertFalse(Dimension.entity_is_canonical(entity=reporting_type_none))

  def testEntityIsReporting(self):
    self.assertTrue(
        Dimension.entity_is_reporting(entity=self.entities['reporting']))
    self.assertFalse(
        Dimension.entity_is_reporting(entity=self.entities['virtual']))

  def testEntityIsVirtual(self):
    self.assertTrue(
        Dimension.entity_is_virtual(entity=self.entities['virtual']))
    self.assertFalse(
        Dimension.entity_is_virtual(entity=self.entities['reporting']))

  def testStr(self):
    self.assertEqual(
        self.dimension.__str__(),
        '{result_composite: 0.0, result_virtual: 0.0, result_reporting: 0.0}')


if __name__ == '__main__':
  absltest.main()
