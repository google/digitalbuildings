package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.Operational;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Return_water_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IRun_command;
import www.google.com.digitalbuildings._0_0_1.fields.Run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Return_water_valve_percentage_sensor;

/**
* Class Rwisovpc 
* Return water isolation valve percentage monitoring.
*/
@SuppressWarnings("serial")
public class Rwisovpc extends www.google.com.digitalbuildings._0_0_1.Operational implements IRwisovpc{

	IRI newInstance;
	public Rwisovpc(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Rwisovpc"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesOptionalsRun_command (IRun_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IRun_command> getUsesOptionalsRun_command (){
		Set<IRun_command> UsesOptionalsRun_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Run_command) {
				UsesOptionalsRun_command.add((Run_command)action);
			}
		});
		return UsesOptionalsRun_command;
	}


  public void addUsesReturn_water_valve_percentage_command (IReturn_water_valve_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IReturn_water_valve_percentage_command> getUsesReturn_water_valve_percentage_command (){
		Set<IReturn_water_valve_percentage_command> UsesReturn_water_valve_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Return_water_valve_percentage_command) {
				UsesReturn_water_valve_percentage_command.add((Return_water_valve_percentage_command)action);
			}
		});
		return UsesReturn_water_valve_percentage_command;
	}


  public void addUsesReturn_water_valve_percentage_sensor (IReturn_water_valve_percentage_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IReturn_water_valve_percentage_sensor> getUsesReturn_water_valve_percentage_sensor (){
		Set<IReturn_water_valve_percentage_sensor> UsesReturn_water_valve_percentage_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Return_water_valve_percentage_sensor) {
				UsesReturn_water_valve_percentage_sensor.add((Return_water_valve_percentage_sensor)action);
			}
		});
		return UsesReturn_water_valve_percentage_sensor;
	}

	public static Set<IRwisovpc> getAllRwisovpcsObjectsCreated(){
		Set<IRwisovpc> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Rwisovpc")).subjects().stream()
		.map(mapper->(IRwisovpc)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}