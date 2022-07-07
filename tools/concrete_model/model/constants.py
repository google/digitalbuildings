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

# TODO(b/231443840) Clean up constants.
"""Constants for ABEL application."""

from os import path

# internally, absolute path is used; github uses relative path
_USE_ABSOLUTE_PATH = False

if _USE_ABSOLUTE_PATH:
  REPO_ROOT = path.join('third_party', 'digitalbuildings')
else:
  REPO_ROOT = path.join(
      path.dirname(path.realpath(__file__)), path.join('..', '..', '..', '..'))

APPLICATION_ROOT = path.join(REPO_ROOT, 'tools', 'concrete_model')

BC_GUID_REGEX = '^[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}:'

CLIENT_CREDENTIALS = path.join(path.expanduser('~'), 'abel/client_secrets.json')

# Google Sheets API constants
BODY_VALUE_RANGE_KEY = 'values'
SHEETS = 'sheets'
V4 = 'v4'
VALUE_INPUT_OPTION_RAW = 'RAW'
SPREADSHEET_ID = 'spreadsheetId'
SPREADSHEET_PROPERTIES = 'properties'
SPREADSHEET_TITLE = 'title'
SPREADSHEET_URL = 'spreadsheetUrl'
WRITE = 'w'
UTF_8 = 'utf-8'

# Authenticator Constants
EXPIRE_TIME = 'expireTime'
ACCESS_TOKEN = 'accessToken'

# Building Config config block constants
CONFIG_METADATA = 'CONFIG_METADATA'
CONFIG_OPERATION = 'operation'
CONFIG_INITIALIZE = 'INITIALIZE'

# Building Config entity block constants
CONFIG_CLOUD_DEVICE_ID = 'cloud_device_id'
CONFIG_CODE = 'code'
CONFIG_CONNECTIONS = 'connections'
CONFIG_TRANSLATION = 'translation'
CONFIG_TYPE = 'type'
CONFIG_LINKS = 'links'
CONFIG_UNITS = 'units'
CONFIG_UNITS_KEY = 'key'
CONFIG_UNITS_VALUES = 'values'
CONFIG_UNITS_PRESENT_VALUE = 'present_value'
CONFIG_STATES = 'states'

# Connection key
SOURCE_ENTITY_GUID = 'Source Entity Guid'
TARGET_ENTITY_GUID = 'Target Entity Guid'
SOURCE_ENTITY_CODE = 'Source Entity Code'
TARGET_ENTITY_CODE = 'Target Entity Code'
CONNECTION_TYPE = 'Connection Type'

# EntityField keys
RAW_FIELD_NAME = 'Raw Field Name'
REPORTING_ENTITY_CODE = 'Reporting Entity Code'
REPORTING_ENTITY_GUID = 'Reporting Entity Guid'
REPORTING_ENTITY_FIELD_NAME = 'Reporting Entity Field'
DATA_TYPE = 'Data Type'
UNITS = 'units'
STATES = 'states'
DEVICE_ID = 'Device ID'
INITIAL_VALUE = 'Initial Value'
NO_UNITS = 'no-units'

# Units keys
RAW_UNIT_PATH = 'Raw Unit Path'
STANDARD_UNIT_VALUE = 'Standard Unit Value'
RAW_UNIT_VALUE = 'Raw Unit Value'

# Entity keys
ETAG = 'Etag'
CLOUD_DEVICE_ID = 'Cloud Device ID'
NAMESPACE = 'Namespace'
GENERAL_TYPE = 'General Type'
IS_REPORTING = 'Is Reporting'

# Site Keys
BUILDING_CODE = 'Building Code'
SITE_NAMESPACE = 'FACILITIES'
SITE_TYPE_NAME = 'BUILDING'
CLOUD_REGION = 'Cloud Region'
LATITUDE = 'latitude'
LONGITUDE = 'longitude'
ALTITUDE = 'altitude'
ORIENTATION = 'orientation'
ADDRESS = 'address'
STREET = 'street'
CITY = 'city'
STATE = 'state'
COUNTY = 'county'
COUNTRY = 'country'
POSTAL_CODE = 'postal_code'
PRIMARY_FUNCTION = 'primary_function'
TIMEZONE = 'timezone'
WEATHER_STATION_REF = 'weather_station_ref'
REGISTRY_ID = 'registry_id'

# state keys
RAW_STATE = 'Payload State'
STANDARD_STATE = 'Standard State'

# multi-use keys
STANDARD_FIELD_NAME = 'Standard Field Name'
ENTITY_CODE = 'Entity Code'
TYPE_NAME = 'Type Name'
METADATA = 'Metadata'
BC_GUID = 'Guid'
CODE = 'code'

