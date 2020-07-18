package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.fields.IFlowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISpray_pump_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.Spray_pump_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_power_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_fan_power_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_supply_water_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Chilled_supply_water_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_air_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_water_bypass_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Chilled_water_bypass_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_request_count;
import www.google.com.digitalbuildings._0_0_1.fields.Heating_request_count;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_air_heating_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_air_heating_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IRun_command;
import www.google.com.digitalbuildings._0_0_1.fields.Run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_water_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Heating_water_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.IPowerfactor_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Powerfactor_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IBuilding_air_static_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Building_air_static_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_speed_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_speed_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ICondenser_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Condenser_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_speed_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_fan_speed_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IDifferential_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Differential_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_speed_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IEvaporator_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Evaporator_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IPressurization_request_count;
import www.google.com.digitalbuildings._0_0_1.fields.Pressurization_request_count;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_deadband_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_air_deadband_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_relative_humidity_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_air_relative_humidity_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.Compressor_run_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_command_4;
import www.google.com.digitalbuildings._0_0_1.fields.Compressor_run_command_4;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_command_3;
import www.google.com.digitalbuildings._0_0_1.fields.Compressor_run_command_3;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.Compressor_run_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_air_flowrate_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_air_flowrate_capacity;
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
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_water_bypass_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Chilled_water_bypass_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_status_3;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_run_status_3;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_status_2;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_run_status_2;
import www.google.com.digitalbuildings._0_0_1.fields.ILeaving_heating_coil_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Leaving_heating_coil_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IFlowrate_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Flowrate_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Return_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_speed_percentage_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_speed_percentage_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_sensor_4;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_speed_percentage_sensor_4;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_sensor_3;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_speed_percentage_sensor_3;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IFlowrate_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.Flowrate_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.ICooling_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Cooling_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_isolation_valve_status;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_water_isolation_valve_status;
import www.google.com.digitalbuildings._0_0_1.fields.IFlowrate_requirement;
import www.google.com.digitalbuildings._0_0_1.fields.Flowrate_requirement;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_speed_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Compressor_speed_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_return_water_isolation_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Chilled_return_water_isolation_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IHeater_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.Heater_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IDifferential_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Differential_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_heating_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_air_heating_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_cooling_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_air_cooling_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_return_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Process_return_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_status_4;
import www.google.com.digitalbuildings._0_0_1.fields.Compressor_run_status_4;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_status_3;
import www.google.com.digitalbuildings._0_0_1.fields.Compressor_run_status_3;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_current_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_current_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_command_4;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_run_command_4;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_current_sensor_3;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_current_sensor_3;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_command_3;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_run_command_3;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_current_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_current_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_status_2;
import www.google.com.digitalbuildings._0_0_1.fields.Compressor_run_status_2;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_run_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_status_1;
import www.google.com.digitalbuildings._0_0_1.fields.Compressor_run_status_1;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_run_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_current_sensor_4;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_current_sensor_4;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IHeat_exchange_supply_water_isolation_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Heat_exchange_supply_water_isolation_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICooling_thermal_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.Cooling_thermal_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_flowrate_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_air_flowrate_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_isolation_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Return_water_isolation_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_isolation_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Return_water_isolation_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_current_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_current_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICooling_request_count;
import www.google.com.digitalbuildings._0_0_1.fields.Cooling_request_count;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_command_4;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_speed_percentage_command_4;
import www.google.com.digitalbuildings._0_0_1.fields.IVentilation_outside_air_flowrate_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Ventilation_outside_air_flowrate_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_speed_percentage_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_flowrate_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_air_flowrate_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_speed_percentage_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_command_3;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_speed_percentage_command_3;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_supply_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Process_supply_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICurrent_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Current_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_damper_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Outside_air_damper_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_run_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_run_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.IEconomizer_mode;
import www.google.com.digitalbuildings._0_0_1.fields.Economizer_mode;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_run_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_run_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.IEfficiency_percentage_specification;
import www.google.com.digitalbuildings._0_0_1.fields.Efficiency_percentage_specification;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_current_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_current_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_current_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_current_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IRefrigerant_evaporator_saturation_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Refrigerant_evaporator_saturation_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IHeat_exchange_supply_water_isolation_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Heat_exchange_supply_water_isolation_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_supply_water_isolation_valve_status;
import www.google.com.digitalbuildings._0_0_1.fields.Chilled_supply_water_isolation_valve_status;
import www.google.com.digitalbuildings._0_0_1.fields.ISpeed_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Speed_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_speed_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_speed_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_cooling_thermal_power_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Process_cooling_thermal_power_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISpray_pump_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.Spray_pump_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Outside_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_water_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_speed_frequency_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_fan_speed_frequency_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_run_status_2;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_run_status_2;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_run_status_1;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_run_status_1;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_water_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Heating_water_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_flowrate_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_air_flowrate_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IVentilation_outside_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Ventilation_outside_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_speed_frequency_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_speed_frequency_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_speed_frequency_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_speed_frequency_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_current_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_fan_current_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_co2_concentration_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_air_co2_concentration_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_water_differential_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Process_water_differential_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_supply_water_isolation_valve_command;
import www.google.com.digitalbuildings._0_0_1.fields.Chilled_supply_water_isolation_valve_command;
import www.google.com.digitalbuildings._0_0_1.fields.IPower_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.Power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_static_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_air_static_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_isolation_valve_command;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_water_isolation_valve_command;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_speed_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Compressor_speed_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_speed_frequency_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Compressor_speed_frequency_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Outside_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_speed_percentage_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_speed_percentage_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_speed_percentage_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_speed_percentage_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_water_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Chilled_water_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_frequency_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_speed_frequency_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_frequency_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_speed_frequency_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_frequency_sensor_4;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_speed_frequency_sensor_4;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_frequency_sensor_3;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_speed_frequency_sensor_3;
import www.google.com.digitalbuildings._0_0_1.fields.ILeaving_cooling_coil_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Leaving_cooling_coil_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_current_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_current_sensor;
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
import www.google.com.digitalbuildings._0_0_1.fields.IBypass_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Bypass_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_static_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_air_static_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IRefrigerant_condenser_saturation_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Refrigerant_condenser_saturation_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.Compressor_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_power_sensor_3;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_power_sensor_3;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_water_differential_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Process_water_differential_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_power_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_power_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_power_sensor_4;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_power_sensor_4;
import www.google.com.digitalbuildings._0_0_1.fields.IHeater_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.Heater_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_isolation_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_water_isolation_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_isolation_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_water_isolation_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.Compressor_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_flowrate_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Outside_air_flowrate_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IBoost_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.Boost_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_power_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_power_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.ICondensing_return_water_isolation_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Condensing_return_water_isolation_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IMixed_air_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Mixed_air_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_supply_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Chilled_supply_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IRun_status;
import www.google.com.digitalbuildings._0_0_1.fields.Run_status;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISpeed_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Speed_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IBuilding_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Building_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_power_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_power_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_isolation_valve_status;
import www.google.com.digitalbuildings._0_0_1.fields.Return_water_isolation_valve_status;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_power_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_power_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_co2_concentration_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_air_co2_concentration_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_power_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_power_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.ICondensing_return_water_isolation_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Condensing_return_water_isolation_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_air_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_air_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_speed_frequency_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_speed_frequency_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Heating_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_return_water_isolation_valve_command;
import www.google.com.digitalbuildings._0_0_1.fields.Chilled_return_water_isolation_valve_command;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_isolation_valve_command;
import www.google.com.digitalbuildings._0_0_1.fields.Return_water_isolation_valve_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_speed_percentage_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_speed_percentage_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.IHeater_run_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.Heater_run_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_speed_percentage_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_speed_percentage_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.ICondensing_supply_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Condensing_supply_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IMixed_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Mixed_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IReversing_valve_command;
import www.google.com.digitalbuildings._0_0_1.fields.Reversing_valve_command;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_input_thermal_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.Heating_input_thermal_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_return_water_isolation_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Chilled_return_water_isolation_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISpeed_frequency_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Speed_frequency_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IHeater_run_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.Heater_run_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.IHeater_run_command_3;
import www.google.com.digitalbuildings._0_0_1.fields.Heater_run_command_3;
import www.google.com.digitalbuildings._0_0_1.fields.IBoost_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.Boost_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.IPower_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Power_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_return_water_isolation_valve_status;
import www.google.com.digitalbuildings._0_0_1.fields.Chilled_return_water_isolation_valve_status;
import www.google.com.digitalbuildings._0_0_1.fields.IBypass_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Bypass_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_return_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Chilled_return_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_air_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_thermal_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.Heating_thermal_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_fan_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Outside_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_speed_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_fan_speed_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Return_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_power_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_power_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICondensing_return_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Condensing_return_water_temperature_sensor;

