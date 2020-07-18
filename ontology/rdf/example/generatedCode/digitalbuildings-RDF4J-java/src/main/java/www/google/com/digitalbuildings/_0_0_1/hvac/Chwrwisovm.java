package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.Monitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_return_water_isolation_valve_status;
import www.google.com.digitalbuildings._0_0_1.fields.Chilled_return_water_isolation_valve_status;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_return_water_isolation_valve_command;
import www.google.com.digitalbuildings._0_0_1.fields.Chilled_return_water_isolation_valve_command;

/**
* Class Chwrwisovm 
* Return side isolation valve monitoring.
*/
@SuppressWarnings("serial")
public class Chwrwisovm extends www.google.com.digitalbuildings._0_0_1.Monitoring implements IChwrwisovm{

	IRI newInstance;
	public Chwrwisovm(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Chwrwisovm"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesChilled_return_water_isolation_valve_command (IChilled_return_water_isolation_valve_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IChilled_return_water_isolation_valve_command> getUsesChilled_return_water_isolation_valve_command (){
		Set<IChilled_return_water_isolation_valve_command> UsesChilled_return_water_isolation_valve_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Chilled_return_water_isolation_valve_command) {
				UsesChilled_return_water_isolation_valve_command.add((Chilled_return_water_isolation_valve_command)action);
			}
		});
		return UsesChilled_return_water_isolation_valve_command;
	}


  public void addUsesChilled_return_water_isolation_valve_status (IChilled_return_water_isolation_valve_status parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IChilled_return_water_isolation_valve_status> getUsesChilled_return_water_isolation_valve_status (){
		Set<IChilled_return_water_isolation_valve_status> UsesChilled_return_water_isolation_valve_status = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Chilled_return_water_isolation_valve_status) {
				UsesChilled_return_water_isolation_valve_status.add((Chilled_return_water_isolation_valve_status)action);
			}
		});
		return UsesChilled_return_water_isolation_valve_status;
	}

	public static Set<IChwrwisovm> getAllChwrwisovmsObjectsCreated(){
		Set<IChwrwisovm> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Chwrwisovm")).subjects().stream()
		.map(mapper->(IChwrwisovm)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}