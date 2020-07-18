package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Outside_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_cooling_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_air_cooling_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_power_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_fan_power_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_air_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_speed_frequency_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_fan_speed_frequency_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_run_status_2;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_run_status_2;
import www.google.com.digitalbuildings._0_0_1.fields.IMixed_air_temperature_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.Mixed_air_temperature_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_run_status_1;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_run_status_1;
import www.google.com.digitalbuildings._0_0_1.fields.IMixed_air_temperature_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.Mixed_air_temperature_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_request_count;
import www.google.com.digitalbuildings._0_0_1.fields.Heating_request_count;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_air_heating_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_air_heating_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_water_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Heating_water_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_water_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Heating_water_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_flowrate_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_air_flowrate_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.IVentilation_outside_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Ventilation_outside_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_speed_frequency_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_speed_frequency_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IBuilding_air_static_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Building_air_static_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_speed_frequency_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_speed_frequency_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_current_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_fan_current_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_speed_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_speed_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_speed_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_fan_speed_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_co2_concentration_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_air_co2_concentration_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_static_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_air_static_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_speed_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Outside_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IPressurization_request_count;
import www.google.com.digitalbuildings._0_0_1.fields.Pressurization_request_count;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_speed_percentage_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_speed_percentage_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_speed_percentage_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_speed_percentage_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_water_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Chilled_water_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_deadband_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_air_deadband_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_relative_humidity_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_air_relative_humidity_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.Compressor_run_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_frequency_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_speed_frequency_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_frequency_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_speed_frequency_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_frequency_sensor_4;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_speed_frequency_sensor_4;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_frequency_sensor_3;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_speed_frequency_sensor_3;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_command_4;
import www.google.com.digitalbuildings._0_0_1.fields.Compressor_run_command_4;
import www.google.com.digitalbuildings._0_0_1.fields.ILeaving_cooling_coil_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Leaving_cooling_coil_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_command_3;
import www.google.com.digitalbuildings._0_0_1.fields.Compressor_run_command_3;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_current_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_current_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.Compressor_run_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.IFilter_differential_pressure_sensor_4;
import www.google.com.digitalbuildings._0_0_1.fields.Filter_differential_pressure_sensor_4;
import www.google.com.digitalbuildings._0_0_1.fields.IFilter_differential_pressure_sensor_3;
import www.google.com.digitalbuildings._0_0_1.fields.Filter_differential_pressure_sensor_3;
import www.google.com.digitalbuildings._0_0_1.fields.IFilter_differential_pressure_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.Filter_differential_pressure_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IFilter_differential_pressure_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.Filter_differential_pressure_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_air_relative_humidity_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_air_relative_humidity_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_air_flowrate_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_air_flowrate_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IBypass_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Bypass_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_static_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_air_static_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IVentilation_outside_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Ventilation_outside_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_speed_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_status_4;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_run_status_4;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_frequency_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_speed_frequency_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_status_1;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_run_status_1;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_status_3;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_run_status_3;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_status_2;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_run_status_2;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.Compressor_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_power_sensor_3;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_power_sensor_3;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_power_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_power_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.ILeaving_heating_coil_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Leaving_heating_coil_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Return_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_power_sensor_4;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_power_sensor_4;
import www.google.com.digitalbuildings._0_0_1.fields.IHeater_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.Heater_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_speed_percentage_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_speed_percentage_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_flowrate_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Outside_air_flowrate_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.Compressor_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_sensor_4;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_speed_percentage_sensor_4;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_sensor_3;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_speed_percentage_sensor_3;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IBoost_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.Boost_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_power_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_power_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.ICooling_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Cooling_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IMixed_air_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Mixed_air_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_speed_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Compressor_speed_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IHeater_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.Heater_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_heating_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_air_heating_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_cooling_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_air_cooling_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IBuilding_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Building_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_power_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_power_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_power_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_power_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_co2_concentration_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_air_co2_concentration_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_power_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_power_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_status_4;
import www.google.com.digitalbuildings._0_0_1.fields.Compressor_run_status_4;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_status_3;
import www.google.com.digitalbuildings._0_0_1.fields.Compressor_run_status_3;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_current_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_current_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_air_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_air_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_command_4;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_run_command_4;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_current_sensor_3;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_current_sensor_3;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_command_3;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_run_command_3;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_current_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_current_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_run_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_status_2;
import www.google.com.digitalbuildings._0_0_1.fields.Compressor_run_status_2;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_run_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_status_1;
import www.google.com.digitalbuildings._0_0_1.fields.Compressor_run_status_1;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_speed_frequency_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_speed_frequency_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_current_sensor_4;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_current_sensor_4;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.ICooling_thermal_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.Cooling_thermal_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_flowrate_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_air_flowrate_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Heating_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_speed_percentage_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_speed_percentage_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_speed_percentage_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_speed_percentage_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.IHeater_run_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.Heater_run_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_current_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_current_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IMixed_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Mixed_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICooling_request_count;
import www.google.com.digitalbuildings._0_0_1.fields.Cooling_request_count;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_command_4;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_speed_percentage_command_4;
import www.google.com.digitalbuildings._0_0_1.fields.IVentilation_outside_air_flowrate_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Ventilation_outside_air_flowrate_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IReversing_valve_command;
import www.google.com.digitalbuildings._0_0_1.fields.Reversing_valve_command;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_speed_percentage_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_flowrate_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_air_flowrate_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_speed_percentage_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.IHeater_run_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.Heater_run_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_command_3;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_speed_percentage_command_3;
import www.google.com.digitalbuildings._0_0_1.fields.IHeater_run_command_3;
import www.google.com.digitalbuildings._0_0_1.fields.Heater_run_command_3;
import www.google.com.digitalbuildings._0_0_1.fields.IBoost_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.Boost_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_damper_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Outside_air_damper_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_run_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_run_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.IEconomizer_mode;
import www.google.com.digitalbuildings._0_0_1.fields.Economizer_mode;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_air_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_run_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_run_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_thermal_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.Heating_thermal_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_fan_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Outside_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_speed_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_fan_speed_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_current_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_current_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_current_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_current_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_power_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_power_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_speed_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_speed_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_heating_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_air_heating_temperature_setpoint;

/**
* Class Mau_sfss_sfvsc_hwsc 
* Reheat (hydronic) make-up air unit.
*/
@SuppressWarnings("serial")
public class Mau_sfss_sfvsc_hwsc extends www.google.com.digitalbuildings._0_0_1.hvac.Sfss implements IMau_sfss_sfvsc_hwsc{

