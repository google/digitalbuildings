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
"""Type documents used for creating fake entity type universe."""

GLOBAL_TYPES_DOCUMENT = {
    'EQUIPMENT': {
        'guid': 'a65cc651-ef1f-4d01-b49a-47a567f66d04',
        'description': 'A piece of equipment.',
        'is_abstract': True,
        'opt_uses': ['manufacturer_label', 'model_label'],
    },
    'NO_ANALYSIS': {
        'guid': '20a95bff-a5b8-4fee-b31c-6fc52c0b41bc',
        'description': (
            'Devices which are not useful in and of themselves. Can be ignored'
            ' by analysis.'
        ),
        'is_abstract': True,
    },
}

FACILITIES_TYPES_DOCUMENT = {
    'BUILDING': {
        'guid': '34b2b505-d412-46a2-b9dd-08a8dbb96a87',
        'description': 'This is a type for BUILDING facilities object',
    },
    'FLOOR': {
        'guid': '4439f98a-c52b-4fff-8765-84e689862423',
        'description': 'This is a type for FLOOR facilities object',
    },
    'ROOM': {
        'guid': '39dd2cf1-b5c0-4b3b-942a-e02620eed5c3',
        'description': 'This is a type for ROOM facilities object',
    },
}

GATEWAYS_TYPES_DOCUMENT = {
    'PASSTHROUGH': {
        'guid': '498af1d0-0ec8-45a3-88a0-c6bc22c632f4',
        'description': (
            'A device that provides translations for virtual entities.'
        ),
        'allow_undefined_fields': True,
    }
}

HVAC_ANALYSIS_TYPES_DOCUMENT = {
    'CONTROL': {
        'guid': '3b5321c4-7f89-41c4-baa3-8b444ad0a696',
        'description': (
            'A tag to represent that the subtype forms a control unit. Ex: '
            'temperature, setpoint, heater output'
        ),
        'is_abstract': True,
    },
    'MONITORING': {
        'guid': '1800a4cf-ef6c-4e7c-b811-f2004c0df85b',
        'description': (
            'A tag to represent that the subtype forms a monitoring group. Ex:'
            ' temperature sensor only.'
        ),
        'is_abstract': True,
    },
}

HVAC_ABSTRACT_TYPES_DOCUMENT = {
    'WDT': {
        'guid': 'c56fdfa0-fba7-4842-b61e-a0e6a891ea46',
        'description': 'Temperature differential across water.',
        'is_abstract': True,
        'implements': ['MONITORING'],
        'uses': [
            'return_water_temperature_sensor',
            'supply_water_temperature_sensor',
        ],
    },
    'EDBPC': {
        'guid': '162682bb-e4af-4776-9ba0-2c458ede278f',
        'description': 'Building static control with exhaust damper.',
        'is_abstract': True,
        'uses': [
            'building_air_static_pressure_sensor',
            'building_air_static_pressure_setpoint',
            'exhaust_air_damper_percentage_command',
        ],
        'implements': ['CONTROL'],
    },
}

HVAC_CHWS_TYPES_DOCUMENT = {
    'CHWS': {
        'guid': '10509e2e-4105-407b-9688-2b9fefde79c8',
        'description': 'Tag for chilled water systems.',
        'is_abstract': True,
        'opt_uses': [
            'thermal_power_capacity',
            'differential_pressure_specification',
            'flowrate_requirement',
        ],
    },
    'CHWS_WDT': {
        'guid': '1ede5c8b-7ebc-4011-8220-a92b262e1ec1',
        'description': (
            'Chilled water system with only basic delta-T monitoring.'
        ),
        'is_canonical': True,
        'implements': ['CHWS', 'WDT'],
    },
    'CHWS_WDT_GATEWAY': {
        'guid': 'a65cc651-ef1f-4d01-b49a-47a567f66d04',
        'description': 'A gateway with required fields.',
        'allow_undefined_fields': True,
        'implements': ['CHWS_WDT'],
    },
    'CHWS_WDT_WDPC2X': {
        'guid': '20a95bff-a5b8-4fee-b31c-6fc52c0b41bc',
        'description': (
            'Chilled water system with dual differential pressure control.'
        ),
        'is_canonical': True,
        'implements': ['CHWS_WDT'],
        'uses': [
            'differential_pressure_sensor_1',
            'differential_pressure_sensor_2',
            'differential_pressure_setpoint',
        ],
    },
}

