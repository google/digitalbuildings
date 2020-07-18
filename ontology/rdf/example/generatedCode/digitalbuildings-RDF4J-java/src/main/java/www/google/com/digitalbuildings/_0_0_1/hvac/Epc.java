package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.Operational;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_static_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_air_static_pressure_setpoint;

/**
* Class Epc 
* Exhaust pressure control.
*/
@SuppressWarnings("serial")
public class Epc extends www.google.com.digitalbuildings._0_0_1.Operational implements IEpc{

	IRI newInstance;
	public Epc(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Epc"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesExhaust_air_static_pressure_sensor (IExhaust_air_static_pressure_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IExhaust_air_static_pressure_sensor> getUsesExhaust_air_static_pressure_sensor (){
		Set<IExhaust_air_static_pressure_sensor> UsesExhaust_air_static_pressure_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_air_static_pressure_sensor) {
				UsesExhaust_air_static_pressure_sensor.add((Exhaust_air_static_pressure_sensor)action);
			}
		});
		return UsesExhaust_air_static_pressure_sensor;
	}


  public void addUsesExhaust_air_static_pressure_setpoint (IExhaust_air_static_pressure_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IExhaust_air_static_pressure_setpoint> getUsesExhaust_air_static_pressure_setpoint (){
		Set<IExhaust_air_static_pressure_setpoint> UsesExhaust_air_static_pressure_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_air_static_pressure_setpoint) {
				UsesExhaust_air_static_pressure_setpoint.add((Exhaust_air_static_pressure_setpoint)action);
			}
		});
		return UsesExhaust_air_static_pressure_setpoint;
	}

	public static Set<IEpc> getAllEpcsObjectsCreated(){
		Set<IEpc> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Epc")).subjects().stream()
		.map(mapper->(IEpc)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}