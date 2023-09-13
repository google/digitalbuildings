# Copyright 2023 Google LLC
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
"""Tests for model_builder."""

import os
from unittest import mock
import uuid

from absl.testing import absltest

# pylint: disable=g-importing-member
from model import import_helper
from model.constants import CONNECTIONS
from model.constants import ENTITIES
from model.constants import ENTITY_FIELDS
from model.constants import SITES
from model.constants import STATES
from model.entity import ReportingEntity
from model.entity_field import MissingField
from model.entity_field import MultistateValueField
from model.model_builder import Model
from model.site import Site
from model.state import State
from tests.test_constants import TEST_CONNECTION_DICT
from tests.test_constants import TEST_DIMENSIONAL_VALUE_FIELD_DICT
from tests.test_constants import TEST_FIELD_DICT_NO_UNITS
from tests.test_constants import TEST_MISSING_FIELD_DICT
from tests.test_constants import TEST_MULTISTATE_VALUE_FIELD_DICT
from tests.test_constants import TEST_REPORTING_ENTITY_DICT
from tests.test_constants import TEST_REPORTING_ENTITY_DICT_NO_GUID
from tests.test_constants import TEST_RESOURCES
from tests.test_constants import TEST_SITE_DICT
from tests.test_constants import TEST_STATE_DICT
from tests.test_constants import TEST_VIRTUAL_ENTITY_DICT