	IRI newInstance;
	public Mau_sfss_sfvsc_hwsc(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Mau_sfss_sfvsc_hwsc"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesSupply_fan_run_command (ISupply_fan_run_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_fan_run_command> getUsesSupply_fan_run_command (){
		Set<ISupply_fan_run_command> UsesSupply_fan_run_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_fan_run_command) {
				UsesSupply_fan_run_command.add((Supply_fan_run_command)action);
			}
		});
		return UsesSupply_fan_run_command;
	}


  public void addUsesSupply_fan_run_status (ISupply_fan_run_status parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_fan_run_status> getUsesSupply_fan_run_status (){
		Set<ISupply_fan_run_status> UsesSupply_fan_run_status = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_fan_run_status) {
				UsesSupply_fan_run_status.add((Supply_fan_run_status)action);
			}
		});
		return UsesSupply_fan_run_status;
	}


  public void addUsesSupply_fan_speed_percentage_command (ISupply_fan_speed_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_fan_speed_percentage_command> getUsesSupply_fan_speed_percentage_command (){
		Set<ISupply_fan_speed_percentage_command> UsesSupply_fan_speed_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_fan_speed_percentage_command) {
				UsesSupply_fan_speed_percentage_command.add((Supply_fan_speed_percentage_command)action);
			}
		});
		return UsesSupply_fan_speed_percentage_command;
	}


  public void addUsesChilled_water_valve_percentage_command (IChilled_water_valve_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IChilled_water_valve_percentage_command> getUsesChilled_water_valve_percentage_command (){
		Set<IChilled_water_valve_percentage_command> UsesChilled_water_valve_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Chilled_water_valve_percentage_command) {
				UsesChilled_water_valve_percentage_command.add((Chilled_water_valve_percentage_command)action);
			}
		});
		return UsesChilled_water_valve_percentage_command;
	}


  public void addUsesSupply_air_temperature_sensor (ISupply_air_temperature_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_air_temperature_sensor> getUsesSupply_air_temperature_sensor (){
		Set<ISupply_air_temperature_sensor> UsesSupply_air_temperature_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_air_temperature_sensor) {
				UsesSupply_air_temperature_sensor.add((Supply_air_temperature_sensor)action);
			}
		});
		return UsesSupply_air_temperature_sensor;
	}


  public void addUsesSupply_air_temperature_setpoint (ISupply_air_temperature_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_air_temperature_setpoint> getUsesSupply_air_temperature_setpoint (){
		Set<ISupply_air_temperature_setpoint> UsesSupply_air_temperature_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_air_temperature_setpoint) {
				UsesSupply_air_temperature_setpoint.add((Supply_air_temperature_setpoint)action);
			}
		});
		return UsesSupply_air_temperature_setpoint;
	}


  public void addUsesSupply_air_static_pressure_sensor (ISupply_air_static_pressure_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_air_static_pressure_sensor> getUsesSupply_air_static_pressure_sensor (){
		Set<ISupply_air_static_pressure_sensor> UsesSupply_air_static_pressure_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_air_static_pressure_sensor) {
				UsesSupply_air_static_pressure_sensor.add((Supply_air_static_pressure_sensor)action);
			}
		});
		return UsesSupply_air_static_pressure_sensor;
	}


  public void addUsesSupply_air_static_pressure_setpoint (ISupply_air_static_pressure_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_air_static_pressure_setpoint> getUsesSupply_air_static_pressure_setpoint (){
		Set<ISupply_air_static_pressure_setpoint> UsesSupply_air_static_pressure_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_air_static_pressure_setpoint) {
				UsesSupply_air_static_pressure_setpoint.add((Supply_air_static_pressure_setpoint)action);
			}
		});
		return UsesSupply_air_static_pressure_setpoint;
	}


  public void addUsesBuilding_air_static_pressure_sensor (IBuilding_air_static_pressure_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IBuilding_air_static_pressure_sensor> getUsesBuilding_air_static_pressure_sensor (){
		Set<IBuilding_air_static_pressure_sensor> UsesBuilding_air_static_pressure_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Building_air_static_pressure_sensor) {
				UsesBuilding_air_static_pressure_sensor.add((Building_air_static_pressure_sensor)action);
			}
		});
		return UsesBuilding_air_static_pressure_sensor;
	}


  public void addUsesBuilding_air_static_pressure_setpoint (IBuilding_air_static_pressure_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IBuilding_air_static_pressure_setpoint> getUsesBuilding_air_static_pressure_setpoint (){
		Set<IBuilding_air_static_pressure_setpoint> UsesBuilding_air_static_pressure_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Building_air_static_pressure_setpoint) {
				UsesBuilding_air_static_pressure_setpoint.add((Building_air_static_pressure_setpoint)action);
			}
		});
		return UsesBuilding_air_static_pressure_setpoint;
	}


  public void addUsesExhaust_fan_run_command (IExhaust_fan_run_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IExhaust_fan_run_command> getUsesExhaust_fan_run_command (){
		Set<IExhaust_fan_run_command> UsesExhaust_fan_run_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_run_command) {
				UsesExhaust_fan_run_command.add((Exhaust_fan_run_command)action);
			}
		});
		return UsesExhaust_fan_run_command;
	}


  public void addUsesExhaust_fan_run_status (IExhaust_fan_run_status parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IExhaust_fan_run_status> getUsesExhaust_fan_run_status (){
		Set<IExhaust_fan_run_status> UsesExhaust_fan_run_status = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_run_status) {
				UsesExhaust_fan_run_status.add((Exhaust_fan_run_status)action);
			}
		});
		return UsesExhaust_fan_run_status;
	}


  public void addUsesExhaust_fan_speed_percentage_command (IExhaust_fan_speed_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IExhaust_fan_speed_percentage_command> getUsesExhaust_fan_speed_percentage_command (){
		Set<IExhaust_fan_speed_percentage_command> UsesExhaust_fan_speed_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_speed_percentage_command) {
				UsesExhaust_fan_speed_percentage_command.add((Exhaust_fan_speed_percentage_command)action);
			}
		});
		return UsesExhaust_fan_speed_percentage_command;
	}


  public void addUsesEconomizer_mode (IEconomizer_mode parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IEconomizer_mode> getUsesEconomizer_mode (){
		Set<IEconomizer_mode> UsesEconomizer_mode = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Economizer_mode) {
				UsesEconomizer_mode.add((Economizer_mode)action);
			}
		});
		return UsesEconomizer_mode;
	}


  public void addUsesMixed_air_temperature_sensor (IMixed_air_temperature_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IMixed_air_temperature_sensor> getUsesMixed_air_temperature_sensor (){
		Set<IMixed_air_temperature_sensor> UsesMixed_air_temperature_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Mixed_air_temperature_sensor) {
				UsesMixed_air_temperature_sensor.add((Mixed_air_temperature_sensor)action);
			}
		});
		return UsesMixed_air_temperature_sensor;
	}


  public void addUsesOutside_air_damper_percentage_command (IOutside_air_damper_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IOutside_air_damper_percentage_command> getUsesOutside_air_damper_percentage_command (){
		Set<IOutside_air_damper_percentage_command> UsesOutside_air_damper_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Outside_air_damper_percentage_command) {
				UsesOutside_air_damper_percentage_command.add((Outside_air_damper_percentage_command)action);
			}
		});
		return UsesOutside_air_damper_percentage_command;
	}


  public void addUsesOutside_air_temperature_sensor (IOutside_air_temperature_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IOutside_air_temperature_sensor> getUsesOutside_air_temperature_sensor (){
		Set<IOutside_air_temperature_sensor> UsesOutside_air_temperature_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Outside_air_temperature_sensor) {
				UsesOutside_air_temperature_sensor.add((Outside_air_temperature_sensor)action);
			}
		});
		return UsesOutside_air_temperature_sensor;
	}


  public void addUsesReturn_air_temperature_sensor (IReturn_air_temperature_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IReturn_air_temperature_sensor> getUsesReturn_air_temperature_sensor (){
		Set<IReturn_air_temperature_sensor> UsesReturn_air_temperature_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Return_air_temperature_sensor) {
				UsesReturn_air_temperature_sensor.add((Return_air_temperature_sensor)action);
			}
		});
		return UsesReturn_air_temperature_sensor;
	}


  public void addUsesHeating_water_valve_percentage_command (IHeating_water_valve_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IHeating_water_valve_percentage_command> getUsesHeating_water_valve_percentage_command (){
		Set<IHeating_water_valve_percentage_command> UsesHeating_water_valve_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Heating_water_valve_percentage_command) {
				UsesHeating_water_valve_percentage_command.add((Heating_water_valve_percentage_command)action);
			}
		});
		return UsesHeating_water_valve_percentage_command;
	}


  public void addUsesExhaust_fan_run_command_1 (IExhaust_fan_run_command_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IExhaust_fan_run_command_1> getUsesExhaust_fan_run_command_1 (){
		Set<IExhaust_fan_run_command_1> UsesExhaust_fan_run_command_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_run_command_1) {
				UsesExhaust_fan_run_command_1.add((Exhaust_fan_run_command_1)action);
			}
		});
		return UsesExhaust_fan_run_command_1;
	}


  public void addUsesExhaust_fan_run_command_2 (IExhaust_fan_run_command_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IExhaust_fan_run_command_2> getUsesExhaust_fan_run_command_2 (){
		Set<IExhaust_fan_run_command_2> UsesExhaust_fan_run_command_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_run_command_2) {
				UsesExhaust_fan_run_command_2.add((Exhaust_fan_run_command_2)action);
			}
		});
		return UsesExhaust_fan_run_command_2;
	}


  public void addUsesExhaust_fan_run_command_3 (IExhaust_fan_run_command_3 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IExhaust_fan_run_command_3> getUsesExhaust_fan_run_command_3 (){
		Set<IExhaust_fan_run_command_3> UsesExhaust_fan_run_command_3 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_run_command_3) {
				UsesExhaust_fan_run_command_3.add((Exhaust_fan_run_command_3)action);
			}
		});
		return UsesExhaust_fan_run_command_3;
	}


  public void addUsesExhaust_fan_run_command_4 (IExhaust_fan_run_command_4 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IExhaust_fan_run_command_4> getUsesExhaust_fan_run_command_4 (){
		Set<IExhaust_fan_run_command_4> UsesExhaust_fan_run_command_4 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_run_command_4) {
				UsesExhaust_fan_run_command_4.add((Exhaust_fan_run_command_4)action);
			}
		});
		return UsesExhaust_fan_run_command_4;
	}


  public void addUsesExhaust_fan_run_status_1 (IExhaust_fan_run_status_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IExhaust_fan_run_status_1> getUsesExhaust_fan_run_status_1 (){
		Set<IExhaust_fan_run_status_1> UsesExhaust_fan_run_status_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_run_status_1) {
				UsesExhaust_fan_run_status_1.add((Exhaust_fan_run_status_1)action);
			}
		});
		return UsesExhaust_fan_run_status_1;
	}


  public void addUsesExhaust_fan_run_status_2 (IExhaust_fan_run_status_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IExhaust_fan_run_status_2> getUsesExhaust_fan_run_status_2 (){
		Set<IExhaust_fan_run_status_2> UsesExhaust_fan_run_status_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_run_status_2) {
				UsesExhaust_fan_run_status_2.add((Exhaust_fan_run_status_2)action);
			}
		});
		return UsesExhaust_fan_run_status_2;
	}


  public void addUsesExhaust_fan_run_status_3 (IExhaust_fan_run_status_3 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IExhaust_fan_run_status_3> getUsesExhaust_fan_run_status_3 (){
		Set<IExhaust_fan_run_status_3> UsesExhaust_fan_run_status_3 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_run_status_3) {
				UsesExhaust_fan_run_status_3.add((Exhaust_fan_run_status_3)action);
			}
		});
		return UsesExhaust_fan_run_status_3;
	}


  public void addUsesExhaust_fan_run_status_4 (IExhaust_fan_run_status_4 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IExhaust_fan_run_status_4> getUsesExhaust_fan_run_status_4 (){
		Set<IExhaust_fan_run_status_4> UsesExhaust_fan_run_status_4 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_run_status_4) {
				UsesExhaust_fan_run_status_4.add((Exhaust_fan_run_status_4)action);
			}
		});
		return UsesExhaust_fan_run_status_4;
	}


  public void addUsesVentilation_outside_air_damper_percentage_command (IVentilation_outside_air_damper_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IVentilation_outside_air_damper_percentage_command> getUsesVentilation_outside_air_damper_percentage_command (){
		Set<IVentilation_outside_air_damper_percentage_command> UsesVentilation_outside_air_damper_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Ventilation_outside_air_damper_percentage_command) {
				UsesVentilation_outside_air_damper_percentage_command.add((Ventilation_outside_air_damper_percentage_command)action);
			}
		});
		return UsesVentilation_outside_air_damper_percentage_command;
	}


  public void addUsesVentilation_outside_air_flowrate_sensor (IVentilation_outside_air_flowrate_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IVentilation_outside_air_flowrate_sensor> getUsesVentilation_outside_air_flowrate_sensor (){
		Set<IVentilation_outside_air_flowrate_sensor> UsesVentilation_outside_air_flowrate_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Ventilation_outside_air_flowrate_sensor) {
				UsesVentilation_outside_air_flowrate_sensor.add((Ventilation_outside_air_flowrate_sensor)action);
			}
		});
		return UsesVentilation_outside_air_flowrate_sensor;
	}


  public void addUsesVentilation_outside_air_flowrate_setpoint (IVentilation_outside_air_flowrate_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IVentilation_outside_air_flowrate_setpoint> getUsesVentilation_outside_air_flowrate_setpoint (){
		Set<IVentilation_outside_air_flowrate_setpoint> UsesVentilation_outside_air_flowrate_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Ventilation_outside_air_flowrate_setpoint) {
				UsesVentilation_outside_air_flowrate_setpoint.add((Ventilation_outside_air_flowrate_setpoint)action);
			}
		});
		return UsesVentilation_outside_air_flowrate_setpoint;
	}


  public void addUsesSupply_fan_run_command_1 (ISupply_fan_run_command_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_fan_run_command_1> getUsesSupply_fan_run_command_1 (){
		Set<ISupply_fan_run_command_1> UsesSupply_fan_run_command_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_fan_run_command_1) {
				UsesSupply_fan_run_command_1.add((Supply_fan_run_command_1)action);
			}
		});
		return UsesSupply_fan_run_command_1;
	}


  public void addUsesSupply_fan_run_command_2 (ISupply_fan_run_command_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_fan_run_command_2> getUsesSupply_fan_run_command_2 (){
		Set<ISupply_fan_run_command_2> UsesSupply_fan_run_command_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_fan_run_command_2) {
				UsesSupply_fan_run_command_2.add((Supply_fan_run_command_2)action);
			}
		});
		return UsesSupply_fan_run_command_2;
	}


  public void addUsesSupply_fan_run_status_1 (ISupply_fan_run_status_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_fan_run_status_1> getUsesSupply_fan_run_status_1 (){
		Set<ISupply_fan_run_status_1> UsesSupply_fan_run_status_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_fan_run_status_1) {
				UsesSupply_fan_run_status_1.add((Supply_fan_run_status_1)action);
			}
		});
		return UsesSupply_fan_run_status_1;
	}


  public void addUsesSupply_fan_run_status_2 (ISupply_fan_run_status_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_fan_run_status_2> getUsesSupply_fan_run_status_2 (){
		Set<ISupply_fan_run_status_2> UsesSupply_fan_run_status_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_fan_run_status_2) {
				UsesSupply_fan_run_status_2.add((Supply_fan_run_status_2)action);
			}
		});
		return UsesSupply_fan_run_status_2;
	}


  public void addUsesExhaust_fan_speed_percentage_command_1 (IExhaust_fan_speed_percentage_command_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IExhaust_fan_speed_percentage_command_1> getUsesExhaust_fan_speed_percentage_command_1 (){
		Set<IExhaust_fan_speed_percentage_command_1> UsesExhaust_fan_speed_percentage_command_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_speed_percentage_command_1) {
				UsesExhaust_fan_speed_percentage_command_1.add((Exhaust_fan_speed_percentage_command_1)action);
			}
		});
		return UsesExhaust_fan_speed_percentage_command_1;
	}


  public void addUsesExhaust_fan_speed_percentage_command_2 (IExhaust_fan_speed_percentage_command_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IExhaust_fan_speed_percentage_command_2> getUsesExhaust_fan_speed_percentage_command_2 (){
		Set<IExhaust_fan_speed_percentage_command_2> UsesExhaust_fan_speed_percentage_command_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_speed_percentage_command_2) {
				UsesExhaust_fan_speed_percentage_command_2.add((Exhaust_fan_speed_percentage_command_2)action);
			}
		});
		return UsesExhaust_fan_speed_percentage_command_2;
	}


  public void addUsesExhaust_fan_speed_percentage_command_3 (IExhaust_fan_speed_percentage_command_3 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IExhaust_fan_speed_percentage_command_3> getUsesExhaust_fan_speed_percentage_command_3 (){
		Set<IExhaust_fan_speed_percentage_command_3> UsesExhaust_fan_speed_percentage_command_3 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_speed_percentage_command_3) {
				UsesExhaust_fan_speed_percentage_command_3.add((Exhaust_fan_speed_percentage_command_3)action);
			}
		});
		return UsesExhaust_fan_speed_percentage_command_3;
	}


  public void addUsesSupply_fan_speed_percentage_command_1 (ISupply_fan_speed_percentage_command_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_fan_speed_percentage_command_1> getUsesSupply_fan_speed_percentage_command_1 (){
		Set<ISupply_fan_speed_percentage_command_1> UsesSupply_fan_speed_percentage_command_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_fan_speed_percentage_command_1) {
				UsesSupply_fan_speed_percentage_command_1.add((Supply_fan_speed_percentage_command_1)action);
			}
		});
		return UsesSupply_fan_speed_percentage_command_1;
	}


  public void addUsesSupply_fan_speed_percentage_command_2 (ISupply_fan_speed_percentage_command_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_fan_speed_percentage_command_2> getUsesSupply_fan_speed_percentage_command_2 (){
		Set<ISupply_fan_speed_percentage_command_2> UsesSupply_fan_speed_percentage_command_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_fan_speed_percentage_command_2) {
				UsesSupply_fan_speed_percentage_command_2.add((Supply_fan_speed_percentage_command_2)action);
			}
		});
		return UsesSupply_fan_speed_percentage_command_2;
	}


  public void addUsesCooling_request_count (ICooling_request_count parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ICooling_request_count> getUsesCooling_request_count (){
		Set<ICooling_request_count> UsesCooling_request_count = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Cooling_request_count) {
				UsesCooling_request_count.add((Cooling_request_count)action);
			}
		});
		return UsesCooling_request_count;
	}


  public void addUsesPressurization_request_count (IPressurization_request_count parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IPressurization_request_count> getUsesPressurization_request_count (){
		Set<IPressurization_request_count> UsesPressurization_request_count = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Pressurization_request_count) {
				UsesPressurization_request_count.add((Pressurization_request_count)action);
			}
		});
		return UsesPressurization_request_count;
	}


  public void addUsesExhaust_fan_speed_percentage_command_4 (IExhaust_fan_speed_percentage_command_4 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IExhaust_fan_speed_percentage_command_4> getUsesExhaust_fan_speed_percentage_command_4 (){
		Set<IExhaust_fan_speed_percentage_command_4> UsesExhaust_fan_speed_percentage_command_4 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_speed_percentage_command_4) {
				UsesExhaust_fan_speed_percentage_command_4.add((Exhaust_fan_speed_percentage_command_4)action);
			}
		});
		return UsesExhaust_fan_speed_percentage_command_4;
	}


  public void addUsesOutside_air_flowrate_sensor (IOutside_air_flowrate_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IOutside_air_flowrate_sensor> getUsesOutside_air_flowrate_sensor (){
		Set<IOutside_air_flowrate_sensor> UsesOutside_air_flowrate_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Outside_air_flowrate_sensor) {
				UsesOutside_air_flowrate_sensor.add((Outside_air_flowrate_sensor)action);
			}
		});
		return UsesOutside_air_flowrate_sensor;
	}


  public void addUsesCompressor_run_command_1 (ICompressor_run_command_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ICompressor_run_command_1> getUsesCompressor_run_command_1 (){
		Set<ICompressor_run_command_1> UsesCompressor_run_command_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Compressor_run_command_1) {
				UsesCompressor_run_command_1.add((Compressor_run_command_1)action);
			}
		});
		return UsesCompressor_run_command_1;
	}


  public void addUsesCompressor_run_command_2 (ICompressor_run_command_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ICompressor_run_command_2> getUsesCompressor_run_command_2 (){
		Set<ICompressor_run_command_2> UsesCompressor_run_command_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Compressor_run_command_2) {
				UsesCompressor_run_command_2.add((Compressor_run_command_2)action);
			}
		});
		return UsesCompressor_run_command_2;
	}


  public void addUsesCompressor_run_status_1 (ICompressor_run_status_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ICompressor_run_status_1> getUsesCompressor_run_status_1 (){
		Set<ICompressor_run_status_1> UsesCompressor_run_status_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Compressor_run_status_1) {
				UsesCompressor_run_status_1.add((Compressor_run_status_1)action);
			}
		});
		return UsesCompressor_run_status_1;
	}


  public void addUsesCompressor_run_status_2 (ICompressor_run_status_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ICompressor_run_status_2> getUsesCompressor_run_status_2 (){
		Set<ICompressor_run_status_2> UsesCompressor_run_status_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Compressor_run_status_2) {
				UsesCompressor_run_status_2.add((Compressor_run_status_2)action);
			}
		});
		return UsesCompressor_run_status_2;
	}


  public void addUsesHeater_run_command (IHeater_run_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IHeater_run_command> getUsesHeater_run_command (){
		Set<IHeater_run_command> UsesHeater_run_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Heater_run_command) {
				UsesHeater_run_command.add((Heater_run_command)action);
			}
		});
		return UsesHeater_run_command;
	}


  public void addUsesOutside_air_flowrate_setpoint (IOutside_air_flowrate_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IOutside_air_flowrate_setpoint> getUsesOutside_air_flowrate_setpoint (){
		Set<IOutside_air_flowrate_setpoint> UsesOutside_air_flowrate_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Outside_air_flowrate_setpoint) {
				UsesOutside_air_flowrate_setpoint.add((Outside_air_flowrate_setpoint)action);
			}
		});
		return UsesOutside_air_flowrate_setpoint;
	}


  public void addUsesFilter_differential_pressure_sensor_1 (IFilter_differential_pressure_sensor_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IFilter_differential_pressure_sensor_1> getUsesFilter_differential_pressure_sensor_1 (){
		Set<IFilter_differential_pressure_sensor_1> UsesFilter_differential_pressure_sensor_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Filter_differential_pressure_sensor_1) {
				UsesFilter_differential_pressure_sensor_1.add((Filter_differential_pressure_sensor_1)action);
			}
		});
		return UsesFilter_differential_pressure_sensor_1;
	}


  public void addUsesFilter_differential_pressure_sensor_2 (IFilter_differential_pressure_sensor_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IFilter_differential_pressure_sensor_2> getUsesFilter_differential_pressure_sensor_2 (){
		Set<IFilter_differential_pressure_sensor_2> UsesFilter_differential_pressure_sensor_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Filter_differential_pressure_sensor_2) {
				UsesFilter_differential_pressure_sensor_2.add((Filter_differential_pressure_sensor_2)action);
			}
		});
		return UsesFilter_differential_pressure_sensor_2;
	}


  public void addUsesFilter_differential_pressure_sensor_3 (IFilter_differential_pressure_sensor_3 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IFilter_differential_pressure_sensor_3> getUsesFilter_differential_pressure_sensor_3 (){
		Set<IFilter_differential_pressure_sensor_3> UsesFilter_differential_pressure_sensor_3 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Filter_differential_pressure_sensor_3) {
				UsesFilter_differential_pressure_sensor_3.add((Filter_differential_pressure_sensor_3)action);
			}
		});
		return UsesFilter_differential_pressure_sensor_3;
	}


  public void addUsesFilter_differential_pressure_sensor_4 (IFilter_differential_pressure_sensor_4 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IFilter_differential_pressure_sensor_4> getUsesFilter_differential_pressure_sensor_4 (){
		Set<IFilter_differential_pressure_sensor_4> UsesFilter_differential_pressure_sensor_4 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Filter_differential_pressure_sensor_4) {
				UsesFilter_differential_pressure_sensor_4.add((Filter_differential_pressure_sensor_4)action);
			}
		});
		return UsesFilter_differential_pressure_sensor_4;
	}


  public void addUsesCompressor_run_command_3 (ICompressor_run_command_3 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ICompressor_run_command_3> getUsesCompressor_run_command_3 (){
		Set<ICompressor_run_command_3> UsesCompressor_run_command_3 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Compressor_run_command_3) {
				UsesCompressor_run_command_3.add((Compressor_run_command_3)action);
			}
		});
		return UsesCompressor_run_command_3;
	}


  public void addUsesCompressor_run_command_4 (ICompressor_run_command_4 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ICompressor_run_command_4> getUsesCompressor_run_command_4 (){
		Set<ICompressor_run_command_4> UsesCompressor_run_command_4 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Compressor_run_command_4) {
				UsesCompressor_run_command_4.add((Compressor_run_command_4)action);
			}
		});
		return UsesCompressor_run_command_4;
	}


  public void addUsesCompressor_run_status_3 (ICompressor_run_status_3 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ICompressor_run_status_3> getUsesCompressor_run_status_3 (){
		Set<ICompressor_run_status_3> UsesCompressor_run_status_3 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Compressor_run_status_3) {
				UsesCompressor_run_status_3.add((Compressor_run_status_3)action);
			}
		});
		return UsesCompressor_run_status_3;
	}


  public void addUsesCompressor_run_status_4 (ICompressor_run_status_4 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ICompressor_run_status_4> getUsesCompressor_run_status_4 (){
		Set<ICompressor_run_status_4> UsesCompressor_run_status_4 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Compressor_run_status_4) {
				UsesCompressor_run_status_4.add((Compressor_run_status_4)action);
			}
		});
		return UsesCompressor_run_status_4;
	}


  public void addUsesZone_air_cooling_temperature_setpoint (IZone_air_cooling_temperature_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IZone_air_cooling_temperature_setpoint> getUsesZone_air_cooling_temperature_setpoint (){
		Set<IZone_air_cooling_temperature_setpoint> UsesZone_air_cooling_temperature_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Zone_air_cooling_temperature_setpoint) {
				UsesZone_air_cooling_temperature_setpoint.add((Zone_air_cooling_temperature_setpoint)action);
			}
		});
		return UsesZone_air_cooling_temperature_setpoint;
	}


  public void addUsesZone_air_temperature_sensor (IZone_air_temperature_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IZone_air_temperature_sensor> getUsesZone_air_temperature_sensor (){
		Set<IZone_air_temperature_sensor> UsesZone_air_temperature_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Zone_air_temperature_sensor) {
				UsesZone_air_temperature_sensor.add((Zone_air_temperature_sensor)action);
			}
		});
		return UsesZone_air_temperature_sensor;
	}


  public void addUsesDischarge_fan_run_command (IDischarge_fan_run_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IDischarge_fan_run_command> getUsesDischarge_fan_run_command (){
		Set<IDischarge_fan_run_command> UsesDischarge_fan_run_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Discharge_fan_run_command) {
				UsesDischarge_fan_run_command.add((Discharge_fan_run_command)action);
			}
		});
		return UsesDischarge_fan_run_command;
	}


  public void addUsesDischarge_fan_run_status (IDischarge_fan_run_status parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IDischarge_fan_run_status> getUsesDischarge_fan_run_status (){
		Set<IDischarge_fan_run_status> UsesDischarge_fan_run_status = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Discharge_fan_run_status) {
				UsesDischarge_fan_run_status.add((Discharge_fan_run_status)action);
			}
		});
		return UsesDischarge_fan_run_status;
	}


  public void addUsesZone_air_heating_temperature_setpoint (IZone_air_heating_temperature_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IZone_air_heating_temperature_setpoint> getUsesZone_air_heating_temperature_setpoint (){
		Set<IZone_air_heating_temperature_setpoint> UsesZone_air_heating_temperature_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Zone_air_heating_temperature_setpoint) {
				UsesZone_air_heating_temperature_setpoint.add((Zone_air_heating_temperature_setpoint)action);
			}
		});
		return UsesZone_air_heating_temperature_setpoint;
	}


  public void addUsesDischarge_fan_speed_percentage_command (IDischarge_fan_speed_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IDischarge_fan_speed_percentage_command> getUsesDischarge_fan_speed_percentage_command (){
		Set<IDischarge_fan_speed_percentage_command> UsesDischarge_fan_speed_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Discharge_fan_speed_percentage_command) {
				UsesDischarge_fan_speed_percentage_command.add((Discharge_fan_speed_percentage_command)action);
			}
		});
		return UsesDischarge_fan_speed_percentage_command;
	}


  public void addUsesMixed_air_temperature_setpoint (IMixed_air_temperature_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IMixed_air_temperature_setpoint> getUsesMixed_air_temperature_setpoint (){
		Set<IMixed_air_temperature_setpoint> UsesMixed_air_temperature_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Mixed_air_temperature_setpoint) {
				UsesMixed_air_temperature_setpoint.add((Mixed_air_temperature_setpoint)action);
			}
		});
		return UsesMixed_air_temperature_setpoint;
	}


  public void addUsesSupply_air_flowrate_sensor (ISupply_air_flowrate_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_air_flowrate_sensor> getUsesSupply_air_flowrate_sensor (){
		Set<ISupply_air_flowrate_sensor> UsesSupply_air_flowrate_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_air_flowrate_sensor) {
				UsesSupply_air_flowrate_sensor.add((Supply_air_flowrate_sensor)action);
			}
		});
		return UsesSupply_air_flowrate_sensor;
	}


  public void addUsesSupply_air_flowrate_setpoint (ISupply_air_flowrate_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_air_flowrate_setpoint> getUsesSupply_air_flowrate_setpoint (){
		Set<ISupply_air_flowrate_setpoint> UsesSupply_air_flowrate_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_air_flowrate_setpoint) {
				UsesSupply_air_flowrate_setpoint.add((Supply_air_flowrate_setpoint)action);
			}
		});
		return UsesSupply_air_flowrate_setpoint;
	}


  public void addUsesCompressor_run_command (ICompressor_run_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ICompressor_run_command> getUsesCompressor_run_command (){
		Set<ICompressor_run_command> UsesCompressor_run_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Compressor_run_command) {
				UsesCompressor_run_command.add((Compressor_run_command)action);
			}
		});
		return UsesCompressor_run_command;
	}


  public void addUsesCompressor_run_status (ICompressor_run_status parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ICompressor_run_status> getUsesCompressor_run_status (){
		Set<ICompressor_run_status> UsesCompressor_run_status = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Compressor_run_status) {
				UsesCompressor_run_status.add((Compressor_run_status)action);
			}
		});
		return UsesCompressor_run_status;
	}


  public void addUsesBypass_air_damper_percentage_command (IBypass_air_damper_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IBypass_air_damper_percentage_command> getUsesBypass_air_damper_percentage_command (){
		Set<IBypass_air_damper_percentage_command> UsesBypass_air_damper_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Bypass_air_damper_percentage_command) {
				UsesBypass_air_damper_percentage_command.add((Bypass_air_damper_percentage_command)action);
			}
		});
		return UsesBypass_air_damper_percentage_command;
	}


  public void addUsesHeater_run_command_1 (IHeater_run_command_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IHeater_run_command_1> getUsesHeater_run_command_1 (){
		Set<IHeater_run_command_1> UsesHeater_run_command_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Heater_run_command_1) {
				UsesHeater_run_command_1.add((Heater_run_command_1)action);
			}
		});
		return UsesHeater_run_command_1;
	}


  public void addUsesHeater_run_command_2 (IHeater_run_command_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IHeater_run_command_2> getUsesHeater_run_command_2 (){
		Set<IHeater_run_command_2> UsesHeater_run_command_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Heater_run_command_2) {
				UsesHeater_run_command_2.add((Heater_run_command_2)action);
			}
		});
		return UsesHeater_run_command_2;
	}


  public void addUsesSupply_air_cooling_temperature_setpoint (ISupply_air_cooling_temperature_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_air_cooling_temperature_setpoint> getUsesSupply_air_cooling_temperature_setpoint (){
		Set<ISupply_air_cooling_temperature_setpoint> UsesSupply_air_cooling_temperature_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_air_cooling_temperature_setpoint) {
				UsesSupply_air_cooling_temperature_setpoint.add((Supply_air_cooling_temperature_setpoint)action);
			}
		});
		return UsesSupply_air_cooling_temperature_setpoint;
	}


  public void addUsesSupply_air_heating_temperature_setpoint (ISupply_air_heating_temperature_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_air_heating_temperature_setpoint> getUsesSupply_air_heating_temperature_setpoint (){
		Set<ISupply_air_heating_temperature_setpoint> UsesSupply_air_heating_temperature_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_air_heating_temperature_setpoint) {
				UsesSupply_air_heating_temperature_setpoint.add((Supply_air_heating_temperature_setpoint)action);
			}
		});
		return UsesSupply_air_heating_temperature_setpoint;
	}


  public void addUsesDischarge_air_temperature_sensor (IDischarge_air_temperature_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IDischarge_air_temperature_sensor> getUsesDischarge_air_temperature_sensor (){
		Set<IDischarge_air_temperature_sensor> UsesDischarge_air_temperature_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Discharge_air_temperature_sensor) {
				UsesDischarge_air_temperature_sensor.add((Discharge_air_temperature_sensor)action);
			}
		});
		return UsesDischarge_air_temperature_sensor;
	}


  public void addUsesDischarge_air_temperature_setpoint (IDischarge_air_temperature_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IDischarge_air_temperature_setpoint> getUsesDischarge_air_temperature_setpoint (){
		Set<IDischarge_air_temperature_setpoint> UsesDischarge_air_temperature_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Discharge_air_temperature_setpoint) {
				UsesDischarge_air_temperature_setpoint.add((Discharge_air_temperature_setpoint)action);
			}
		});
		return UsesDischarge_air_temperature_setpoint;
	}


  public void addUsesZone_air_static_pressure_sensor (IZone_air_static_pressure_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IZone_air_static_pressure_sensor> getUsesZone_air_static_pressure_sensor (){
		Set<IZone_air_static_pressure_sensor> UsesZone_air_static_pressure_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Zone_air_static_pressure_sensor) {
				UsesZone_air_static_pressure_sensor.add((Zone_air_static_pressure_sensor)action);
			}
		});
		return UsesZone_air_static_pressure_sensor;
	}


  public void addUsesZone_air_static_pressure_setpoint (IZone_air_static_pressure_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IZone_air_static_pressure_setpoint> getUsesZone_air_static_pressure_setpoint (){
		Set<IZone_air_static_pressure_setpoint> UsesZone_air_static_pressure_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Zone_air_static_pressure_setpoint) {
				UsesZone_air_static_pressure_setpoint.add((Zone_air_static_pressure_setpoint)action);
			}
		});
		return UsesZone_air_static_pressure_setpoint;
	}


  public void addUsesZone_air_temperature_setpoint (IZone_air_temperature_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IZone_air_temperature_setpoint> getUsesZone_air_temperature_setpoint (){
		Set<IZone_air_temperature_setpoint> UsesZone_air_temperature_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Zone_air_temperature_setpoint) {
				UsesZone_air_temperature_setpoint.add((Zone_air_temperature_setpoint)action);
			}
		});
		return UsesZone_air_temperature_setpoint;
	}


  public void addUsesZone_air_co2_concentration_sensor (IZone_air_co2_concentration_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IZone_air_co2_concentration_sensor> getUsesZone_air_co2_concentration_sensor (){
		Set<IZone_air_co2_concentration_sensor> UsesZone_air_co2_concentration_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Zone_air_co2_concentration_sensor) {
				UsesZone_air_co2_concentration_sensor.add((Zone_air_co2_concentration_sensor)action);
			}
		});
		return UsesZone_air_co2_concentration_sensor;
	}


  public void addUsesZone_air_co2_concentration_setpoint (IZone_air_co2_concentration_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IZone_air_co2_concentration_setpoint> getUsesZone_air_co2_concentration_setpoint (){
		Set<IZone_air_co2_concentration_setpoint> UsesZone_air_co2_concentration_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Zone_air_co2_concentration_setpoint) {
				UsesZone_air_co2_concentration_setpoint.add((Zone_air_co2_concentration_setpoint)action);
			}
		});
		return UsesZone_air_co2_concentration_setpoint;
	}


  public void addUsesBoost_fan_run_command (IBoost_fan_run_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IBoost_fan_run_command> getUsesBoost_fan_run_command (){
		Set<IBoost_fan_run_command> UsesBoost_fan_run_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Boost_fan_run_command) {
				UsesBoost_fan_run_command.add((Boost_fan_run_command)action);
			}
		});
		return UsesBoost_fan_run_command;
	}


  public void addUsesBoost_fan_run_status (IBoost_fan_run_status parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IBoost_fan_run_status> getUsesBoost_fan_run_status (){
		Set<IBoost_fan_run_status> UsesBoost_fan_run_status = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Boost_fan_run_status) {
				UsesBoost_fan_run_status.add((Boost_fan_run_status)action);
			}
		});
		return UsesBoost_fan_run_status;
	}


  public void addUsesReversing_valve_command (IReversing_valve_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IReversing_valve_command> getUsesReversing_valve_command (){
		Set<IReversing_valve_command> UsesReversing_valve_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Reversing_valve_command) {
				UsesReversing_valve_command.add((Reversing_valve_command)action);
			}
		});
		return UsesReversing_valve_command;
	}


  public void addUsesDischarge_air_heating_temperature_setpoint (IDischarge_air_heating_temperature_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IDischarge_air_heating_temperature_setpoint> getUsesDischarge_air_heating_temperature_setpoint (){
		Set<IDischarge_air_heating_temperature_setpoint> UsesDischarge_air_heating_temperature_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Discharge_air_heating_temperature_setpoint) {
				UsesDischarge_air_heating_temperature_setpoint.add((Discharge_air_heating_temperature_setpoint)action);
			}
		});
		return UsesDischarge_air_heating_temperature_setpoint;
	}


  public void addUsesHeater_run_command_3 (IHeater_run_command_3 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IHeater_run_command_3> getUsesHeater_run_command_3 (){
		Set<IHeater_run_command_3> UsesHeater_run_command_3 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Heater_run_command_3) {
				UsesHeater_run_command_3.add((Heater_run_command_3)action);
			}
		});
		return UsesHeater_run_command_3;
	}


  public void addUsesMixed_air_temperature_sensor_1 (IMixed_air_temperature_sensor_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IMixed_air_temperature_sensor_1> getUsesMixed_air_temperature_sensor_1 (){
		Set<IMixed_air_temperature_sensor_1> UsesMixed_air_temperature_sensor_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Mixed_air_temperature_sensor_1) {
				UsesMixed_air_temperature_sensor_1.add((Mixed_air_temperature_sensor_1)action);
			}
		});
		return UsesMixed_air_temperature_sensor_1;
	}


  public void addUsesMixed_air_temperature_sensor_2 (IMixed_air_temperature_sensor_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IMixed_air_temperature_sensor_2> getUsesMixed_air_temperature_sensor_2 (){
		Set<IMixed_air_temperature_sensor_2> UsesMixed_air_temperature_sensor_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Mixed_air_temperature_sensor_2) {
				UsesMixed_air_temperature_sensor_2.add((Mixed_air_temperature_sensor_2)action);
			}
		});
		return UsesMixed_air_temperature_sensor_2;
	}


  public void addUsesOptionalsSupply_fan_current_sensor (ISupply_fan_current_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<ISupply_fan_current_sensor> getUsesOptionalsSupply_fan_current_sensor (){
		Set<ISupply_fan_current_sensor> UsesOptionalsSupply_fan_current_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_fan_current_sensor) {
				UsesOptionalsSupply_fan_current_sensor.add((Supply_fan_current_sensor)action);
			}
		});
		return UsesOptionalsSupply_fan_current_sensor;
	}


  public void addUsesOptionalsSupply_fan_power_sensor (ISupply_fan_power_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<ISupply_fan_power_sensor> getUsesOptionalsSupply_fan_power_sensor (){
		Set<ISupply_fan_power_sensor> UsesOptionalsSupply_fan_power_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_fan_power_sensor) {
				UsesOptionalsSupply_fan_power_sensor.add((Supply_fan_power_sensor)action);
			}
		});
		return UsesOptionalsSupply_fan_power_sensor;
	}


  public void addUsesOptionalsSupply_fan_speed_frequency_sensor (ISupply_fan_speed_frequency_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<ISupply_fan_speed_frequency_sensor> getUsesOptionalsSupply_fan_speed_frequency_sensor (){
		Set<ISupply_fan_speed_frequency_sensor> UsesOptionalsSupply_fan_speed_frequency_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_fan_speed_frequency_sensor) {
				UsesOptionalsSupply_fan_speed_frequency_sensor.add((Supply_fan_speed_frequency_sensor)action);
			}
		});
		return UsesOptionalsSupply_fan_speed_frequency_sensor;
	}


  public void addUsesOptionalsSupply_fan_speed_percentage_sensor (ISupply_fan_speed_percentage_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<ISupply_fan_speed_percentage_sensor> getUsesOptionalsSupply_fan_speed_percentage_sensor (){
		Set<ISupply_fan_speed_percentage_sensor> UsesOptionalsSupply_fan_speed_percentage_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_fan_speed_percentage_sensor) {
				UsesOptionalsSupply_fan_speed_percentage_sensor.add((Supply_fan_speed_percentage_sensor)action);
			}
		});
		return UsesOptionalsSupply_fan_speed_percentage_sensor;
	}


  public void addUsesOptionalsCooling_thermal_power_capacity (ICooling_thermal_power_capacity parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<ICooling_thermal_power_capacity> getUsesOptionalsCooling_thermal_power_capacity (){
		Set<ICooling_thermal_power_capacity> UsesOptionalsCooling_thermal_power_capacity = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Cooling_thermal_power_capacity) {
				UsesOptionalsCooling_thermal_power_capacity.add((Cooling_thermal_power_capacity)action);
			}
		});
		return UsesOptionalsCooling_thermal_power_capacity;
	}


  public void addUsesOptionalsLeaving_cooling_coil_temperature_sensor (ILeaving_cooling_coil_temperature_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<ILeaving_cooling_coil_temperature_sensor> getUsesOptionalsLeaving_cooling_coil_temperature_sensor (){
		Set<ILeaving_cooling_coil_temperature_sensor> UsesOptionalsLeaving_cooling_coil_temperature_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Leaving_cooling_coil_temperature_sensor) {
				UsesOptionalsLeaving_cooling_coil_temperature_sensor.add((Leaving_cooling_coil_temperature_sensor)action);
			}
		});
		return UsesOptionalsLeaving_cooling_coil_temperature_sensor;
	}


  public void addUsesOptionalsPressurization_request_count (IPressurization_request_count parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IPressurization_request_count> getUsesOptionalsPressurization_request_count (){
		Set<IPressurization_request_count> UsesOptionalsPressurization_request_count = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Pressurization_request_count) {
				UsesOptionalsPressurization_request_count.add((Pressurization_request_count)action);
			}
		});
		return UsesOptionalsPressurization_request_count;
	}


  public void addUsesOptionalsSupply_air_damper_percentage_command (ISupply_air_damper_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<ISupply_air_damper_percentage_command> getUsesOptionalsSupply_air_damper_percentage_command (){
		Set<ISupply_air_damper_percentage_command> UsesOptionalsSupply_air_damper_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_air_damper_percentage_command) {
				UsesOptionalsSupply_air_damper_percentage_command.add((Supply_air_damper_percentage_command)action);
			}
		});
		return UsesOptionalsSupply_air_damper_percentage_command;
	}


  public void addUsesOptionalsSupply_air_flowrate_sensor (ISupply_air_flowrate_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<ISupply_air_flowrate_sensor> getUsesOptionalsSupply_air_flowrate_sensor (){
		Set<ISupply_air_flowrate_sensor> UsesOptionalsSupply_air_flowrate_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_air_flowrate_sensor) {
				UsesOptionalsSupply_air_flowrate_sensor.add((Supply_air_flowrate_sensor)action);
			}
		});
		return UsesOptionalsSupply_air_flowrate_sensor;
	}


  public void addUsesOptionalsSupply_fan_run_command (ISupply_fan_run_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<ISupply_fan_run_command> getUsesOptionalsSupply_fan_run_command (){
		Set<ISupply_fan_run_command> UsesOptionalsSupply_fan_run_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_fan_run_command) {
				UsesOptionalsSupply_fan_run_command.add((Supply_fan_run_command)action);
			}
		});
		return UsesOptionalsSupply_fan_run_command;
	}


  public void addUsesOptionalsSupply_fan_run_status (ISupply_fan_run_status parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<ISupply_fan_run_status> getUsesOptionalsSupply_fan_run_status (){
		Set<ISupply_fan_run_status> UsesOptionalsSupply_fan_run_status = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_fan_run_status) {
				UsesOptionalsSupply_fan_run_status.add((Supply_fan_run_status)action);
			}
		});
		return UsesOptionalsSupply_fan_run_status;
	}


  public void addUsesOptionalsSupply_fan_speed_percentage_command (ISupply_fan_speed_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<ISupply_fan_speed_percentage_command> getUsesOptionalsSupply_fan_speed_percentage_command (){
		Set<ISupply_fan_speed_percentage_command> UsesOptionalsSupply_fan_speed_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_fan_speed_percentage_command) {
				UsesOptionalsSupply_fan_speed_percentage_command.add((Supply_fan_speed_percentage_command)action);
			}
		});
		return UsesOptionalsSupply_fan_speed_percentage_command;
	}


  public void addUsesOptionalsHeating_thermal_power_capacity (IHeating_thermal_power_capacity parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IHeating_thermal_power_capacity> getUsesOptionalsHeating_thermal_power_capacity (){
		Set<IHeating_thermal_power_capacity> UsesOptionalsHeating_thermal_power_capacity = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Heating_thermal_power_capacity) {
				UsesOptionalsHeating_thermal_power_capacity.add((Heating_thermal_power_capacity)action);
			}
		});
		return UsesOptionalsHeating_thermal_power_capacity;
	}


  public void addUsesOptionalsHeating_water_valve_percentage_sensor (IHeating_water_valve_percentage_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IHeating_water_valve_percentage_sensor> getUsesOptionalsHeating_water_valve_percentage_sensor (){
		Set<IHeating_water_valve_percentage_sensor> UsesOptionalsHeating_water_valve_percentage_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Heating_water_valve_percentage_sensor) {
				UsesOptionalsHeating_water_valve_percentage_sensor.add((Heating_water_valve_percentage_sensor)action);
			}
		});
		return UsesOptionalsHeating_water_valve_percentage_sensor;
	}


  public void addUsesOptionalsExhaust_air_flowrate_capacity (IExhaust_air_flowrate_capacity parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IExhaust_air_flowrate_capacity> getUsesOptionalsExhaust_air_flowrate_capacity (){
		Set<IExhaust_air_flowrate_capacity> UsesOptionalsExhaust_air_flowrate_capacity = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_air_flowrate_capacity) {
				UsesOptionalsExhaust_air_flowrate_capacity.add((Exhaust_air_flowrate_capacity)action);
			}
		});
		return UsesOptionalsExhaust_air_flowrate_capacity;
	}


  public void addUsesOptionalsExhaust_fan_current_sensor_1 (IExhaust_fan_current_sensor_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IExhaust_fan_current_sensor_1> getUsesOptionalsExhaust_fan_current_sensor_1 (){
		Set<IExhaust_fan_current_sensor_1> UsesOptionalsExhaust_fan_current_sensor_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_current_sensor_1) {
				UsesOptionalsExhaust_fan_current_sensor_1.add((Exhaust_fan_current_sensor_1)action);
			}
		});
		return UsesOptionalsExhaust_fan_current_sensor_1;
	}


  public void addUsesOptionalsExhaust_fan_current_sensor_2 (IExhaust_fan_current_sensor_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IExhaust_fan_current_sensor_2> getUsesOptionalsExhaust_fan_current_sensor_2 (){
		Set<IExhaust_fan_current_sensor_2> UsesOptionalsExhaust_fan_current_sensor_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_current_sensor_2) {
				UsesOptionalsExhaust_fan_current_sensor_2.add((Exhaust_fan_current_sensor_2)action);
			}
		});
		return UsesOptionalsExhaust_fan_current_sensor_2;
	}


  public void addUsesOptionalsExhaust_fan_current_sensor_3 (IExhaust_fan_current_sensor_3 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IExhaust_fan_current_sensor_3> getUsesOptionalsExhaust_fan_current_sensor_3 (){
		Set<IExhaust_fan_current_sensor_3> UsesOptionalsExhaust_fan_current_sensor_3 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_current_sensor_3) {
				UsesOptionalsExhaust_fan_current_sensor_3.add((Exhaust_fan_current_sensor_3)action);
			}
		});
		return UsesOptionalsExhaust_fan_current_sensor_3;
	}


  public void addUsesOptionalsExhaust_fan_current_sensor_4 (IExhaust_fan_current_sensor_4 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IExhaust_fan_current_sensor_4> getUsesOptionalsExhaust_fan_current_sensor_4 (){
		Set<IExhaust_fan_current_sensor_4> UsesOptionalsExhaust_fan_current_sensor_4 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_current_sensor_4) {
				UsesOptionalsExhaust_fan_current_sensor_4.add((Exhaust_fan_current_sensor_4)action);
			}
		});
		return UsesOptionalsExhaust_fan_current_sensor_4;
	}


  public void addUsesOptionalsExhaust_fan_power_capacity (IExhaust_fan_power_capacity parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IExhaust_fan_power_capacity> getUsesOptionalsExhaust_fan_power_capacity (){
		Set<IExhaust_fan_power_capacity> UsesOptionalsExhaust_fan_power_capacity = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_power_capacity) {
				UsesOptionalsExhaust_fan_power_capacity.add((Exhaust_fan_power_capacity)action);
			}
		});
		return UsesOptionalsExhaust_fan_power_capacity;
	}


  public void addUsesOptionalsExhaust_fan_power_sensor_1 (IExhaust_fan_power_sensor_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IExhaust_fan_power_sensor_1> getUsesOptionalsExhaust_fan_power_sensor_1 (){
		Set<IExhaust_fan_power_sensor_1> UsesOptionalsExhaust_fan_power_sensor_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_power_sensor_1) {
				UsesOptionalsExhaust_fan_power_sensor_1.add((Exhaust_fan_power_sensor_1)action);
			}
		});
		return UsesOptionalsExhaust_fan_power_sensor_1;
	}


  public void addUsesOptionalsExhaust_fan_power_sensor_2 (IExhaust_fan_power_sensor_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IExhaust_fan_power_sensor_2> getUsesOptionalsExhaust_fan_power_sensor_2 (){
		Set<IExhaust_fan_power_sensor_2> UsesOptionalsExhaust_fan_power_sensor_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_power_sensor_2) {
				UsesOptionalsExhaust_fan_power_sensor_2.add((Exhaust_fan_power_sensor_2)action);
			}
		});
		return UsesOptionalsExhaust_fan_power_sensor_2;
	}


  public void addUsesOptionalsExhaust_fan_power_sensor_3 (IExhaust_fan_power_sensor_3 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IExhaust_fan_power_sensor_3> getUsesOptionalsExhaust_fan_power_sensor_3 (){
		Set<IExhaust_fan_power_sensor_3> UsesOptionalsExhaust_fan_power_sensor_3 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_power_sensor_3) {
				UsesOptionalsExhaust_fan_power_sensor_3.add((Exhaust_fan_power_sensor_3)action);
			}
		});
		return UsesOptionalsExhaust_fan_power_sensor_3;
	}


  public void addUsesOptionalsExhaust_fan_power_sensor_4 (IExhaust_fan_power_sensor_4 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IExhaust_fan_power_sensor_4> getUsesOptionalsExhaust_fan_power_sensor_4 (){
		Set<IExhaust_fan_power_sensor_4> UsesOptionalsExhaust_fan_power_sensor_4 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_power_sensor_4) {
				UsesOptionalsExhaust_fan_power_sensor_4.add((Exhaust_fan_power_sensor_4)action);
			}
		});
		return UsesOptionalsExhaust_fan_power_sensor_4;
	}


  public void addUsesOptionalsExhaust_fan_current_sensor (IExhaust_fan_current_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IExhaust_fan_current_sensor> getUsesOptionalsExhaust_fan_current_sensor (){
		Set<IExhaust_fan_current_sensor> UsesOptionalsExhaust_fan_current_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_current_sensor) {
				UsesOptionalsExhaust_fan_current_sensor.add((Exhaust_fan_current_sensor)action);
			}
		});
		return UsesOptionalsExhaust_fan_current_sensor;
	}


  public void addUsesOptionalsExhaust_fan_power_sensor (IExhaust_fan_power_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IExhaust_fan_power_sensor> getUsesOptionalsExhaust_fan_power_sensor (){
		Set<IExhaust_fan_power_sensor> UsesOptionalsExhaust_fan_power_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_power_sensor) {
				UsesOptionalsExhaust_fan_power_sensor.add((Exhaust_fan_power_sensor)action);
			}
		});
		return UsesOptionalsExhaust_fan_power_sensor;
	}


  public void addUsesOptionalsExhaust_fan_speed_frequency_sensor (IExhaust_fan_speed_frequency_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IExhaust_fan_speed_frequency_sensor> getUsesOptionalsExhaust_fan_speed_frequency_sensor (){
		Set<IExhaust_fan_speed_frequency_sensor> UsesOptionalsExhaust_fan_speed_frequency_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_speed_frequency_sensor) {
				UsesOptionalsExhaust_fan_speed_frequency_sensor.add((Exhaust_fan_speed_frequency_sensor)action);
			}
		});
		return UsesOptionalsExhaust_fan_speed_frequency_sensor;
	}


  public void addUsesOptionalsExhaust_fan_speed_percentage_sensor (IExhaust_fan_speed_percentage_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IExhaust_fan_speed_percentage_sensor> getUsesOptionalsExhaust_fan_speed_percentage_sensor (){
		Set<IExhaust_fan_speed_percentage_sensor> UsesOptionalsExhaust_fan_speed_percentage_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_speed_percentage_sensor) {
				UsesOptionalsExhaust_fan_speed_percentage_sensor.add((Exhaust_fan_speed_percentage_sensor)action);
			}
		});
		return UsesOptionalsExhaust_fan_speed_percentage_sensor;
	}


  public void addUsesOptionalsExhaust_air_damper_percentage_command (IExhaust_air_damper_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IExhaust_air_damper_percentage_command> getUsesOptionalsExhaust_air_damper_percentage_command (){
		Set<IExhaust_air_damper_percentage_command> UsesOptionalsExhaust_air_damper_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_air_damper_percentage_command) {
				UsesOptionalsExhaust_air_damper_percentage_command.add((Exhaust_air_damper_percentage_command)action);
			}
		});
		return UsesOptionalsExhaust_air_damper_percentage_command;
	}


  public void addUsesOptionalsExhaust_fan_run_status (IExhaust_fan_run_status parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IExhaust_fan_run_status> getUsesOptionalsExhaust_fan_run_status (){
		Set<IExhaust_fan_run_status> UsesOptionalsExhaust_fan_run_status = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_run_status) {
				UsesOptionalsExhaust_fan_run_status.add((Exhaust_fan_run_status)action);
			}
		});
		return UsesOptionalsExhaust_fan_run_status;
	}


  public void addUsesOptionalsSupply_air_flowrate_capacity (ISupply_air_flowrate_capacity parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<ISupply_air_flowrate_capacity> getUsesOptionalsSupply_air_flowrate_capacity (){
		Set<ISupply_air_flowrate_capacity> UsesOptionalsSupply_air_flowrate_capacity = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_air_flowrate_capacity) {
				UsesOptionalsSupply_air_flowrate_capacity.add((Supply_air_flowrate_capacity)action);
			}
		});
		return UsesOptionalsSupply_air_flowrate_capacity;
	}


  public void addUsesOptionalsSupply_fan_current_sensor_1 (ISupply_fan_current_sensor_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<ISupply_fan_current_sensor_1> getUsesOptionalsSupply_fan_current_sensor_1 (){
		Set<ISupply_fan_current_sensor_1> UsesOptionalsSupply_fan_current_sensor_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_fan_current_sensor_1) {
				UsesOptionalsSupply_fan_current_sensor_1.add((Supply_fan_current_sensor_1)action);
			}
		});
		return UsesOptionalsSupply_fan_current_sensor_1;
	}


  public void addUsesOptionalsSupply_fan_current_sensor_2 (ISupply_fan_current_sensor_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<ISupply_fan_current_sensor_2> getUsesOptionalsSupply_fan_current_sensor_2 (){
		Set<ISupply_fan_current_sensor_2> UsesOptionalsSupply_fan_current_sensor_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_fan_current_sensor_2) {
				UsesOptionalsSupply_fan_current_sensor_2.add((Supply_fan_current_sensor_2)action);
			}
		});
		return UsesOptionalsSupply_fan_current_sensor_2;
	}


  public void addUsesOptionalsSupply_fan_power_capacity (ISupply_fan_power_capacity parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<ISupply_fan_power_capacity> getUsesOptionalsSupply_fan_power_capacity (){
		Set<ISupply_fan_power_capacity> UsesOptionalsSupply_fan_power_capacity = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_fan_power_capacity) {
				UsesOptionalsSupply_fan_power_capacity.add((Supply_fan_power_capacity)action);
			}
		});
		return UsesOptionalsSupply_fan_power_capacity;
	}


  public void addUsesOptionalsSupply_fan_power_sensor_1 (ISupply_fan_power_sensor_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<ISupply_fan_power_sensor_1> getUsesOptionalsSupply_fan_power_sensor_1 (){
		Set<ISupply_fan_power_sensor_1> UsesOptionalsSupply_fan_power_sensor_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_fan_power_sensor_1) {
				UsesOptionalsSupply_fan_power_sensor_1.add((Supply_fan_power_sensor_1)action);
			}
		});
		return UsesOptionalsSupply_fan_power_sensor_1;
	}


  public void addUsesOptionalsSupply_fan_power_sensor_2 (ISupply_fan_power_sensor_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<ISupply_fan_power_sensor_2> getUsesOptionalsSupply_fan_power_sensor_2 (){
		Set<ISupply_fan_power_sensor_2> UsesOptionalsSupply_fan_power_sensor_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_fan_power_sensor_2) {
				UsesOptionalsSupply_fan_power_sensor_2.add((Supply_fan_power_sensor_2)action);
			}
		});
		return UsesOptionalsSupply_fan_power_sensor_2;
	}


  public void addUsesOptionalsOutside_air_flowrate_sensor (IOutside_air_flowrate_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IOutside_air_flowrate_sensor> getUsesOptionalsOutside_air_flowrate_sensor (){
		Set<IOutside_air_flowrate_sensor> UsesOptionalsOutside_air_flowrate_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Outside_air_flowrate_sensor) {
				UsesOptionalsOutside_air_flowrate_sensor.add((Outside_air_flowrate_sensor)action);
			}
		});
		return UsesOptionalsOutside_air_flowrate_sensor;
	}


  public void addUsesOptionalsOutside_air_flowrate_setpoint (IOutside_air_flowrate_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IOutside_air_flowrate_setpoint> getUsesOptionalsOutside_air_flowrate_setpoint (){
		Set<IOutside_air_flowrate_setpoint> UsesOptionalsOutside_air_flowrate_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Outside_air_flowrate_setpoint) {
				UsesOptionalsOutside_air_flowrate_setpoint.add((Outside_air_flowrate_setpoint)action);
			}
		});
		return UsesOptionalsOutside_air_flowrate_setpoint;
	}


  public void addUsesOptionalsSupply_air_temperature_sensor (ISupply_air_temperature_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<ISupply_air_temperature_sensor> getUsesOptionalsSupply_air_temperature_sensor (){
		Set<ISupply_air_temperature_sensor> UsesOptionalsSupply_air_temperature_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_air_temperature_sensor) {
				UsesOptionalsSupply_air_temperature_sensor.add((Supply_air_temperature_sensor)action);
			}
		});
		return UsesOptionalsSupply_air_temperature_sensor;
	}


  public void addUsesOptionalsExhaust_fan_speed_frequency_sensor_1 (IExhaust_fan_speed_frequency_sensor_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IExhaust_fan_speed_frequency_sensor_1> getUsesOptionalsExhaust_fan_speed_frequency_sensor_1 (){
		Set<IExhaust_fan_speed_frequency_sensor_1> UsesOptionalsExhaust_fan_speed_frequency_sensor_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_speed_frequency_sensor_1) {
				UsesOptionalsExhaust_fan_speed_frequency_sensor_1.add((Exhaust_fan_speed_frequency_sensor_1)action);
			}
		});
		return UsesOptionalsExhaust_fan_speed_frequency_sensor_1;
	}


  public void addUsesOptionalsExhaust_fan_speed_frequency_sensor_2 (IExhaust_fan_speed_frequency_sensor_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IExhaust_fan_speed_frequency_sensor_2> getUsesOptionalsExhaust_fan_speed_frequency_sensor_2 (){
		Set<IExhaust_fan_speed_frequency_sensor_2> UsesOptionalsExhaust_fan_speed_frequency_sensor_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_speed_frequency_sensor_2) {
				UsesOptionalsExhaust_fan_speed_frequency_sensor_2.add((Exhaust_fan_speed_frequency_sensor_2)action);
			}
		});
		return UsesOptionalsExhaust_fan_speed_frequency_sensor_2;
	}


  public void addUsesOptionalsExhaust_fan_speed_frequency_sensor_3 (IExhaust_fan_speed_frequency_sensor_3 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IExhaust_fan_speed_frequency_sensor_3> getUsesOptionalsExhaust_fan_speed_frequency_sensor_3 (){
		Set<IExhaust_fan_speed_frequency_sensor_3> UsesOptionalsExhaust_fan_speed_frequency_sensor_3 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_speed_frequency_sensor_3) {
				UsesOptionalsExhaust_fan_speed_frequency_sensor_3.add((Exhaust_fan_speed_frequency_sensor_3)action);
			}
		});
		return UsesOptionalsExhaust_fan_speed_frequency_sensor_3;
	}


  public void addUsesOptionalsExhaust_fan_speed_percentage_sensor_1 (IExhaust_fan_speed_percentage_sensor_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IExhaust_fan_speed_percentage_sensor_1> getUsesOptionalsExhaust_fan_speed_percentage_sensor_1 (){
		Set<IExhaust_fan_speed_percentage_sensor_1> UsesOptionalsExhaust_fan_speed_percentage_sensor_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_speed_percentage_sensor_1) {
				UsesOptionalsExhaust_fan_speed_percentage_sensor_1.add((Exhaust_fan_speed_percentage_sensor_1)action);
			}
		});
		return UsesOptionalsExhaust_fan_speed_percentage_sensor_1;
	}


  public void addUsesOptionalsExhaust_fan_speed_percentage_sensor_2 (IExhaust_fan_speed_percentage_sensor_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IExhaust_fan_speed_percentage_sensor_2> getUsesOptionalsExhaust_fan_speed_percentage_sensor_2 (){
		Set<IExhaust_fan_speed_percentage_sensor_2> UsesOptionalsExhaust_fan_speed_percentage_sensor_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_speed_percentage_sensor_2) {
				UsesOptionalsExhaust_fan_speed_percentage_sensor_2.add((Exhaust_fan_speed_percentage_sensor_2)action);
			}
		});
		return UsesOptionalsExhaust_fan_speed_percentage_sensor_2;
	}


  public void addUsesOptionalsExhaust_fan_speed_percentage_sensor_3 (IExhaust_fan_speed_percentage_sensor_3 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IExhaust_fan_speed_percentage_sensor_3> getUsesOptionalsExhaust_fan_speed_percentage_sensor_3 (){
		Set<IExhaust_fan_speed_percentage_sensor_3> UsesOptionalsExhaust_fan_speed_percentage_sensor_3 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_speed_percentage_sensor_3) {
				UsesOptionalsExhaust_fan_speed_percentage_sensor_3.add((Exhaust_fan_speed_percentage_sensor_3)action);
			}
		});
		return UsesOptionalsExhaust_fan_speed_percentage_sensor_3;
	}


  public void addUsesOptionalsSupply_fan_speed_frequency_sensor_1 (ISupply_fan_speed_frequency_sensor_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<ISupply_fan_speed_frequency_sensor_1> getUsesOptionalsSupply_fan_speed_frequency_sensor_1 (){
		Set<ISupply_fan_speed_frequency_sensor_1> UsesOptionalsSupply_fan_speed_frequency_sensor_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_fan_speed_frequency_sensor_1) {
				UsesOptionalsSupply_fan_speed_frequency_sensor_1.add((Supply_fan_speed_frequency_sensor_1)action);
			}
		});
		return UsesOptionalsSupply_fan_speed_frequency_sensor_1;
	}


  public void addUsesOptionalsSupply_fan_speed_frequency_sensor_2 (ISupply_fan_speed_frequency_sensor_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<ISupply_fan_speed_frequency_sensor_2> getUsesOptionalsSupply_fan_speed_frequency_sensor_2 (){
		Set<ISupply_fan_speed_frequency_sensor_2> UsesOptionalsSupply_fan_speed_frequency_sensor_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_fan_speed_frequency_sensor_2) {
				UsesOptionalsSupply_fan_speed_frequency_sensor_2.add((Supply_fan_speed_frequency_sensor_2)action);
			}
		});
		return UsesOptionalsSupply_fan_speed_frequency_sensor_2;
	}


  public void addUsesOptionalsSupply_fan_speed_percentage_sensor_1 (ISupply_fan_speed_percentage_sensor_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<ISupply_fan_speed_percentage_sensor_1> getUsesOptionalsSupply_fan_speed_percentage_sensor_1 (){
		Set<ISupply_fan_speed_percentage_sensor_1> UsesOptionalsSupply_fan_speed_percentage_sensor_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_fan_speed_percentage_sensor_1) {
				UsesOptionalsSupply_fan_speed_percentage_sensor_1.add((Supply_fan_speed_percentage_sensor_1)action);
			}
		});
		return UsesOptionalsSupply_fan_speed_percentage_sensor_1;
	}


  public void addUsesOptionalsSupply_fan_speed_percentage_sensor_2 (ISupply_fan_speed_percentage_sensor_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<ISupply_fan_speed_percentage_sensor_2> getUsesOptionalsSupply_fan_speed_percentage_sensor_2 (){
		Set<ISupply_fan_speed_percentage_sensor_2> UsesOptionalsSupply_fan_speed_percentage_sensor_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_fan_speed_percentage_sensor_2) {
				UsesOptionalsSupply_fan_speed_percentage_sensor_2.add((Supply_fan_speed_percentage_sensor_2)action);
			}
		});
		return UsesOptionalsSupply_fan_speed_percentage_sensor_2;
	}


  public void addUsesOptionalsHeating_request_count (IHeating_request_count parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IHeating_request_count> getUsesOptionalsHeating_request_count (){
		Set<IHeating_request_count> UsesOptionalsHeating_request_count = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Heating_request_count) {
				UsesOptionalsHeating_request_count.add((Heating_request_count)action);
			}
		});
		return UsesOptionalsHeating_request_count;
	}


  public void addUsesOptionalsExhaust_fan_speed_frequency_sensor_4 (IExhaust_fan_speed_frequency_sensor_4 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IExhaust_fan_speed_frequency_sensor_4> getUsesOptionalsExhaust_fan_speed_frequency_sensor_4 (){
		Set<IExhaust_fan_speed_frequency_sensor_4> UsesOptionalsExhaust_fan_speed_frequency_sensor_4 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_speed_frequency_sensor_4) {
				UsesOptionalsExhaust_fan_speed_frequency_sensor_4.add((Exhaust_fan_speed_frequency_sensor_4)action);
			}
		});
		return UsesOptionalsExhaust_fan_speed_frequency_sensor_4;
	}


  public void addUsesOptionalsExhaust_fan_speed_percentage_sensor_4 (IExhaust_fan_speed_percentage_sensor_4 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IExhaust_fan_speed_percentage_sensor_4> getUsesOptionalsExhaust_fan_speed_percentage_sensor_4 (){
		Set<IExhaust_fan_speed_percentage_sensor_4> UsesOptionalsExhaust_fan_speed_percentage_sensor_4 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_speed_percentage_sensor_4) {
				UsesOptionalsExhaust_fan_speed_percentage_sensor_4.add((Exhaust_fan_speed_percentage_sensor_4)action);
			}
		});
		return UsesOptionalsExhaust_fan_speed_percentage_sensor_4;
	}


  public void addUsesOptionalsMixed_air_temperature_sensor (IMixed_air_temperature_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IMixed_air_temperature_sensor> getUsesOptionalsMixed_air_temperature_sensor (){
		Set<IMixed_air_temperature_sensor> UsesOptionalsMixed_air_temperature_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Mixed_air_temperature_sensor) {
				UsesOptionalsMixed_air_temperature_sensor.add((Mixed_air_temperature_sensor)action);
			}
		});
		return UsesOptionalsMixed_air_temperature_sensor;
	}


  public void addUsesOptionalsCompressor_speed_percentage_command (ICompressor_speed_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<ICompressor_speed_percentage_command> getUsesOptionalsCompressor_speed_percentage_command (){
		Set<ICompressor_speed_percentage_command> UsesOptionalsCompressor_speed_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Compressor_speed_percentage_command) {
				UsesOptionalsCompressor_speed_percentage_command.add((Compressor_speed_percentage_command)action);
			}
		});
		return UsesOptionalsCompressor_speed_percentage_command;
	}


  public void addUsesOptionalsCooling_percentage_command (ICooling_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<ICooling_percentage_command> getUsesOptionalsCooling_percentage_command (){
		Set<ICooling_percentage_command> UsesOptionalsCooling_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Cooling_percentage_command) {
				UsesOptionalsCooling_percentage_command.add((Cooling_percentage_command)action);
			}
		});
		return UsesOptionalsCooling_percentage_command;
	}


  public void addUsesOptionalsHeater_run_status (IHeater_run_status parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IHeater_run_status> getUsesOptionalsHeater_run_status (){
		Set<IHeater_run_status> UsesOptionalsHeater_run_status = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Heater_run_status) {
				UsesOptionalsHeater_run_status.add((Heater_run_status)action);
			}
		});
		return UsesOptionalsHeater_run_status;
	}


  public void addUsesOptionalsHeating_percentage_command (IHeating_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IHeating_percentage_command> getUsesOptionalsHeating_percentage_command (){
		Set<IHeating_percentage_command> UsesOptionalsHeating_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Heating_percentage_command) {
				UsesOptionalsHeating_percentage_command.add((Heating_percentage_command)action);
			}
		});
		return UsesOptionalsHeating_percentage_command;
	}


  public void addUsesOptionalsDischarge_air_temperature_sensor (IDischarge_air_temperature_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IDischarge_air_temperature_sensor> getUsesOptionalsDischarge_air_temperature_sensor (){
		Set<IDischarge_air_temperature_sensor> UsesOptionalsDischarge_air_temperature_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Discharge_air_temperature_sensor) {
				UsesOptionalsDischarge_air_temperature_sensor.add((Discharge_air_temperature_sensor)action);
			}
		});
		return UsesOptionalsDischarge_air_temperature_sensor;
	}


  public void addUsesOptionalsDischarge_air_flowrate_capacity (IDischarge_air_flowrate_capacity parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IDischarge_air_flowrate_capacity> getUsesOptionalsDischarge_air_flowrate_capacity (){
		Set<IDischarge_air_flowrate_capacity> UsesOptionalsDischarge_air_flowrate_capacity = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Discharge_air_flowrate_capacity) {
				UsesOptionalsDischarge_air_flowrate_capacity.add((Discharge_air_flowrate_capacity)action);
			}
		});
		return UsesOptionalsDischarge_air_flowrate_capacity;
	}


  public void addUsesOptionalsDischarge_fan_current_sensor (IDischarge_fan_current_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IDischarge_fan_current_sensor> getUsesOptionalsDischarge_fan_current_sensor (){
		Set<IDischarge_fan_current_sensor> UsesOptionalsDischarge_fan_current_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Discharge_fan_current_sensor) {
				UsesOptionalsDischarge_fan_current_sensor.add((Discharge_fan_current_sensor)action);
			}
		});
		return UsesOptionalsDischarge_fan_current_sensor;
	}


  public void addUsesOptionalsDischarge_fan_power_capacity (IDischarge_fan_power_capacity parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IDischarge_fan_power_capacity> getUsesOptionalsDischarge_fan_power_capacity (){
		Set<IDischarge_fan_power_capacity> UsesOptionalsDischarge_fan_power_capacity = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Discharge_fan_power_capacity) {
				UsesOptionalsDischarge_fan_power_capacity.add((Discharge_fan_power_capacity)action);
			}
		});
		return UsesOptionalsDischarge_fan_power_capacity;
	}


  public void addUsesOptionalsDischarge_fan_power_sensor (IDischarge_fan_power_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IDischarge_fan_power_sensor> getUsesOptionalsDischarge_fan_power_sensor (){
		Set<IDischarge_fan_power_sensor> UsesOptionalsDischarge_fan_power_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Discharge_fan_power_sensor) {
				UsesOptionalsDischarge_fan_power_sensor.add((Discharge_fan_power_sensor)action);
			}
		});
		return UsesOptionalsDischarge_fan_power_sensor;
	}


  public void addUsesOptionalsOutside_air_damper_percentage_sensor (IOutside_air_damper_percentage_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IOutside_air_damper_percentage_sensor> getUsesOptionalsOutside_air_damper_percentage_sensor (){
		Set<IOutside_air_damper_percentage_sensor> UsesOptionalsOutside_air_damper_percentage_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Outside_air_damper_percentage_sensor) {
				UsesOptionalsOutside_air_damper_percentage_sensor.add((Outside_air_damper_percentage_sensor)action);
			}
		});
		return UsesOptionalsOutside_air_damper_percentage_sensor;
	}


  public void addUsesOptionalsReturn_air_temperature_sensor (IReturn_air_temperature_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IReturn_air_temperature_sensor> getUsesOptionalsReturn_air_temperature_sensor (){
		Set<IReturn_air_temperature_sensor> UsesOptionalsReturn_air_temperature_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Return_air_temperature_sensor) {
				UsesOptionalsReturn_air_temperature_sensor.add((Return_air_temperature_sensor)action);
			}
		});
		return UsesOptionalsReturn_air_temperature_sensor;
	}


  public void addUsesOptionalsZone_air_relative_humidity_sensor (IZone_air_relative_humidity_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IZone_air_relative_humidity_sensor> getUsesOptionalsZone_air_relative_humidity_sensor (){
		Set<IZone_air_relative_humidity_sensor> UsesOptionalsZone_air_relative_humidity_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Zone_air_relative_humidity_sensor) {
				UsesOptionalsZone_air_relative_humidity_sensor.add((Zone_air_relative_humidity_sensor)action);
			}
		});
		return UsesOptionalsZone_air_relative_humidity_sensor;
	}


  public void addUsesOptionalsDischarge_fan_speed_frequency_sensor (IDischarge_fan_speed_frequency_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IDischarge_fan_speed_frequency_sensor> getUsesOptionalsDischarge_fan_speed_frequency_sensor (){
		Set<IDischarge_fan_speed_frequency_sensor> UsesOptionalsDischarge_fan_speed_frequency_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Discharge_fan_speed_frequency_sensor) {
				UsesOptionalsDischarge_fan_speed_frequency_sensor.add((Discharge_fan_speed_frequency_sensor)action);
			}
		});
		return UsesOptionalsDischarge_fan_speed_frequency_sensor;
	}


  public void addUsesOptionalsDischarge_fan_speed_percentage_sensor (IDischarge_fan_speed_percentage_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IDischarge_fan_speed_percentage_sensor> getUsesOptionalsDischarge_fan_speed_percentage_sensor (){
		Set<IDischarge_fan_speed_percentage_sensor> UsesOptionalsDischarge_fan_speed_percentage_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Discharge_fan_speed_percentage_sensor) {
				UsesOptionalsDischarge_fan_speed_percentage_sensor.add((Discharge_fan_speed_percentage_sensor)action);
			}
		});
		return UsesOptionalsDischarge_fan_speed_percentage_sensor;
	}


  public void addUsesOptionalsCooling_request_count (ICooling_request_count parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<ICooling_request_count> getUsesOptionalsCooling_request_count (){
		Set<ICooling_request_count> UsesOptionalsCooling_request_count = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Cooling_request_count) {
				UsesOptionalsCooling_request_count.add((Cooling_request_count)action);
			}
		});
		return UsesOptionalsCooling_request_count;
	}


  public void addUsesOptionalsZone_air_deadband_temperature_setpoint (IZone_air_deadband_temperature_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IZone_air_deadband_temperature_setpoint> getUsesOptionalsZone_air_deadband_temperature_setpoint (){
		Set<IZone_air_deadband_temperature_setpoint> UsesOptionalsZone_air_deadband_temperature_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Zone_air_deadband_temperature_setpoint) {
				UsesOptionalsZone_air_deadband_temperature_setpoint.add((Zone_air_deadband_temperature_setpoint)action);
			}
		});
		return UsesOptionalsZone_air_deadband_temperature_setpoint;
	}


  public void addUsesOptionalsDischarge_air_relative_humidity_sensor (IDischarge_air_relative_humidity_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IDischarge_air_relative_humidity_sensor> getUsesOptionalsDischarge_air_relative_humidity_sensor (){
		Set<IDischarge_air_relative_humidity_sensor> UsesOptionalsDischarge_air_relative_humidity_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Discharge_air_relative_humidity_sensor) {
				UsesOptionalsDischarge_air_relative_humidity_sensor.add((Discharge_air_relative_humidity_sensor)action);
			}
		});
		return UsesOptionalsDischarge_air_relative_humidity_sensor;
	}


  public void addUsesOptionalsLeaving_heating_coil_temperature_sensor (ILeaving_heating_coil_temperature_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<ILeaving_heating_coil_temperature_sensor> getUsesOptionalsLeaving_heating_coil_temperature_sensor (){
		Set<ILeaving_heating_coil_temperature_sensor> UsesOptionalsLeaving_heating_coil_temperature_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Leaving_heating_coil_temperature_sensor) {
				UsesOptionalsLeaving_heating_coil_temperature_sensor.add((Leaving_heating_coil_temperature_sensor)action);
			}
		});
		return UsesOptionalsLeaving_heating_coil_temperature_sensor;
	}

	public static Set<IMau_sfss_sfvsc_hwsc> getAllMau_sfss_sfvsc_hwscsObjectsCreated(){
		Set<IMau_sfss_sfvsc_hwsc> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Mau_sfss_sfvsc_hwsc")).subjects().stream()
		.map(mapper->(IMau_sfss_sfvsc_hwsc)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}