package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.Operational;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_air_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_deadband_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_air_deadband_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_relative_humidity_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_air_relative_humidity_sensor;

/**
* Class Ztc 
* Single control setpoint with deadband.
*/
@SuppressWarnings("serial")
public class Ztc extends www.google.com.digitalbuildings._0_0_1.Operational implements IZtc{

	IRI newInstance;
	public Ztc(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Ztc"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesOptionalsZone_air_deadband_temperature_setpoint (IZone_air_deadband_temperature_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IZone_air_deadband_temperature_setpoint> getUsesOptionalsZone_air_deadband_temperature_setpoint (){
		Set<IZone_air_deadband_temperature_setpoint> UsesOptionalsZone_air_deadband_temperature_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Zone_air_deadband_temperature_setpoint) {
				UsesOptionalsZone_air_deadband_temperature_setpoint.add((Zone_air_deadband_temperature_setpoint)action);
			}
		});
		return UsesOptionalsZone_air_deadband_temperature_setpoint;
	}


  public void addUsesOptionalsZone_air_relative_humidity_sensor (IZone_air_relative_humidity_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IZone_air_relative_humidity_sensor> getUsesOptionalsZone_air_relative_humidity_sensor (){
		Set<IZone_air_relative_humidity_sensor> UsesOptionalsZone_air_relative_humidity_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Zone_air_relative_humidity_sensor) {
				UsesOptionalsZone_air_relative_humidity_sensor.add((Zone_air_relative_humidity_sensor)action);
			}
		});
		return UsesOptionalsZone_air_relative_humidity_sensor;
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


  public void addUsesZone_air_temperature_setpoint (IZone_air_temperature_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IZone_air_temperature_setpoint> getUsesZone_air_temperature_setpoint (){
		Set<IZone_air_temperature_setpoint> UsesZone_air_temperature_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Zone_air_temperature_setpoint) {
				UsesZone_air_temperature_setpoint.add((Zone_air_temperature_setpoint)action);
			}
		});
		return UsesZone_air_temperature_setpoint;
	}

	public static Set<IZtc> getAllZtcsObjectsCreated(){
		Set<IZtc> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Ztc")).subjects().stream()
		.map(mapper->(IZtc)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}