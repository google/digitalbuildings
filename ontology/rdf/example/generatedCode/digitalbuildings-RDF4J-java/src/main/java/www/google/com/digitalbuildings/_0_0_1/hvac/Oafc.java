package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IControl;
import www.google.com.digitalbuildings._0_0_1.Control;
import www.google.com.digitalbuildings._0_0_1.fields.IEconomizer_mode;
import www.google.com.digitalbuildings._0_0_1.fields.Economizer_mode;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Outside_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IMixed_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Mixed_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Outside_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_flowrate_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Outside_air_flowrate_setpoint;

/**
* Class Oafc 
* Outside Air Flow Control
*/
@SuppressWarnings("serial")
public class Oafc extends www.google.com.digitalbuildings._0_0_1.Control implements IOafc{

	IRI newInstance;
	public Oafc(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Oafc"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesOutside_air_damper_percentage_command (IOutside_air_damper_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IOutside_air_damper_percentage_command> getUsesOutside_air_damper_percentage_command (){
		Set<IOutside_air_damper_percentage_command> UsesOutside_air_damper_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Outside_air_damper_percentage_command) {
				UsesOutside_air_damper_percentage_command.add((Outside_air_damper_percentage_command)action);
			}
		});
		return UsesOutside_air_damper_percentage_command;
	}


  public void addUsesOutside_air_flowrate_sensor (IOutside_air_flowrate_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IOutside_air_flowrate_sensor> getUsesOutside_air_flowrate_sensor (){
		Set<IOutside_air_flowrate_sensor> UsesOutside_air_flowrate_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Outside_air_flowrate_sensor) {
				UsesOutside_air_flowrate_sensor.add((Outside_air_flowrate_sensor)action);
			}
		});
		return UsesOutside_air_flowrate_sensor;
	}


  public void addUsesOutside_air_flowrate_setpoint (IOutside_air_flowrate_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IOutside_air_flowrate_setpoint> getUsesOutside_air_flowrate_setpoint (){
		Set<IOutside_air_flowrate_setpoint> UsesOutside_air_flowrate_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Outside_air_flowrate_setpoint) {
				UsesOutside_air_flowrate_setpoint.add((Outside_air_flowrate_setpoint)action);
			}
		});
		return UsesOutside_air_flowrate_setpoint;
	}


  public void addUsesOptionalsEconomizer_mode (IEconomizer_mode parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IEconomizer_mode> getUsesOptionalsEconomizer_mode (){
		Set<IEconomizer_mode> UsesOptionalsEconomizer_mode = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Economizer_mode) {
				UsesOptionalsEconomizer_mode.add((Economizer_mode)action);
			}
		});
		return UsesOptionalsEconomizer_mode;
	}


  public void addUsesOptionalsMixed_air_temperature_sensor (IMixed_air_temperature_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IMixed_air_temperature_sensor> getUsesOptionalsMixed_air_temperature_sensor (){
		Set<IMixed_air_temperature_sensor> UsesOptionalsMixed_air_temperature_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Mixed_air_temperature_sensor) {
				UsesOptionalsMixed_air_temperature_sensor.add((Mixed_air_temperature_sensor)action);
			}
		});
		return UsesOptionalsMixed_air_temperature_sensor;
	}

	public static Set<IOafc> getAllOafcsObjectsCreated(){
		Set<IOafc> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Oafc")).subjects().stream()
		.map(mapper->(IOafc)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}