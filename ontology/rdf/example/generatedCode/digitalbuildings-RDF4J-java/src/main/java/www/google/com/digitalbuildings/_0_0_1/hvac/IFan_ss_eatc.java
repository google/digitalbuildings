package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.fields.IFlowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISpray_pump_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_power_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_supply_water_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_water_bypass_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_request_count;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_air_heating_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_water_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IRun_command;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.IPowerfactor_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IBuilding_air_static_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_speed_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ICondenser_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_speed_percentage_sensor;
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
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_status_4;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_frequency_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_status_1;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_water_bypass_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_status_3;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_status_2;
import www.google.com.digitalbuildings._0_0_1.fields.ILeaving_heating_coil_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IFlowrate_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_sensor_4;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_sensor_3;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IFlowrate_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.ICooling_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_isolation_valve_status;
import www.google.com.digitalbuildings._0_0_1.fields.IFlowrate_requirement;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_speed_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_return_water_isolation_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IHeater_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IDifferential_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_heating_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_cooling_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_return_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_status_4;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_status_3;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_current_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_command_4;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_current_sensor_3;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_command_3;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_current_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_status_2;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_status_1;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_current_sensor_4;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IHeat_exchange_supply_water_isolation_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICooling_thermal_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_flowrate_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_isolation_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_isolation_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_current_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICooling_request_count;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_command_4;
import www.google.com.digitalbuildings._0_0_1.fields.IVentilation_outside_air_flowrate_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_flowrate_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_command_3;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_supply_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICurrent_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_damper_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_run_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.IEconomizer_mode;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_run_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.IEfficiency_percentage_specification;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_current_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_current_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IRefrigerant_evaporator_saturation_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IHeat_exchange_supply_water_isolation_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_supply_water_isolation_valve_status;
import www.google.com.digitalbuildings._0_0_1.fields.ISpeed_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_speed_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISpray_pump_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_air_relative_humidity_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_speed_frequency_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_run_status_2;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_run_status_1;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_water_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_flowrate_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IVentilation_outside_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_speed_frequency_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_speed_frequency_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_current_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_co2_concentration_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_water_differential_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_supply_water_isolation_valve_command;
import www.google.com.digitalbuildings._0_0_1.fields.IPower_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_static_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_isolation_valve_command;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_speed_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_speed_frequency_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_speed_percentage_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_speed_percentage_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_water_valve_percentage_command;
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
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_power_sensor_3;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_water_differential_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_power_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_power_sensor_4;
import www.google.com.digitalbuildings._0_0_1.fields.IHeater_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_isolation_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_isolation_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_flowrate_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IBoost_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_power_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.ICondensing_return_water_isolation_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IMixed_air_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_supply_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IRun_status;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISpeed_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IBuilding_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_power_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_isolation_valve_status;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_power_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_co2_concentration_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_power_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.ICondensing_return_water_isolation_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_air_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_speed_frequency_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_return_water_isolation_valve_command;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_isolation_valve_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_speed_percentage_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.IHeater_run_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_speed_percentage_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.ICondensing_supply_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IMixed_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IReversing_valve_command;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_input_thermal_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_return_water_isolation_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISpeed_frequency_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IHeater_run_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.IHeater_run_command_3;
import www.google.com.digitalbuildings._0_0_1.fields.IBoost_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.IPower_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_return_water_isolation_valve_status;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_return_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_thermal_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_speed_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_power_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICondensing_return_water_temperature_sensor;
/**
* Class Fan_ss_eatc 
* Exhaust air temp control fan (one-off).
*/
public interface IFan_ss_eatc extends IFan, ISs, IRtm{

	public IRI iri();

    public void addUsesExhaust_air_temperature_sensor (IExhaust_air_temperature_sensor parameter);

	public Set<IExhaust_air_temperature_sensor> getUsesExhaust_air_temperature_sensor();

    public void addUsesReturn_air_relative_humidity_sensor (IReturn_air_relative_humidity_sensor parameter);

	public Set<IReturn_air_relative_humidity_sensor> getUsesReturn_air_relative_humidity_sensor();

    public void addUsesRun_command (IRun_command parameter);

	public Set<IRun_command> getUsesRun_command();

    public void addUsesRun_status (IRun_status parameter);

	public Set<IRun_status> getUsesRun_status();

    public void addUsesHeater_run_command_1 (IHeater_run_command_1 parameter);

