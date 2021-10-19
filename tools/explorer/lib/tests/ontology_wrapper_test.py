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

"""Testing module for ontology_wrapper.py."""
from absl.testing import absltest
from lib.model import EntityTypeField
from lib.model import StandardField
from lib.ontology_wrapper import OntologyWrapper

from validate.universe_helper.config_universe import create_simplified_universe
from yamlformat.validator import namespace_validator as nv


class OntologyTest(absltest.TestCase):

  def setUp(self):
    super(OntologyTest, self).setUp()
    self.universe = create_simplified_universe()
    nv.NamespaceValidator(self.universe.GetEntityTypeNamespaces())
    self.ontology = OntologyWrapper(self.universe)

  def testGetAllFieldsForTypeName(self):
    expected_output = [
        EntityTypeField('', 'exhaust_air_damper_command', False),
        EntityTypeField('', 'exhaust_air_damper_status', False),
        EntityTypeField('', 'manufacturer_label', True),
        EntityTypeField('', 'model_label', True)
    ]

    function_output = self.ontology.GetFieldsForTypeName(
        'HVAC',
        'DMP_EDM'
    )

    self.assertEqual(function_output, expected_output)

  def testGetRequiredFieldsForTypeName(self):
    expected_output = [
        EntityTypeField('', 'exhaust_air_damper_command', False),
        EntityTypeField('', 'exhaust_air_damper_status', False)
    ]

    function_output = self.ontology.GetFieldsForTypeName(
        namespace='HVAC',
        entity_type_name='DMP_EDM',
        required_only=True
    )

    self.assertEqual(function_output, expected_output)

  def testValidField(self):
    valid_test_field = StandardField('', 'zone_use_label')
    function_output = self.ontology.IsFieldValid(valid_test_field)
    self.assertTrue(function_output)

  def testInvalidField(self):
    invalid_test_field = StandardField('HVAC', 'exhaust_air_damper_command')
    function_output = self.ontology.IsFieldValid(invalid_test_field)
    self.assertFalse(function_output)

if __name__ == '__main__':
  absltest.main()
