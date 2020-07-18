package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.Monitoring;
import www.google.com.digitalbuildings._0_0_1.fields.ICondensing_water_isolation_valve_command;
import www.google.com.digitalbuildings._0_0_1.fields.Condensing_water_isolation_valve_command;
import www.google.com.digitalbuildings._0_0_1.fields.ICondensing_water_isolation_valve_status;
import www.google.com.digitalbuildings._0_0_1.fields.Condensing_water_isolation_valve_status;
import www.google.com.digitalbuildings._0_0_1.fields.IRun_command;
import www.google.com.digitalbuildings._0_0_1.fields.Run_command;

/**
* Class Cdwisovm 
* Condensing water isolation valve monitoring.
*/
@SuppressWarnings("serial")
public class Cdwisovm extends www.google.com.digitalbuildings._0_0_1.Monitoring implements ICdwisovm{

	IRI newInstance;
	public Cdwisovm(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Cdwisovm"));
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


  public void addUsesCondensing_water_isolation_valve_command (ICondensing_water_isolation_valve_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ICondensing_water_isolation_valve_command> getUsesCondensing_water_isolation_valve_command (){
		Set<ICondensing_water_isolation_valve_command> UsesCondensing_water_isolation_valve_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Condensing_water_isolation_valve_command) {
				UsesCondensing_water_isolation_valve_command.add((Condensing_water_isolation_valve_command)action);
			}
		});
		return UsesCondensing_water_isolation_valve_command;
	}


  public void addUsesCondensing_water_isolation_valve_status (ICondensing_water_isolation_valve_status parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ICondensing_water_isolation_valve_status> getUsesCondensing_water_isolation_valve_status (){
		Set<ICondensing_water_isolation_valve_status> UsesCondensing_water_isolation_valve_status = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Condensing_water_isolation_valve_status) {
				UsesCondensing_water_isolation_valve_status.add((Condensing_water_isolation_valve_status)action);
			}
		});
		return UsesCondensing_water_isolation_valve_status;
	}

	public static Set<ICdwisovm> getAllCdwisovmsObjectsCreated(){
		Set<ICdwisovm> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Cdwisovm")).subjects().stream()
		.map(mapper->(ICdwisovm)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}