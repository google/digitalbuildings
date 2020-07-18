package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IControl;
import www.google.com.digitalbuildings._0_0_1.Control;
import www.google.com.digitalbuildings._0_0_1.fields.IHeater_run_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.Heater_run_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_air_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_thermal_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.Heating_thermal_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Heating_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IHeater_run_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.Heater_run_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.IHeater_run_command_3;
import www.google.com.digitalbuildings._0_0_1.fields.Heater_run_command_3;

/**
* Class Ht3sc 
* Three gas or electric heater control on supply side.
*/
@SuppressWarnings("serial")
public class Ht3sc extends www.google.com.digitalbuildings._0_0_1.Control implements IHt3sc{

	IRI newInstance;
	public Ht3sc(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Ht3sc"));
	}

	public IRI iri()
	{
		return newInstance;
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

	public static Set<IHt3sc> getAllHt3scsObjectsCreated(){
		Set<IHt3sc> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Ht3sc")).subjects().stream()
		.map(mapper->(IHt3sc)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}