package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.Operational;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_current_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_current_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_power_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_power_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_speed_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_speed_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_speed_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_speed_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_speed_frequency_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_speed_frequency_sensor;

/**
* Class Sfvsc 
* Variable speed control for supply fans.
*/
@SuppressWarnings("serial")
public class Sfvsc extends www.google.com.digitalbuildings._0_0_1.Operational implements ISfvsc{

	IRI newInstance;
	public Sfvsc(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Sfvsc"));
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


  public void addUsesSupply_fan_speed_percentage_command (ISupply_fan_speed_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_fan_speed_percentage_command> getUsesSupply_fan_speed_percentage_command (){
		Set<ISupply_fan_speed_percentage_command> UsesSupply_fan_speed_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_fan_speed_percentage_command) {
				UsesSupply_fan_speed_percentage_command.add((Supply_fan_speed_percentage_command)action);
			}
		});
		return UsesSupply_fan_speed_percentage_command;
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


  public void addUsesOptionalsSupply_fan_speed_frequency_sensor (ISupply_fan_speed_frequency_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<ISupply_fan_speed_frequency_sensor> getUsesOptionalsSupply_fan_speed_frequency_sensor (){
		Set<ISupply_fan_speed_frequency_sensor> UsesOptionalsSupply_fan_speed_frequency_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_fan_speed_frequency_sensor) {
				UsesOptionalsSupply_fan_speed_frequency_sensor.add((Supply_fan_speed_frequency_sensor)action);
			}
		});
		return UsesOptionalsSupply_fan_speed_frequency_sensor;
	}


  public void addUsesOptionalsSupply_fan_speed_percentage_sensor (ISupply_fan_speed_percentage_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<ISupply_fan_speed_percentage_sensor> getUsesOptionalsSupply_fan_speed_percentage_sensor (){
		Set<ISupply_fan_speed_percentage_sensor> UsesOptionalsSupply_fan_speed_percentage_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_fan_speed_percentage_sensor) {
				UsesOptionalsSupply_fan_speed_percentage_sensor.add((Supply_fan_speed_percentage_sensor)action);
			}
		});
		return UsesOptionalsSupply_fan_speed_percentage_sensor;
	}

	public static Set<ISfvsc> getAllSfvscsObjectsCreated(){
		Set<ISfvsc> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Sfvsc")).subjects().stream()
		.map(mapper->(ISfvsc)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}