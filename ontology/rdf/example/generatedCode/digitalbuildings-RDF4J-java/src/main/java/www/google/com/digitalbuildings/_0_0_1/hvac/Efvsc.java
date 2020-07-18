package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.Operational;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_current_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_current_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_speed_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_speed_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_power_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_power_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_frequency_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_speed_frequency_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_run_command;

/**
* Class Efvsc 
* Variable speed control for exhaust fans.
*/
@SuppressWarnings("serial")
public class Efvsc extends www.google.com.digitalbuildings._0_0_1.Operational implements IEfvsc{

	IRI newInstance;
	public Efvsc(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Efvsc"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesOptionalsExhaust_fan_current_sensor (IExhaust_fan_current_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IExhaust_fan_current_sensor> getUsesOptionalsExhaust_fan_current_sensor (){
		Set<IExhaust_fan_current_sensor> UsesOptionalsExhaust_fan_current_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_current_sensor) {
				UsesOptionalsExhaust_fan_current_sensor.add((Exhaust_fan_current_sensor)action);
			}
		});
		return UsesOptionalsExhaust_fan_current_sensor;
	}


  public void addUsesOptionalsExhaust_fan_power_sensor (IExhaust_fan_power_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IExhaust_fan_power_sensor> getUsesOptionalsExhaust_fan_power_sensor (){
		Set<IExhaust_fan_power_sensor> UsesOptionalsExhaust_fan_power_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_power_sensor) {
				UsesOptionalsExhaust_fan_power_sensor.add((Exhaust_fan_power_sensor)action);
			}
		});
		return UsesOptionalsExhaust_fan_power_sensor;
	}


  public void addUsesOptionalsExhaust_fan_speed_frequency_sensor (IExhaust_fan_speed_frequency_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IExhaust_fan_speed_frequency_sensor> getUsesOptionalsExhaust_fan_speed_frequency_sensor (){
		Set<IExhaust_fan_speed_frequency_sensor> UsesOptionalsExhaust_fan_speed_frequency_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_speed_frequency_sensor) {
				UsesOptionalsExhaust_fan_speed_frequency_sensor.add((Exhaust_fan_speed_frequency_sensor)action);
			}
		});
		return UsesOptionalsExhaust_fan_speed_frequency_sensor;
	}


  public void addUsesOptionalsExhaust_fan_speed_percentage_sensor (IExhaust_fan_speed_percentage_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IExhaust_fan_speed_percentage_sensor> getUsesOptionalsExhaust_fan_speed_percentage_sensor (){
		Set<IExhaust_fan_speed_percentage_sensor> UsesOptionalsExhaust_fan_speed_percentage_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_speed_percentage_sensor) {
				UsesOptionalsExhaust_fan_speed_percentage_sensor.add((Exhaust_fan_speed_percentage_sensor)action);
			}
		});
		return UsesOptionalsExhaust_fan_speed_percentage_sensor;
	}


  public void addUsesExhaust_fan_run_command (IExhaust_fan_run_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IExhaust_fan_run_command> getUsesExhaust_fan_run_command (){
		Set<IExhaust_fan_run_command> UsesExhaust_fan_run_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_run_command) {
				UsesExhaust_fan_run_command.add((Exhaust_fan_run_command)action);
			}
		});
		return UsesExhaust_fan_run_command;
	}


  public void addUsesExhaust_fan_run_status (IExhaust_fan_run_status parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IExhaust_fan_run_status> getUsesExhaust_fan_run_status (){
		Set<IExhaust_fan_run_status> UsesExhaust_fan_run_status = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_run_status) {
				UsesExhaust_fan_run_status.add((Exhaust_fan_run_status)action);
			}
		});
		return UsesExhaust_fan_run_status;
	}


  public void addUsesExhaust_fan_speed_percentage_command (IExhaust_fan_speed_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IExhaust_fan_speed_percentage_command> getUsesExhaust_fan_speed_percentage_command (){
		Set<IExhaust_fan_speed_percentage_command> UsesExhaust_fan_speed_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_speed_percentage_command) {
				UsesExhaust_fan_speed_percentage_command.add((Exhaust_fan_speed_percentage_command)action);
			}
		});
		return UsesExhaust_fan_speed_percentage_command;
	}

	public static Set<IEfvsc> getAllEfvscsObjectsCreated(){
		Set<IEfvsc> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Efvsc")).subjects().stream()
		.map(mapper->(IEfvsc)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}