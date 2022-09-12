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
"""Tests for model_builder."""

import os

from absl.testing import absltest

from model import import_helper
from model.constants import CONNECTIONS
from model.constants import ENTITIES
from model.constants import ENTITY_FIELDS
from model.constants import SITES
from model.constants import STATES
from model.entity import ReportingEntity
from model.entity_field import EntityField
from model.guid_to_entity_map import GuidToEntityMap
from model.model_builder import ModelBuilder
from model.site import Site
from model.state import State
from abel.tests.test_constants import TEST_CONNECTION_DICT
from abel.tests.test_constants import TEST_ENTITY_FIELD_DICT_WITH_NO_UNITS
from abel.tests.test_constants import TEST_ENTITY_FIELD_DICT_WITH_UNITS
from abel.tests.test_constants import TEST_REPORTING_ENTITY_DICT
from abel.tests.test_constants import TEST_RESOURCES
from abel.tests.test_constants import TEST_SITE_DICT
from abel.tests.test_constants import TEST_STATE_DICT
from abel.tests.test_constants import TEST_VIRTUAL_ENTITY_DICT


class ModelBuilderTest(absltest.TestCase):

  def setUp(self):
    super().setUp()
    self.guid_to_entity_map = GuidToEntityMap()

  def testBuild(self):
    test_spreadsheet = {
        SITES: [TEST_SITE_DICT],
        ENTITIES: [TEST_REPORTING_ENTITY_DICT, TEST_VIRTUAL_ENTITY_DICT],
        ENTITY_FIELDS: [
            TEST_ENTITY_FIELD_DICT_WITH_UNITS,
            TEST_ENTITY_FIELD_DICT_WITH_NO_UNITS
        ],
        CONNECTIONS: [TEST_CONNECTION_DICT],
        STATES: [TEST_STATE_DICT]
    }
    self.guid_to_entity_map.Clear()

    model = ModelBuilder.FromSpreadsheet(test_spreadsheet)
    model.Build()
    # Traversing through the model to check that model is connected properly
    added_entity = self.guid_to_entity_map.GetEntityByGuid(
        model.site.entities[0])
    source_entity = self.guid_to_entity_map.GetEntityByGuid(
        self.guid_to_entity_map.GetEntityByGuid(
            model.site.entities[1]).connections[0].source_entity_guid)

    self.assertEqual(added_entity.translations[1],
                     EntityField.FromDict(TEST_ENTITY_FIELD_DICT_WITH_NO_UNITS))
    self.assertEqual(added_entity.translations[1].states[0],
                     State.FromDict(TEST_STATE_DICT))
    self.assertEqual(source_entity.code,
                     ReportingEntity.FromDict(TEST_REPORTING_ENTITY_DICT).code)

  def testFromSpreadsheet(self):
    test_spreadsheet = {
        SITES: [TEST_SITE_DICT],
        ENTITIES: [TEST_REPORTING_ENTITY_DICT, TEST_VIRTUAL_ENTITY_DICT],
        ENTITY_FIELDS: [
            TEST_ENTITY_FIELD_DICT_WITH_UNITS,
            TEST_ENTITY_FIELD_DICT_WITH_NO_UNITS
        ],
        CONNECTIONS: [TEST_CONNECTION_DICT],
        STATES: [TEST_STATE_DICT]
    }
    self.guid_to_entity_map.Clear()

    model = ModelBuilder.FromSpreadsheet(test_spreadsheet)

    self.assertIsInstance(
        self.guid_to_entity_map.GetEntityByGuid(model.site.guid), Site)
    self.assertEqual(model.site, Site.FromDict(TEST_SITE_DICT))
    self.assertLen(model.entities, 2)
    self.assertLen(model.fields, 2)
    self.assertLen(model.connections, 1)
    self.assertLen(model.states, 1)

  def testFromBuildingConfig(self):
    self.guid_to_entity_map.Clear()
    imported_building_config = import_helper.DeserializeBuildingConfiguration(
        filepath=os.path.join(TEST_RESOURCES, 'good_test_building_config.yaml'))

    model = ModelBuilder.FromBuildingConfig(
        site=imported_building_config[0],
        building_config_dict=imported_building_config[1])

    self.assertIsInstance(
        self.guid_to_entity_map.GetEntityByGuid(model.site.guid), Site)
    self.assertEqual(model.site.code, 'TEST_BUILDING')
    self.assertLen(model.entities, 6)
    self.assertLen(model.fields, 9)
    self.assertLen(model.connections, 1)
    self.assertLen(model.states, 2)

  def testToModelDictionary(self):
    test_spreadsheet = {
        SITES: [TEST_SITE_DICT],
        ENTITIES: [TEST_REPORTING_ENTITY_DICT, TEST_VIRTUAL_ENTITY_DICT],
        ENTITY_FIELDS: [
            TEST_ENTITY_FIELD_DICT_WITH_UNITS,
            TEST_ENTITY_FIELD_DICT_WITH_NO_UNITS
        ],
        CONNECTIONS: [TEST_CONNECTION_DICT],
        STATES: [TEST_STATE_DICT]
    }
    self.guid_to_entity_map.Clear()
    model = ModelBuilder.FromSpreadsheet(test_spreadsheet)
    expected_result = {
        'Site': [['Building Code', 'Guid'], ['UK-LON-S2', 'test_site_guid']],
        'Entities': [[
            'Entity Code', 'Guid', 'Is Reporting', 'Cloud Device ID', 'Etag',
            'Namespace', 'Type Name'
        ],
                     [
                         'CHWS-1', 'test_reporting_guid', True, '12345678910',
                         None, 'HVAC', 'CHWS_WDT'
                     ],
                     [
                         'VLV-23', 'test_virtual_guid', False, None, None,
                         'HVAC', 'CHWS_WDT'
                     ]],
        'Entity Fields':
            [[
                'Standard Field Name', 'Raw Field Name',
                'Reporting Entity Field', 'Entity Code', 'Guid',
                'Reporting Entity Code', 'Reporting Entity Guid',
                'Raw Unit Path', 'Standard Unit Value', 'Raw Unit Value'
            ],
             [
                 'supply_water_temperature_sensor',
                 'points.supply_water_temperature_sensor.present_value',
                 'supply_water_temperature_sensor_1', 'VLV-23',
                 'test_virtual_guid', 'CHWS-1', 'test_reporting_guid',
                 'pointset.points.filter_differential_pressure_setpoint.units',
                 'pascals', 'Pa'
             ],
             [
                 'run_command', 'points.run_command.present_value',
                 'run_command', 'CHWS-1', 'test_reporting_guid', 'CHWS-1',
                 'test_reporting_guid'
             ]],
        'States': [[
            'Entity Code', 'Guid', 'Standard Field Name', 'Standard State',
            'Payload State'
        ], ['CHWS-1', 'test_reporting_guid', 'run_command', 'ON', 'TRUE']],
        'Connections': [[
            'Source Entity Code', 'Source Entity Guid', 'Target Entity Code',
            'Target Entity Guid', 'Connection Type'
        ],
                        [
                            'CHWS-1', 'test_reporting_guid', 'VLV-23',
                            'test_virtual_guid', 'CONTROLS'
                        ]]
    }

    sheets_result = model.ToModelDictionary()

    self.assertEqual(expected_result, sheets_result)

  def testReportingEntitiesAddedFromEntityInstance(self):
    self.guid_to_entity_map.Clear()
    imported_building_config = import_helper.DeserializeBuildingConfiguration(
        filepath=os.path.join(TEST_RESOURCES, 'good_test_building_config.yaml'))

    model = ModelBuilder.FromBuildingConfig(
        site=imported_building_config[0],
        building_config_dict=imported_building_config[1])

    self.assertNotEqual(model.fields[2].entity_guid,
                        model.fields[2].reporting_entity_guid)
    self.assertNotEqual(model.fields[2].standard_field_name,
                        model.fields[2].reporting_entity_field_name)


if __name__ == '__main__':
  absltest.main()
