package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.Monitoring;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_isolation_valve_status;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_water_isolation_valve_status;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_isolation_valve_command;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_water_isolation_valve_command;

/**
* Class Swisovm 
* Supply side isolation valve monitoring.
*/
@SuppressWarnings("serial")
public class Swisovm extends www.google.com.digitalbuildings._0_0_1.Monitoring implements ISwisovm{

	IRI newInstance;
	public Swisovm(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Swisovm"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesSupply_water_isolation_valve_command (ISupply_water_isolation_valve_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_water_isolation_valve_command> getUsesSupply_water_isolation_valve_command (){
		Set<ISupply_water_isolation_valve_command> UsesSupply_water_isolation_valve_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_water_isolation_valve_command) {
				UsesSupply_water_isolation_valve_command.add((Supply_water_isolation_valve_command)action);
			}
		});
		return UsesSupply_water_isolation_valve_command;
	}


  public void addUsesSupply_water_isolation_valve_status (ISupply_water_isolation_valve_status parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_water_isolation_valve_status> getUsesSupply_water_isolation_valve_status (){
		Set<ISupply_water_isolation_valve_status> UsesSupply_water_isolation_valve_status = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_water_isolation_valve_status) {
				UsesSupply_water_isolation_valve_status.add((Supply_water_isolation_valve_status)action);
			}
		});
		return UsesSupply_water_isolation_valve_status;
	}

	public static Set<ISwisovm> getAllSwisovmsObjectsCreated(){
		Set<ISwisovm> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Swisovm")).subjects().stream()
		.map(mapper->(ISwisovm)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}