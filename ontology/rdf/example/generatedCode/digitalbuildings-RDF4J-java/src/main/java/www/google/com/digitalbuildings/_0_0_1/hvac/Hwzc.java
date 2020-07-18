package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IControl;
import www.google.com.digitalbuildings._0_0_1.Control;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_thermal_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.Heating_thermal_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_water_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Heating_water_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_water_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Heating_water_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_heating_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_air_heating_temperature_setpoint;

/**
* Class Hwzc 
* Heating water valve monitoring on zone side (DSP/CSP).
*/
@SuppressWarnings("serial")
public class Hwzc extends www.google.com.digitalbuildings._0_0_1.Control implements IHwzc{

	IRI newInstance;
	public Hwzc(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Hwzc"));
	}

	public IRI iri()
	{
		return newInstance;
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

	public static Set<IHwzc> getAllHwzcsObjectsCreated(){
		Set<IHwzc> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Hwzc")).subjects().stream()
		.map(mapper->(IHwzc)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}