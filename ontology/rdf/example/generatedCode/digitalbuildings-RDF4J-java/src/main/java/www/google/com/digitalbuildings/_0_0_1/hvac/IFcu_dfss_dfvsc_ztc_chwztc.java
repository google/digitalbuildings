package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.fields.IFlowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IMedium_discharge_fan_speed_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISpray_pump_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_power_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_supply_water_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_water_bypass_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IMixed_air_temperature_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IMixed_air_temperature_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_request_count;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_air_heating_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IRun_command;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_water_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.IPowerfactor_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IBuilding_air_static_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_speed_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_speed_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICondenser_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ILow_discharge_fan_speed_command;
import www.google.com.digitalbuildings._0_0_1.fields.IDifferential_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IEvaporator_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IPressurization_request_count;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_deadband_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_relative_humidity_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_command_4;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_command_3;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_air_flowrate_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IVentilation_outside_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_frequency_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_status_4;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_status_1;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_status_3;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_water_bypass_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_status_2;
import www.google.com.digitalbuildings._0_0_1.fields.ILeaving_heating_coil_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IFlowrate_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_sensor_4;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_sensor_3;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.ICooling_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IFlowrate_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_isolation_valve_status;
import www.google.com.digitalbuildings._0_0_1.fields.IFlowrate_requirement;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_speed_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_return_water_isolation_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IHeater_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IDifferential_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_heating_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_cooling_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_run_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_run_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_return_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_status_4;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_status_3;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_current_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_current_sensor_3;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_command_4;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_current_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_command_3;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_status_2;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_current_sensor_4;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_status_1;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IHeat_exchange_supply_water_isolation_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICooling_thermal_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_flowrate_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_isolation_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_isolation_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IHigh_discharge_fan_speed_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_current_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICooling_request_count;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_command_4;
import www.google.com.digitalbuildings._0_0_1.fields.IHumidification_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IVentilation_outside_air_flowrate_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_flowrate_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_command_3;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_supply_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICurrent_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_damper_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_run_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IEconomizer_mode;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_run_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.IEfficiency_percentage_specification;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_current_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_current_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IRefrigerant_evaporator_saturation_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_speed_mode;
import www.google.com.digitalbuildings._0_0_1.fields.IHeat_exchange_supply_water_isolation_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_speed_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISpeed_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_supply_water_isolation_valve_status;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_cooling_thermal_power_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISpray_pump_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_cooling_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_air_relative_humidity_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_speed_frequency_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_run_status_2;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_run_status_1;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_water_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_flowrate_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_air_relative_humidity_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_speed_frequency_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IVentilation_outside_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_speed_frequency_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_current_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IDehumidification_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_co2_concentration_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_water_differential_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IPower_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_supply_water_isolation_valve_command;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_static_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_isolation_valve_command;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_speed_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_speed_frequency_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_speed_percentage_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_speed_percentage_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_water_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_run_status_2;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_run_status_1;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_frequency_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_frequency_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_frequency_sensor_4;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_frequency_sensor_3;
import www.google.com.digitalbuildings._0_0_1.fields.ILeaving_cooling_coil_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_current_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IFilter_differential_pressure_sensor_4;
import www.google.com.digitalbuildings._0_0_1.fields.IFilter_differential_pressure_sensor_3;
import www.google.com.digitalbuildings._0_0_1.fields.IFilter_differential_pressure_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IFilter_differential_pressure_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_air_relative_humidity_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IBypass_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_static_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IRefrigerant_condenser_saturation_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IFilter_differential_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_power_sensor_3;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_power_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_water_differential_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_power_sensor_4;
import www.google.com.digitalbuildings._0_0_1.fields.IHeater_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_isolation_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_isolation_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_flowrate_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.IBoost_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_power_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.ICondensing_return_water_isolation_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_relative_humidity_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IMixed_air_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_supply_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IRun_status;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISpeed_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IBuilding_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_power_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_isolation_valve_status;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_power_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_power_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_co2_concentration_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.ICondensing_return_water_isolation_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_air_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_speed_frequency_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_return_water_isolation_valve_command;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_isolation_valve_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_speed_percentage_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_speed_percentage_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.IHeater_run_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.ICondensing_supply_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IMixed_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_input_thermal_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IReversing_valve_command;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.ISpeed_frequency_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_return_water_isolation_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IHeater_run_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.IHeater_run_command_3;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_air_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IBoost_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.IPower_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_return_water_isolation_valve_status;
import www.google.com.digitalbuildings._0_0_1.fields.IBypass_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_return_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_thermal_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_speed_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_power_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICondensing_return_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_heating_temperature_setpoint;
/**
* Class Fcu_dfss_dfvsc_ztc_chwztc 
* Hydronic varaible speed fan coil with cooling and heating (zone temp control).
*/
public interface IFcu_dfss_dfvsc_ztc_chwztc extends IChwztc, IFcu, IDfss, IZtc, IDfvsc{

