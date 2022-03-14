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
"""Tests for EntityType class."""

from absl.testing import absltest

from model.entity_type import EntityType
from lib import ontology_wrapper
from validate import universe_helper


class EntityTypeTest(absltest.TestCase):

  def setUp(self):
    super().setUp()
    self.universe = universe_helper.create_simplified_universe()
    self.ontology = ontology_wrapper.OntologyWrapper(self.universe)
    self.test_namespace = 'HVAC'
    self.test_general_type = 'DMP'
    self.test_required_fields = [
        'exhaust_air_damper_command',
        'exhaust_air_damper_status'
    ]
    self.test_optional_fields = [
        'model_label',
        'manufacturer_label'
    ]
    self.test_type_name = 'DMP_EDM'

  def testEntityFromCompleteDict(self):
    test_entity_type_dict_complete = {
        'namespace': self.test_namespace,
        'general_type': self.test_general_type,
        'required_fields': self.test_required_fields,
        'optional_fields': self.test_optional_fields,
        'entity_type': self.test_type_name
    }

    test_entity_type_with_type_name = EntityType.FromDict(
        test_entity_type_dict_complete, self.ontology)

    self.assertEqual(self.test_type_name,
                     test_entity_type_with_type_name.entity_type_name)
    self.assertEqual(self.test_general_type,
                     test_entity_type_with_type_name.general_type)
    self.assertEqual(self.test_namespace,
                     test_entity_type_with_type_name.namespace)
    self.assertEqual(self.test_required_fields,
                     test_entity_type_with_type_name.required_fields)
    self.assertEqual(self.test_optional_fields,
                     test_entity_type_with_type_name.optional_fields)
    self.assertEqual(self.test_type_name,
                     test_entity_type_with_type_name.entity_type_name)

  def testEntityTypeGeneratedType(self):
    test_entity_type_dict_without_type_name = {
        'namespace': self.test_namespace,
        'general_type': self.test_general_type,
        'required_fields': self.test_required_fields,
        'optional_fields': self.test_optional_fields,
        'entity_type': None
    }

    test_entity_type_without_type_name = EntityType.FromDict(
        test_entity_type_dict_without_type_name, self.ontology)

    self.assertEqual(self.test_type_name,
                     test_entity_type_without_type_name.entity_type_name)
    self.assertEqual(self.test_general_type,
                     test_entity_type_without_type_name.general_type)
    self.assertEqual(self.test_namespace,
                     test_entity_type_without_type_name.namespace)
    self.assertEqual(self.test_required_fields,
                     test_entity_type_without_type_name.required_fields)
    self.assertEqual(self.test_optional_fields,
                     test_entity_type_without_type_name.optional_fields)

if __name__ == '__main__':
  absltest.main()