	public Set<IHeater_run_command_1> getUsesHeater_run_command_1();

    public void addUsesHeater_run_command_2 (IHeater_run_command_2 parameter);

	public Set<IHeater_run_command_2> getUsesHeater_run_command_2();

    public void addUsesSupply_water_temperature_sensor (ISupply_water_temperature_sensor parameter);

	public Set<ISupply_water_temperature_sensor> getUsesSupply_water_temperature_sensor();

    public void addUsesSupply_water_temperature_setpoint (ISupply_water_temperature_setpoint parameter);

	public Set<ISupply_water_temperature_setpoint> getUsesSupply_water_temperature_setpoint();

    public void addUsesReturn_water_isolation_valve_command (IReturn_water_isolation_valve_command parameter);

	public Set<IReturn_water_isolation_valve_command> getUsesReturn_water_isolation_valve_command();

    public void addUsesReturn_water_isolation_valve_status (IReturn_water_isolation_valve_status parameter);

	public Set<IReturn_water_isolation_valve_status> getUsesReturn_water_isolation_valve_status();

    public void addUsesSupply_water_isolation_valve_command (ISupply_water_isolation_valve_command parameter);

	public Set<ISupply_water_isolation_valve_command> getUsesSupply_water_isolation_valve_command();

    public void addUsesSupply_water_isolation_valve_status (ISupply_water_isolation_valve_status parameter);

	public Set<ISupply_water_isolation_valve_status> getUsesSupply_water_isolation_valve_status();

    public void addUsesChilled_supply_water_temperature_sensor (IChilled_supply_water_temperature_sensor parameter);

	public Set<IChilled_supply_water_temperature_sensor> getUsesChilled_supply_water_temperature_sensor();

    public void addUsesChilled_supply_water_temperature_setpoint (IChilled_supply_water_temperature_setpoint parameter);

	public Set<IChilled_supply_water_temperature_setpoint> getUsesChilled_supply_water_temperature_setpoint();

    public void addUsesChilled_return_water_isolation_valve_percentage_command (IChilled_return_water_isolation_valve_percentage_command parameter);

	public Set<IChilled_return_water_isolation_valve_percentage_command> getUsesChilled_return_water_isolation_valve_percentage_command();

    public void addUsesChilled_return_water_isolation_valve_percentage_sensor (IChilled_return_water_isolation_valve_percentage_sensor parameter);

	public Set<IChilled_return_water_isolation_valve_percentage_sensor> getUsesChilled_return_water_isolation_valve_percentage_sensor();

    public void addUsesCompressor_run_command (ICompressor_run_command parameter);

	public Set<ICompressor_run_command> getUsesCompressor_run_command();

    public void addUsesCompressor_run_status (ICompressor_run_status parameter);

	public Set<ICompressor_run_status> getUsesCompressor_run_status();

    public void addUsesCondenser_pressure_sensor (ICondenser_pressure_sensor parameter);

	public Set<ICondenser_pressure_sensor> getUsesCondenser_pressure_sensor();

    public void addUsesDifferential_pressure_sensor (IDifferential_pressure_sensor parameter);

	public Set<IDifferential_pressure_sensor> getUsesDifferential_pressure_sensor();

    public void addUsesEvaporator_pressure_sensor (IEvaporator_pressure_sensor parameter);

	public Set<IEvaporator_pressure_sensor> getUsesEvaporator_pressure_sensor();

    public void addUsesChilled_return_water_isolation_valve_command (IChilled_return_water_isolation_valve_command parameter);

	public Set<IChilled_return_water_isolation_valve_command> getUsesChilled_return_water_isolation_valve_command();

    public void addUsesChilled_return_water_isolation_valve_status (IChilled_return_water_isolation_valve_status parameter);

	public Set<IChilled_return_water_isolation_valve_status> getUsesChilled_return_water_isolation_valve_status();

    public void addUsesCondensing_return_water_isolation_valve_percentage_command (ICondensing_return_water_isolation_valve_percentage_command parameter);

	public Set<ICondensing_return_water_isolation_valve_percentage_command> getUsesCondensing_return_water_isolation_valve_percentage_command();

    public void addUsesCondensing_return_water_isolation_valve_percentage_sensor (ICondensing_return_water_isolation_valve_percentage_sensor parameter);