	public IRI iri();

    public void addUsesOptionalsDischarge_air_static_pressure_sensor (IDischarge_air_static_pressure_sensor parameter);

	public Set<IDischarge_air_static_pressure_sensor> getUsesOptionalsDischarge_air_static_pressure_sensor();

    public void addUsesOptionalsFilter_differential_pressure_sensor (IFilter_differential_pressure_sensor parameter);

	public Set<IFilter_differential_pressure_sensor> getUsesOptionalsFilter_differential_pressure_sensor();

    public void addUsesOptionalsZone_air_co2_concentration_sensor (IZone_air_co2_concentration_sensor parameter);

	public Set<IZone_air_co2_concentration_sensor> getUsesOptionalsZone_air_co2_concentration_sensor();

    public void addUsesOptionalsCooling_thermal_power_capacity (ICooling_thermal_power_capacity parameter);

	public Set<ICooling_thermal_power_capacity> getUsesOptionalsCooling_thermal_power_capacity();

    public void addUsesOptionalsDischarge_air_temperature_sensor (IDischarge_air_temperature_sensor parameter);

	public Set<IDischarge_air_temperature_sensor> getUsesOptionalsDischarge_air_temperature_sensor();

    public void addUsesOptionalsLeaving_cooling_coil_temperature_sensor (ILeaving_cooling_coil_temperature_sensor parameter);

	public Set<ILeaving_cooling_coil_temperature_sensor> getUsesOptionalsLeaving_cooling_coil_temperature_sensor();

    public void addUsesOptionalsReturn_air_relative_humidity_sensor (IReturn_air_relative_humidity_sensor parameter);

	public Set<IReturn_air_relative_humidity_sensor> getUsesOptionalsReturn_air_relative_humidity_sensor();

    public void addUsesOptionalsReturn_air_temperature_sensor (IReturn_air_temperature_sensor parameter);

	public Set<IReturn_air_temperature_sensor> getUsesOptionalsReturn_air_temperature_sensor();

    public void addUsesOptionalsCompressor_speed_percentage_command (ICompressor_speed_percentage_command parameter);

	public Set<ICompressor_speed_percentage_command> getUsesOptionalsCompressor_speed_percentage_command();

    public void addUsesOptionalsCooling_percentage_command (ICooling_percentage_command parameter);

	public Set<ICooling_percentage_command> getUsesOptionalsCooling_percentage_command();

    public void addUsesOptionalsDischarge_air_flowrate_capacity (IDischarge_air_flowrate_capacity parameter);

	public Set<IDischarge_air_flowrate_capacity> getUsesOptionalsDischarge_air_flowrate_capacity();

    public void addUsesOptionalsDischarge_fan_current_sensor (IDischarge_fan_current_sensor parameter);

	public Set<IDischarge_fan_current_sensor> getUsesOptionalsDischarge_fan_current_sensor();

