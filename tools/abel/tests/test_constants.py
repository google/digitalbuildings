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

# pylint: disable=g-importing-member
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
from model.constants import MISSING
from model.constants import NAMESPACE
from model.constants import NO_UNITS
from model.constants import OPERATION
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


# pylint: disable=line-too-long

TEST_ROOT = path.join(APPLICATION_ROOT, 'tests')
TEST_RESOURCES = path.join(TEST_ROOT, 'test_resources')

TEST_NAMESPACE = 'HVAC'
TEST_GENERAL_TYPE = 'CHWS'
TEST_TYPE_NAME = 'CHWS_WDT'

# Constants for EntityField testing
TEST_DIMENSIONAL_VALUE_STANDARD_FIELD_NAME = 'supply_water_temperature_sensor'
TEST_MULTISTATE_STANDARD_FIELD_NAME = 'fire_alarm'
TEST_MISSING_STANDARD_FIELD_NAME = 'return_water_temperature_sensor'
TEST_STANDARD_FIELD_NAME_NO_UNITS = 'cooling_stage_run_count'
TEST_BAD_MULTISTATE_FIELD_NAME = 'bad_mulistate_field'
TEST_DIMENSIONAL_REPORTING_FIELD_NAME = 'supply_water_temperature_sensor_1'
TEST_MULTISTATE_REPORTING_FIELD_NAME = 'fire_alarm_5'
TEST_DIMENSIONAL_VALUE_RAW_FIELD_NAME = 'points.supply_water_temperature_sensor.present_value'
TEST_MULTISTATE_RAW_FIELD_NAME = 'points.fire_alarm_5.present_value'
TEST_MISSING_RAW_FIELD_NAME = 'points.return_water_temperature_sensor.present_value'
TEST_RAW_FIELD_NAME_NO_UNITS = 'points.cooling_stage_run_count.present_value'
TEST_BAD_MULTISTATE_FIELD_RAW_FIELD_NAME = 'points.bad_multistate_field.present_value'
TEST_RAW_UNIT_PATH = 'pointset.points.supply_water_temperature_sensor.units'
TEST_RAW_UNIT_PATH_NO_UNITS = 'pointset.points.cooling_stage_run_count.units'
TEST_STANDARD_UNIT_VALUE = 'degrees-celsius'
TEST_DEVICE_ID = '12345'

# Constants for Entity testing
TEST_VIRTUAL_ENTITY_CODE = 'VLV-23'
TEST_REPORTING_ENTITY_CODE = 'CHWS-1'
TEST_ENTITY_IS_REPORTING = False
TEST_CLOUD_DEVICE_ID = '2541901344105616'
TEST_REPORTING_GUID = 'test_reporting_guid'
TEST_VIRTUAL_GUID = 'test_virtual_guid'
TEST_ETAG = '1234567'

# Test Site instances
TEST_SITE_DICT = {
    BUILDING_CODE: 'UK-LON-S2',
    BC_GUID: 'test_site_guid',
    ETAG: '1234567'
}

# Test Entity instances
TEST_SITE_DICT_NO_GUID = {
    BUILDING_CODE: 'UK-LON-S2',
    BC_GUID: None,
}

TEST_REPORTING_ENTITY_DICT = {
    ENTITY_CODE: TEST_REPORTING_ENTITY_CODE,
    BC_GUID: TEST_REPORTING_GUID,
    NAMESPACE: TEST_NAMESPACE,
    ETAG: TEST_ETAG,
    CLOUD_DEVICE_ID: TEST_CLOUD_DEVICE_ID,
    TYPE_NAME: TEST_TYPE_NAME,
    IS_REPORTING: 'TRUE',
    OPERATION: 'ADD',
}

TEST_REPORTING_ENTITY_DICT_NO_GUID = {
    ENTITY_CODE: TEST_REPORTING_ENTITY_CODE,
    BC_GUID: None,
    NAMESPACE: TEST_NAMESPACE,
    ETAG: TEST_ETAG,
    CLOUD_DEVICE_ID: TEST_CLOUD_DEVICE_ID,
    TYPE_NAME: TEST_TYPE_NAME,
    IS_REPORTING: 'TRUE',
    OPERATION: 'ADD',
}

TEST_VIRTUAL_ENTITY_DICT = {
    ENTITY_CODE: TEST_VIRTUAL_ENTITY_CODE,
    BC_GUID: TEST_VIRTUAL_GUID,
    NAMESPACE: TEST_NAMESPACE,
    ETAG: TEST_ETAG,
    CLOUD_DEVICE_ID: None,
    TYPE_NAME: TEST_TYPE_NAME,
    IS_REPORTING: 'FALSE',
    OPERATION: 'ADD',
}

# Test Entity Field instances
# Test instance for a dimensional value field
TEST_DIMENSIONAL_VALUE_FIELD_DICT = {
    STANDARD_FIELD_NAME: TEST_DIMENSIONAL_VALUE_STANDARD_FIELD_NAME,
    RAW_FIELD_NAME: TEST_DIMENSIONAL_VALUE_RAW_FIELD_NAME,
    MISSING: 'FALSE',
    REPORTING_ENTITY_FIELD_NAME: TEST_DIMENSIONAL_REPORTING_FIELD_NAME,
    ENTITY_CODE: TEST_VIRTUAL_ENTITY_CODE,
    BC_GUID: TEST_VIRTUAL_GUID,
    REPORTING_ENTITY_CODE: TEST_REPORTING_ENTITY_CODE,
    REPORTING_ENTITY_GUID: TEST_REPORTING_GUID,
    RAW_UNIT_PATH: 'points.filter_differential_pressure_setpoint.units',
    STANDARD_UNIT_VALUE: 'pascals',
    RAW_UNIT_VALUE: 'Pa',
}