	public Set<ICondensing_return_water_isolation_valve_percentage_sensor> getUsesCondensing_return_water_isolation_valve_percentage_sensor();

    public void addUsesRefrigerant_condenser_saturation_temperature_sensor (IRefrigerant_condenser_saturation_temperature_sensor parameter);

	public Set<IRefrigerant_condenser_saturation_temperature_sensor> getUsesRefrigerant_condenser_saturation_temperature_sensor();

    public void addUsesRefrigerant_evaporator_saturation_temperature_sensor (IRefrigerant_evaporator_saturation_temperature_sensor parameter);

	public Set<IRefrigerant_evaporator_saturation_temperature_sensor> getUsesRefrigerant_evaporator_saturation_temperature_sensor();

    public void addUsesCompressor_run_command_1 (ICompressor_run_command_1 parameter);

	public Set<ICompressor_run_command_1> getUsesCompressor_run_command_1();

    public void addUsesCompressor_run_command_2 (ICompressor_run_command_2 parameter);

	public Set<ICompressor_run_command_2> getUsesCompressor_run_command_2();

    public void addUsesCompressor_run_status_1 (ICompressor_run_status_1 parameter);

	public Set<ICompressor_run_status_1> getUsesCompressor_run_status_1();

    public void addUsesCompressor_run_status_2 (ICompressor_run_status_2 parameter);

	public Set<ICompressor_run_status_2> getUsesCompressor_run_status_2();

    public void addUsesChilled_supply_water_isolation_valve_command (IChilled_supply_water_isolation_valve_command parameter);

	public Set<IChilled_supply_water_isolation_valve_command> getUsesChilled_supply_water_isolation_valve_command();

    public void addUsesChilled_supply_water_isolation_valve_status (IChilled_supply_water_isolation_valve_status parameter);

	public Set<IChilled_supply_water_isolation_valve_status> getUsesChilled_supply_water_isolation_valve_status();

    public void addUsesChilled_water_bypass_valve_percentage_command (IChilled_water_bypass_valve_percentage_command parameter);

	public Set<IChilled_water_bypass_valve_percentage_command> getUsesChilled_water_bypass_valve_percentage_command();

    public void addUsesChilled_water_bypass_valve_percentage_sensor (IChilled_water_bypass_valve_percentage_sensor parameter);

	public Set<IChilled_water_bypass_valve_percentage_sensor> getUsesChilled_water_bypass_valve_percentage_sensor();

    public void addUsesCondensing_return_water_temperature_sensor (ICondensing_return_water_temperature_sensor parameter);

	public Set<ICondensing_return_water_temperature_sensor> getUsesCondensing_return_water_temperature_sensor();

    public void addUsesCondensing_supply_water_temperature_sensor (ICondensing_supply_water_temperature_sensor parameter);

	public Set<ICondensing_supply_water_temperature_sensor> getUsesCondensing_supply_water_temperature_sensor();

    public void addUsesSpray_pump_run_command (ISpray_pump_run_command parameter);

	public Set<ISpray_pump_run_command> getUsesSpray_pump_run_command();

    public void addUsesSpray_pump_run_status (ISpray_pump_run_status parameter);

	public Set<ISpray_pump_run_status> getUsesSpray_pump_run_status();

    public void addUsesReturn_water_isolation_valve_percentage_command (IReturn_water_isolation_valve_percentage_command parameter);

	public Set<IReturn_water_isolation_valve_percentage_command> getUsesReturn_water_isolation_valve_percentage_command();

    public void addUsesReturn_water_isolation_valve_percentage_sensor (IReturn_water_isolation_valve_percentage_sensor parameter);

	public Set<IReturn_water_isolation_valve_percentage_sensor> getUsesReturn_water_isolation_valve_percentage_sensor();

    public void addUsesHeater_run_command (IHeater_run_command parameter);

	public Set<IHeater_run_command> getUsesHeater_run_command();

    public void addUsesDifferential_pressure_setpoint (IDifferential_pressure_setpoint parameter);

	public Set<IDifferential_pressure_setpoint> getUsesDifferential_pressure_setpoint();

    public void addUsesProcess_water_differential_pressure_sensor (IProcess_water_differential_pressure_sensor parameter);

	public Set<IProcess_water_differential_pressure_sensor> getUsesProcess_water_differential_pressure_sensor();

    public void addUsesProcess_water_differential_pressure_setpoint (IProcess_water_differential_pressure_setpoint parameter);

