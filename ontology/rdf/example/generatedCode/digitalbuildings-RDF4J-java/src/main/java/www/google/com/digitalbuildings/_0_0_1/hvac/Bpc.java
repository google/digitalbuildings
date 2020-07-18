package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.Operational;
import www.google.com.digitalbuildings._0_0_1.fields.IBuilding_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Building_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IBuilding_air_static_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Building_air_static_pressure_setpoint;

/**
* Class Bpc 
* Building pressure control (stand-alone fan).
*/
@SuppressWarnings("serial")
public class Bpc extends www.google.com.digitalbuildings._0_0_1.Operational implements IBpc{

	IRI newInstance;
	public Bpc(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Bpc"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesBuilding_air_static_pressure_sensor (IBuilding_air_static_pressure_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IBuilding_air_static_pressure_sensor> getUsesBuilding_air_static_pressure_sensor (){
		Set<IBuilding_air_static_pressure_sensor> UsesBuilding_air_static_pressure_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Building_air_static_pressure_sensor) {
				UsesBuilding_air_static_pressure_sensor.add((Building_air_static_pressure_sensor)action);
			}
		});
		return UsesBuilding_air_static_pressure_sensor;
	}


  public void addUsesBuilding_air_static_pressure_setpoint (IBuilding_air_static_pressure_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IBuilding_air_static_pressure_setpoint> getUsesBuilding_air_static_pressure_setpoint (){
		Set<IBuilding_air_static_pressure_setpoint> UsesBuilding_air_static_pressure_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Building_air_static_pressure_setpoint) {
				UsesBuilding_air_static_pressure_setpoint.add((Building_air_static_pressure_setpoint)action);
			}
		});
		return UsesBuilding_air_static_pressure_setpoint;
	}

	public static Set<IBpc> getAllBpcsObjectsCreated(){
		Set<IBpc> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Bpc")).subjects().stream()
		.map(mapper->(IBpc)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}