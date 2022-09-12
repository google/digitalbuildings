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
"""Constants for ABEL testing libary."""

from os import path

from model.constants import APPLICATION_ROOT
from model.constants import BC_GUID
from model.constants import BUILDING_CODE
from model.constants import CLOUD_DEVICE_ID
from model.constants import CONNECTION_TYPE
from model.constants import CONNECTIONS
from model.constants import ENTITIES
from model.constants import ENTITY_CODE
from model.constants import ENTITY_FIELDS
from model.constants import ETAG
from model.constants import IS_REPORTING
from model.constants import METADATA
from model.constants import NAMESPACE
from model.constants import RAW_FIELD_NAME
from model.constants import RAW_STATE
from model.constants import RAW_UNIT_PATH
from model.constants import RAW_UNIT_VALUE
from model.constants import REPORTING_ENTITY_CODE
from model.constants import REPORTING_ENTITY_FIELD_NAME
from model.constants import REPORTING_ENTITY_GUID
from model.constants import SITES
from model.constants import SOURCE_ENTITY_CODE
from model.constants import SOURCE_ENTITY_GUID
from model.constants import STANDARD_FIELD_NAME
from model.constants import STANDARD_STATE
from model.constants import STANDARD_UNIT_VALUE
from model.constants import STATES
from model.constants import TARGET_ENTITY_CODE
from model.constants import TARGET_ENTITY_GUID
from model.constants import TYPE_NAME
from model.units import Units
from tests import test_constants

TEST_ROOT = path.join(APPLICATION_ROOT, 'tests')
TEST_RESOURCES = path.join(TEST_ROOT, 'test_resources')
TEST_BUILDING_CONFIG_PATH = test_constants.TEST_INSTANCES

TEST_NAMESPACE = 'HVAC'
TEST_GENERAL_TYPE = 'CHWS'
TEST_TYPE_NAME = 'CHWS_WDT'

# Constants for EntityField testing
TEST_STANDARD_FIELD_NAME = 'supply_water_temperature_sensor'
TEST_STANDARD_FIELD_NAME_2 = 'run_command'
TEST_RAW_FIELD_NAME = 'points.supply_water_temperature_sensor.present_value'
TEST_RAW_FIELD_NAME_2 = 'points.run_command.present_value'
TEST_RAW_UNIT_PATH = 'points.supply_water_temperature_sensor.units'
TEST_STANDARD_UNIT_VALUE = 'degrees-celsius'
TEST_DEVICE_ID = '12345'

# Constants for Entity testing
TEST_VIRTUAL_ENTITY_CODE = 'VLV-23'
TEST_REPORTING_ENTITY_CODE = 'CHWS-1'
TEST_ENTITY_IS_REPORTING = False
TEST_CLOUD_DEVICE_ID = '12345678910'
TEST_REPORTING_GUID = 'test_reporting_guid'
TEST_VIRTUAL_GUID = 'test_virtual_guid'
TEST_ETAG = '1234567'

# Test instances and resources
TEST_SITE_DICT = {
    BUILDING_CODE: 'UK-LON-S2',
    BC_GUID: 'test_site_guid',
}

TEST_SITE_DICT_NO_GUID = {
    BUILDING_CODE: 'UK-LON-S2',
    BC_GUID: None,
}

TEST_REPORTING_ENTITY_DICT = {
    ENTITY_CODE: TEST_REPORTING_ENTITY_CODE,
    BC_GUID: TEST_REPORTING_GUID,
    NAMESPACE: TEST_NAMESPACE,
    ETAG: None,
    CLOUD_DEVICE_ID: TEST_CLOUD_DEVICE_ID,
    TYPE_NAME: TEST_TYPE_NAME,
    IS_REPORTING: 'TRUE',
    METADATA + '.test': 'test metadata'
}

TEST_VIRTUAL_ENTITY_DICT = {
    ENTITY_CODE: TEST_VIRTUAL_ENTITY_CODE,
    BC_GUID: TEST_VIRTUAL_GUID,
    NAMESPACE: TEST_NAMESPACE,
    ETAG: None,
    CLOUD_DEVICE_ID: None,
    TYPE_NAME: TEST_TYPE_NAME,
    IS_REPORTING: 'FASLE',
    METADATA + '.test': 'test metadata'
}

TEST_ENTITY_FIELD_DICT_WITH_NO_UNITS = {
    STANDARD_FIELD_NAME: TEST_STANDARD_FIELD_NAME_2,
    RAW_FIELD_NAME: TEST_RAW_FIELD_NAME_2,
    ENTITY_CODE: TEST_REPORTING_ENTITY_CODE,
    REPORTING_ENTITY_FIELD_NAME: TEST_STANDARD_FIELD_NAME_2,
    REPORTING_ENTITY_CODE: TEST_REPORTING_ENTITY_CODE,
    REPORTING_ENTITY_GUID: TEST_REPORTING_GUID,
    BC_GUID: TEST_REPORTING_GUID,
    RAW_UNIT_PATH: 'no-units',
    STANDARD_UNIT_VALUE: 'no-units',
    RAW_UNIT_VALUE: 'no-units',
    METADATA + '.test': 'test metadata'
}

TEST_ENTITY_FIELD_DICT_WITH_UNITS = {
    STANDARD_FIELD_NAME:
        TEST_STANDARD_FIELD_NAME,
    RAW_FIELD_NAME:
        TEST_RAW_FIELD_NAME,
    REPORTING_ENTITY_FIELD_NAME:
        TEST_STANDARD_FIELD_NAME + '_1',
    ENTITY_CODE:
        TEST_VIRTUAL_ENTITY_CODE,
    BC_GUID:
        TEST_VIRTUAL_GUID,
    REPORTING_ENTITY_CODE:
        TEST_REPORTING_ENTITY_CODE,
    REPORTING_ENTITY_GUID:
        TEST_REPORTING_GUID,
    RAW_UNIT_PATH:
        'pointset.points.filter_differential_pressure_setpoint.units',
    STANDARD_UNIT_VALUE:
        'pascals',
    RAW_UNIT_VALUE:
        'Pa',
    METADATA + '.test':
        'test metadata'
}

TEST_CONNECTION_DICT = {
    SOURCE_ENTITY_CODE: TEST_REPORTING_ENTITY_CODE,
    SOURCE_ENTITY_GUID: TEST_REPORTING_GUID,
    TARGET_ENTITY_CODE: TEST_VIRTUAL_ENTITY_CODE,
    TARGET_ENTITY_GUID: TEST_VIRTUAL_GUID,
    CONNECTION_TYPE: 'CONTROLS'
}

TEST_STATE_DICT = {
    ENTITY_CODE: TEST_REPORTING_ENTITY_CODE,
    BC_GUID: TEST_REPORTING_GUID,
    STANDARD_FIELD_NAME: TEST_STANDARD_FIELD_NAME_2,
    STANDARD_STATE: 'ON',
    RAW_STATE: 'TRUE'
}

TEST_UNITS = Units(
    raw_unit_path='points.return_air_temperature_sensor.units',
    standard_to_raw_unit_map={'degrees_celsius': 'degC'})

TEST_SPREADSHEET = {
    SITES: [TEST_SITE_DICT],
    ENTITIES: [TEST_REPORTING_ENTITY_DICT, TEST_VIRTUAL_ENTITY_DICT],
    ENTITY_FIELDS: [
        TEST_ENTITY_FIELD_DICT_WITH_UNITS, TEST_ENTITY_FIELD_DICT_WITH_NO_UNITS
    ],
    CONNECTIONS: [TEST_CONNECTION_DICT],
    STATES: [TEST_STATE_DICT]
}