/**
* Class Fan_ss_ztm 
* Fan with zone temperature monitoring.
*/
@SuppressWarnings("serial")
public class Fan_ss_ztm extends www.google.com.digitalbuildings._0_0_1.hvac.Ztm implements IFan_ss_ztm{

	IRI newInstance;
	public Fan_ss_ztm(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Fan_ss_ztm"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesRun_command (IRun_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IRun_command> getUsesRun_command (){
		Set<IRun_command> UsesRun_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Run_command) {
				UsesRun_command.add((Run_command)action);
			}
		});
		return UsesRun_command;
	}


  public void addUsesRun_status (IRun_status parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IRun_status> getUsesRun_status (){
		Set<IRun_status> UsesRun_status = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Run_status) {
				UsesRun_status.add((Run_status)action);
			}
		});
		return UsesRun_status;
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


  public void addUsesSupply_water_temperature_sensor (ISupply_water_temperature_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_water_temperature_sensor> getUsesSupply_water_temperature_sensor (){
		Set<ISupply_water_temperature_sensor> UsesSupply_water_temperature_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_water_temperature_sensor) {
				UsesSupply_water_temperature_sensor.add((Supply_water_temperature_sensor)action);
			}
		});
		return UsesSupply_water_temperature_sensor;
	}


  public void addUsesSupply_water_temperature_setpoint (ISupply_water_temperature_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_water_temperature_setpoint> getUsesSupply_water_temperature_setpoint (){
		Set<ISupply_water_temperature_setpoint> UsesSupply_water_temperature_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_water_temperature_setpoint) {
				UsesSupply_water_temperature_setpoint.add((Supply_water_temperature_setpoint)action);
			}
		});
		return UsesSupply_water_temperature_setpoint;
	}


  public void addUsesReturn_water_isolation_valve_command (IReturn_water_isolation_valve_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IReturn_water_isolation_valve_command> getUsesReturn_water_isolation_valve_command (){
		Set<IReturn_water_isolation_valve_command> UsesReturn_water_isolation_valve_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Return_water_isolation_valve_command) {
				UsesReturn_water_isolation_valve_command.add((Return_water_isolation_valve_command)action);
			}
		});
		return UsesReturn_water_isolation_valve_command;
	}


  public void addUsesReturn_water_isolation_valve_status (IReturn_water_isolation_valve_status parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IReturn_water_isolation_valve_status> getUsesReturn_water_isolation_valve_status (){
		Set<IReturn_water_isolation_valve_status> UsesReturn_water_isolation_valve_status = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Return_water_isolation_valve_status) {
				UsesReturn_water_isolation_valve_status.add((Return_water_isolation_valve_status)action);
			}
		});
		return UsesReturn_water_isolation_valve_status;
	}


  public void addUsesSupply_water_isolation_valve_command (ISupply_water_isolation_valve_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_water_isolation_valve_command> getUsesSupply_water_isolation_valve_command (){
		Set<ISupply_water_isolation_valve_command> UsesSupply_water_isolation_valve_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_water_isolation_valve_command) {
				UsesSupply_water_isolation_valve_command.add((Supply_water_isolation_valve_command)action);
			}
		});
		return UsesSupply_water_isolation_valve_command;
	}


  public void addUsesSupply_water_isolation_valve_status (ISupply_water_isolation_valve_status parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_water_isolation_valve_status> getUsesSupply_water_isolation_valve_status (){
		Set<ISupply_water_isolation_valve_status> UsesSupply_water_isolation_valve_status = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_water_isolation_valve_status) {
				UsesSupply_water_isolation_valve_status.add((Supply_water_isolation_valve_status)action);
			}
		});
		return UsesSupply_water_isolation_valve_status;
	}


  public void addUsesChilled_supply_water_temperature_sensor (IChilled_supply_water_temperature_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IChilled_supply_water_temperature_sensor> getUsesChilled_supply_water_temperature_sensor (){
		Set<IChilled_supply_water_temperature_sensor> UsesChilled_supply_water_temperature_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Chilled_supply_water_temperature_sensor) {
				UsesChilled_supply_water_temperature_sensor.add((Chilled_supply_water_temperature_sensor)action);
			}
		});
		return UsesChilled_supply_water_temperature_sensor;
	}


  public void addUsesChilled_supply_water_temperature_setpoint (IChilled_supply_water_temperature_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IChilled_supply_water_temperature_setpoint> getUsesChilled_supply_water_temperature_setpoint (){
		Set<IChilled_supply_water_temperature_setpoint> UsesChilled_supply_water_temperature_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Chilled_supply_water_temperature_setpoint) {
				UsesChilled_supply_water_temperature_setpoint.add((Chilled_supply_water_temperature_setpoint)action);
			}
		});
		return UsesChilled_supply_water_temperature_setpoint;
	}


  public void addUsesChilled_return_water_isolation_valve_percentage_command (IChilled_return_water_isolation_valve_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IChilled_return_water_isolation_valve_percentage_command> getUsesChilled_return_water_isolation_valve_percentage_command (){
		Set<IChilled_return_water_isolation_valve_percentage_command> UsesChilled_return_water_isolation_valve_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Chilled_return_water_isolation_valve_percentage_command) {
				UsesChilled_return_water_isolation_valve_percentage_command.add((Chilled_return_water_isolation_valve_percentage_command)action);
			}
		});
		return UsesChilled_return_water_isolation_valve_percentage_command;
	}


  public void addUsesChilled_return_water_isolation_valve_percentage_sensor (IChilled_return_water_isolation_valve_percentage_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IChilled_return_water_isolation_valve_percentage_sensor> getUsesChilled_return_water_isolation_valve_percentage_sensor (){
		Set<IChilled_return_water_isolation_valve_percentage_sensor> UsesChilled_return_water_isolation_valve_percentage_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Chilled_return_water_isolation_valve_percentage_sensor) {
				UsesChilled_return_water_isolation_valve_percentage_sensor.add((Chilled_return_water_isolation_valve_percentage_sensor)action);
			}
		});
		return UsesChilled_return_water_isolation_valve_percentage_sensor;
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


  public void addUsesCondenser_pressure_sensor (ICondenser_pressure_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ICondenser_pressure_sensor> getUsesCondenser_pressure_sensor (){
		Set<ICondenser_pressure_sensor> UsesCondenser_pressure_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Condenser_pressure_sensor) {
				UsesCondenser_pressure_sensor.add((Condenser_pressure_sensor)action);
			}
		});
		return UsesCondenser_pressure_sensor;
	}


  public void addUsesDifferential_pressure_sensor (IDifferential_pressure_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IDifferential_pressure_sensor> getUsesDifferential_pressure_sensor (){
		Set<IDifferential_pressure_sensor> UsesDifferential_pressure_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Differential_pressure_sensor) {
				UsesDifferential_pressure_sensor.add((Differential_pressure_sensor)action);
			}
		});
		return UsesDifferential_pressure_sensor;
	}


  public void addUsesEvaporator_pressure_sensor (IEvaporator_pressure_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IEvaporator_pressure_sensor> getUsesEvaporator_pressure_sensor (){
		Set<IEvaporator_pressure_sensor> UsesEvaporator_pressure_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Evaporator_pressure_sensor) {
				UsesEvaporator_pressure_sensor.add((Evaporator_pressure_sensor)action);
			}
		});
		return UsesEvaporator_pressure_sensor;
	}


  public void addUsesChilled_return_water_isolation_valve_command (IChilled_return_water_isolation_valve_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IChilled_return_water_isolation_valve_command> getUsesChilled_return_water_isolation_valve_command (){
		Set<IChilled_return_water_isolation_valve_command> UsesChilled_return_water_isolation_valve_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Chilled_return_water_isolation_valve_command) {
				UsesChilled_return_water_isolation_valve_command.add((Chilled_return_water_isolation_valve_command)action);
			}
		});
		return UsesChilled_return_water_isolation_valve_command;
	}


  public void addUsesChilled_return_water_isolation_valve_status (IChilled_return_water_isolation_valve_status parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IChilled_return_water_isolation_valve_status> getUsesChilled_return_water_isolation_valve_status (){
		Set<IChilled_return_water_isolation_valve_status> UsesChilled_return_water_isolation_valve_status = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Chilled_return_water_isolation_valve_status) {
				UsesChilled_return_water_isolation_valve_status.add((Chilled_return_water_isolation_valve_status)action);
			}
		});
		return UsesChilled_return_water_isolation_valve_status;
	}


  public void addUsesCondensing_return_water_isolation_valve_percentage_command (ICondensing_return_water_isolation_valve_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ICondensing_return_water_isolation_valve_percentage_command> getUsesCondensing_return_water_isolation_valve_percentage_command (){
		Set<ICondensing_return_water_isolation_valve_percentage_command> UsesCondensing_return_water_isolation_valve_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Condensing_return_water_isolation_valve_percentage_command) {
				UsesCondensing_return_water_isolation_valve_percentage_command.add((Condensing_return_water_isolation_valve_percentage_command)action);
			}
		});
		return UsesCondensing_return_water_isolation_valve_percentage_command;
	}


  public void addUsesCondensing_return_water_isolation_valve_percentage_sensor (ICondensing_return_water_isolation_valve_percentage_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ICondensing_return_water_isolation_valve_percentage_sensor> getUsesCondensing_return_water_isolation_valve_percentage_sensor (){
		Set<ICondensing_return_water_isolation_valve_percentage_sensor> UsesCondensing_return_water_isolation_valve_percentage_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Condensing_return_water_isolation_valve_percentage_sensor) {
				UsesCondensing_return_water_isolation_valve_percentage_sensor.add((Condensing_return_water_isolation_valve_percentage_sensor)action);
			}
		});
		return UsesCondensing_return_water_isolation_valve_percentage_sensor;
	}


  public void addUsesRefrigerant_condenser_saturation_temperature_sensor (IRefrigerant_condenser_saturation_temperature_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IRefrigerant_condenser_saturation_temperature_sensor> getUsesRefrigerant_condenser_saturation_temperature_sensor (){
		Set<IRefrigerant_condenser_saturation_temperature_sensor> UsesRefrigerant_condenser_saturation_temperature_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Refrigerant_condenser_saturation_temperature_sensor) {
				UsesRefrigerant_condenser_saturation_temperature_sensor.add((Refrigerant_condenser_saturation_temperature_sensor)action);
			}
		});
		return UsesRefrigerant_condenser_saturation_temperature_sensor;
	}


  public void addUsesRefrigerant_evaporator_saturation_temperature_sensor (IRefrigerant_evaporator_saturation_temperature_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IRefrigerant_evaporator_saturation_temperature_sensor> getUsesRefrigerant_evaporator_saturation_temperature_sensor (){
		Set<IRefrigerant_evaporator_saturation_temperature_sensor> UsesRefrigerant_evaporator_saturation_temperature_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Refrigerant_evaporator_saturation_temperature_sensor) {
				UsesRefrigerant_evaporator_saturation_temperature_sensor.add((Refrigerant_evaporator_saturation_temperature_sensor)action);
			}
		});
		return UsesRefrigerant_evaporator_saturation_temperature_sensor;
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


  public void addUsesChilled_supply_water_isolation_valve_command (IChilled_supply_water_isolation_valve_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IChilled_supply_water_isolation_valve_command> getUsesChilled_supply_water_isolation_valve_command (){
		Set<IChilled_supply_water_isolation_valve_command> UsesChilled_supply_water_isolation_valve_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Chilled_supply_water_isolation_valve_command) {
				UsesChilled_supply_water_isolation_valve_command.add((Chilled_supply_water_isolation_valve_command)action);
			}
		});
		return UsesChilled_supply_water_isolation_valve_command;
	}


  public void addUsesChilled_supply_water_isolation_valve_status (IChilled_supply_water_isolation_valve_status parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IChilled_supply_water_isolation_valve_status> getUsesChilled_supply_water_isolation_valve_status (){
		Set<IChilled_supply_water_isolation_valve_status> UsesChilled_supply_water_isolation_valve_status = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Chilled_supply_water_isolation_valve_status) {
				UsesChilled_supply_water_isolation_valve_status.add((Chilled_supply_water_isolation_valve_status)action);
			}
		});
		return UsesChilled_supply_water_isolation_valve_status;
	}


  public void addUsesChilled_water_bypass_valve_percentage_command (IChilled_water_bypass_valve_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IChilled_water_bypass_valve_percentage_command> getUsesChilled_water_bypass_valve_percentage_command (){
		Set<IChilled_water_bypass_valve_percentage_command> UsesChilled_water_bypass_valve_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Chilled_water_bypass_valve_percentage_command) {
				UsesChilled_water_bypass_valve_percentage_command.add((Chilled_water_bypass_valve_percentage_command)action);
			}
		});
		return UsesChilled_water_bypass_valve_percentage_command;
	}


  public void addUsesChilled_water_bypass_valve_percentage_sensor (IChilled_water_bypass_valve_percentage_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IChilled_water_bypass_valve_percentage_sensor> getUsesChilled_water_bypass_valve_percentage_sensor (){
		Set<IChilled_water_bypass_valve_percentage_sensor> UsesChilled_water_bypass_valve_percentage_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Chilled_water_bypass_valve_percentage_sensor) {
				UsesChilled_water_bypass_valve_percentage_sensor.add((Chilled_water_bypass_valve_percentage_sensor)action);
			}
		});
		return UsesChilled_water_bypass_valve_percentage_sensor;
	}


  public void addUsesCondensing_return_water_temperature_sensor (ICondensing_return_water_temperature_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ICondensing_return_water_temperature_sensor> getUsesCondensing_return_water_temperature_sensor (){
		Set<ICondensing_return_water_temperature_sensor> UsesCondensing_return_water_temperature_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Condensing_return_water_temperature_sensor) {
				UsesCondensing_return_water_temperature_sensor.add((Condensing_return_water_temperature_sensor)action);
			}
		});
		return UsesCondensing_return_water_temperature_sensor;
	}


  public void addUsesCondensing_supply_water_temperature_sensor (ICondensing_supply_water_temperature_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ICondensing_supply_water_temperature_sensor> getUsesCondensing_supply_water_temperature_sensor (){
		Set<ICondensing_supply_water_temperature_sensor> UsesCondensing_supply_water_temperature_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Condensing_supply_water_temperature_sensor) {
				UsesCondensing_supply_water_temperature_sensor.add((Condensing_supply_water_temperature_sensor)action);
			}
		});
		return UsesCondensing_supply_water_temperature_sensor;
	}


  public void addUsesSpray_pump_run_command (ISpray_pump_run_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISpray_pump_run_command> getUsesSpray_pump_run_command (){
		Set<ISpray_pump_run_command> UsesSpray_pump_run_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Spray_pump_run_command) {
				UsesSpray_pump_run_command.add((Spray_pump_run_command)action);
			}
		});
		return UsesSpray_pump_run_command;
	}


  public void addUsesSpray_pump_run_status (ISpray_pump_run_status parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISpray_pump_run_status> getUsesSpray_pump_run_status (){
		Set<ISpray_pump_run_status> UsesSpray_pump_run_status = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Spray_pump_run_status) {
				UsesSpray_pump_run_status.add((Spray_pump_run_status)action);
			}
		});
		return UsesSpray_pump_run_status;
	}


  public void addUsesReturn_water_isolation_valve_percentage_command (IReturn_water_isolation_valve_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IReturn_water_isolation_valve_percentage_command> getUsesReturn_water_isolation_valve_percentage_command (){
		Set<IReturn_water_isolation_valve_percentage_command> UsesReturn_water_isolation_valve_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Return_water_isolation_valve_percentage_command) {
				UsesReturn_water_isolation_valve_percentage_command.add((Return_water_isolation_valve_percentage_command)action);
			}
		});
		return UsesReturn_water_isolation_valve_percentage_command;
	}


  public void addUsesReturn_water_isolation_valve_percentage_sensor (IReturn_water_isolation_valve_percentage_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IReturn_water_isolation_valve_percentage_sensor> getUsesReturn_water_isolation_valve_percentage_sensor (){
		Set<IReturn_water_isolation_valve_percentage_sensor> UsesReturn_water_isolation_valve_percentage_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Return_water_isolation_valve_percentage_sensor) {
				UsesReturn_water_isolation_valve_percentage_sensor.add((Return_water_isolation_valve_percentage_sensor)action);
			}
		});
		return UsesReturn_water_isolation_valve_percentage_sensor;
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


  public void addUsesDifferential_pressure_setpoint (IDifferential_pressure_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IDifferential_pressure_setpoint> getUsesDifferential_pressure_setpoint (){
		Set<IDifferential_pressure_setpoint> UsesDifferential_pressure_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Differential_pressure_setpoint) {
				UsesDifferential_pressure_setpoint.add((Differential_pressure_setpoint)action);
			}
		});
		return UsesDifferential_pressure_setpoint;
	}


  public void addUsesProcess_water_differential_pressure_sensor (IProcess_water_differential_pressure_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IProcess_water_differential_pressure_sensor> getUsesProcess_water_differential_pressure_sensor (){
		Set<IProcess_water_differential_pressure_sensor> UsesProcess_water_differential_pressure_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Process_water_differential_pressure_sensor) {
				UsesProcess_water_differential_pressure_sensor.add((Process_water_differential_pressure_sensor)action);
			}
		});
		return UsesProcess_water_differential_pressure_sensor;
	}


  public void addUsesProcess_water_differential_pressure_setpoint (IProcess_water_differential_pressure_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IProcess_water_differential_pressure_setpoint> getUsesProcess_water_differential_pressure_setpoint (){
		Set<IProcess_water_differential_pressure_setpoint> UsesProcess_water_differential_pressure_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Process_water_differential_pressure_setpoint) {
				UsesProcess_water_differential_pressure_setpoint.add((Process_water_differential_pressure_setpoint)action);
			}
		});
		return UsesProcess_water_differential_pressure_setpoint;
	}


  public void addUsesProcess_return_water_temperature_sensor (IProcess_return_water_temperature_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IProcess_return_water_temperature_sensor> getUsesProcess_return_water_temperature_sensor (){
		Set<IProcess_return_water_temperature_sensor> UsesProcess_return_water_temperature_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Process_return_water_temperature_sensor) {
				UsesProcess_return_water_temperature_sensor.add((Process_return_water_temperature_sensor)action);
			}
		});
		return UsesProcess_return_water_temperature_sensor;
	}


  public void addUsesProcess_supply_water_temperature_sensor (IProcess_supply_water_temperature_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IProcess_supply_water_temperature_sensor> getUsesProcess_supply_water_temperature_sensor (){
		Set<IProcess_supply_water_temperature_sensor> UsesProcess_supply_water_temperature_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Process_supply_water_temperature_sensor) {
				UsesProcess_supply_water_temperature_sensor.add((Process_supply_water_temperature_sensor)action);
			}
		});
		return UsesProcess_supply_water_temperature_sensor;
	}


  public void addUsesHeat_exchange_supply_water_isolation_valve_percentage_command (IHeat_exchange_supply_water_isolation_valve_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IHeat_exchange_supply_water_isolation_valve_percentage_command> getUsesHeat_exchange_supply_water_isolation_valve_percentage_command (){
		Set<IHeat_exchange_supply_water_isolation_valve_percentage_command> UsesHeat_exchange_supply_water_isolation_valve_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Heat_exchange_supply_water_isolation_valve_percentage_command) {
				UsesHeat_exchange_supply_water_isolation_valve_percentage_command.add((Heat_exchange_supply_water_isolation_valve_percentage_command)action);
			}
		});
		return UsesHeat_exchange_supply_water_isolation_valve_percentage_command;
	}


  public void addUsesHeat_exchange_supply_water_isolation_valve_percentage_sensor (IHeat_exchange_supply_water_isolation_valve_percentage_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IHeat_exchange_supply_water_isolation_valve_percentage_sensor> getUsesHeat_exchange_supply_water_isolation_valve_percentage_sensor (){
		Set<IHeat_exchange_supply_water_isolation_valve_percentage_sensor> UsesHeat_exchange_supply_water_isolation_valve_percentage_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Heat_exchange_supply_water_isolation_valve_percentage_sensor) {
				UsesHeat_exchange_supply_water_isolation_valve_percentage_sensor.add((Heat_exchange_supply_water_isolation_valve_percentage_sensor)action);
			}
		});
		return UsesHeat_exchange_supply_water_isolation_valve_percentage_sensor;
	}


  public void addUsesFlowrate_sensor (IFlowrate_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IFlowrate_sensor> getUsesFlowrate_sensor (){
		Set<IFlowrate_sensor> UsesFlowrate_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Flowrate_sensor) {
				UsesFlowrate_sensor.add((Flowrate_sensor)action);
			}
		});
		return UsesFlowrate_sensor;
	}


  public void addUsesFlowrate_setpoint (IFlowrate_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IFlowrate_setpoint> getUsesFlowrate_setpoint (){
		Set<IFlowrate_setpoint> UsesFlowrate_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Flowrate_setpoint) {
				UsesFlowrate_setpoint.add((Flowrate_setpoint)action);
			}
		});
		return UsesFlowrate_setpoint;
	}


  public void addUsesSupply_water_isolation_valve_percentage_command (ISupply_water_isolation_valve_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_water_isolation_valve_percentage_command> getUsesSupply_water_isolation_valve_percentage_command (){
		Set<ISupply_water_isolation_valve_percentage_command> UsesSupply_water_isolation_valve_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_water_isolation_valve_percentage_command) {
				UsesSupply_water_isolation_valve_percentage_command.add((Supply_water_isolation_valve_percentage_command)action);
			}
		});
		return UsesSupply_water_isolation_valve_percentage_command;
	}


  public void addUsesSupply_water_isolation_valve_percentage_sensor (ISupply_water_isolation_valve_percentage_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_water_isolation_valve_percentage_sensor> getUsesSupply_water_isolation_valve_percentage_sensor (){
		Set<ISupply_water_isolation_valve_percentage_sensor> UsesSupply_water_isolation_valve_percentage_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_water_isolation_valve_percentage_sensor) {
				UsesSupply_water_isolation_valve_percentage_sensor.add((Supply_water_isolation_valve_percentage_sensor)action);
			}
		});
		return UsesSupply_water_isolation_valve_percentage_sensor;
	}


  public void addUsesSpeed_percentage_command (ISpeed_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISpeed_percentage_command> getUsesSpeed_percentage_command (){
		Set<ISpeed_percentage_command> UsesSpeed_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Speed_percentage_command) {
				UsesSpeed_percentage_command.add((Speed_percentage_command)action);
			}
		});
		return UsesSpeed_percentage_command;
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


  public void addUsesOptionalsCurrent_sensor (ICurrent_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<ICurrent_sensor> getUsesOptionalsCurrent_sensor (){
		Set<ICurrent_sensor> UsesOptionalsCurrent_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Current_sensor) {
				UsesOptionalsCurrent_sensor.add((Current_sensor)action);
			}
		});
		return UsesOptionalsCurrent_sensor;
	}


  public void addUsesOptionalsFlowrate_capacity (IFlowrate_capacity parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IFlowrate_capacity> getUsesOptionalsFlowrate_capacity (){
		Set<IFlowrate_capacity> UsesOptionalsFlowrate_capacity = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Flowrate_capacity) {
				UsesOptionalsFlowrate_capacity.add((Flowrate_capacity)action);
			}
		});
		return UsesOptionalsFlowrate_capacity;
	}


  public void addUsesOptionalsPower_capacity (IPower_capacity parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IPower_capacity> getUsesOptionalsPower_capacity (){
		Set<IPower_capacity> UsesOptionalsPower_capacity = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Power_capacity) {
				UsesOptionalsPower_capacity.add((Power_capacity)action);
			}
		});
		return UsesOptionalsPower_capacity;
	}


  public void addUsesOptionalsPower_sensor (IPower_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IPower_sensor> getUsesOptionalsPower_sensor (){
		Set<IPower_sensor> UsesOptionalsPower_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Power_sensor) {
				UsesOptionalsPower_sensor.add((Power_sensor)action);
			}
		});
		return UsesOptionalsPower_sensor;
	}


  public void addUsesOptionalsPowerfactor_sensor (IPowerfactor_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IPowerfactor_sensor> getUsesOptionalsPowerfactor_sensor (){
		Set<IPowerfactor_sensor> UsesOptionalsPowerfactor_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Powerfactor_sensor) {
				UsesOptionalsPowerfactor_sensor.add((Powerfactor_sensor)action);
			}
		});
		return UsesOptionalsPowerfactor_sensor;
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


  public void addUsesOptionalsEfficiency_percentage_specification (IEfficiency_percentage_specification parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IEfficiency_percentage_specification> getUsesOptionalsEfficiency_percentage_specification (){
		Set<IEfficiency_percentage_specification> UsesOptionalsEfficiency_percentage_specification = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Efficiency_percentage_specification) {
				UsesOptionalsEfficiency_percentage_specification.add((Efficiency_percentage_specification)action);
			}
		});
		return UsesOptionalsEfficiency_percentage_specification;
	}


  public void addUsesOptionalsFlowrate_requirement (IFlowrate_requirement parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IFlowrate_requirement> getUsesOptionalsFlowrate_requirement (){
		Set<IFlowrate_requirement> UsesOptionalsFlowrate_requirement = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Flowrate_requirement) {
				UsesOptionalsFlowrate_requirement.add((Flowrate_requirement)action);
			}
		});
		return UsesOptionalsFlowrate_requirement;
	}


  public void addUsesOptionalsHeating_input_thermal_power_capacity (IHeating_input_thermal_power_capacity parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IHeating_input_thermal_power_capacity> getUsesOptionalsHeating_input_thermal_power_capacity (){
		Set<IHeating_input_thermal_power_capacity> UsesOptionalsHeating_input_thermal_power_capacity = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Heating_input_thermal_power_capacity) {
				UsesOptionalsHeating_input_thermal_power_capacity.add((Heating_input_thermal_power_capacity)action);
			}
		});
		return UsesOptionalsHeating_input_thermal_power_capacity;
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


  public void addUsesOptionalsReturn_water_temperature_sensor (IReturn_water_temperature_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IReturn_water_temperature_sensor> getUsesOptionalsReturn_water_temperature_sensor (){
		Set<IReturn_water_temperature_sensor> UsesOptionalsReturn_water_temperature_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Return_water_temperature_sensor) {
				UsesOptionalsReturn_water_temperature_sensor.add((Return_water_temperature_sensor)action);
			}
		});
		return UsesOptionalsReturn_water_temperature_sensor;
	}


  public void addUsesOptionalsRun_command (IRun_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IRun_command> getUsesOptionalsRun_command (){
		Set<IRun_command> UsesOptionalsRun_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Run_command) {
				UsesOptionalsRun_command.add((Run_command)action);
			}
		});
		return UsesOptionalsRun_command;
	}


  public void addUsesOptionalsChilled_return_water_temperature_sensor (IChilled_return_water_temperature_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IChilled_return_water_temperature_sensor> getUsesOptionalsChilled_return_water_temperature_sensor (){
		Set<IChilled_return_water_temperature_sensor> UsesOptionalsChilled_return_water_temperature_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Chilled_return_water_temperature_sensor) {
				UsesOptionalsChilled_return_water_temperature_sensor.add((Chilled_return_water_temperature_sensor)action);
			}
		});
		return UsesOptionalsChilled_return_water_temperature_sensor;
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


  public void addUsesOptionalsCompressor_speed_percentage_sensor (ICompressor_speed_percentage_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<ICompressor_speed_percentage_sensor> getUsesOptionalsCompressor_speed_percentage_sensor (){
		Set<ICompressor_speed_percentage_sensor> UsesOptionalsCompressor_speed_percentage_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Compressor_speed_percentage_sensor) {
				UsesOptionalsCompressor_speed_percentage_sensor.add((Compressor_speed_percentage_sensor)action);
			}
		});
		return UsesOptionalsCompressor_speed_percentage_sensor;
	}


  public void addUsesOptionalsCompressor_speed_frequency_sensor (ICompressor_speed_frequency_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<ICompressor_speed_frequency_sensor> getUsesOptionalsCompressor_speed_frequency_sensor (){
		Set<ICompressor_speed_frequency_sensor> UsesOptionalsCompressor_speed_frequency_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Compressor_speed_frequency_sensor) {
				UsesOptionalsCompressor_speed_frequency_sensor.add((Compressor_speed_frequency_sensor)action);
			}
		});
		return UsesOptionalsCompressor_speed_frequency_sensor;
	}


  public void addUsesOptionalsSpeed_frequency_sensor (ISpeed_frequency_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<ISpeed_frequency_sensor> getUsesOptionalsSpeed_frequency_sensor (){
		Set<ISpeed_frequency_sensor> UsesOptionalsSpeed_frequency_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Speed_frequency_sensor) {
				UsesOptionalsSpeed_frequency_sensor.add((Speed_frequency_sensor)action);
			}
		});
		return UsesOptionalsSpeed_frequency_sensor;
	}


  public void addUsesOptionalsSpeed_percentage_sensor (ISpeed_percentage_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<ISpeed_percentage_sensor> getUsesOptionalsSpeed_percentage_sensor (){
		Set<ISpeed_percentage_sensor> UsesOptionalsSpeed_percentage_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Speed_percentage_sensor) {
				UsesOptionalsSpeed_percentage_sensor.add((Speed_percentage_sensor)action);
			}
		});
		return UsesOptionalsSpeed_percentage_sensor;
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


  public void addUsesOptionalsProcess_cooling_thermal_power_sensor (IProcess_cooling_thermal_power_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IProcess_cooling_thermal_power_sensor> getUsesOptionalsProcess_cooling_thermal_power_sensor (){
		Set<IProcess_cooling_thermal_power_sensor> UsesOptionalsProcess_cooling_thermal_power_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Process_cooling_thermal_power_sensor) {
				UsesOptionalsProcess_cooling_thermal_power_sensor.add((Process_cooling_thermal_power_sensor)action);
			}
		});
		return UsesOptionalsProcess_cooling_thermal_power_sensor;
	}


  public void addUsesOptionalsBypass_valve_percentage_sensor (IBypass_valve_percentage_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IBypass_valve_percentage_sensor> getUsesOptionalsBypass_valve_percentage_sensor (){
		Set<IBypass_valve_percentage_sensor> UsesOptionalsBypass_valve_percentage_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Bypass_valve_percentage_sensor) {
				UsesOptionalsBypass_valve_percentage_sensor.add((Bypass_valve_percentage_sensor)action);
			}
		});
		return UsesOptionalsBypass_valve_percentage_sensor;
	}

	public static Set<IFan_ss_ztm> getAllFan_ss_ztmsObjectsCreated(){
		Set<IFan_ss_ztm> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Fan_ss_ztm")).subjects().stream()
		.map(mapper->(IFan_ss_ztm)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}