package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IControl;
import www.google.com.digitalbuildings._0_0_1.Control;
import www.google.com.digitalbuildings._0_0_1.fields.IBypass_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Bypass_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IFlowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IMin_flowrate_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Min_flowrate_setpoint;

/**
* Class Minfc 
* Minimum flow control for entire loop.
*/
@SuppressWarnings("serial")
public class Minfc extends www.google.com.digitalbuildings._0_0_1.Control implements IMinfc{

	IRI newInstance;
	public Minfc(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Minfc"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesBypass_valve_percentage_command (IBypass_valve_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IBypass_valve_percentage_command> getUsesBypass_valve_percentage_command (){
		Set<IBypass_valve_percentage_command> UsesBypass_valve_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Bypass_valve_percentage_command) {
				UsesBypass_valve_percentage_command.add((Bypass_valve_percentage_command)action);
			}
		});
		return UsesBypass_valve_percentage_command;
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


  public void addUsesMin_flowrate_setpoint (IMin_flowrate_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IMin_flowrate_setpoint> getUsesMin_flowrate_setpoint (){
		Set<IMin_flowrate_setpoint> UsesMin_flowrate_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Min_flowrate_setpoint) {
				UsesMin_flowrate_setpoint.add((Min_flowrate_setpoint)action);
			}
		});
		return UsesMin_flowrate_setpoint;
	}

	public static Set<IMinfc> getAllMinfcsObjectsCreated(){
		Set<IMinfc> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Minfc")).subjects().stream()
		.map(mapper->(IMinfc)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}