	public Set<IProcess_water_differential_pressure_setpoint> getUsesProcess_water_differential_pressure_setpoint();

    public void addUsesProcess_return_water_temperature_sensor (IProcess_return_water_temperature_sensor parameter);

	public Set<IProcess_return_water_temperature_sensor> getUsesProcess_return_water_temperature_sensor();

    public void addUsesProcess_supply_water_temperature_sensor (IProcess_supply_water_temperature_sensor parameter);

	public Set<IProcess_supply_water_temperature_sensor> getUsesProcess_supply_water_temperature_sensor();

    public void addUsesHeat_exchange_supply_water_isolation_valve_percentage_command (IHeat_exchange_supply_water_isolation_valve_percentage_command parameter);

	public Set<IHeat_exchange_supply_water_isolation_valve_percentage_command> getUsesHeat_exchange_supply_water_isolation_valve_percentage_command();

    public void addUsesHeat_exchange_supply_water_isolation_valve_percentage_sensor (IHeat_exchange_supply_water_isolation_valve_percentage_sensor parameter);

	public Set<IHeat_exchange_supply_water_isolation_valve_percentage_sensor> getUsesHeat_exchange_supply_water_isolation_valve_percentage_sensor();

    public void addUsesFlowrate_sensor (IFlowrate_sensor parameter);

	public Set<IFlowrate_sensor> getUsesFlowrate_sensor();

    public void addUsesFlowrate_setpoint (IFlowrate_setpoint parameter);

	public Set<IFlowrate_setpoint> getUsesFlowrate_setpoint();

    public void addUsesSupply_water_isolation_valve_percentage_command (ISupply_water_isolation_valve_percentage_command parameter);

	public Set<ISupply_water_isolation_valve_percentage_command> getUsesSupply_water_isolation_valve_percentage_command();

    public void addUsesSupply_water_isolation_valve_percentage_sensor (ISupply_water_isolation_valve_percentage_sensor parameter);

	public Set<ISupply_water_isolation_valve_percentage_sensor> getUsesSupply_water_isolation_valve_percentage_sensor();

    public void addUsesSpeed_percentage_command (ISpeed_percentage_command parameter);

	public Set<ISpeed_percentage_command> getUsesSpeed_percentage_command();

    public void addUsesZone_air_cooling_temperature_setpoint (IZone_air_cooling_temperature_setpoint parameter);

	public Set<IZone_air_cooling_temperature_setpoint> getUsesZone_air_cooling_temperature_setpoint();

    public void addUsesZone_air_heating_temperature_setpoint (IZone_air_heating_temperature_setpoint parameter);

	public Set<IZone_air_heating_temperature_setpoint> getUsesZone_air_heating_temperature_setpoint();

    public void addUsesZone_air_temperature_sensor (IZone_air_temperature_sensor parameter);

	public Set<IZone_air_temperature_sensor> getUsesZone_air_temperature_sensor();

    public void addUsesEconomizer_mode (IEconomizer_mode parameter);

	public Set<IEconomizer_mode> getUsesEconomizer_mode();

    public void addUsesOutside_air_damper_percentage_command (IOutside_air_damper_percentage_command parameter);

	public Set<IOutside_air_damper_percentage_command> getUsesOutside_air_damper_percentage_command();

    public void addUsesOutside_air_temperature_sensor (IOutside_air_temperature_sensor parameter);

	public Set<IOutside_air_temperature_sensor> getUsesOutside_air_temperature_sensor();

    public void addUsesExhaust_fan_run_command (IExhaust_fan_run_command parameter);

	public Set<IExhaust_fan_run_command> getUsesExhaust_fan_run_command();

    public void addUsesExhaust_fan_run_status (IExhaust_fan_run_status parameter);

	public Set<IExhaust_fan_run_status> getUsesExhaust_fan_run_status();

    public void addUsesExhaust_fan_speed_percentage_command (IExhaust_fan_speed_percentage_command parameter);

	public Set<IExhaust_fan_speed_percentage_command> getUsesExhaust_fan_speed_percentage_command();

    public void addUsesSupply_air_static_pressure_sensor (ISupply_air_static_pressure_sensor parameter);

	public Set<ISupply_air_static_pressure_sensor> getUsesSupply_air_static_pressure_sensor();

