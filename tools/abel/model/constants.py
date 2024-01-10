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
"""Constants for ABEL application."""

import datetime
import os

# pylint: disable=line-too-long
# internally, absolute path is used; github uses relative path
_USE_ABSOLUTE_PATH = False

# Path to the repository root.
if _USE_ABSOLUTE_PATH:
  REPO_ROOT = os.path.join('third_party', 'digitalbuildings')
else:
  REPO_ROOT = os.path.join(
      os.path.dirname(os.path.realpath(__file__)),
      os.path.join('..', '..', '..'),
  )

# Path to ontology from abel
ONTOLOGY_ROOT = os.path.join(REPO_ROOT, 'ontology', 'yaml', 'resources')

# Path to abel/ from repo root.
APPLICATION_ROOT = os.path.join(REPO_ROOT, 'tools', 'abel')

# Reg-ex pattern for GUIDs
BC_GUID_REGEX = '^[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}:'

# Faciltities naming patterns
MEZZANINE_PATTERN = '([0-9]*)M'
SINGLE_LETTER_PATTERN = 'R|D|LG|FB|S|SBA|SBB'
PERMUTED_NUMBER_LETTER_PATTERN = 'B[0-9]*|[0-9]+B'
LETTER_NUMBER_PATTERN = '(G|UG|M)[0-9]*'
NUMBERS_PATTERN = '[0-9]+'

COUNTRY_ID_PATTERN = '[A-Za-z]{2}'
CITY_ID_PATTERN = '[A-Za-z]{2,4}'
BUILDING_ID_PATTERN = '[A-Za-z0-9]{2,10}'
FLOOR_ID_PATTERN = f'{MEZZANINE_PATTERN}|{SINGLE_LETTER_PATTERN}|{BUILDING_ID_PATTERN}|{PERMUTED_NUMBER_LETTER_PATTERN}|{LETTER_NUMBER_PATTERN}|{NUMBERS_PATTERN}'

BUILDING_CODE_REGEX = (
    f'^{COUNTRY_ID_PATTERN}-{CITY_ID_PATTERN}-{BUILDING_ID_PATTERN}'
)
FACILTITIES_ENTITY_CODE_REGEX = BUILDING_CODE_REGEX + f'-({FLOOR_ID_PATTERN})'

# Current date and time
DATETIME_STRING = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M')

# Output path for spreadsheet validation report
SPREADSHEET_VALIDATOR_FILE_NAME = (
    f'spreadsheet_validation_{DATETIME_STRING}.log'
)

# Output path for Building Config instance validation report.
INSTANCE_VALIDATION_REPORT_NAME = f'instance_validation_{DATETIME_STRING}.log'

# Output path for exporting a Building Config file.
EXPORT_BUILDING_CONFIG_NAME = f'bc_export_{DATETIME_STRING}.yaml'

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
STRING_VALUE = 'stringValue'
VALUES = 'values'
USER_ENTERED_VALUE = 'userEnteredValue'
DATA = 'data'
ROW_DATA = 'rowData'
PROPERTIES = 'properties'
TITLE = 'title'
SHEETS = 'sheets'
GRID_PROPERTIES = 'gridProperties'
FROZEN_ROW_COUNT = 'frozenRowCount'
DATA_VALIDATION = 'dataValidation'
CONDITION = 'condition'
CONDITION_TYPE = 'type'
STRICT_VALIDATION = 'strict'
SHOW_CUSTOM_UI = 'showCustomUi'
ONE_OF_LIST = 'ONE_OF_LIST'
USER_ENTERED_FORMAT = 'userEnteredFormat'
BACKGROUND_COLOR_STYLE = 'backgroundColorStyle'
RGB_COLOR = 'rgbColor'
TEXT_FORMAT = 'textFormat'

# Authenticator Constants
EXPIRE_TIME = 'expireTime'
ACCESS_TOKEN = 'accessToken'

# Building Config config block constants
CONFIG_METADATA = 'CONFIG_METADATA'
CONFIG_OPERATION = 'operation'
CONFIG_INITIALIZE = 'INITIALIZE'

# Building Config entity block constants
BC_MISSING = 'MISSING'
CONFIG_CLOUD_DEVICE_ID = 'cloud_device_id'
CONFIG_CODE = 'code'
CONFIG_ETAG = 'etag'
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
CONNECTION_TYPE = 'DBO Connection Type'

# EntityField keys
RAW_FIELD_NAME = 'Raw Field Name'
REPORTING_ENTITY_CODE = 'Reporting Entity Code'
REPORTING_ENTITY_GUID = 'Reporting Entity Guid'
REPORTING_ENTITY_FIELD_NAME = 'Reporting Entity Field'
DATA_TYPE = 'Data Type'
UNITS = 'units'
STATES = 'states'
DEVICE_ID = 'Device ID'
NO_UNITS = 'no-units'
MISSING = 'Missing'
MISSING_FALSE = 'FALSE'
MISSING_TRUE = 'TRUE'

# Units keys
RAW_UNIT_PATH = 'Raw Unit Path'
STANDARD_UNIT_VALUE = 'DBO Standard Unit Value'
RAW_UNIT_VALUE = 'Raw Unit Value'

