package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.Operational;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_water_differential_pressure_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.Process_water_differential_pressure_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_water_differential_pressure_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.Process_water_differential_pressure_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IHeater_run_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.Heater_run_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_isolation_valve_status;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_water_isolation_valve_status;
import www.google.com.digitalbuildings._0_0_1.fields.IFlowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IDifferential_pressure_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.Differential_pressure_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IFlowrate_requirement;
import www.google.com.digitalbuildings._0_0_1.fields.Flowrate_requirement;
import www.google.com.digitalbuildings._0_0_1.fields.IDifferential_pressure_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.Differential_pressure_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_supply_water_temperature_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.Process_supply_water_temperature_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICooling_request_count;
import www.google.com.digitalbuildings._0_0_1.fields.Cooling_request_count;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_water_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IRun_status;
import www.google.com.digitalbuildings._0_0_1.fields.Run_status;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_input_thermal_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.Heating_input_thermal_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_return_water_temperature_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.Process_return_water_temperature_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IHeater_run_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.Heater_run_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_return_water_temperature_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.Process_return_water_temperature_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_cooling_thermal_power_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.Process_cooling_thermal_power_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_cooling_thermal_power_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.Process_cooling_thermal_power_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IPower_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Power_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IBypass_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Bypass_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_request_count;
import www.google.com.digitalbuildings._0_0_1.fields.Heating_request_count;
import www.google.com.digitalbuildings._0_0_1.fields.IMin_flowrate_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Min_flowrate_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IRun_command;
import www.google.com.digitalbuildings._0_0_1.fields.Run_command;
import www.google.com.digitalbuildings._0_0_1.fields.ICurrent_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Current_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IPowerfactor_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Powerfactor_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IDifferential_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Differential_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IHeater_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.Heater_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_thermal_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.Heating_thermal_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_isolation_valve_status;
import www.google.com.digitalbuildings._0_0_1.fields.Return_water_isolation_valve_status;
import www.google.com.digitalbuildings._0_0_1.fields.IEfficiency_percentage_specification;
import www.google.com.digitalbuildings._0_0_1.fields.Efficiency_percentage_specification;
import www.google.com.digitalbuildings._0_0_1.fields.IPower_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.Power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_isolation_valve_command;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_water_isolation_valve_command;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Return_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Heating_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_isolation_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Return_water_isolation_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_isolation_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Return_water_isolation_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IPressurization_request_count;
import www.google.com.digitalbuildings._0_0_1.fields.Pressurization_request_count;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_supply_water_temperature_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.Process_supply_water_temperature_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IFlowrate_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.Flowrate_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_isolation_valve_command;
import www.google.com.digitalbuildings._0_0_1.fields.Return_water_isolation_valve_command;

/**
* Class Wdpc2x 
* Differential pressure control in whichever system, 2 sensors.
*/
@SuppressWarnings("serial")
public class Wdpc2x extends www.google.com.digitalbuildings._0_0_1.Operational implements IWdpc2x{

	IRI newInstance;
	public Wdpc2x(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Wdpc2x"));
	}