    public void addUsesSupply_air_static_pressure_setpoint (ISupply_air_static_pressure_setpoint parameter);

	public Set<ISupply_air_static_pressure_setpoint> getUsesSupply_air_static_pressure_setpoint();

    public void addUsesBuilding_air_static_pressure_sensor (IBuilding_air_static_pressure_sensor parameter);

	public Set<IBuilding_air_static_pressure_sensor> getUsesBuilding_air_static_pressure_sensor();

    public void addUsesBuilding_air_static_pressure_setpoint (IBuilding_air_static_pressure_setpoint parameter);

	public Set<IBuilding_air_static_pressure_setpoint> getUsesBuilding_air_static_pressure_setpoint();

    public void addUsesMixed_air_temperature_sensor (IMixed_air_temperature_sensor parameter);

	public Set<IMixed_air_temperature_sensor> getUsesMixed_air_temperature_sensor();

    public void addUsesReturn_air_temperature_sensor (IReturn_air_temperature_sensor parameter);

	public Set<IReturn_air_temperature_sensor> getUsesReturn_air_temperature_sensor();

    public void addUsesSupply_air_temperature_setpoint (ISupply_air_temperature_setpoint parameter);

	public Set<ISupply_air_temperature_setpoint> getUsesSupply_air_temperature_setpoint();

    public void addUsesVentilation_outside_air_damper_percentage_command (IVentilation_outside_air_damper_percentage_command parameter);

	public Set<IVentilation_outside_air_damper_percentage_command> getUsesVentilation_outside_air_damper_percentage_command();

    public void addUsesVentilation_outside_air_flowrate_sensor (IVentilation_outside_air_flowrate_sensor parameter);

	public Set<IVentilation_outside_air_flowrate_sensor> getUsesVentilation_outside_air_flowrate_sensor();

    public void addUsesVentilation_outside_air_flowrate_setpoint (IVentilation_outside_air_flowrate_setpoint parameter);

	public Set<IVentilation_outside_air_flowrate_setpoint> getUsesVentilation_outside_air_flowrate_setpoint();

    public void addUsesSupply_fan_run_command_1 (ISupply_fan_run_command_1 parameter);

	public Set<ISupply_fan_run_command_1> getUsesSupply_fan_run_command_1();

    public void addUsesSupply_fan_run_command_2 (ISupply_fan_run_command_2 parameter);

	public Set<ISupply_fan_run_command_2> getUsesSupply_fan_run_command_2();

    public void addUsesSupply_fan_run_status_1 (ISupply_fan_run_status_1 parameter);

	public Set<ISupply_fan_run_status_1> getUsesSupply_fan_run_status_1();

    public void addUsesSupply_fan_run_status_2 (ISupply_fan_run_status_2 parameter);

	public Set<ISupply_fan_run_status_2> getUsesSupply_fan_run_status_2();

    public void addUsesChilled_water_valve_percentage_command (IChilled_water_valve_percentage_command parameter);

	public Set<IChilled_water_valve_percentage_command> getUsesChilled_water_valve_percentage_command();

    public void addUsesSupply_air_temperature_sensor (ISupply_air_temperature_sensor parameter);

	public Set<ISupply_air_temperature_sensor> getUsesSupply_air_temperature_sensor();

    public void addUsesExhaust_fan_run_command_1 (IExhaust_fan_run_command_1 parameter);

	public Set<IExhaust_fan_run_command_1> getUsesExhaust_fan_run_command_1();

    public void addUsesExhaust_fan_run_command_2 (IExhaust_fan_run_command_2 parameter);

	public Set<IExhaust_fan_run_command_2> getUsesExhaust_fan_run_command_2();

    public void addUsesExhaust_fan_run_command_3 (IExhaust_fan_run_command_3 parameter);

	public Set<IExhaust_fan_run_command_3> getUsesExhaust_fan_run_command_3();

    public void addUsesExhaust_fan_run_status_1 (IExhaust_fan_run_status_1 parameter);

	public Set<IExhaust_fan_run_status_1> getUsesExhaust_fan_run_status_1();

    public void addUsesExhaust_fan_run_status_2 (IExhaust_fan_run_status_2 parameter);

	public Set<IExhaust_fan_run_status_2> getUsesExhaust_fan_run_status_2();

    public void addUsesExhaust_fan_run_status_3 (IExhaust_fan_run_status_3 parameter);

