package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.Operational;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Return_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_air_static_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Return_air_static_pressure_setpoint;

/**
* Class Rspc 
* Return air static pressure control.
*/
@SuppressWarnings("serial")
public class Rspc extends www.google.com.digitalbuildings._0_0_1.Operational implements IRspc{

	IRI newInstance;
	public Rspc(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Rspc"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesReturn_air_static_pressure_sensor (IReturn_air_static_pressure_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IReturn_air_static_pressure_sensor> getUsesReturn_air_static_pressure_sensor (){
		Set<IReturn_air_static_pressure_sensor> UsesReturn_air_static_pressure_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Return_air_static_pressure_sensor) {
				UsesReturn_air_static_pressure_sensor.add((Return_air_static_pressure_sensor)action);
			}
		});
		return UsesReturn_air_static_pressure_sensor;
	}


  public void addUsesReturn_air_static_pressure_setpoint (IReturn_air_static_pressure_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IReturn_air_static_pressure_setpoint> getUsesReturn_air_static_pressure_setpoint (){
		Set<IReturn_air_static_pressure_setpoint> UsesReturn_air_static_pressure_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Return_air_static_pressure_setpoint) {
				UsesReturn_air_static_pressure_setpoint.add((Return_air_static_pressure_setpoint)action);
			}
		});
		return UsesReturn_air_static_pressure_setpoint;
	}

	public static Set<IRspc> getAllRspcsObjectsCreated(){
		Set<IRspc> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Rspc")).subjects().stream()
		.map(mapper->(IRspc)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}