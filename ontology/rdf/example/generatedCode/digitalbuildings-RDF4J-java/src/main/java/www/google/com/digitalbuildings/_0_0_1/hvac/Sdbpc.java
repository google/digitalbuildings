package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.Monitoring;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_static_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_air_static_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_damper_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_air_damper_percentage_sensor;

/**
* Class Sdbpc 
* Back-pressure controlling supply damper.
*/
@SuppressWarnings("serial")
public class Sdbpc extends www.google.com.digitalbuildings._0_0_1.Monitoring implements ISdbpc{

	IRI newInstance;
	public Sdbpc(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Sdbpc"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesOptionalsSupply_air_flowrate_sensor (ISupply_air_flowrate_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<ISupply_air_flowrate_sensor> getUsesOptionalsSupply_air_flowrate_sensor (){
		Set<ISupply_air_flowrate_sensor> UsesOptionalsSupply_air_flowrate_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_air_flowrate_sensor) {
				UsesOptionalsSupply_air_flowrate_sensor.add((Supply_air_flowrate_sensor)action);
			}
		});
		return UsesOptionalsSupply_air_flowrate_sensor;
	}


  public void addUsesSupply_air_damper_percentage_command (ISupply_air_damper_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_air_damper_percentage_command> getUsesSupply_air_damper_percentage_command (){
		Set<ISupply_air_damper_percentage_command> UsesSupply_air_damper_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_air_damper_percentage_command) {
				UsesSupply_air_damper_percentage_command.add((Supply_air_damper_percentage_command)action);
			}
		});
		return UsesSupply_air_damper_percentage_command;
	}


  public void addUsesSupply_air_damper_percentage_sensor (ISupply_air_damper_percentage_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_air_damper_percentage_sensor> getUsesSupply_air_damper_percentage_sensor (){
		Set<ISupply_air_damper_percentage_sensor> UsesSupply_air_damper_percentage_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_air_damper_percentage_sensor) {
				UsesSupply_air_damper_percentage_sensor.add((Supply_air_damper_percentage_sensor)action);
			}
		});
		return UsesSupply_air_damper_percentage_sensor;
	}


  public void addUsesSupply_air_static_pressure_sensor (ISupply_air_static_pressure_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_air_static_pressure_sensor> getUsesSupply_air_static_pressure_sensor (){
		Set<ISupply_air_static_pressure_sensor> UsesSupply_air_static_pressure_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_air_static_pressure_sensor) {
				UsesSupply_air_static_pressure_sensor.add((Supply_air_static_pressure_sensor)action);
			}
		});
		return UsesSupply_air_static_pressure_sensor;
	}


  public void addUsesSupply_air_static_pressure_setpoint (ISupply_air_static_pressure_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_air_static_pressure_setpoint> getUsesSupply_air_static_pressure_setpoint (){
		Set<ISupply_air_static_pressure_setpoint> UsesSupply_air_static_pressure_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_air_static_pressure_setpoint) {
				UsesSupply_air_static_pressure_setpoint.add((Supply_air_static_pressure_setpoint)action);
			}
		});
		return UsesSupply_air_static_pressure_setpoint;
	}

	public static Set<ISdbpc> getAllSdbpcsObjectsCreated(){
		Set<ISdbpc> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Sdbpc")).subjects().stream()
		.map(mapper->(ISdbpc)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}