	public Set<IExhaust_fan_run_status_3> getUsesExhaust_fan_run_status_3();

    public void addUsesExhaust_fan_speed_percentage_command_1 (IExhaust_fan_speed_percentage_command_1 parameter);

	public Set<IExhaust_fan_speed_percentage_command_1> getUsesExhaust_fan_speed_percentage_command_1();

    public void addUsesExhaust_fan_speed_percentage_command_2 (IExhaust_fan_speed_percentage_command_2 parameter);

	public Set<IExhaust_fan_speed_percentage_command_2> getUsesExhaust_fan_speed_percentage_command_2();

    public void addUsesExhaust_fan_speed_percentage_command_3 (IExhaust_fan_speed_percentage_command_3 parameter);

	public Set<IExhaust_fan_speed_percentage_command_3> getUsesExhaust_fan_speed_percentage_command_3();

    public void addUsesSupply_fan_speed_percentage_command_1 (ISupply_fan_speed_percentage_command_1 parameter);

	public Set<ISupply_fan_speed_percentage_command_1> getUsesSupply_fan_speed_percentage_command_1();

    public void addUsesSupply_fan_speed_percentage_command_2 (ISupply_fan_speed_percentage_command_2 parameter);

	public Set<ISupply_fan_speed_percentage_command_2> getUsesSupply_fan_speed_percentage_command_2();

    public void addUsesCooling_request_count (ICooling_request_count parameter);

	public Set<ICooling_request_count> getUsesCooling_request_count();

    public void addUsesPressurization_request_count (IPressurization_request_count parameter);

	public Set<IPressurization_request_count> getUsesPressurization_request_count();

    public void addUsesSupply_fan_run_command (ISupply_fan_run_command parameter);

	public Set<ISupply_fan_run_command> getUsesSupply_fan_run_command();

    public void addUsesSupply_fan_run_status (ISupply_fan_run_status parameter);

	public Set<ISupply_fan_run_status> getUsesSupply_fan_run_status();

    public void addUsesSupply_fan_speed_percentage_command (ISupply_fan_speed_percentage_command parameter);

	public Set<ISupply_fan_speed_percentage_command> getUsesSupply_fan_speed_percentage_command();

    public void addUsesExhaust_fan_run_command_4 (IExhaust_fan_run_command_4 parameter);

	public Set<IExhaust_fan_run_command_4> getUsesExhaust_fan_run_command_4();

    public void addUsesExhaust_fan_run_status_4 (IExhaust_fan_run_status_4 parameter);

	public Set<IExhaust_fan_run_status_4> getUsesExhaust_fan_run_status_4();

    public void addUsesExhaust_fan_speed_percentage_command_4 (IExhaust_fan_speed_percentage_command_4 parameter);

	public Set<IExhaust_fan_speed_percentage_command_4> getUsesExhaust_fan_speed_percentage_command_4();

    public void addUsesOutside_air_flowrate_sensor (IOutside_air_flowrate_sensor parameter);

	public Set<IOutside_air_flowrate_sensor> getUsesOutside_air_flowrate_sensor();

    public void addUsesDischarge_fan_run_command (IDischarge_fan_run_command parameter);

	public Set<IDischarge_fan_run_command> getUsesDischarge_fan_run_command();

    public void addUsesDischarge_fan_run_status (IDischarge_fan_run_status parameter);

	public Set<IDischarge_fan_run_status> getUsesDischarge_fan_run_status();

    public void addUsesDischarge_fan_speed_percentage_command (IDischarge_fan_speed_percentage_command parameter);

	public Set<IDischarge_fan_speed_percentage_command> getUsesDischarge_fan_speed_percentage_command();

    public void addUsesOutside_air_flowrate_setpoint (IOutside_air_flowrate_setpoint parameter);

	public Set<IOutside_air_flowrate_setpoint> getUsesOutside_air_flowrate_setpoint();

    public void addUsesFilter_differential_pressure_sensor_1 (IFilter_differential_pressure_sensor_1 parameter);

	public Set<IFilter_differential_pressure_sensor_1> getUsesFilter_differential_pressure_sensor_1();

    public void addUsesFilter_differential_pressure_sensor_2 (IFilter_differential_pressure_sensor_2 parameter);

	public Set<IFilter_differential_pressure_sensor_2> getUsesFilter_differential_pressure_sensor_2();

