package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.Monitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IRun_command;
import www.google.com.digitalbuildings._0_0_1.fields.Run_command;
import www.google.com.digitalbuildings._0_0_1.fields.ICondensing_water_isolation_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Condensing_water_isolation_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ICondensing_water_isolation_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Condensing_water_isolation_valve_percentage_sensor;

/**
* Class Cdwisovpm 
* Condensing water isolation valve percentage monitoring.
*/
@SuppressWarnings("serial")
public class Cdwisovpm extends www.google.com.digitalbuildings._0_0_1.Monitoring implements ICdwisovpm{

	IRI newInstance;
	public Cdwisovpm(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Cdwisovpm"));
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


  public void addUsesCondensing_water_isolation_valve_percentage_command (ICondensing_water_isolation_valve_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ICondensing_water_isolation_valve_percentage_command> getUsesCondensing_water_isolation_valve_percentage_command (){
		Set<ICondensing_water_isolation_valve_percentage_command> UsesCondensing_water_isolation_valve_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Condensing_water_isolation_valve_percentage_command) {
				UsesCondensing_water_isolation_valve_percentage_command.add((Condensing_water_isolation_valve_percentage_command)action);
			}
		});
		return UsesCondensing_water_isolation_valve_percentage_command;
	}


  public void addUsesCondensing_water_isolation_valve_percentage_sensor (ICondensing_water_isolation_valve_percentage_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ICondensing_water_isolation_valve_percentage_sensor> getUsesCondensing_water_isolation_valve_percentage_sensor (){
		Set<ICondensing_water_isolation_valve_percentage_sensor> UsesCondensing_water_isolation_valve_percentage_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Condensing_water_isolation_valve_percentage_sensor) {
				UsesCondensing_water_isolation_valve_percentage_sensor.add((Condensing_water_isolation_valve_percentage_sensor)action);
			}
		});
		return UsesCondensing_water_isolation_valve_percentage_sensor;
	}

	public static Set<ICdwisovpm> getAllCdwisovpmsObjectsCreated(){
		Set<ICdwisovpm> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Cdwisovpm")).subjects().stream()
		.map(mapper->(ICdwisovpm)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}