	public IRI iri()
	{
		return newInstance;
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


  public void addUsesOptionalsProcess_cooling_thermal_power_sensor_1 (IProcess_cooling_thermal_power_sensor_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IProcess_cooling_thermal_power_sensor_1> getUsesOptionalsProcess_cooling_thermal_power_sensor_1 (){
		Set<IProcess_cooling_thermal_power_sensor_1> UsesOptionalsProcess_cooling_thermal_power_sensor_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Process_cooling_thermal_power_sensor_1) {
				UsesOptionalsProcess_cooling_thermal_power_sensor_1.add((Process_cooling_thermal_power_sensor_1)action);
			}
		});
		return UsesOptionalsProcess_cooling_thermal_power_sensor_1;
	}


  public void addUsesOptionalsProcess_cooling_thermal_power_sensor_2 (IProcess_cooling_thermal_power_sensor_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IProcess_cooling_thermal_power_sensor_2> getUsesOptionalsProcess_cooling_thermal_power_sensor_2 (){
		Set<IProcess_cooling_thermal_power_sensor_2> UsesOptionalsProcess_cooling_thermal_power_sensor_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Process_cooling_thermal_power_sensor_2) {
				UsesOptionalsProcess_cooling_thermal_power_sensor_2.add((Process_cooling_thermal_power_sensor_2)action);
			}
		});
		return UsesOptionalsProcess_cooling_thermal_power_sensor_2;
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


  public void addUsesDifferential_pressure_sensor_1 (IDifferential_pressure_sensor_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IDifferential_pressure_sensor_1> getUsesDifferential_pressure_sensor_1 (){
		Set<IDifferential_pressure_sensor_1> UsesDifferential_pressure_sensor_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Differential_pressure_sensor_1) {
				UsesDifferential_pressure_sensor_1.add((Differential_pressure_sensor_1)action);
			}
		});
		return UsesDifferential_pressure_sensor_1;
	}


  public void addUsesDifferential_pressure_sensor_2 (IDifferential_pressure_sensor_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IDifferential_pressure_sensor_2> getUsesDifferential_pressure_sensor_2 (){
		Set<IDifferential_pressure_sensor_2> UsesDifferential_pressure_sensor_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Differential_pressure_sensor_2) {
				UsesDifferential_pressure_sensor_2.add((Differential_pressure_sensor_2)action);
			}
		});
		return UsesDifferential_pressure_sensor_2;
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


  public void addUsesProcess_water_differential_pressure_sensor_1 (IProcess_water_differential_pressure_sensor_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IProcess_water_differential_pressure_sensor_1> getUsesProcess_water_differential_pressure_sensor_1 (){
		Set<IProcess_water_differential_pressure_sensor_1> UsesProcess_water_differential_pressure_sensor_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Process_water_differential_pressure_sensor_1) {
				UsesProcess_water_differential_pressure_sensor_1.add((Process_water_differential_pressure_sensor_1)action);
			}
		});
		return UsesProcess_water_differential_pressure_sensor_1;
	}


  public void addUsesProcess_water_differential_pressure_sensor_2 (IProcess_water_differential_pressure_sensor_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IProcess_water_differential_pressure_sensor_2> getUsesProcess_water_differential_pressure_sensor_2 (){
		Set<IProcess_water_differential_pressure_sensor_2> UsesProcess_water_differential_pressure_sensor_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Process_water_differential_pressure_sensor_2) {
				UsesProcess_water_differential_pressure_sensor_2.add((Process_water_differential_pressure_sensor_2)action);
			}
		});
		return UsesProcess_water_differential_pressure_sensor_2;
	}


  public void addUsesBypass_valve_percentage_command (IBypass_valve_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IBypass_valve_percentage_command> getUsesBypass_valve_percentage_command (){
		Set<IBypass_valve_percentage_command> UsesBypass_valve_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Bypass_valve_percentage_command) {
				UsesBypass_valve_percentage_command.add((Bypass_valve_percentage_command)action);
			}
		});
		return UsesBypass_valve_percentage_command;
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


  public void addUsesMin_flowrate_setpoint (IMin_flowrate_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IMin_flowrate_setpoint> getUsesMin_flowrate_setpoint (){
		Set<IMin_flowrate_setpoint> UsesMin_flowrate_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Min_flowrate_setpoint) {
				UsesMin_flowrate_setpoint.add((Min_flowrate_setpoint)action);
			}
		});
		return UsesMin_flowrate_setpoint;
	}


  public void addUsesProcess_return_water_temperature_sensor_1 (IProcess_return_water_temperature_sensor_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IProcess_return_water_temperature_sensor_1> getUsesProcess_return_water_temperature_sensor_1 (){
		Set<IProcess_return_water_temperature_sensor_1> UsesProcess_return_water_temperature_sensor_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Process_return_water_temperature_sensor_1) {
				UsesProcess_return_water_temperature_sensor_1.add((Process_return_water_temperature_sensor_1)action);
			}
		});
		return UsesProcess_return_water_temperature_sensor_1;
	}


  public void addUsesProcess_return_water_temperature_sensor_2 (IProcess_return_water_temperature_sensor_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IProcess_return_water_temperature_sensor_2> getUsesProcess_return_water_temperature_sensor_2 (){
		Set<IProcess_return_water_temperature_sensor_2> UsesProcess_return_water_temperature_sensor_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Process_return_water_temperature_sensor_2) {
				UsesProcess_return_water_temperature_sensor_2.add((Process_return_water_temperature_sensor_2)action);
			}
		});
		return UsesProcess_return_water_temperature_sensor_2;
	}


  public void addUsesProcess_supply_water_temperature_sensor_1 (IProcess_supply_water_temperature_sensor_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IProcess_supply_water_temperature_sensor_1> getUsesProcess_supply_water_temperature_sensor_1 (){
		Set<IProcess_supply_water_temperature_sensor_1> UsesProcess_supply_water_temperature_sensor_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Process_supply_water_temperature_sensor_1) {
				UsesProcess_supply_water_temperature_sensor_1.add((Process_supply_water_temperature_sensor_1)action);
			}
		});
		return UsesProcess_supply_water_temperature_sensor_1;
	}


  public void addUsesProcess_supply_water_temperature_sensor_2 (IProcess_supply_water_temperature_sensor_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IProcess_supply_water_temperature_sensor_2> getUsesProcess_supply_water_temperature_sensor_2 (){
		Set<IProcess_supply_water_temperature_sensor_2> UsesProcess_supply_water_temperature_sensor_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Process_supply_water_temperature_sensor_2) {
				UsesProcess_supply_water_temperature_sensor_2.add((Process_supply_water_temperature_sensor_2)action);
			}
		});
		return UsesProcess_supply_water_temperature_sensor_2;
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

	public static Set<IWdpc2x> getAllWdpc2xsObjectsCreated(){
		Set<IWdpc2x> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Wdpc2x")).subjects().stream()
		.map(mapper->(IWdpc2x)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}