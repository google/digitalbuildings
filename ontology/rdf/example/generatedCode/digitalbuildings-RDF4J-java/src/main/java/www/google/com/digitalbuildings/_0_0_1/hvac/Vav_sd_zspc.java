package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_use_label;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_use_label;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_static_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_air_static_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_air_static_pressure_sensor;

/**
* Class Vav_sd_zspc 
* Supply air zone pressure control VAV.
*/
@SuppressWarnings("serial")
public class Vav_sd_zspc extends www.google.com.digitalbuildings._0_0_1.hvac.Sd implements IVav_sd_zspc{

	IRI newInstance;
	public Vav_sd_zspc(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Vav_sd_zspc"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesOptionalsZone_use_label (IZone_use_label parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IZone_use_label> getUsesOptionalsZone_use_label (){
		Set<IZone_use_label> UsesOptionalsZone_use_label = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Zone_use_label) {
				UsesOptionalsZone_use_label.add((Zone_use_label)action);
			}
		});
		return UsesOptionalsZone_use_label;
	}


  public void addUsesZone_air_static_pressure_sensor (IZone_air_static_pressure_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IZone_air_static_pressure_sensor> getUsesZone_air_static_pressure_sensor (){
		Set<IZone_air_static_pressure_sensor> UsesZone_air_static_pressure_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Zone_air_static_pressure_sensor) {
				UsesZone_air_static_pressure_sensor.add((Zone_air_static_pressure_sensor)action);
			}
		});
		return UsesZone_air_static_pressure_sensor;
	}


  public void addUsesZone_air_static_pressure_setpoint (IZone_air_static_pressure_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IZone_air_static_pressure_setpoint> getUsesZone_air_static_pressure_setpoint (){
		Set<IZone_air_static_pressure_setpoint> UsesZone_air_static_pressure_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Zone_air_static_pressure_setpoint) {
				UsesZone_air_static_pressure_setpoint.add((Zone_air_static_pressure_setpoint)action);
			}
		});
		return UsesZone_air_static_pressure_setpoint;
	}

	public static Set<IVav_sd_zspc> getAllVav_sd_zspcsObjectsCreated(){
		Set<IVav_sd_zspc> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Vav_sd_zspc")).subjects().stream()
		.map(mapper->(IVav_sd_zspc)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}