    public void addUsesOptionalsDischarge_fan_power_capacity (IDischarge_fan_power_capacity parameter);

	public Set<IDischarge_fan_power_capacity> getUsesOptionalsDischarge_fan_power_capacity();

    public void addUsesOptionalsDischarge_fan_power_sensor (IDischarge_fan_power_sensor parameter);

	public Set<IDischarge_fan_power_sensor> getUsesOptionalsDischarge_fan_power_sensor();

    public void addUsesOptionalsZone_air_relative_humidity_sensor (IZone_air_relative_humidity_sensor parameter);

	public Set<IZone_air_relative_humidity_sensor> getUsesOptionalsZone_air_relative_humidity_sensor();

    public void addUsesOptionalsMixed_air_temperature_sensor (IMixed_air_temperature_sensor parameter);

	public Set<IMixed_air_temperature_sensor> getUsesOptionalsMixed_air_temperature_sensor();

    public void addUsesOptionalsOutside_air_damper_percentage_sensor (IOutside_air_damper_percentage_sensor parameter);

	public Set<IOutside_air_damper_percentage_sensor> getUsesOptionalsOutside_air_damper_percentage_sensor();

    public void addUsesOptionalsOutside_air_flowrate_sensor (IOutside_air_flowrate_sensor parameter);

	public Set<IOutside_air_flowrate_sensor> getUsesOptionalsOutside_air_flowrate_sensor();

    public void addUsesOptionalsOutside_air_flowrate_setpoint (IOutside_air_flowrate_setpoint parameter);

	public Set<IOutside_air_flowrate_setpoint> getUsesOptionalsOutside_air_flowrate_setpoint();

    public void addUsesOptionalsExhaust_air_flowrate_capacity (IExhaust_air_flowrate_capacity parameter);

	public Set<IExhaust_air_flowrate_capacity> getUsesOptionalsExhaust_air_flowrate_capacity();

    public void addUsesOptionalsExhaust_fan_current_sensor (IExhaust_fan_current_sensor parameter);

	public Set<IExhaust_fan_current_sensor> getUsesOptionalsExhaust_fan_current_sensor();

    public void addUsesOptionalsExhaust_fan_power_capacity (IExhaust_fan_power_capacity parameter);

	public Set<IExhaust_fan_power_capacity> getUsesOptionalsExhaust_fan_power_capacity();

    public void addUsesOptionalsExhaust_fan_power_sensor (IExhaust_fan_power_sensor parameter);

	public Set<IExhaust_fan_power_sensor> getUsesOptionalsExhaust_fan_power_sensor();

    public void addUsesOptionalsExhaust_fan_speed_frequency_sensor (IExhaust_fan_speed_frequency_sensor parameter);

	public Set<IExhaust_fan_speed_frequency_sensor> getUsesOptionalsExhaust_fan_speed_frequency_sensor();

    public void addUsesOptionalsExhaust_fan_speed_percentage_sensor (IExhaust_fan_speed_percentage_sensor parameter);

	public Set<IExhaust_fan_speed_percentage_sensor> getUsesOptionalsExhaust_fan_speed_percentage_sensor();

    public void addUsesOptionalsPressurization_request_count (IPressurization_request_count parameter);

	public Set<IPressurization_request_count> getUsesOptionalsPressurization_request_count();

    public void addUsesOptionalsSupply_air_damper_percentage_command (ISupply_air_damper_percentage_command parameter);

	public Set<ISupply_air_damper_percentage_command> getUsesOptionalsSupply_air_damper_percentage_command();

    public void addUsesOptionalsSupply_air_flowrate_sensor (ISupply_air_flowrate_sensor parameter);

	public Set<ISupply_air_flowrate_sensor> getUsesOptionalsSupply_air_flowrate_sensor();

    public void addUsesOptionalsSupply_fan_run_command (ISupply_fan_run_command parameter);

