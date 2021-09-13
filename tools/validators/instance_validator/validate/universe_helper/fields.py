"""Fields documents used for creating fake field universe."""

TELEMETRY_FIELDS_DOCUMENT = {
    'literals': [
        'building_air_static_pressure_sensor',
        'building_air_static_pressure_setpoint',
        'bypass_valve_percentage_command',
        'chilled_return_water_temperature_sensor',
        'chilled_supply_water_flowrate_sensor',
        'chilled_supply_water_temperature_sensor',
        'chilled_supply_water_temperature_setpoint',
        'chilled_water_bypass_valve_percentage_command',
        'chilled_water_bypass_valve_percentage_sensor',
        'chilled_water_differential_pressure_sensor',
        'chilled_water_differential_pressure_setpoint',
        'chilled_water_isolation_valve_percentage_command',
        'chilled_water_isolation_valve_percentage_sensor', {
            'chilled_water_isolation_valve_command': ['OPEN', 'CLOSED']
        }, 'chilled_water_valve_percentage_command', {
            'circulation_pump_run_status': ['ON', 'OFF']
        }, {
            'compressor_run_command': ['ON', 'OFF']
        }, {
            'compressor_run_status': ['ON', 'OFF', 'UNKNOWN']
        }, 'compressor_speed_percentage_sensor',
        'refrigerant_condenser_saturation_temperature_sensor',
        'condensing_return_water_temperature_sensor',
        'condensing_supply_water_temperature_sensor',
        'condensing_supply_water_temperature_setpoint',
        'condensing_water_flowrate_sensor', 'cooling_output_percentage_command',
        'current_sensor', 'differential_pressure_sensor',
        'differential_pressure_setpoint',
        'discharge_air_cooling_temperature_setpoint',
        'discharge_air_heating_temperature_setpoint',
        'discharge_air_temperature_sensor',
        'discharge_air_temperature_setpoint', 'discharge_fan_current_sensor', {
            'discharge_fan_run_command': ['ON', 'OFF']
        }, {
            'discharge_fan_run_status': ['ON', 'OFF']
        }, {
            'discharge_fan_speed_mode': [
                'AUTO', 'LOW', 'MEDIUM', 'HIGH', 'OFF'
            ]
        }, 'discharge_fan_speed_percentage_command', {
            'dryer_run_status': ['ON', 'OFF']
        }, {
            'economizer_mode': ['ON', 'OFF', 'AUTO']
        }, 'evaporator_pressure_sensor',
        'refrigerant_evaporator_saturation_temperature_sensor',
        'exhaust_air_damper_percentage_command',
        'exhaust_air_temperature_sensor', 'exhaust_fan_current_sensor',
        'exhaust_fan_power_sensor', {
            'exhaust_fan_run_command': ['ON', 'OFF']
        }, {
            'exhaust_fan_run_status': ['ON', 'OFF', 'UNKNOWN']
        }, 'exhaust_fan_speed_frequency_sensor',
        'exhaust_fan_speed_percentage_command',
        'exhaust_fan_speed_percentage_sensor', {
            'fan_run_status': ['ON', 'OFF']
        }, 'fan_speed_percentage_command', 'flowrate_sensor', {
            'heater_run_command': ['ON', 'OFF']
        }, 'heating_water_valve_percentage_command',
        'inlet_guidevane_percentage_sensor', {
            'isolation_damper_status': ['OPEN', 'CLOSED']
        }, 'isolation_damper_percentage_sensor', 'line_current_sensor',
        'line_powerfactor_sensor',
        'loop_chilled_water_differential_pressure_sensor',
        'loop_differential_pressure_sensor', 'min_flowrate_setpoint',
        'min_chilled_water_flowrate_setpoint',
        'ventilation_outside_air_damper_percentage_command',
        'ventilation_outside_air_flowrate_sensor',
        'ventilation_outside_air_flowrate_setpoint',
        'mixed_air_temperature_sensor', 'outside_air_damper_percentage_command',
        'outside_air_specificenthalpy_sensor', 'outside_air_flowrate_sensor',
        'outside_air_flowrate_setpoint', 'outside_air_relative_humidity_sensor',
        'outside_air_temperature_sensor',
        'outside_air_wetbulb_temperature_sensor', 'power_sensor',
        'return_air_relative_humidity_sensor', 'return_air_temperature_sensor',
        'return_air_temperature_setpoint', 'return_water_temperature_sensor', {
            'reversing_valve_command': ['OPEN', 'CLOSED']
        }, {
            'exhaust_air_damper_command': ['OPEN', 'CLOSED']
        }, {
            'exhaust_air_damper_status': ['OPEN', 'CLOSED']
        }, {
            'run_command': ['ON', 'OFF']
        }, {
            'run_status': ['ON', 'OFF']
        }, 'shade_extent_percentage_command', 'speed_frequency_sensor',
        'speed_percentage_command', 'speed_percentage_sensor',
        'supply_air_damper_percentage_command', 'supply_air_flowrate_sensor',
        'supply_air_flowrate_setpoint', 'supply_air_static_pressure_sensor',
        'supply_air_static_pressure_setpoint', 'supply_air_temperature_sensor',
        'supply_air_temperature_setpoint', 'supply_fan_current_sensor',
        'supply_fan_power_sensor', {
            'supply_fan_run_command': ['ON', 'OFF']
        }, {
            'supply_fan_run_status': ['ON', 'OFF', 'UNKNOWN']
        }, 'supply_fan_speed_frequency_command',
        'supply_fan_speed_frequency_sensor',
        'supply_fan_speed_percentage_command',
        'supply_fan_speed_percentage_sensor', 'supply_water_flowrate_sensor',
        'supply_water_temperature_sensor', 'supply_water_temperature_setpoint',
        'cooling_request_count', 'heating_request_count',
        'pressurization_request_count', 'zone_air_co2_concentration_sensor',
        'zone_air_co2_concentration_setpoint',
        'zone_air_co_concentration_setpoint',
        'zone_air_cooling_temperature_setpoint',
        'zone_air_heating_temperature_setpoint',
        'zone_air_refrigerant_concentration_sensor',
        'zone_air_relative_humidity_sensor',
        'zone_air_deadband_temperature_setpoint', 'zone_air_temperature_sensor'
    ]
}

METADATA_FIELDS_DOCUMENT = {
    'literals': [
        'manufacturer_label',
        'model_label',
        'zone_use_label',
        'cooling_thermal_power_capacity',
        'discharge_air_flowrate_capacity',
        'discharge_fan_power_capacity',
        'exhaust_air_flowrate_capacity',
        'exhaust_fan_power_capacity',
        'flowrate_capacity',
        'heating_input_thermal_power_capacity',
        'heating_thermal_power_capacity',
        'thermal_power_capacity',
        'power_capacity',
        'return_air_flowrate_capacity',
        'return_fan_power_capacity',
        'supply_air_flowrate_capacity',
        'supply_air_cooling_flowrate_capacity',
        'supply_air_heating_flowrate_capacity',
        'supply_fan_power_capacity',
        'differential_pressure_specification',
        'efficiency_percentage_specification',
        'flowrate_requirement',
        'outside_air_flowrate_requirement',
        'supply_air_ventilation_flowrate_requirement',
    ]
}
