package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.Operational;
import www.google.com.digitalbuildings._0_0_1.fields.IDehumidification_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.Dehumidification_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_dehumidification_relative_humidity_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_air_dehumidification_relative_humidity_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IHumidification_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.Humidification_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_relative_humidity_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_air_relative_humidity_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_humidification_relative_humidity_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_air_humidification_relative_humidity_setpoint;

/**
* Class Shc 
* Supply air relative humidity control.
*/
@SuppressWarnings("serial")
public class Shc extends www.google.com.digitalbuildings._0_0_1.Operational implements IShc{

	IRI newInstance;
	public Shc(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Shc"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesDehumidification_run_command (IDehumidification_run_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IDehumidification_run_command> getUsesDehumidification_run_command (){
		Set<IDehumidification_run_command> UsesDehumidification_run_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Dehumidification_run_command) {
				UsesDehumidification_run_command.add((Dehumidification_run_command)action);
			}
		});
		return UsesDehumidification_run_command;
	}


  public void addUsesHumidification_run_command (IHumidification_run_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IHumidification_run_command> getUsesHumidification_run_command (){
		Set<IHumidification_run_command> UsesHumidification_run_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Humidification_run_command) {
				UsesHumidification_run_command.add((Humidification_run_command)action);
			}
		});
		return UsesHumidification_run_command;
	}


  public void addUsesSupply_air_dehumidification_relative_humidity_setpoint (ISupply_air_dehumidification_relative_humidity_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_air_dehumidification_relative_humidity_setpoint> getUsesSupply_air_dehumidification_relative_humidity_setpoint (){
		Set<ISupply_air_dehumidification_relative_humidity_setpoint> UsesSupply_air_dehumidification_relative_humidity_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_air_dehumidification_relative_humidity_setpoint) {
				UsesSupply_air_dehumidification_relative_humidity_setpoint.add((Supply_air_dehumidification_relative_humidity_setpoint)action);
			}
		});
		return UsesSupply_air_dehumidification_relative_humidity_setpoint;
	}


  public void addUsesSupply_air_humidification_relative_humidity_setpoint (ISupply_air_humidification_relative_humidity_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_air_humidification_relative_humidity_setpoint> getUsesSupply_air_humidification_relative_humidity_setpoint (){
		Set<ISupply_air_humidification_relative_humidity_setpoint> UsesSupply_air_humidification_relative_humidity_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_air_humidification_relative_humidity_setpoint) {
				UsesSupply_air_humidification_relative_humidity_setpoint.add((Supply_air_humidification_relative_humidity_setpoint)action);
			}
		});
		return UsesSupply_air_humidification_relative_humidity_setpoint;
	}


  public void addUsesSupply_air_relative_humidity_sensor (ISupply_air_relative_humidity_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_air_relative_humidity_sensor> getUsesSupply_air_relative_humidity_sensor (){
		Set<ISupply_air_relative_humidity_sensor> UsesSupply_air_relative_humidity_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_air_relative_humidity_sensor) {
				UsesSupply_air_relative_humidity_sensor.add((Supply_air_relative_humidity_sensor)action);
			}
		});
		return UsesSupply_air_relative_humidity_sensor;
	}

	public static Set<IShc> getAllShcsObjectsCreated(){
		Set<IShc> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Shc")).subjects().stream()
		.map(mapper->(IShc)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}