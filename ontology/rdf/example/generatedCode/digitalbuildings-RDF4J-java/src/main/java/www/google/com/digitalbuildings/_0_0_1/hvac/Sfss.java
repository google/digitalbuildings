package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.Operational;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_current_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_current_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_power_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_power_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_flowrate_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_air_flowrate_capacity;

/**
* Class Sfss 
* Basic combination of supply fan run command and status (start/stop).
*/
@SuppressWarnings("serial")
public class Sfss extends www.google.com.digitalbuildings._0_0_1.Operational implements ISfss{

	IRI newInstance;
	public Sfss(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Sfss"));
	}

	public IRI iri()
	{
		return newInstance;
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

	public static Set<ISfss> getAllSfsssObjectsCreated(){
		Set<ISfss> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Sfss")).subjects().stream()
		.map(mapper->(ISfss)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}