	public Set<ISupply_fan_run_command> getUsesOptionalsSupply_fan_run_command();

    public void addUsesOptionalsSupply_fan_run_status (ISupply_fan_run_status parameter);

	public Set<ISupply_fan_run_status> getUsesOptionalsSupply_fan_run_status();

    public void addUsesOptionalsSupply_fan_speed_frequency_sensor (ISupply_fan_speed_frequency_sensor parameter);

	public Set<ISupply_fan_speed_frequency_sensor> getUsesOptionalsSupply_fan_speed_frequency_sensor();

    public void addUsesOptionalsSupply_fan_speed_percentage_command (ISupply_fan_speed_percentage_command parameter);

	public Set<ISupply_fan_speed_percentage_command> getUsesOptionalsSupply_fan_speed_percentage_command();

    public void addUsesOptionalsHeating_thermal_power_capacity (IHeating_thermal_power_capacity parameter);

	public Set<IHeating_thermal_power_capacity> getUsesOptionalsHeating_thermal_power_capacity();

    public void addUsesOptionalsHeating_water_valve_percentage_sensor (IHeating_water_valve_percentage_sensor parameter);

	public Set<IHeating_water_valve_percentage_sensor> getUsesOptionalsHeating_water_valve_percentage_sensor();

    public void addUsesOptionalsExhaust_fan_current_sensor_1 (IExhaust_fan_current_sensor_1 parameter);

	public Set<IExhaust_fan_current_sensor_1> getUsesOptionalsExhaust_fan_current_sensor_1();

    public void addUsesOptionalsExhaust_fan_current_sensor_2 (IExhaust_fan_current_sensor_2 parameter);

	public Set<IExhaust_fan_current_sensor_2> getUsesOptionalsExhaust_fan_current_sensor_2();

    public void addUsesOptionalsExhaust_fan_current_sensor_3 (IExhaust_fan_current_sensor_3 parameter);

	public Set<IExhaust_fan_current_sensor_3> getUsesOptionalsExhaust_fan_current_sensor_3();

    public void addUsesOptionalsExhaust_fan_current_sensor_4 (IExhaust_fan_current_sensor_4 parameter);

	public Set<IExhaust_fan_current_sensor_4> getUsesOptionalsExhaust_fan_current_sensor_4();

    public void addUsesOptionalsExhaust_fan_power_sensor_1 (IExhaust_fan_power_sensor_1 parameter);

	public Set<IExhaust_fan_power_sensor_1> getUsesOptionalsExhaust_fan_power_sensor_1();

    public void addUsesOptionalsExhaust_fan_power_sensor_2 (IExhaust_fan_power_sensor_2 parameter);

	public Set<IExhaust_fan_power_sensor_2> getUsesOptionalsExhaust_fan_power_sensor_2();

    public void addUsesOptionalsExhaust_fan_power_sensor_3 (IExhaust_fan_power_sensor_3 parameter);

	public Set<IExhaust_fan_power_sensor_3> getUsesOptionalsExhaust_fan_power_sensor_3();

    public void addUsesOptionalsExhaust_fan_power_sensor_4 (IExhaust_fan_power_sensor_4 parameter);

	public Set<IExhaust_fan_power_sensor_4> getUsesOptionalsExhaust_fan_power_sensor_4();

    public void addUsesOptionalsExhaust_air_damper_percentage_command (IExhaust_air_damper_percentage_command parameter);

	public Set<IExhaust_air_damper_percentage_command> getUsesOptionalsExhaust_air_damper_percentage_command();

    public void addUsesOptionalsExhaust_fan_run_status (IExhaust_fan_run_status parameter);

	public Set<IExhaust_fan_run_status> getUsesOptionalsExhaust_fan_run_status();

    public void addUsesOptionalsSupply_air_flowrate_capacity (ISupply_air_flowrate_capacity parameter);

