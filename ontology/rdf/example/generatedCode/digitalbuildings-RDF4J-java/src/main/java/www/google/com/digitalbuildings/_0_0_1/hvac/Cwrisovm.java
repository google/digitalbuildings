package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.Monitoring;
import www.google.com.digitalbuildings._0_0_1.fields.ICondensing_return_water_isolation_valve_status;
import www.google.com.digitalbuildings._0_0_1.fields.Condensing_return_water_isolation_valve_status;
import www.google.com.digitalbuildings._0_0_1.fields.ICondensing_return_water_isolation_valve_command;
import www.google.com.digitalbuildings._0_0_1.fields.Condensing_return_water_isolation_valve_command;

/**
* Class Cwrisovm 
* Condensing water return isolation monitoring.
*/
@SuppressWarnings("serial")
public class Cwrisovm extends www.google.com.digitalbuildings._0_0_1.Monitoring implements ICwrisovm{

	IRI newInstance;
	public Cwrisovm(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Cwrisovm"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesCondensing_return_water_isolation_valve_command (ICondensing_return_water_isolation_valve_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ICondensing_return_water_isolation_valve_command> getUsesCondensing_return_water_isolation_valve_command (){
		Set<ICondensing_return_water_isolation_valve_command> UsesCondensing_return_water_isolation_valve_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Condensing_return_water_isolation_valve_command) {
				UsesCondensing_return_water_isolation_valve_command.add((Condensing_return_water_isolation_valve_command)action);
			}
		});
		return UsesCondensing_return_water_isolation_valve_command;
	}


  public void addUsesCondensing_return_water_isolation_valve_status (ICondensing_return_water_isolation_valve_status parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ICondensing_return_water_isolation_valve_status> getUsesCondensing_return_water_isolation_valve_status (){
		Set<ICondensing_return_water_isolation_valve_status> UsesCondensing_return_water_isolation_valve_status = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Condensing_return_water_isolation_valve_status) {
				UsesCondensing_return_water_isolation_valve_status.add((Condensing_return_water_isolation_valve_status)action);
			}
		});
		return UsesCondensing_return_water_isolation_valve_status;
	}

	public static Set<ICwrisovm> getAllCwrisovmsObjectsCreated(){
		Set<ICwrisovm> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Cwrisovm")).subjects().stream()
		.map(mapper->(ICwrisovm)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}