package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IControl;
import www.google.com.digitalbuildings._0_0_1.Control;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Return_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Return_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_air_flowrate_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Return_air_flowrate_setpoint;

/**
* Class Rd 
* Return damper flow control.
*/
@SuppressWarnings("serial")
public class Rd extends www.google.com.digitalbuildings._0_0_1.Control implements IRd{

	IRI newInstance;
	public Rd(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Rd"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesReturn_air_damper_percentage_command (IReturn_air_damper_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IReturn_air_damper_percentage_command> getUsesReturn_air_damper_percentage_command (){
		Set<IReturn_air_damper_percentage_command> UsesReturn_air_damper_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Return_air_damper_percentage_command) {
				UsesReturn_air_damper_percentage_command.add((Return_air_damper_percentage_command)action);
			}
		});
		return UsesReturn_air_damper_percentage_command;
	}


  public void addUsesReturn_air_flowrate_sensor (IReturn_air_flowrate_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IReturn_air_flowrate_sensor> getUsesReturn_air_flowrate_sensor (){
		Set<IReturn_air_flowrate_sensor> UsesReturn_air_flowrate_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Return_air_flowrate_sensor) {
				UsesReturn_air_flowrate_sensor.add((Return_air_flowrate_sensor)action);
			}
		});
		return UsesReturn_air_flowrate_sensor;
	}


  public void addUsesReturn_air_flowrate_setpoint (IReturn_air_flowrate_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IReturn_air_flowrate_setpoint> getUsesReturn_air_flowrate_setpoint (){
		Set<IReturn_air_flowrate_setpoint> UsesReturn_air_flowrate_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Return_air_flowrate_setpoint) {
				UsesReturn_air_flowrate_setpoint.add((Return_air_flowrate_setpoint)action);
			}
		});
		return UsesReturn_air_flowrate_setpoint;
	}

	public static Set<IRd> getAllRdsObjectsCreated(){
		Set<IRd> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Rd")).subjects().stream()
		.map(mapper->(IRd)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}