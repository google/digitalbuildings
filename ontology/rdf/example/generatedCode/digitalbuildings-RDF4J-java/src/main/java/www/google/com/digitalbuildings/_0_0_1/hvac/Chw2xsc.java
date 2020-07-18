package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IControl;
import www.google.com.digitalbuildings._0_0_1.Control;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_water_valve_percentage_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.Chilled_water_valve_percentage_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.ILeaving_cooling_coil_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Leaving_cooling_coil_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_air_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.ICooling_thermal_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.Cooling_thermal_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_water_valve_percentage_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.Chilled_water_valve_percentage_command_2;

/**
* Class Chw2xsc 
* Two chilled water valves.
*/
@SuppressWarnings("serial")
public class Chw2xsc extends www.google.com.digitalbuildings._0_0_1.Control implements IChw2xsc{

	IRI newInstance;
	public Chw2xsc(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Chw2xsc"));
	}

	public IRI iri()
	{
		return newInstance;
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


  public void addUsesChilled_water_valve_percentage_command_1 (IChilled_water_valve_percentage_command_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IChilled_water_valve_percentage_command_1> getUsesChilled_water_valve_percentage_command_1 (){
		Set<IChilled_water_valve_percentage_command_1> UsesChilled_water_valve_percentage_command_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Chilled_water_valve_percentage_command_1) {
				UsesChilled_water_valve_percentage_command_1.add((Chilled_water_valve_percentage_command_1)action);
			}
		});
		return UsesChilled_water_valve_percentage_command_1;
	}


  public void addUsesChilled_water_valve_percentage_command_2 (IChilled_water_valve_percentage_command_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IChilled_water_valve_percentage_command_2> getUsesChilled_water_valve_percentage_command_2 (){
		Set<IChilled_water_valve_percentage_command_2> UsesChilled_water_valve_percentage_command_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Chilled_water_valve_percentage_command_2) {
				UsesChilled_water_valve_percentage_command_2.add((Chilled_water_valve_percentage_command_2)action);
			}
		});
		return UsesChilled_water_valve_percentage_command_2;
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

	public static Set<IChw2xsc> getAllChw2xscsObjectsCreated(){
		Set<IChw2xsc> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Chw2xsc")).subjects().stream()
		.map(mapper->(IChw2xsc)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}