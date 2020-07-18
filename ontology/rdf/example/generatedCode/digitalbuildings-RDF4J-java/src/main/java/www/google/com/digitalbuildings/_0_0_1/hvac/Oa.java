package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.Monitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_relative_humidity_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Outside_air_relative_humidity_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_specificenthalpy_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Outside_air_specificenthalpy_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_dewpoint_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Outside_air_dewpoint_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Outside_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_wetbulb_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Outside_air_wetbulb_temperature_sensor;

/**
* Class Oa 
* Basic weather station (drybulb temp and humidity).
*/
@SuppressWarnings("serial")
public class Oa extends www.google.com.digitalbuildings._0_0_1.Monitoring implements IOa{

	IRI newInstance;
	public Oa(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Oa"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesOptionalsOutside_air_dewpoint_temperature_sensor (IOutside_air_dewpoint_temperature_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IOutside_air_dewpoint_temperature_sensor> getUsesOptionalsOutside_air_dewpoint_temperature_sensor (){
		Set<IOutside_air_dewpoint_temperature_sensor> UsesOptionalsOutside_air_dewpoint_temperature_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Outside_air_dewpoint_temperature_sensor) {
				UsesOptionalsOutside_air_dewpoint_temperature_sensor.add((Outside_air_dewpoint_temperature_sensor)action);
			}
		});
		return UsesOptionalsOutside_air_dewpoint_temperature_sensor;
	}


  public void addUsesOptionalsOutside_air_relative_humidity_sensor (IOutside_air_relative_humidity_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IOutside_air_relative_humidity_sensor> getUsesOptionalsOutside_air_relative_humidity_sensor (){
		Set<IOutside_air_relative_humidity_sensor> UsesOptionalsOutside_air_relative_humidity_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Outside_air_relative_humidity_sensor) {
				UsesOptionalsOutside_air_relative_humidity_sensor.add((Outside_air_relative_humidity_sensor)action);
			}
		});
		return UsesOptionalsOutside_air_relative_humidity_sensor;
	}


  public void addUsesOptionalsOutside_air_specificenthalpy_sensor (IOutside_air_specificenthalpy_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IOutside_air_specificenthalpy_sensor> getUsesOptionalsOutside_air_specificenthalpy_sensor (){
		Set<IOutside_air_specificenthalpy_sensor> UsesOptionalsOutside_air_specificenthalpy_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Outside_air_specificenthalpy_sensor) {
				UsesOptionalsOutside_air_specificenthalpy_sensor.add((Outside_air_specificenthalpy_sensor)action);
			}
		});
		return UsesOptionalsOutside_air_specificenthalpy_sensor;
	}


  public void addUsesOptionalsOutside_air_wetbulb_temperature_sensor (IOutside_air_wetbulb_temperature_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IOutside_air_wetbulb_temperature_sensor> getUsesOptionalsOutside_air_wetbulb_temperature_sensor (){
		Set<IOutside_air_wetbulb_temperature_sensor> UsesOptionalsOutside_air_wetbulb_temperature_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Outside_air_wetbulb_temperature_sensor) {
				UsesOptionalsOutside_air_wetbulb_temperature_sensor.add((Outside_air_wetbulb_temperature_sensor)action);
			}
		});
		return UsesOptionalsOutside_air_wetbulb_temperature_sensor;
	}


  public void addUsesOutside_air_temperature_sensor (IOutside_air_temperature_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IOutside_air_temperature_sensor> getUsesOutside_air_temperature_sensor (){
		Set<IOutside_air_temperature_sensor> UsesOutside_air_temperature_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Outside_air_temperature_sensor) {
				UsesOutside_air_temperature_sensor.add((Outside_air_temperature_sensor)action);
			}
		});
		return UsesOutside_air_temperature_sensor;
	}

	public static Set<IOa> getAllOasObjectsCreated(){
		Set<IOa> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Oa")).subjects().stream()
		.map(mapper->(IOa)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}