# Spreadsheet sheet title keys
SITES = 'Site'
ENTITIES = 'Entities'
ENTITY_FIELDS = 'Entity Fields'
STATES = 'States'
CONNECTIONS = 'Connections'
SPREADSHEET_RANGE = [SITES, ENTITIES, ENTITY_FIELDS, STATES, CONNECTIONS]

# Spreadsheet headers for importing
REQUIRED_SITE_HEADERS = [BUILDING_CODE]
REQUIRED_ENTITY_HEADERS = [ENTITY_CODE, IS_REPORTING, NAMESPACE, TYPE_NAME]
REQUIRED_FIELD_HEADERS = [ENTITY_CODE, STANDARD_FIELD_NAME, RAW_FIELD_NAME]
REQUIRED_STATE_HEADERS = [
    ENTITY_CODE, STANDARD_FIELD_NAME, STANDARD_STATE, RAW_STATE
]
REQUIRED_CONNECTION_HEADERS = [
    SOURCE_ENTITY_CODE, TARGET_ENTITY_CODE, CONNECTION_TYPE
]

ALL_SITE_HEADERS = [BUILDING_CODE, BC_GUID]
ALL_ENTITY_HEADERS = [
    ENTITY_CODE, BC_GUID, IS_REPORTING, CLOUD_DEVICE_ID, ETAG, NAMESPACE,
    TYPE_NAME
]
ALL_FIELD_HEADERS = [
    STANDARD_FIELD_NAME, RAW_FIELD_NAME, REPORTING_ENTITY_FIELD_NAME,
    ENTITY_CODE, BC_GUID, REPORTING_ENTITY_CODE, REPORTING_ENTITY_GUID,
    RAW_UNIT_PATH, STANDARD_UNIT_VALUE, RAW_UNIT_VALUE
]
ALL_STATE_HEADERS = [
    ENTITY_CODE, BC_GUID, STANDARD_FIELD_NAME, STANDARD_STATE, RAW_STATE
]
ALL_CONNECTION_HEADERS = [
    SOURCE_ENTITY_CODE, SOURCE_ENTITY_GUID, TARGET_ENTITY_CODE,
    TARGET_ENTITY_GUID, CONNECTION_TYPE
]

# List of tuples for an object attribute and a spreadsheet header for exporting
# to a spreadsheet.
SITE_ATTRIBUTE_LIST = [('code', BUILDING_CODE), ('guid', BC_GUID)]
REPORTING_ENTITY_ATTRIBUTE_LIST = [('code', ENTITY_CODE), ('bc_guid', BC_GUID),
                                   ('cloud_device_id', CLOUD_DEVICE_ID),
                                   ('namespace', NAMESPACE),
                                   ('type_name', TYPE_NAME)]
VIRTUAL_ENTITY_ATTRIBUTE_LIST = [('code', ENTITY_CODE), ('bc_guid', BC_GUID),
                                 ('namespace', NAMESPACE),
                                 ('type_name', TYPE_NAME)]
ENTITY_FIELD_ATTRIBUTE_LIST = [('standard_field_name', STANDARD_FIELD_NAME),
                               ('raw_field_name', RAW_FIELD_NAME),
                               ('entity_guid', BC_GUID),
                               ('reporting_entity_guid', REPORTING_ENTITY_GUID),
                               ('reporting_entity_field_name',
                                REPORTING_ENTITY_FIELD_NAME)]
STATE_ATTRIBUTE_LIST = [('entity_code', ENTITY_CODE), ('entity_guid', BC_GUID),
                        ('standard_field_name', STANDARD_FIELD_NAME),
                        ('standard_state', STANDARD_STATE),
                        ('raw_state', RAW_STATE)]
UNITS_ATTRIBUTE_LIST = [('raw_unit_path', RAW_UNIT_PATH),
                        ('standard_unit_value', STANDARD_UNIT_VALUE),
                        ('raw_unit_value', RAW_UNIT_VALUE)]
CONNECTION_ATTRIBUTE_LIST = [('source_entity_code', SOURCE_ENTITY_CODE),
                             ('source_entity_guid', SOURCE_ENTITY_GUID),
                             ('target_entity_code', TARGET_ENTITY_CODE),
                             ('target_entity_guid', TARGET_ENTITY_GUID),
                             ('connection_type', CONNECTION_TYPE)]
OBJECT_ATTRIBUTE_LISTS = [
    SITE_ATTRIBUTE_LIST, REPORTING_ENTITY_ATTRIBUTE_LIST,
    VIRTUAL_ENTITY_ATTRIBUTE_LIST, ENTITY_FIELD_ATTRIBUTE_LIST,
    STATE_ATTRIBUTE_LIST, UNITS_ATTRIBUTE_LIST, CONNECTION_ATTRIBUTE_LIST
]
