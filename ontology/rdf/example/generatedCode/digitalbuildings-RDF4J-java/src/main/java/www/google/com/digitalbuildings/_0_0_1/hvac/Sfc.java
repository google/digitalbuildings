package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.Operational;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_flowrate_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_air_flowrate_setpoint;

/**
* Class Sfc 
* Supply air flow control.
*/
@SuppressWarnings("serial")
public class Sfc extends www.google.com.digitalbuildings._0_0_1.Operational implements ISfc{

	IRI newInstance;
	public Sfc(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Sfc"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesSupply_air_flowrate_sensor (ISupply_air_flowrate_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_air_flowrate_sensor> getUsesSupply_air_flowrate_sensor (){
		Set<ISupply_air_flowrate_sensor> UsesSupply_air_flowrate_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_air_flowrate_sensor) {
				UsesSupply_air_flowrate_sensor.add((Supply_air_flowrate_sensor)action);
			}
		});
		return UsesSupply_air_flowrate_sensor;
	}


  public void addUsesSupply_air_flowrate_setpoint (ISupply_air_flowrate_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_air_flowrate_setpoint> getUsesSupply_air_flowrate_setpoint (){
		Set<ISupply_air_flowrate_setpoint> UsesSupply_air_flowrate_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_air_flowrate_setpoint) {
				UsesSupply_air_flowrate_setpoint.add((Supply_air_flowrate_setpoint)action);
			}
		});
		return UsesSupply_air_flowrate_setpoint;
	}

	public static Set<ISfc> getAllSfcsObjectsCreated(){
		Set<ISfc> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Sfc")).subjects().stream()
		.map(mapper->(ISfc)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}