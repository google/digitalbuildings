package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.Operational;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_air_relative_humidity_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Return_air_relative_humidity_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_air_relative_humidity_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Return_air_relative_humidity_setpoint;

/**
* Class Rhc 
* Return air relative humidity control.
*/
@SuppressWarnings("serial")
public class Rhc extends www.google.com.digitalbuildings._0_0_1.Operational implements IRhc{

	IRI newInstance;
	public Rhc(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Rhc"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesReturn_air_relative_humidity_sensor (IReturn_air_relative_humidity_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IReturn_air_relative_humidity_sensor> getUsesReturn_air_relative_humidity_sensor (){
		Set<IReturn_air_relative_humidity_sensor> UsesReturn_air_relative_humidity_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Return_air_relative_humidity_sensor) {
				UsesReturn_air_relative_humidity_sensor.add((Return_air_relative_humidity_sensor)action);
			}
		});
		return UsesReturn_air_relative_humidity_sensor;
	}


  public void addUsesReturn_air_relative_humidity_setpoint (IReturn_air_relative_humidity_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IReturn_air_relative_humidity_setpoint> getUsesReturn_air_relative_humidity_setpoint (){
		Set<IReturn_air_relative_humidity_setpoint> UsesReturn_air_relative_humidity_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Return_air_relative_humidity_setpoint) {
				UsesReturn_air_relative_humidity_setpoint.add((Return_air_relative_humidity_setpoint)action);
			}
		});
		return UsesReturn_air_relative_humidity_setpoint;
	}

	public static Set<IRhc> getAllRhcsObjectsCreated(){
		Set<IRhc> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Rhc")).subjects().stream()
		.map(mapper->(IRhc)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}