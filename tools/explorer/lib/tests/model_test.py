# Copyright 2021 Google LLC
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

"""Testing module for model.py."""
from absl.testing import absltest
from lib.model import EntityTypeField
from lib.model import Match
from lib.model import StandardField
from lib.model import StandardizeField

from validate.universe_helper.config_universe import create_simplified_universe
from yamlformat.validator import namespace_validator as nv
from yamlformat.validator import presubmit_validate_types_lib
from yamlformat.validator.entity_type_lib import EntityType
from yamlformat.validator.external_file_lib import RecursiveDirWalk


class StandardFieldTest(absltest.TestCase):

  def setUp(self):
    super(StandardFieldTest, self).setUp()
    self.test_standard_field = StandardField(
        namespace_name='', standard_field_name='supply_air_flowrate_sensor')

  def testGetNamespaceName(self):
    # testing with '' because it is the global namespace which, in practice,
    # all fields are defined under the global namespace
    expected_output = ''
    function_output = self.test_standard_field.GetNamespaceName()

    self.assertEqual(function_output, expected_output)

  def testGetStandardFieldName(self):
    expected_output = 'supply_air_flowrate_sensor'
    function_output = self.test_standard_field.GetStandardFieldName()

    self.assertEqual(function_output, expected_output)


class EntityTypeFieldTest(absltest.TestCase):
  # Testing EntityTypeField objects defined in the global namespace

  def setUp(self):
    super(EntityTypeFieldTest, self).setUp()
    self.test_entity_type_field = EntityTypeField(
        namespace_name='',
        standard_field_name='supply_air_flowrate_sensor',
        is_optional=False,
        increment='_1_12')

  def testGetIncrement(self):
    expected_output = '_1_12'
    function_output = self.test_entity_type_field.GetIncrement()

    self.assertEqual(function_output, expected_output)

  def testIsOptional(self):
    self.assertFalse(self.test_entity_type_field.IsOptional())

  def testStandardizeField(self):
    expected_output = StandardField(
        namespace_name='', standard_field_name='supply_air_flowrate_sensor')

    function_output = StandardizeField(self.test_entity_type_field)

    self.assertEqual(function_output, expected_output)


class ModelTest(absltest.TestCase):

  def setUp(self):
    super(ModelTest, self).setUp()
    self.universe = create_simplified_universe()
    nv.NamespaceValidator(self.universe.GetEntityTypeNamespaces())
    test_entity_type = self.universe.entity_type_universe.GetEntityType(
        namespace_name='HVAC', typename='DMP_EDM')
    test_field_list = [
        EntityTypeField(optwrapper.field.namespace, optwrapper.field.field[0:],
                        optwrapper.optional, optwrapper.field.increment)
        for optwrapper in test_entity_type.GetAllFields().values()
    ]
    self.test_match = Match(
        field_list=test_field_list,
        entity_type=test_entity_type,
        match_score=1.0)

  def testGetFieldList(self):
    expected_output = [
        EntityTypeField('', 'manufacturer_label', True),
        EntityTypeField('', 'model_label', True),
        EntityTypeField('', 'exhaust_air_damper_command', False),
        EntityTypeField('', 'exhaust_air_damper_status', False)
    ]

    function_output = self.test_match.GetFieldList()

    self.assertEqual(function_output, expected_output)

  def testGetEntityType(self):
    function_output = self.test_match.GetEntityType()

    self.assertIsInstance(function_output, EntityType)
    self.assertEqual(function_output.typename, 'DMP_EDM')

  def testGetMatchScore(self):
    function_output = self.test_match.GetMatchScore()

    self.assertEqual(function_output, 1.0)


if __name__ == '__main__':
  absltest.main()
