package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IControl;
import www.google.com.digitalbuildings._0_0_1.Control;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Heating_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ICooling_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Cooling_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_thermal_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.Heating_thermal_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_heating_flowrate_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_air_heating_flowrate_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_air_flowrate_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Heating_air_flowrate_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICooling_thermal_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.Cooling_thermal_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.ICooling_air_flowrate_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Cooling_air_flowrate_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IRun_command;
import www.google.com.digitalbuildings._0_0_1.fields.Run_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_ventilation_flowrate_requirement;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_air_ventilation_flowrate_requirement;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_cooling_flowrate_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_air_cooling_flowrate_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Heating_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICooling_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Cooling_air_damper_percentage_command;

/**
* Class Dd 
* Dual duct flow control (hot deck, cold deck).
*/
@SuppressWarnings("serial")
public class Dd extends www.google.com.digitalbuildings._0_0_1.Control implements IDd{

	IRI newInstance;
	public Dd(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Dd"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesCooling_air_damper_percentage_command (ICooling_air_damper_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ICooling_air_damper_percentage_command> getUsesCooling_air_damper_percentage_command (){
		Set<ICooling_air_damper_percentage_command> UsesCooling_air_damper_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Cooling_air_damper_percentage_command) {
				UsesCooling_air_damper_percentage_command.add((Cooling_air_damper_percentage_command)action);
			}
		});
		return UsesCooling_air_damper_percentage_command;
	}


  public void addUsesCooling_air_flowrate_sensor (ICooling_air_flowrate_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ICooling_air_flowrate_sensor> getUsesCooling_air_flowrate_sensor (){
		Set<ICooling_air_flowrate_sensor> UsesCooling_air_flowrate_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Cooling_air_flowrate_sensor) {
				UsesCooling_air_flowrate_sensor.add((Cooling_air_flowrate_sensor)action);
			}
		});
		return UsesCooling_air_flowrate_sensor;
	}


  public void addUsesCooling_air_flowrate_setpoint (ICooling_air_flowrate_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ICooling_air_flowrate_setpoint> getUsesCooling_air_flowrate_setpoint (){
		Set<ICooling_air_flowrate_setpoint> UsesCooling_air_flowrate_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Cooling_air_flowrate_setpoint) {
				UsesCooling_air_flowrate_setpoint.add((Cooling_air_flowrate_setpoint)action);
			}
		});
		return UsesCooling_air_flowrate_setpoint;
	}


  public void addUsesHeating_air_damper_percentage_command (IHeating_air_damper_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IHeating_air_damper_percentage_command> getUsesHeating_air_damper_percentage_command (){
		Set<IHeating_air_damper_percentage_command> UsesHeating_air_damper_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Heating_air_damper_percentage_command) {
				UsesHeating_air_damper_percentage_command.add((Heating_air_damper_percentage_command)action);
			}
		});
		return UsesHeating_air_damper_percentage_command;
	}


  public void addUsesHeating_air_flowrate_sensor (IHeating_air_flowrate_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IHeating_air_flowrate_sensor> getUsesHeating_air_flowrate_sensor (){
		Set<IHeating_air_flowrate_sensor> UsesHeating_air_flowrate_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Heating_air_flowrate_sensor) {
				UsesHeating_air_flowrate_sensor.add((Heating_air_flowrate_sensor)action);
			}
		});
		return UsesHeating_air_flowrate_sensor;
	}


  public void addUsesHeating_air_flowrate_setpoint (IHeating_air_flowrate_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IHeating_air_flowrate_setpoint> getUsesHeating_air_flowrate_setpoint (){
		Set<IHeating_air_flowrate_setpoint> UsesHeating_air_flowrate_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Heating_air_flowrate_setpoint) {
				UsesHeating_air_flowrate_setpoint.add((Heating_air_flowrate_setpoint)action);
			}
		});
		return UsesHeating_air_flowrate_setpoint;
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


  public void addUsesOptionalsSupply_air_cooling_flowrate_capacity (ISupply_air_cooling_flowrate_capacity parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<ISupply_air_cooling_flowrate_capacity> getUsesOptionalsSupply_air_cooling_flowrate_capacity (){
		Set<ISupply_air_cooling_flowrate_capacity> UsesOptionalsSupply_air_cooling_flowrate_capacity = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_air_cooling_flowrate_capacity) {
				UsesOptionalsSupply_air_cooling_flowrate_capacity.add((Supply_air_cooling_flowrate_capacity)action);
			}
		});
		return UsesOptionalsSupply_air_cooling_flowrate_capacity;
	}


  public void addUsesOptionalsSupply_air_heating_flowrate_capacity (ISupply_air_heating_flowrate_capacity parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<ISupply_air_heating_flowrate_capacity> getUsesOptionalsSupply_air_heating_flowrate_capacity (){
		Set<ISupply_air_heating_flowrate_capacity> UsesOptionalsSupply_air_heating_flowrate_capacity = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_air_heating_flowrate_capacity) {
				UsesOptionalsSupply_air_heating_flowrate_capacity.add((Supply_air_heating_flowrate_capacity)action);
			}
		});
		return UsesOptionalsSupply_air_heating_flowrate_capacity;
	}


  public void addUsesOptionalsSupply_air_ventilation_flowrate_requirement (ISupply_air_ventilation_flowrate_requirement parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<ISupply_air_ventilation_flowrate_requirement> getUsesOptionalsSupply_air_ventilation_flowrate_requirement (){
		Set<ISupply_air_ventilation_flowrate_requirement> UsesOptionalsSupply_air_ventilation_flowrate_requirement = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_air_ventilation_flowrate_requirement) {
				UsesOptionalsSupply_air_ventilation_flowrate_requirement.add((Supply_air_ventilation_flowrate_requirement)action);
			}
		});
		return UsesOptionalsSupply_air_ventilation_flowrate_requirement;
	}

	public static Set<IDd> getAllDdsObjectsCreated(){
		Set<IDd> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Dd")).subjects().stream()
		.map(mapper->(IDd)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}