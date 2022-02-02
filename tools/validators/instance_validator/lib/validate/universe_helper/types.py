# Copyright 2021 Google LLC
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
        'id': '9693662434551660544',
        'description': 'A piece of equipment.',
        'is_abstract': True,
        'opt_uses': ['manufacturer_label', 'model_label']
    },
    'NO_ANALYSIS': {
        'id': '10044943205486559232',
        'description':
            'Devices which are not useful in and of themselves. Can be ignored'
            ' by analysis.',
        'is_abstract': True
    },
}

FACILITIES_TYPES_DOCUMENT = {
    'BUILDING': {
        'id': '15204152342002794496',
        'description': 'This is a type for BUILDING facilities object'
    }
}

GATEWAYS_TYPES_DOCUMENT = {
    'PASSTHROUGH': {
        'id': '',
        'description':
            'A device that provides translations for virtual entities.',
        'allow_undefined_fields': True
    }
}

HVAC_ANALYSIS_TYPES_DOCUMENT = {
    'CONTROL': {
        'id': '14773441339248869376',
        'description':
            'A tag to represent that the subtype forms a control unit. Ex: '
            'temperature, setpoint, heater output',
        'is_abstract': True
    },
    'MONITORING': {
        'id': '8216200281797427200',
        'description':
            'A tag to represent that the subtype forms a monitoring group. Ex:'
            ' temperature sensor only.',
        'is_abstract': True
    }
}

HVAC_ABSTRACT_TYPES_DOCUMENT = {
    'WDT': {
        'id': '12148045066631380992',
        'description': 'Temperature differential across water.',
        'is_abstract': True,
        'implements': ['MONITORING'],
        'uses': [
            'return_water_temperature_sensor',
            'supply_water_temperature_sensor',
        ]
    },
    'EDBPC': {
        'id': '15769475728711614464',
        'description': 'Building static control with exhaust damper.',
        'is_abstract': True,
        'uses': [
            'building_air_static_pressure_sensor',
            'building_air_static_pressure_setpoint',
            'exhaust_air_damper_percentage_command'
        ],
        'implements': ['CONTROL']
    }
}

HVAC_CHWS_TYPES_DOCUMENT = {
    'CHWS': {
        'id': '5338602430047191040',
        'description': 'Tag for chilled water systems.',
        'is_abstract': True,
        'opt_uses': [
            'thermal_power_capacity',
            'differential_pressure_specification',
            'flowrate_requirement',
        ]
    },
    'CHWS_WDT': {
        'id': '1917740281059344384',
        'description':
            'Chilled water system with only basic delta-T monitoring.',
        'is_canonical': True,
        'implements': ['CHWS', 'WDT']
    },
    'CHWS_WDT_GATEWAY': {
        'description': 'A gateway with required fields.',
        'allow_undefined_fields': True,
        'implements': ['CHWS_WDT']
    }
}

HVAC_GENERAL_TYPES_DOCUMENT = {
    'SDC': {
        'id': '4852143301546999808',
        'description': 'Tag for automated window shades.',
        'is_abstract': True,
        'implements': ['EQUIPMENT']
    },
    'DMP': {
        'id': '2708579412500021248',
        'description':
            'Tag for general, stand-alone dampers. Dampers are devices which '
            'control the flow of air from one space to another (or to '
            'outside). ',
        'is_abstract': True,
        'implements': ['EQUIPMENT']
    },
    'EDM': {
        'id': '3621015733879701504',
        'description': 'Exhaust air damper monitoring.',
        'is_abstract': True,
        'uses': ['exhaust_air_damper_command', 'exhaust_air_damper_status']
    },
}

HVAC_SDC_TYPES_DOCUMENT = {
    'SDC_EXT': {
        'id': '6117654796838109184',
        'description': 'Simple shade with extension control only.',
        'is_canonical': True,
        'implements': ['SDC'],
        'uses': ['shade_extent_percentage_command']
    },
}

HVAC_DMP_TYPES_DOCUMENT = {
    'DMP_EDM': {
        'id': '17221675502306066432',
        'description': 'Exhaust damper monitoring.',
        'implements': ['DMP', 'EDM']
    },
}