	public Set<ISupply_air_flowrate_capacity> getUsesOptionalsSupply_air_flowrate_capacity();

    public void addUsesOptionalsSupply_fan_current_sensor_1 (ISupply_fan_current_sensor_1 parameter);

	public Set<ISupply_fan_current_sensor_1> getUsesOptionalsSupply_fan_current_sensor_1();

    public void addUsesOptionalsSupply_fan_current_sensor_2 (ISupply_fan_current_sensor_2 parameter);

	public Set<ISupply_fan_current_sensor_2> getUsesOptionalsSupply_fan_current_sensor_2();

    public void addUsesOptionalsSupply_fan_power_capacity (ISupply_fan_power_capacity parameter);

	public Set<ISupply_fan_power_capacity> getUsesOptionalsSupply_fan_power_capacity();

    public void addUsesOptionalsSupply_fan_power_sensor_1 (ISupply_fan_power_sensor_1 parameter);

	public Set<ISupply_fan_power_sensor_1> getUsesOptionalsSupply_fan_power_sensor_1();

    public void addUsesOptionalsSupply_fan_power_sensor_2 (ISupply_fan_power_sensor_2 parameter);

	public Set<ISupply_fan_power_sensor_2> getUsesOptionalsSupply_fan_power_sensor_2();

    public void addUsesOptionalsSupply_air_temperature_sensor (ISupply_air_temperature_sensor parameter);

	public Set<ISupply_air_temperature_sensor> getUsesOptionalsSupply_air_temperature_sensor();

    public void addUsesOptionalsExhaust_fan_speed_frequency_sensor_1 (IExhaust_fan_speed_frequency_sensor_1 parameter);

	public Set<IExhaust_fan_speed_frequency_sensor_1> getUsesOptionalsExhaust_fan_speed_frequency_sensor_1();

    public void addUsesOptionalsExhaust_fan_speed_frequency_sensor_2 (IExhaust_fan_speed_frequency_sensor_2 parameter);

	public Set<IExhaust_fan_speed_frequency_sensor_2> getUsesOptionalsExhaust_fan_speed_frequency_sensor_2();

    public void addUsesOptionalsExhaust_fan_speed_frequency_sensor_3 (IExhaust_fan_speed_frequency_sensor_3 parameter);

	public Set<IExhaust_fan_speed_frequency_sensor_3> getUsesOptionalsExhaust_fan_speed_frequency_sensor_3();

    public void addUsesOptionalsExhaust_fan_speed_percentage_sensor_1 (IExhaust_fan_speed_percentage_sensor_1 parameter);

	public Set<IExhaust_fan_speed_percentage_sensor_1> getUsesOptionalsExhaust_fan_speed_percentage_sensor_1();

    public void addUsesOptionalsExhaust_fan_speed_percentage_sensor_2 (IExhaust_fan_speed_percentage_sensor_2 parameter);

	public Set<IExhaust_fan_speed_percentage_sensor_2> getUsesOptionalsExhaust_fan_speed_percentage_sensor_2();

    public void addUsesOptionalsExhaust_fan_speed_percentage_sensor_3 (IExhaust_fan_speed_percentage_sensor_3 parameter);

	public Set<IExhaust_fan_speed_percentage_sensor_3> getUsesOptionalsExhaust_fan_speed_percentage_sensor_3();

    public void addUsesOptionalsSupply_fan_speed_frequency_sensor_1 (ISupply_fan_speed_frequency_sensor_1 parameter);

	public Set<ISupply_fan_speed_frequency_sensor_1> getUsesOptionalsSupply_fan_speed_frequency_sensor_1();

    public void addUsesOptionalsSupply_fan_speed_frequency_sensor_2 (ISupply_fan_speed_frequency_sensor_2 parameter);

	public Set<ISupply_fan_speed_frequency_sensor_2> getUsesOptionalsSupply_fan_speed_frequency_sensor_2();

