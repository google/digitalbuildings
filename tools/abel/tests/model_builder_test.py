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
from tests.test_constants import TEST_CONNECTION_DICT
from tests.test_constants import TEST_ENTITY_FIELD_DICT_WITH_STATES
from tests.test_constants import TEST_ENTITY_FIELD_DICT_WITH_UNITS
from tests.test_constants import TEST_MISSING_ENTITY_FIELD
from tests.test_constants import TEST_REPORTING_ENTITY_DICT
from tests.test_constants import TEST_RESOURCES
from tests.test_constants import TEST_SITE_DICT
from tests.test_constants import TEST_STATE_DICT
from tests.test_constants import TEST_VIRTUAL_ENTITY_DICT


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
            TEST_ENTITY_FIELD_DICT_WITH_STATES, TEST_MISSING_ENTITY_FIELD
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
                     EntityField.FromDict(TEST_ENTITY_FIELD_DICT_WITH_STATES))
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
            TEST_ENTITY_FIELD_DICT_WITH_STATES
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

  def testFromBuildingConfigWithMissingFields(self):
    self.guid_to_entity_map.Clear()
    imported_building_config = import_helper.DeserializeBuildingConfiguration(
        filepath=os.path.join(TEST_RESOURCES,
                              'building_config_with_missing_fields.yaml'))

    model = ModelBuilder.FromBuildingConfig(
        site=imported_building_config[0],
        building_config_dict=imported_building_config[1])

    self.assertIsInstance(
        self.guid_to_entity_map.GetEntityByGuid(model.site.guid), Site)
    self.assertEqual(model.site.code, 'TEST_BUILDING')
    self.assertLen(model.entities, 1)
    self.assertLen(model.fields, 3)
    self.assertLen([field for field in model.fields if field.missing], 2)
    self.assertEmpty(model.connections)
    self.assertLen(model.states, 2)

  def testToModelDictionary(self):
    """Builds a dictionary model of an ABEL spreadsheet.

    Values correspond to spreadsheet headers and values.
    """
    test_spreadsheet = {
        SITES: [TEST_SITE_DICT],
        ENTITIES: [TEST_REPORTING_ENTITY_DICT, TEST_VIRTUAL_ENTITY_DICT],
        ENTITY_FIELDS: [
            TEST_ENTITY_FIELD_DICT_WITH_UNITS,
            TEST_ENTITY_FIELD_DICT_WITH_STATES, TEST_MISSING_ENTITY_FIELD
        ],
        CONNECTIONS: [TEST_CONNECTION_DICT],
        STATES: [TEST_STATE_DICT]
    }
    self.guid_to_entity_map.Clear()
    model = ModelBuilder.FromSpreadsheet(test_spreadsheet)
    expected_result = {
        'Site': [['Building Code', 'Entity Guid'],
                 ['UK-LON-S2', 'test_site_guid']],
        'Entities': [
            [
                'Entity Code', 'Entity Guid', 'Etag', 'Is Reporting',
                'Cloud Device ID', 'DBO Namespace', 'DBO Entity Type Name'
            ],
            [
                'CHWS-1',
                'test_reporting_guid',
                # Etag = None
                None,
                # Is reporting = True
                True,
                '2541901344105616',
                'HVAC',
                'CHWS_WDT'
            ],
            [
                'VLV-23',
                'test_virtual_guid',
                # Etag = None
                None,
                # Is reporting = False
                False,
                # Cloud device id = None because this is a virtual entity
                None,
                'HVAC',
                'CHWS_WDT'
            ]
        ],
        'Entity Fields':
            [[
                'Entity Code', 'Entity Guid', 'Reporting Entity Code',
                'Reporting Entity Guid', 'Reporting Entity Field',
                'DBO Standard Field Name', 'Missing', 'Raw Field Name',
                'Raw Unit Path', 'DBO Standard Unit Value', 'Raw Unit Value'
            ],
             [
                 'VLV-23', 'test_virtual_guid', 'CHWS-1', 'test_reporting_guid',
                 'supply_water_temperature_sensor_1',
                 'supply_water_temperature_sensor', 'FALSE',
                 'points.supply_water_temperature_sensor.present_value',
                 'pointset.points.filter_differential_pressure_setpoint.units',
                 'pascals', 'Pa'
             ],
             [
                 'CHWS-1', 'test_reporting_guid', 'CHWS-1',
                 'test_reporting_guid', 'fire_alarm_5', 'fire_alarm', 'FALSE',
                 'points.fire_alarm_5.present_value'
             ],
             [
                 'VLV-23', 'test_virtual_guid', 'CHWS-1', 'test_reporting_guid',
                 None, 'supply_water_temperature_sensor', 'TRUE', None
             ]],
        'States': [[
            'Entity Code', 'Entity Guid', 'Reporting Entity Field',
            'DBO Standard State', 'Raw State'
        ], ['CHWS-1', 'test_reporting_guid', 'fire_alarm_5', 'ON', 'TRUE']],
        'Connections': [[
            'Source Entity Code', 'Source Entity Guid', 'DBO Connection Type',
            'Target Entity Code', 'Target Entity Guid'
        ],
                        [
                            'CHWS-1', 'test_reporting_guid', 'CONTROLS',
                            'VLV-23', 'test_virtual_guid'
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
