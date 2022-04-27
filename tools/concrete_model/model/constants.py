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
"""Constants for concrete model application."""

BC_GUID_REGEX = '^[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}:'

# Connection key
SOURCE_ENTITY_GUID = 'Source Entity GUID'
TARGET_ENTITY_GUID = 'Target Entity GUID'
SOURCE_ENTITY_CODE = 'Source Entity Code'
TARGET_ENTITY_CODE = 'Target Entity Code'
CONNECTION_TYPE = 'Connection Type'

# EntityField keys
RAW_FIELD_NAME = 'Raw Field Name'
LINKED_ENTITY_CODE = 'Linked Entity Code'
LINKED_ENTITY_GUID = 'Linked Entity Guid'
DATA_TYPE = 'Data Type'
UNITS = 'units'
STATES = 'states'
DEVICE_ID = 'Device ID'
INITIAL_VALUE = 'Initial Value'

# Units keys
RAW_UNIT_PATH = 'Raw Unit Path'
STANDARD_UNIT_VALUE = 'Standard Unit Value'
RAW_UNIT_VALUE = 'Raw Unit Value'

# Entity keys
UDMI_GUID = 'UDMI GUID'
ETAG = 'Etag'
CLOUD_DEVICE_ID = 'Cloud Device ID'
NAMESPACE = 'Namespace'
GENERAL_TYPE = 'General Type'
IS_REPORTING = 'is_reporting'

# Site Keys
SITE_TYPE_NAME = 'FACILITIES/BUILDING'
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
BC_GUID = 'BC GUID'

# Spreadsheet sheet title keys
SITES = 'Site'
ENTITIES = 'Entities'
ENTITY_FIELDS = 'Entity Fields'
STATES = 'States'
CONNECTIONS = 'Connections'
SPREADSHEET_RANGE = [SITES, ENTITIES, ENTITY_FIELDS, STATES, CONNECTIONS]


