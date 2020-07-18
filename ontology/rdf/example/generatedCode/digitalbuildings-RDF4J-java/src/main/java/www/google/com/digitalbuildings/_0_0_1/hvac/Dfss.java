package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.Operational;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_fan_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_current_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_fan_current_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_power_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_fan_power_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_air_flowrate_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_air_flowrate_capacity;

/**
* Class Dfss 
* Basic combination of discharge fan run command and status (start/stop).
*/
@SuppressWarnings("serial")
public class Dfss extends www.google.com.digitalbuildings._0_0_1.Operational implements IDfss{

	IRI newInstance;
	public Dfss(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Dfss"));
	}

	public IRI iri()
	{
		return newInstance;
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

	public static Set<IDfss> getAllDfsssObjectsCreated(){
		Set<IDfss> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Dfss")).subjects().stream()
		.map(mapper->(IDfss)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}