# Entity keys
ETAG = 'Etag'
CLOUD_DEVICE_ID = 'Cloud Device ID'
NAMESPACE = 'DBO Namespace'
FACILITIES_NAMESPACE = 'FACILITIES'
GENERAL_TYPE = 'DBO General Type'
IS_REPORTING = 'Is Reporting'
OPERATION = 'Operation'
IS_REPORTING_TRUE = 'TRUE'
IS_REPORTING_FALSE = 'FALSE'

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
RAW_STATE = 'Raw State'
STANDARD_STATE = 'DBO Standard State'

# multi-use keys
STANDARD_FIELD_NAME = 'DBO Standard Field Name'
ENTITY_CODE = 'Entity Code'
TYPE_NAME = 'DBO Entity Type Name'
METADATA = 'Metadata'
BC_GUID = 'Entity Guid'
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
REQUIRED_FIELD_HEADERS = [ENTITY_CODE, STANDARD_FIELD_NAME, MISSING]
REQUIRED_STATE_HEADERS = [
    REPORTING_ENTITY_CODE,
    REPORTING_ENTITY_FIELD_NAME,
    STANDARD_STATE,
    RAW_STATE,
]
REQUIRED_CONNECTION_HEADERS = [
    SOURCE_ENTITY_CODE,
    TARGET_ENTITY_CODE,
    CONNECTION_TYPE,
]

ALL_SITE_HEADERS = [BUILDING_CODE, BC_GUID, ETAG]
ALL_ENTITY_HEADERS = [
    ENTITY_CODE,
    BC_GUID,
    ETAG,
    IS_REPORTING,
    CLOUD_DEVICE_ID,
    NAMESPACE,
    TYPE_NAME,
    OPERATION,
]
ALL_FIELD_HEADERS = [
    STANDARD_FIELD_NAME,
    RAW_FIELD_NAME,
    REPORTING_ENTITY_FIELD_NAME,
    ENTITY_CODE,
    BC_GUID,
    REPORTING_ENTITY_CODE,
    REPORTING_ENTITY_GUID,
    MISSING,
    RAW_UNIT_PATH,
    STANDARD_UNIT_VALUE,
    RAW_UNIT_VALUE,
]
ALL_STATE_HEADERS = [
    REPORTING_ENTITY_CODE,
    REPORTING_ENTITY_GUID,
    REPORTING_ENTITY_FIELD_NAME,
    STANDARD_STATE,
    RAW_STATE,
]
ALL_CONNECTION_HEADERS = [
    SOURCE_ENTITY_CODE,
    SOURCE_ENTITY_GUID,
    CONNECTION_TYPE,
    TARGET_ENTITY_CODE,
    TARGET_ENTITY_GUID,
]

# List of tuples for an object attribute and a spreadsheet header for exporting
# to a spreadsheet.
SITE_ATTRIBUTE_LIST = [
    ('code', BUILDING_CODE),
    ('guid', BC_GUID),
    ('etag', ETAG),
]
REPORTING_ENTITY_ATTRIBUTE_LIST = [
    ('code', ENTITY_CODE),
    ('bc_guid', BC_GUID),
    ('cloud_device_id', CLOUD_DEVICE_ID),
    ('namespace', NAMESPACE),
    ('type_name', TYPE_NAME),
]
VIRTUAL_ENTITY_ATTRIBUTE_LIST = [
    ('code', ENTITY_CODE),
    ('bc_guid', BC_GUID),
    ('namespace', NAMESPACE),
    ('type_name', TYPE_NAME),
]
ENTITY_FIELD_ATTRIBUTE_LIST = [
    ('standard_field_name', STANDARD_FIELD_NAME),
    ('raw_field_name', RAW_FIELD_NAME),
    ('entity_guid', BC_GUID),
    ('reporting_entity_guid', REPORTING_ENTITY_GUID),
    ('reporting_entity_field_name', REPORTING_ENTITY_FIELD_NAME),
]
STATE_ATTRIBUTE_LIST = [
    ('reporting_entity_code', REPORTING_ENTITY_CODE),
    ('reporting_entity_guid', REPORTING_ENTITY_GUID),
    ('standard_field_name', REPORTING_ENTITY_FIELD_NAME),
    ('standard_state', STANDARD_STATE),
    ('raw_state', RAW_STATE),
]
UNITS_ATTRIBUTE_LIST = [
    ('raw_unit_path', RAW_UNIT_PATH),
    ('standard_unit_value', STANDARD_UNIT_VALUE),
    ('raw_unit_value', RAW_UNIT_VALUE),
]
CONNECTION_ATTRIBUTE_LIST = [
    ('source_entity_code', SOURCE_ENTITY_CODE),
    ('source_entity_guid', SOURCE_ENTITY_GUID),
    ('target_entity_code', TARGET_ENTITY_CODE),
    ('target_entity_guid', TARGET_ENTITY_GUID),
    ('connection_type', CONNECTION_TYPE),
]
OBJECT_ATTRIBUTE_LISTS = [
    SITE_ATTRIBUTE_LIST,
    REPORTING_ENTITY_ATTRIBUTE_LIST,
    VIRTUAL_ENTITY_ATTRIBUTE_LIST,
    ENTITY_FIELD_ATTRIBUTE_LIST,
    STATE_ATTRIBUTE_LIST,
    UNITS_ATTRIBUTE_LIST,
    CONNECTION_ATTRIBUTE_LIST,
]
