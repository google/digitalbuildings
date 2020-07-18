package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IControl;
import www.google.com.digitalbuildings._0_0_1.Control;
import www.google.com.digitalbuildings._0_0_1.fields.IDehumidification_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.Dehumidification_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_relative_humidity_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_air_relative_humidity_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IHumidification_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.Humidification_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_relative_humidity_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_air_relative_humidity_sensor;

/**
* Class Zhdhc 
* Zone humidification/dehumidification control.
*/
@SuppressWarnings("serial")
public class Zhdhc extends www.google.com.digitalbuildings._0_0_1.Control implements IZhdhc{

	IRI newInstance;
	public Zhdhc(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Zhdhc"));
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


  public void addUsesZone_air_relative_humidity_sensor (IZone_air_relative_humidity_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IZone_air_relative_humidity_sensor> getUsesZone_air_relative_humidity_sensor (){
		Set<IZone_air_relative_humidity_sensor> UsesZone_air_relative_humidity_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Zone_air_relative_humidity_sensor) {
				UsesZone_air_relative_humidity_sensor.add((Zone_air_relative_humidity_sensor)action);
			}
		});
		return UsesZone_air_relative_humidity_sensor;
	}


  public void addUsesZone_air_relative_humidity_setpoint (IZone_air_relative_humidity_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IZone_air_relative_humidity_setpoint> getUsesZone_air_relative_humidity_setpoint (){
		Set<IZone_air_relative_humidity_setpoint> UsesZone_air_relative_humidity_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Zone_air_relative_humidity_setpoint) {
				UsesZone_air_relative_humidity_setpoint.add((Zone_air_relative_humidity_setpoint)action);
			}
		});
		return UsesZone_air_relative_humidity_setpoint;
	}

	public static Set<IZhdhc> getAllZhdhcsObjectsCreated(){
		Set<IZhdhc> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Zhdhc")).subjects().stream()
		.map(mapper->(IZhdhc)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}