    public void addUsesOptionalsSupply_fan_speed_percentage_sensor_1 (ISupply_fan_speed_percentage_sensor_1 parameter);

	public Set<ISupply_fan_speed_percentage_sensor_1> getUsesOptionalsSupply_fan_speed_percentage_sensor_1();

    public void addUsesOptionalsSupply_fan_speed_percentage_sensor_2 (ISupply_fan_speed_percentage_sensor_2 parameter);

	public Set<ISupply_fan_speed_percentage_sensor_2> getUsesOptionalsSupply_fan_speed_percentage_sensor_2();

    public void addUsesOptionalsHeating_request_count (IHeating_request_count parameter);

	public Set<IHeating_request_count> getUsesOptionalsHeating_request_count();

    public void addUsesOptionalsExhaust_fan_speed_frequency_sensor_4 (IExhaust_fan_speed_frequency_sensor_4 parameter);

	public Set<IExhaust_fan_speed_frequency_sensor_4> getUsesOptionalsExhaust_fan_speed_frequency_sensor_4();

    public void addUsesOptionalsExhaust_fan_speed_percentage_sensor_4 (IExhaust_fan_speed_percentage_sensor_4 parameter);

	public Set<IExhaust_fan_speed_percentage_sensor_4> getUsesOptionalsExhaust_fan_speed_percentage_sensor_4();

    public void addUsesOptionalsSupply_fan_current_sensor (ISupply_fan_current_sensor parameter);

	public Set<ISupply_fan_current_sensor> getUsesOptionalsSupply_fan_current_sensor();

    public void addUsesOptionalsSupply_fan_power_sensor (ISupply_fan_power_sensor parameter);

	public Set<ISupply_fan_power_sensor> getUsesOptionalsSupply_fan_power_sensor();

    public void addUsesOptionalsSupply_fan_speed_percentage_sensor (ISupply_fan_speed_percentage_sensor parameter);

	public Set<ISupply_fan_speed_percentage_sensor> getUsesOptionalsSupply_fan_speed_percentage_sensor();

    public void addUsesOptionalsDischarge_fan_speed_frequency_sensor (IDischarge_fan_speed_frequency_sensor parameter);

	public Set<IDischarge_fan_speed_frequency_sensor> getUsesOptionalsDischarge_fan_speed_frequency_sensor();

    public void addUsesOptionalsDischarge_fan_speed_percentage_sensor (IDischarge_fan_speed_percentage_sensor parameter);

	public Set<IDischarge_fan_speed_percentage_sensor> getUsesOptionalsDischarge_fan_speed_percentage_sensor();

    public void addUsesOptionalsZone_air_deadband_temperature_setpoint (IZone_air_deadband_temperature_setpoint parameter);

	public Set<IZone_air_deadband_temperature_setpoint> getUsesOptionalsZone_air_deadband_temperature_setpoint();

    public void addUsesOptionalsHeater_run_status (IHeater_run_status parameter);

	public Set<IHeater_run_status> getUsesOptionalsHeater_run_status();

    public void addUsesOptionalsHeating_percentage_command (IHeating_percentage_command parameter);

	public Set<IHeating_percentage_command> getUsesOptionalsHeating_percentage_command();

    public void addUsesOptionalsDischarge_air_relative_humidity_sensor (IDischarge_air_relative_humidity_sensor parameter);

	public Set<IDischarge_air_relative_humidity_sensor> getUsesOptionalsDischarge_air_relative_humidity_sensor();

    public void addUsesOptionalsCooling_request_count (ICooling_request_count parameter);

	public Set<ICooling_request_count> getUsesOptionalsCooling_request_count();

    public void addUsesOptionalsLeaving_heating_coil_temperature_sensor (ILeaving_heating_coil_temperature_sensor parameter);

	public Set<ILeaving_heating_coil_temperature_sensor> getUsesOptionalsLeaving_heating_coil_temperature_sensor();