    public void addUsesFilter_differential_pressure_sensor_3 (IFilter_differential_pressure_sensor_3 parameter);

	public Set<IFilter_differential_pressure_sensor_3> getUsesFilter_differential_pressure_sensor_3();

    public void addUsesFilter_differential_pressure_sensor_4 (IFilter_differential_pressure_sensor_4 parameter);

	public Set<IFilter_differential_pressure_sensor_4> getUsesFilter_differential_pressure_sensor_4();

    public void addUsesCompressor_run_command_3 (ICompressor_run_command_3 parameter);

	public Set<ICompressor_run_command_3> getUsesCompressor_run_command_3();

    public void addUsesCompressor_run_command_4 (ICompressor_run_command_4 parameter);

	public Set<ICompressor_run_command_4> getUsesCompressor_run_command_4();

    public void addUsesCompressor_run_status_3 (ICompressor_run_status_3 parameter);

	public Set<ICompressor_run_status_3> getUsesCompressor_run_status_3();

    public void addUsesCompressor_run_status_4 (ICompressor_run_status_4 parameter);

	public Set<ICompressor_run_status_4> getUsesCompressor_run_status_4();

    public void addUsesMixed_air_temperature_setpoint (IMixed_air_temperature_setpoint parameter);

	public Set<IMixed_air_temperature_setpoint> getUsesMixed_air_temperature_setpoint();

    public void addUsesSupply_air_flowrate_sensor (ISupply_air_flowrate_sensor parameter);

	public Set<ISupply_air_flowrate_sensor> getUsesSupply_air_flowrate_sensor();

    public void addUsesSupply_air_flowrate_setpoint (ISupply_air_flowrate_setpoint parameter);

	public Set<ISupply_air_flowrate_setpoint> getUsesSupply_air_flowrate_setpoint();

    public void addUsesBypass_air_damper_percentage_command (IBypass_air_damper_percentage_command parameter);

	public Set<IBypass_air_damper_percentage_command> getUsesBypass_air_damper_percentage_command();

    public void addUsesZone_air_temperature_setpoint (IZone_air_temperature_setpoint parameter);

	public Set<IZone_air_temperature_setpoint> getUsesZone_air_temperature_setpoint();

    public void addUsesDischarge_air_temperature_sensor (IDischarge_air_temperature_sensor parameter);

	public Set<IDischarge_air_temperature_sensor> getUsesDischarge_air_temperature_sensor();

    public void addUsesDischarge_air_temperature_setpoint (IDischarge_air_temperature_setpoint parameter);

	public Set<IDischarge_air_temperature_setpoint> getUsesDischarge_air_temperature_setpoint();

    public void addUsesZone_air_co2_concentration_sensor (IZone_air_co2_concentration_sensor parameter);

	public Set<IZone_air_co2_concentration_sensor> getUsesZone_air_co2_concentration_sensor();

    public void addUsesZone_air_co2_concentration_setpoint (IZone_air_co2_concentration_setpoint parameter);

	public Set<IZone_air_co2_concentration_setpoint> getUsesZone_air_co2_concentration_setpoint();

    public void addUsesBoost_fan_run_command (IBoost_fan_run_command parameter);

	public Set<IBoost_fan_run_command> getUsesBoost_fan_run_command();

    public void addUsesBoost_fan_run_status (IBoost_fan_run_status parameter);

	public Set<IBoost_fan_run_status> getUsesBoost_fan_run_status();

    public void addUsesReversing_valve_command (IReversing_valve_command parameter);

	public Set<IReversing_valve_command> getUsesReversing_valve_command();

    public void addUsesZone_air_static_pressure_sensor (IZone_air_static_pressure_sensor parameter);

	public Set<IZone_air_static_pressure_sensor> getUsesZone_air_static_pressure_sensor();

    public void addUsesZone_air_static_pressure_setpoint (IZone_air_static_pressure_setpoint parameter);

	public Set<IZone_air_static_pressure_setpoint> getUsesZone_air_static_pressure_setpoint();

    public void addUsesDischarge_air_heating_temperature_setpoint (IDischarge_air_heating_temperature_setpoint parameter);

	public Set<IDischarge_air_heating_temperature_setpoint> getUsesDischarge_air_heating_temperature_setpoint();

    public void addUsesHeater_run_command_3 (IHeater_run_command_3 parameter);

	public Set<IHeater_run_command_3> getUsesHeater_run_command_3();

}