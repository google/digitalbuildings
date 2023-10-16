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
import re
from validate import enumerations

#### Public Text parsing Constants ####
ENTITY_ID_KEY = 'id'  # deprecated; kept for legacy reasons
ENTITY_GUID_KEY = 'guid'
ENTITY_CODE_KEY = 'code'
ENTITY_CLOUD_DEVICE_ID_KEY = 'cloud_device_id'
ENTITY_TYPE_KEY = 'type'
ENTITY_OPERATION_KEY = 'operation'

LINKS_KEY = 'links'
TRANSLATION_KEY = 'translation'
CONNECTIONS_KEY = 'connections'
METADATA_KEY = 'metadata'
PRESENT_VALUE_KEY = 'present_value'
POINTS = 'points'
VALUE_RANGE_KEY = 'value_range'
UNITS_KEY = 'units'
UNIT_NAME_KEY = 'key'
UNIT_VALUES_KEY = 'values'
STATES_KEY = 'states'
UPDATE_MASK_KEY = 'update_mask'
ETAG_KEY = 'etag'

# Minimum threshold for a valid entity name.  Additional validation is required
# check adherence to more specific naming conventions
# Note: As-written this will capture the metadata key below, so logic should
# check for it first
_ENTITY_CODE_REGEX = r'^[a-zA-Z][a-zA-Z0-9/\-_ ]+:'
_ENTITY_GUID_REGEX = r'^[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}:'
_ENTITY_CODE_PATTERN = re.compile(_ENTITY_CODE_REGEX)
_ENTITY_GUID_PATTERN = re.compile(_ENTITY_GUID_REGEX)

# Exact key for the configuration metadata block
_CONFIG_METADATA_KEY = 'CONFIG_METADATA'
_CONFIG_METADATA_REGEX = f'^{_CONFIG_METADATA_KEY}:'
_CONFIG_METADATA_PATTERN = re.compile(_CONFIG_METADATA_REGEX)
# Key that marks the mode to parse file in.
_CONFIG_MODE_KEY = 'operation'

_TRANSLATION_SCHEMA = {
    '$id': '/schemas/translation',
    'type': 'object',
    'properties': {
        PRESENT_VALUE_KEY: {'type': 'string'},
        STATES_KEY: {
            'type': 'array',
            'prefixItems': [
            # Not sure if this right?
                {{'type': 'string'}: {'type': 'string'}}
            ]
        },
        UNITS_KEY: {
            'type': 'object',
            'properties': {
                UNIT_NAME_KEY: {'type': 'string'},
                UNIT_VALUES_KEY: {
                    'type': 'array'
                }
            }
        }
    },
    'required': [PRESENT_VALUE_KEY]
}

_METADATA_SCHEMA = {
    '$id': '/schemas/config-metadata',
    _CONFIG_MODE_KEY: {
        'oneOf': [
            {'const': enumerations.ConfigMode.UPDATE.value},
            {'const': enumerations.ConfigMode.INITIALIZE.value},
            {'const': enumerations.ConfigMode.EXPORT.value},
        ]
    }
}

_ENTITY_ATTR_SCHEMA = {
    '$id': '/schemas/entity-attributes',
    'type': 'object',
    'properties': {
        ENTITY_CODE_KEY: {'type': 'string'},
        CONNECTIONS_KEY: {
            'type': 'array'
        },
        LINKS_KEY: {'type': 'array'},
        TRANSLATION_KEY: {'$ref': '/schemas/translation'}
    }
}

_ENTITY_BASE_SCHEMA = {
    '$id': '/schemas/entity-base-schema',
    'type': 'object',
    'properties': {
        ENTITY_CLOUD_DEVICE_ID_KEY: {'type': 'string'},
        ENTITY_CODE_KEY: {'type': 'string'},
        ENTITY_GUID_KEY: {'type': 'string'},
        'allOf': [
            {'$ref': '/schemas/entity-attributes'}
        ]
    }

}

_ENTITY_UPDATE_SCHEMA = {
    'type': 'object',
    'properties': {
        ETAG_KEY: {'type': 'string'},
        ENTITY_TYPE_KEY: {'type': 'string'},
        'allOf': [
            {'$ref': '/schemas/entity-base-schema'}
        ],
        ENTITY_OPERATION_KEY: {'const': enumerations.EntityOperation.UPDATE.value},
        UPDATE_MASK_KEY: {
            'type': 'array',
            'uniqueItems': True
        },
    },
    'required': [ETAG_KEY, ENTITY_TYPE_KEY],
    'dependentRequired': {
        UPDATE_MASK_KEY: [ENTITY_OPERATION_KEY]
    }
}

_ENTITY_ADD_SCHEMA = {
    'type': 'object',
    'properties': {
        ENTITY_TYPE_KEY: {'type': 'string'},
        'allOf': [
            {'$ref': '/schemas/entity-base-schema'}
        ],
        ENTITY_OPERATION_KEY: {'const': enumerations.EntityOperation.ADD.value},
    }
}

_ENTITY_DELETE_SCHEMA = {
    'type': 'object',
    'properties': {
        'allOf': [
            {'$ref': '/schemas/entity-base-schema'}
        ],
        ENTITY_OPERATION_KEY: {'const': enumerations.EntityOperation.DELETE.value},
    }
}

_ENTITY_EXPORT_SCHEMA = {
    'type': 'object',
        'properties': {
            ETAG_KEY: {'type': 'string'},
            ENTITY_TYPE_KEY: {'type': 'string'},
            'allOf': [
                {'$ref': '/schemas/entity-base-schema'}
            ],
            ENTITY_OPERATION_KEY: {'const': enumerations.EntityOperation.EXPORT.value},
        }
}