    public void addUsesOptionalsCurrent_sensor (ICurrent_sensor parameter);

	public Set<ICurrent_sensor> getUsesOptionalsCurrent_sensor();

    public void addUsesOptionalsPower_sensor (IPower_sensor parameter);

	public Set<IPower_sensor> getUsesOptionalsPower_sensor();

    public void addUsesOptionalsSpeed_frequency_sensor (ISpeed_frequency_sensor parameter);

	public Set<ISpeed_frequency_sensor> getUsesOptionalsSpeed_frequency_sensor();

    public void addUsesOptionalsSpeed_percentage_sensor (ISpeed_percentage_sensor parameter);

	public Set<ISpeed_percentage_sensor> getUsesOptionalsSpeed_percentage_sensor();

    public void addUsesOptionalsReturn_water_temperature_sensor (IReturn_water_temperature_sensor parameter);

	public Set<IReturn_water_temperature_sensor> getUsesOptionalsReturn_water_temperature_sensor();

    public void addUsesOptionalsRun_command (IRun_command parameter);

	public Set<IRun_command> getUsesOptionalsRun_command();

    public void addUsesOptionalsEfficiency_percentage_specification (IEfficiency_percentage_specification parameter);

	public Set<IEfficiency_percentage_specification> getUsesOptionalsEfficiency_percentage_specification();

    public void addUsesOptionalsFlowrate_requirement (IFlowrate_requirement parameter);

	public Set<IFlowrate_requirement> getUsesOptionalsFlowrate_requirement();

    public void addUsesOptionalsHeating_input_thermal_power_capacity (IHeating_input_thermal_power_capacity parameter);

	public Set<IHeating_input_thermal_power_capacity> getUsesOptionalsHeating_input_thermal_power_capacity();

    public void addUsesOptionalsFlowrate_capacity (IFlowrate_capacity parameter);

	public Set<IFlowrate_capacity> getUsesOptionalsFlowrate_capacity();

    public void addUsesOptionalsPower_capacity (IPower_capacity parameter);

	public Set<IPower_capacity> getUsesOptionalsPower_capacity();

    public void addUsesOptionalsPowerfactor_sensor (IPowerfactor_sensor parameter);

	public Set<IPowerfactor_sensor> getUsesOptionalsPowerfactor_sensor();

    public void addUsesOptionalsChilled_return_water_temperature_sensor (IChilled_return_water_temperature_sensor parameter);

	public Set<IChilled_return_water_temperature_sensor> getUsesOptionalsChilled_return_water_temperature_sensor();

    public void addUsesOptionalsCompressor_speed_percentage_sensor (ICompressor_speed_percentage_sensor parameter);

	public Set<ICompressor_speed_percentage_sensor> getUsesOptionalsCompressor_speed_percentage_sensor();

    public void addUsesOptionalsCompressor_speed_frequency_sensor (ICompressor_speed_frequency_sensor parameter);

	public Set<ICompressor_speed_frequency_sensor> getUsesOptionalsCompressor_speed_frequency_sensor();

    public void addUsesOptionalsProcess_cooling_thermal_power_sensor (IProcess_cooling_thermal_power_sensor parameter);

	public Set<IProcess_cooling_thermal_power_sensor> getUsesOptionalsProcess_cooling_thermal_power_sensor();

    public void addUsesOptionalsBypass_valve_percentage_sensor (IBypass_valve_percentage_sensor parameter);

	public Set<IBypass_valve_percentage_sensor> getUsesOptionalsBypass_valve_percentage_sensor();

    public void addUsesOptionalsDischarge_fan_run_command (IDischarge_fan_run_command parameter);

	public Set<IDischarge_fan_run_command> getUsesOptionalsDischarge_fan_run_command();

    public void addUsesOptionalsDischarge_fan_run_status (IDischarge_fan_run_status parameter);

	public Set<IDischarge_fan_run_status> getUsesOptionalsDischarge_fan_run_status();

}