HVAC_GENERAL_TYPES_DOCUMENT = {
    'SDC': {
        'guid': '34b2b505-d412-46a2-b9dd-08a8dbb96a87',
        'description': 'Tag for automated window shades.',
        'is_abstract': True,
        'implements': ['EQUIPMENT'],
    },
    'DMP': {
        'guid': '498af1d0-0ec8-45a3-88a0-c6bc22c632f4',
        'description': (
            'Tag for general, stand-alone dampers. Dampers are devices which '
            'control the flow of air from one space to another (or to '
            'outside). '
        ),
        'is_abstract': True,
        'implements': ['EQUIPMENT'],
    },
    'EDM': {
        'guid': '10509e2e-4105-407b-9688-2b9fefde79c8',
        'description': 'Exhaust air damper monitoring.',
        'is_abstract': True,
        'uses': ['exhaust_air_damper_command', 'exhaust_air_damper_status'],
    },
}

HVAC_SDC_TYPES_DOCUMENT = {
    'SDC_EXT': {
        'guid': '1ede5c8b-7ebc-4011-8220-a92b262e1ec1',
        'description': 'Simple shade with extension control only.',
        'is_canonical': True,
        'implements': ['SDC'],
        'uses': ['shade_extent_percentage_command'],
    },
}

HVAC_DMP_TYPES_DOCUMENT = {
    'DMP_EDM': {
        'guid': 'a65cc651-ef1f-4d01-b49a-47a567f66d04',
        'description': 'Exhaust damper monitoring.',
        'implements': ['DMP', 'EDM'],
    },
}


HVAC_FAN_TYPES_DOCUMENT = {
    'FAN_SS': {
        'guid': '20a95bff-a5b8-4fee-b31c-6fc52c0b41bc',
        'description': 'Basic fan with start/stop and status.',
        'is_canonical': True,
        'uses': ['run_command', 'run_status'],
        'opt_uses': ['power_sensor'],
    },
    'FAN_SS_ABC': {
        'guid': '34b2b505-d412-46a2-b9dd-08a8dbb96a87',
        'description': 'Reffan',
        'is_canonical': True,
        'uses': [
            'run_command',
            'run_status',
            'zone_air_temperature_sensor_1',
            'zone_air_temperature_sensor_2',
        ],
    },
}


SAFETY_ABSTRACT_TYPES_DOCUMENT = {
    'FA2X': {
        'guid': '350243a7-bac9-45b8-b614-6ada6cf48ef6',
        'description': 'Fire alarm monitoring.',
        'is_abstract': True,
        'uses': ['fire_alarm_1', 'fire_alarm_2'],
    }
}


SAFETY_GENERAL_TYPES_DOCUMENT = {
    'FACP': {
        'guid': '2b337ced-6542-48aa-8440-42f40dde61d5',
        'description': 'Fire alarm control panel.',
        'is_abstract': True,
        'implements': ['EQUIPMENT'],
    }
}


SAFETY_FACP_TYPES_DOCUMENT = {
    'FACP_FA2X': {
        'guid': '2e387831-935a-4d81-849f-47af7943c0ce',
        'description': (
            'Fire alarm panel with 2 fire alarm alertness and a fire fault'
            ' status'
        ),
        'is_canonical': True,
        'implements': ['FACP', 'FA2X'],
        'opt_uses': ['panel_alarm'],
    }
}