# Test instance for a multi-state value field
TEST_MULTISTATE_VALUE_FIELD_DICT = {
    STANDARD_FIELD_NAME: TEST_MULTISTATE_STANDARD_FIELD_NAME,
    RAW_FIELD_NAME: TEST_MULTISTATE_RAW_FIELD_NAME,
    MISSING: 'FALSE',
    ENTITY_CODE: TEST_REPORTING_ENTITY_CODE,
    REPORTING_ENTITY_FIELD_NAME: TEST_MULTISTATE_REPORTING_FIELD_NAME,
    REPORTING_ENTITY_CODE: TEST_REPORTING_ENTITY_CODE,
    REPORTING_ENTITY_GUID: TEST_REPORTING_GUID,
    BC_GUID: TEST_REPORTING_GUID,
    RAW_UNIT_PATH: '',
    STANDARD_UNIT_VALUE: '',
    RAW_UNIT_VALUE: '',
}

# Test instance for a missing field
TEST_MISSING_FIELD_DICT = {
    STANDARD_FIELD_NAME: TEST_MISSING_STANDARD_FIELD_NAME,
    RAW_FIELD_NAME: '',
    ENTITY_CODE: TEST_REPORTING_ENTITY_CODE,
    REPORTING_ENTITY_FIELD_NAME: TEST_MISSING_STANDARD_FIELD_NAME,
    REPORTING_ENTITY_CODE: TEST_REPORTING_ENTITY_CODE,
    REPORTING_ENTITY_GUID: TEST_REPORTING_GUID,
    BC_GUID: TEST_REPORTING_GUID,
    MISSING: 'TRUE',
    RAW_UNIT_PATH: '',
    STANDARD_UNIT_VALUE: '',
    RAW_UNIT_VALUE: '',
}

# Test instance with no units
TEST_FIELD_DICT_NO_UNITS = {
    STANDARD_FIELD_NAME: TEST_STANDARD_FIELD_NAME_NO_UNITS,
    RAW_FIELD_NAME: TEST_RAW_FIELD_NAME_NO_UNITS,
    MISSING: 'FALSE',
    REPORTING_ENTITY_FIELD_NAME: '',
    ENTITY_CODE: TEST_VIRTUAL_ENTITY_CODE,
    BC_GUID: TEST_VIRTUAL_GUID,
    REPORTING_ENTITY_CODE: TEST_REPORTING_ENTITY_CODE,
    REPORTING_ENTITY_GUID: TEST_REPORTING_GUID,
    RAW_UNIT_PATH: TEST_RAW_UNIT_PATH_NO_UNITS,
    STANDARD_UNIT_VALUE: NO_UNITS,
    RAW_UNIT_VALUE: NO_UNITS,
}

TEST_FIELD_DICT_NO_REPORTING_FIELD_NAME = {
    STANDARD_FIELD_NAME: 'standard_field_name',
    RAW_FIELD_NAME: TEST_MULTISTATE_RAW_FIELD_NAME,
    MISSING: 'FALSE',
    ENTITY_CODE: TEST_REPORTING_ENTITY_CODE,
    REPORTING_ENTITY_FIELD_NAME: '',
    REPORTING_ENTITY_CODE: TEST_REPORTING_ENTITY_CODE,
    REPORTING_ENTITY_GUID: TEST_REPORTING_GUID,
    BC_GUID: TEST_REPORTING_GUID,
    RAW_UNIT_PATH: 'raw_unit_path',
    STANDARD_UNIT_VALUE: 'std_unit_value',
    RAW_UNIT_VALUE: 'raw_unit_value',
}

TEST_BAD_MULTISTATE_FIELD_DICT_NO_STATES = {
    STANDARD_FIELD_NAME: TEST_BAD_MULTISTATE_FIELD_NAME,
    RAW_FIELD_NAME: TEST_BAD_MULTISTATE_FIELD_RAW_FIELD_NAME,
    ENTITY_CODE: TEST_REPORTING_ENTITY_CODE,
    REPORTING_ENTITY_FIELD_NAME: '',
    REPORTING_ENTITY_CODE: TEST_REPORTING_ENTITY_CODE,
    REPORTING_ENTITY_GUID: TEST_REPORTING_GUID,
    BC_GUID: TEST_REPORTING_GUID,
    MISSING: 'FALSE',
    RAW_UNIT_PATH: '',
    STANDARD_UNIT_VALUE: '',
    RAW_UNIT_VALUE: '',
}

# Test Connection instance
TEST_CONNECTION_DICT = {
    SOURCE_ENTITY_CODE: TEST_REPORTING_ENTITY_CODE,
    SOURCE_ENTITY_GUID: TEST_REPORTING_GUID,
    CONNECTION_TYPE: 'CONTROLS',
    TARGET_ENTITY_CODE: TEST_VIRTUAL_ENTITY_CODE,
    TARGET_ENTITY_GUID: TEST_VIRTUAL_GUID,
}

# Test State instance
TEST_STATE_DICT = {
    REPORTING_ENTITY_CODE: TEST_REPORTING_ENTITY_CODE,
    REPORTING_ENTITY_GUID: TEST_REPORTING_GUID,
    REPORTING_ENTITY_FIELD_NAME: TEST_MULTISTATE_REPORTING_FIELD_NAME,
    STANDARD_STATE: 'ON',
    RAW_STATE: 'TRUE',
}

# Test units instance
TEST_UNITS = Units(
    raw_unit_path='points.return_air_temperature_sensor.units',
    standard_to_raw_unit_map={'degrees_celsius': 'degC'},
)

TEST_SPREADSHEET = {
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
