package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.Operational;
import www.google.com.digitalbuildings._0_0_1.fields.IFlowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ILow_limit_flowrate_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Low_limit_flowrate_setpoint;

/**
* Class Mwfrc 
* Minimum water flowrate control.
*/
@SuppressWarnings("serial")
public class Mwfrc extends www.google.com.digitalbuildings._0_0_1.Operational implements IMwfrc{

	IRI newInstance;
	public Mwfrc(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Mwfrc"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesFlowrate_sensor (IFlowrate_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IFlowrate_sensor> getUsesFlowrate_sensor (){
		Set<IFlowrate_sensor> UsesFlowrate_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Flowrate_sensor) {
				UsesFlowrate_sensor.add((Flowrate_sensor)action);
			}
		});
		return UsesFlowrate_sensor;
	}


  public void addUsesLow_limit_flowrate_setpoint (ILow_limit_flowrate_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ILow_limit_flowrate_setpoint> getUsesLow_limit_flowrate_setpoint (){
		Set<ILow_limit_flowrate_setpoint> UsesLow_limit_flowrate_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Low_limit_flowrate_setpoint) {
				UsesLow_limit_flowrate_setpoint.add((Low_limit_flowrate_setpoint)action);
			}
		});
		return UsesLow_limit_flowrate_setpoint;
	}

	public static Set<IMwfrc> getAllMwfrcsObjectsCreated(){
		Set<IMwfrc> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Mwfrc")).subjects().stream()
		.map(mapper->(IMwfrc)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}