package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_water_differential_pressure_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_water_differential_pressure_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IHeater_run_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_isolation_valve_status;
import www.google.com.digitalbuildings._0_0_1.fields.IFlowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IDifferential_pressure_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IFlowrate_requirement;
import www.google.com.digitalbuildings._0_0_1.fields.IDifferential_pressure_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_supply_water_temperature_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICooling_request_count;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IRun_status;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_input_thermal_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_return_water_temperature_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IHeater_run_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_return_water_temperature_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_cooling_thermal_power_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_cooling_thermal_power_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IPower_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IBypass_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_request_count;
import www.google.com.digitalbuildings._0_0_1.fields.IMin_flowrate_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IRun_command;
import www.google.com.digitalbuildings._0_0_1.fields.ICurrent_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IPowerfactor_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IDifferential_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IHeater_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_thermal_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_isolation_valve_status;
import www.google.com.digitalbuildings._0_0_1.fields.IEfficiency_percentage_specification;
import www.google.com.digitalbuildings._0_0_1.fields.IPower_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_isolation_valve_command;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_isolation_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_isolation_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IPressurization_request_count;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_supply_water_temperature_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IFlowrate_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_isolation_valve_command;
/**
* Class Wdpc2x 
* Differential pressure control in whichever system, 2 sensors.
*/
public interface IWdpc2x extends IFunctionality, IOperational{

	public IRI iri();

    public void addUsesOptionalsPressurization_request_count (IPressurization_request_count parameter);

	public Set<IPressurization_request_count> getUsesOptionalsPressurization_request_count();

    public void addUsesOptionalsRun_command (IRun_command parameter);

	public Set<IRun_command> getUsesOptionalsRun_command();

    public void addUsesOptionalsProcess_cooling_thermal_power_sensor_1 (IProcess_cooling_thermal_power_sensor_1 parameter);

	public Set<IProcess_cooling_thermal_power_sensor_1> getUsesOptionalsProcess_cooling_thermal_power_sensor_1();

    public void addUsesOptionalsProcess_cooling_thermal_power_sensor_2 (IProcess_cooling_thermal_power_sensor_2 parameter);

	public Set<IProcess_cooling_thermal_power_sensor_2> getUsesOptionalsProcess_cooling_thermal_power_sensor_2();

    public void addUsesOptionalsCooling_request_count (ICooling_request_count parameter);

	public Set<ICooling_request_count> getUsesOptionalsCooling_request_count();

    public void addUsesOptionalsHeating_request_count (IHeating_request_count parameter);

	public Set<IHeating_request_count> getUsesOptionalsHeating_request_count();

    public void addUsesOptionalsReturn_water_temperature_sensor (IReturn_water_temperature_sensor parameter);

	public Set<IReturn_water_temperature_sensor> getUsesOptionalsReturn_water_temperature_sensor();

    public void addUsesOptionalsEfficiency_percentage_specification (IEfficiency_percentage_specification parameter);

	public Set<IEfficiency_percentage_specification> getUsesOptionalsEfficiency_percentage_specification();

    public void addUsesOptionalsFlowrate_requirement (IFlowrate_requirement parameter);

	public Set<IFlowrate_requirement> getUsesOptionalsFlowrate_requirement();

    public void addUsesOptionalsHeating_input_thermal_power_capacity (IHeating_input_thermal_power_capacity parameter);

	public Set<IHeating_input_thermal_power_capacity> getUsesOptionalsHeating_input_thermal_power_capacity();

    public void addUsesOptionalsHeating_thermal_power_capacity (IHeating_thermal_power_capacity parameter);

	public Set<IHeating_thermal_power_capacity> getUsesOptionalsHeating_thermal_power_capacity();

    public void addUsesOptionalsCurrent_sensor (ICurrent_sensor parameter);

	public Set<ICurrent_sensor> getUsesOptionalsCurrent_sensor();

    public void addUsesOptionalsFlowrate_capacity (IFlowrate_capacity parameter);

	public Set<IFlowrate_capacity> getUsesOptionalsFlowrate_capacity();

    public void addUsesOptionalsPower_capacity (IPower_capacity parameter);

	public Set<IPower_capacity> getUsesOptionalsPower_capacity();

    public void addUsesOptionalsPower_sensor (IPower_sensor parameter);

	public Set<IPower_sensor> getUsesOptionalsPower_sensor();

    public void addUsesOptionalsPowerfactor_sensor (IPowerfactor_sensor parameter);

	public Set<IPowerfactor_sensor> getUsesOptionalsPowerfactor_sensor();

    public void addUsesOptionalsHeating_percentage_command (IHeating_percentage_command parameter);

	public Set<IHeating_percentage_command> getUsesOptionalsHeating_percentage_command();

    public void addUsesDifferential_pressure_sensor_1 (IDifferential_pressure_sensor_1 parameter);

	public Set<IDifferential_pressure_sensor_1> getUsesDifferential_pressure_sensor_1();