# pylint: disable=unused-variable
class ModelBuilderTest(absltest.TestCase):

  def testBuild(self):
    test_spreadsheet = {
        SITES: [TEST_SITE_DICT],
        ENTITIES: [TEST_REPORTING_ENTITY_DICT, TEST_VIRTUAL_ENTITY_DICT],
        ENTITY_FIELDS: [
            TEST_DIMENSIONAL_VALUE_FIELD_DICT,
            TEST_MULTISTATE_VALUE_FIELD_DICT,
            TEST_MISSING_FIELD_DICT,
        ],
        CONNECTIONS: [TEST_CONNECTION_DICT],
        STATES: [TEST_STATE_DICT],
    }

    unbuilt_model, operations = Model.Builder.FromSpreadsheet(test_spreadsheet)
    model = unbuilt_model.Build()
    # Traversing through the model to check that model is connected properly
    added_entity = model.guid_to_entity_map.GetEntityByGuid(
        model.site.entities[0]
    )
    source_entity = model.guid_to_entity_map.GetEntityByGuid(
        model.guid_to_entity_map.GetEntityByGuid(model.site.entities[1])
        .connections[0]
        .source_entity_guid
    )
    expected_multistate_entity = MultistateValueField.FromDict(
        TEST_MULTISTATE_VALUE_FIELD_DICT,
    )
    expected_multistate_entity.states.append(
        State.FromDict(TEST_STATE_DICT)
    )

    self.assertEqual(
        added_entity.translations[1],
        expected_multistate_entity,
    )
    self.assertEqual(
        added_entity.translations[1].states[0],
        State.FromDict(TEST_STATE_DICT),
    )
    self.assertEqual(
        source_entity.code,
        ReportingEntity.FromDict(TEST_REPORTING_ENTITY_DICT).code,
    )

  @mock.patch.object(uuid, 'uuid4')
  def testFromSpreadsheet_reportingEntityNoGuid_createsGuidFromUuid(
      self, mock_uuid
  ):
    mock_uuid.uuid4().return_value = 'uuid-created-guid'
    test_spreadsheet = {
        SITES: [TEST_SITE_DICT],
        ENTITIES: [
            TEST_REPORTING_ENTITY_DICT_NO_GUID,
            TEST_VIRTUAL_ENTITY_DICT,
        ],
        ENTITY_FIELDS: [
            TEST_DIMENSIONAL_VALUE_FIELD_DICT,
            TEST_FIELD_DICT_NO_UNITS,
            TEST_MISSING_FIELD_DICT,
        ],
        CONNECTIONS: [TEST_CONNECTION_DICT],
        STATES: [TEST_STATE_DICT],
    }

    unbuilt_model, operations = Model.Builder.FromSpreadsheet(test_spreadsheet)
    model = unbuilt_model.Build()

    mock_uuid.assert_called_once_with()
    self.assertIsInstance(
        model.guid_to_entity_map.GetEntityByGuid(model.site.guid), Site
    )
    self.assertEqual(model.site, Site.FromDict(TEST_SITE_DICT))
    self.assertLen(model.entities, 2)
    self.assertLen(model.fields, 3)
    self.assertLen(model.connections, 1)
    self.assertLen(model.states, 1)
    self.assertLen(model.guid_to_entity_map.GetGuidToEntityMap(), 3)

  def testFromSpreadsheet_buildsModel(self):
    test_spreadsheet = {
        SITES: [TEST_SITE_DICT],
        ENTITIES: [TEST_REPORTING_ENTITY_DICT, TEST_VIRTUAL_ENTITY_DICT],
        ENTITY_FIELDS: [
            TEST_DIMENSIONAL_VALUE_FIELD_DICT,
            TEST_FIELD_DICT_NO_UNITS,
            TEST_MISSING_FIELD_DICT,
        ],
        CONNECTIONS: [TEST_CONNECTION_DICT],
        STATES: [TEST_STATE_DICT],
    }

    unbuilt_model, operations = Model.Builder.FromSpreadsheet(test_spreadsheet)
    model = unbuilt_model.Build()

    self.assertIsInstance(
        model.guid_to_entity_map.GetEntityByGuid(model.site.guid), Site
    )
    self.assertEqual(model.site, Site.FromDict(TEST_SITE_DICT))
    self.assertLen(model.entities, 2)
    self.assertLen(model.fields, 3)
    self.assertLen(model.connections, 1)
    self.assertLen(model.states, 1)
    self.assertLen(model.guid_to_entity_map.GetGuidToEntityMap(), 3)

  def testFromBuildingConfig(self):
    imported_building_config = import_helper.DeserializeBuildingConfiguration(
        filepath=os.path.join(TEST_RESOURCES, 'good_test_building_config.yaml')
    )

    unbuilt_model, operations = Model.Builder.FromBuildingConfig(
        site=imported_building_config[0],
        building_config_dict=imported_building_config[1],
    )
    model = unbuilt_model.Build()

    self.assertIsInstance(
        model.guid_to_entity_map.GetEntityByGuid(model.site.guid), Site
    )
    self.assertEqual(model.site.code, 'TEST_BUILDING')
    self.assertLen(model.entities, 6)
    self.assertLen(model.fields, 9)
    self.assertLen(model.connections, 1)
    self.assertLen(model.states, 2)
    self.assertLen(model.guid_to_entity_map.GetGuidToEntityMap(), 7)

  def testFromBuildingConfigWithMissingFields(self):
    imported_building_config = import_helper.DeserializeBuildingConfiguration(
        filepath=os.path.join(
            TEST_RESOURCES, 'building_config_with_missing_fields.yaml'
        )
    )

    unbuilt_model, operations = Model.Builder.FromBuildingConfig(
        site=imported_building_config[0],
        building_config_dict=imported_building_config[1],
    )
    model = unbuilt_model.Build()

    self.assertIsInstance(
        model.guid_to_entity_map.GetEntityByGuid(model.site.guid), Site
    )
    self.assertEqual(model.site.code, 'TEST_BUILDING')
    self.assertLen(model.entities, 1)
    self.assertLen(model.fields, 3)
    self.assertLen(
        [field for field in model.fields if isinstance(field, MissingField)],
        2,
    )
    self.assertEmpty(model.connections)
    self.assertLen(model.states, 2)
    self.assertLen(model.guid_to_entity_map.GetGuidToEntityMap(), 2)

  def testReportingEntitiesAddedFromEntityInstance(self):
    imported_building_config = import_helper.DeserializeBuildingConfiguration(
        filepath=os.path.join(TEST_RESOURCES, 'good_test_building_config.yaml')
    )

    unbuilt_model, operation = Model.Builder.FromBuildingConfig(
        site=imported_building_config[0],
        building_config_dict=imported_building_config[1],
    )
    model = unbuilt_model.Build()

    self.assertNotEqual(
        model.fields[2].entity_guid, model.fields[2].reporting_entity_guid
    )
    self.assertNotEqual(
        model.fields[2].std_field_name,
        model.fields[2].reporting_entity_field_name,
    )


if __name__ == '__main__':
  absltest.main()
