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
"""Unit document used for creating fake unit universe."""

UNIT_DOCUMENT = {
    'concentration': {
        'parts_per_million': 'STANDARD'
    },
    'current': {
        'amperes': 'STANDARD',
        'milliamperes': {
            'multiplier': 0.001,
            'offset': 0
        }
    },
    'energy': {
        'joules': 'STANDARD',
        'kilowatt_hours': {
            'multiplier': 3600000,
            'offset': 0
        }
    },
    'flowrate': {
        'cubic_meters_per_second': 'STANDARD',
        'cubic_feet_per_minute': {
            'multiplier': 0.0004719474432000001,
            'offset': 0
        },
        'gallons_per_minute': {
            'multiplier': 0.0000630901964,
            'offset': 0
        },
        'liters_per_second': {
            'multiplier': 0.001,
            'offset': 0
        }
    },
    'frequency': {
        'hertz': 'STANDARD'
    },
    'humidity': {
        'percent_relative_humidity': 'STANDARD'
    },
    'illuminance': {
        'lux': 'STANDARD'
    },
    'level': {
        'meters': 'STANDARD',
        'feet': {
            'multiplier': 0.3048,
            'offset': 0
        }
    },
    'linearvelocity': {
        'meters_per_second': 'STANDARD',
        'feet_per_minute': {
            'multiplier': 0.00508,
            'offset': 0
        },
        'miles_per_hour': {
            'multiplier': 0.44704,
            'offset': 0
        },
    },
    'percentage': {
        'percent': 'STANDARD'
    },
    'powerfactor': {
        'no_units': 'STANDARD'
    },
    'power': {
        'watts': 'STANDARD',
        'kilowatts': {
            'multiplier': 1000,
            'offset': 0
        },
        'tons_of_refrigeration': {
            'multiplier': 3517,
            'offset': 0
        },
        'kilovolt_amperes': {
            'multiplier': 1000,
            'offset': 0
        }
    },
    'pressure': {
        'pascals': 'STANDARD',
        'inches_of_water': {
            'multiplier': 249.080024,
            'offset': 0
        },
        'pounds_force_per_square_inch': {
            'multiplier': 6894.75789,
            'offset': 0
        }
    },
    'resistance': {
        'ohms': 'STANDARD',
        'kiloohms': {
            'multiplier': 1000,
            'offset': 0
        }
    },
    'specificenthalpy': {
        'joules_per_kilogram': 'STANDARD',
        'btus_per_pound_dry_air': {
            'multiplier': 2326,
            'offset': 0
        }
    },
    'temperature': {
        'kelvins': 'STANDARD',
        'degrees_celsius': {
            'multiplier': 1,
            'offset': 273.15
        },
        'degrees_fahrenheit': {
            'multiplier': 0.5555555555555556,
            'offset': 255.37037037037038
        }
    },
    'voltage': {
        'volts': 'STANDARD'
    },
    'volume': {
        'cubic_meters': 'STANDARD',
        'us_gallons': {
            'multiplier': 0.003785412,
            'offset': 0
        }
    },
}