    public void addUsesDifferential_pressure_sensor_2 (IDifferential_pressure_sensor_2 parameter);

	public Set<IDifferential_pressure_sensor_2> getUsesDifferential_pressure_sensor_2();

    public void addUsesDifferential_pressure_setpoint (IDifferential_pressure_setpoint parameter);

	public Set<IDifferential_pressure_setpoint> getUsesDifferential_pressure_setpoint();

    public void addUsesProcess_water_differential_pressure_sensor_1 (IProcess_water_differential_pressure_sensor_1 parameter);

	public Set<IProcess_water_differential_pressure_sensor_1> getUsesProcess_water_differential_pressure_sensor_1();

    public void addUsesProcess_water_differential_pressure_sensor_2 (IProcess_water_differential_pressure_sensor_2 parameter);

	public Set<IProcess_water_differential_pressure_sensor_2> getUsesProcess_water_differential_pressure_sensor_2();

    public void addUsesBypass_valve_percentage_command (IBypass_valve_percentage_command parameter);

	public Set<IBypass_valve_percentage_command> getUsesBypass_valve_percentage_command();

    public void addUsesFlowrate_sensor (IFlowrate_sensor parameter);

	public Set<IFlowrate_sensor> getUsesFlowrate_sensor();

    public void addUsesMin_flowrate_setpoint (IMin_flowrate_setpoint parameter);

	public Set<IMin_flowrate_setpoint> getUsesMin_flowrate_setpoint();

    public void addUsesProcess_return_water_temperature_sensor_1 (IProcess_return_water_temperature_sensor_1 parameter);

	public Set<IProcess_return_water_temperature_sensor_1> getUsesProcess_return_water_temperature_sensor_1();

    public void addUsesProcess_return_water_temperature_sensor_2 (IProcess_return_water_temperature_sensor_2 parameter);

	public Set<IProcess_return_water_temperature_sensor_2> getUsesProcess_return_water_temperature_sensor_2();

    public void addUsesProcess_supply_water_temperature_sensor_1 (IProcess_supply_water_temperature_sensor_1 parameter);

	public Set<IProcess_supply_water_temperature_sensor_1> getUsesProcess_supply_water_temperature_sensor_1();

    public void addUsesProcess_supply_water_temperature_sensor_2 (IProcess_supply_water_temperature_sensor_2 parameter);

	public Set<IProcess_supply_water_temperature_sensor_2> getUsesProcess_supply_water_temperature_sensor_2();

    public void addUsesSupply_water_temperature_sensor (ISupply_water_temperature_sensor parameter);

	public Set<ISupply_water_temperature_sensor> getUsesSupply_water_temperature_sensor();

    public void addUsesSupply_water_temperature_setpoint (ISupply_water_temperature_setpoint parameter);

	public Set<ISupply_water_temperature_setpoint> getUsesSupply_water_temperature_setpoint();

    public void addUsesRun_command (IRun_command parameter);

	public Set<IRun_command> getUsesRun_command();

    public void addUsesRun_status (IRun_status parameter);

	public Set<IRun_status> getUsesRun_status();

    public void addUsesHeater_run_command_1 (IHeater_run_command_1 parameter);

	public Set<IHeater_run_command_1> getUsesHeater_run_command_1();

    public void addUsesHeater_run_command_2 (IHeater_run_command_2 parameter);

	public Set<IHeater_run_command_2> getUsesHeater_run_command_2();

    public void addUsesReturn_water_isolation_valve_percentage_command (IReturn_water_isolation_valve_percentage_command parameter);

	public Set<IReturn_water_isolation_valve_percentage_command> getUsesReturn_water_isolation_valve_percentage_command();

    public void addUsesReturn_water_isolation_valve_percentage_sensor (IReturn_water_isolation_valve_percentage_sensor parameter);

	public Set<IReturn_water_isolation_valve_percentage_sensor> getUsesReturn_water_isolation_valve_percentage_sensor();

    public void addUsesHeater_run_command (IHeater_run_command parameter);

	public Set<IHeater_run_command> getUsesHeater_run_command();

    public void addUsesReturn_water_isolation_valve_command (IReturn_water_isolation_valve_command parameter);

	public Set<IReturn_water_isolation_valve_command> getUsesReturn_water_isolation_valve_command();

    public void addUsesReturn_water_isolation_valve_status (IReturn_water_isolation_valve_status parameter);

	public Set<IReturn_water_isolation_valve_status> getUsesReturn_water_isolation_valve_status();

    public void addUsesSupply_water_isolation_valve_command (ISupply_water_isolation_valve_command parameter);

	public Set<ISupply_water_isolation_valve_command> getUsesSupply_water_isolation_valve_command();

    public void addUsesSupply_water_isolation_valve_status (ISupply_water_isolation_valve_status parameter);

	public Set<ISupply_water_isolation_valve_status> getUsesSupply_water_isolation_valve_status();

}