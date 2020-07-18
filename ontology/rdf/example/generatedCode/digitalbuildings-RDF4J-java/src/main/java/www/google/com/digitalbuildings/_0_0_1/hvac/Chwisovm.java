package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.Monitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_water_isolation_valve_status;
import www.google.com.digitalbuildings._0_0_1.fields.Chilled_water_isolation_valve_status;
import www.google.com.digitalbuildings._0_0_1.fields.IRun_command;
import www.google.com.digitalbuildings._0_0_1.fields.Run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_water_isolation_valve_command;
import www.google.com.digitalbuildings._0_0_1.fields.Chilled_water_isolation_valve_command;

/**
* Class Chwisovm 
* Chilled water isolation valve monitoring.
*/
@SuppressWarnings("serial")
public class Chwisovm extends www.google.com.digitalbuildings._0_0_1.Monitoring implements IChwisovm{

	IRI newInstance;
	public Chwisovm(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Chwisovm"));
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


  public void addUsesChilled_water_isolation_valve_command (IChilled_water_isolation_valve_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IChilled_water_isolation_valve_command> getUsesChilled_water_isolation_valve_command (){
		Set<IChilled_water_isolation_valve_command> UsesChilled_water_isolation_valve_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Chilled_water_isolation_valve_command) {
				UsesChilled_water_isolation_valve_command.add((Chilled_water_isolation_valve_command)action);
			}
		});
		return UsesChilled_water_isolation_valve_command;
	}


  public void addUsesChilled_water_isolation_valve_status (IChilled_water_isolation_valve_status parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IChilled_water_isolation_valve_status> getUsesChilled_water_isolation_valve_status (){
		Set<IChilled_water_isolation_valve_status> UsesChilled_water_isolation_valve_status = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Chilled_water_isolation_valve_status) {
				UsesChilled_water_isolation_valve_status.add((Chilled_water_isolation_valve_status)action);
			}
		});
		return UsesChilled_water_isolation_valve_status;
	}

	public static Set<IChwisovm> getAllChwisovmsObjectsCreated(){
		Set<IChwisovm> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Chwisovm")).subjects().stream()
		.map(mapper->(IChwisovm)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}