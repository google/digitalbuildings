package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.Monitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_water_isolation_valve_command;
import www.google.com.digitalbuildings._0_0_1.fields.Process_water_isolation_valve_command;

/**
* Class Pwisovm 
* Process water iso valve monitoring.
*/
@SuppressWarnings("serial")
public class Pwisovm extends www.google.com.digitalbuildings._0_0_1.Monitoring implements IPwisovm{

	IRI newInstance;
	public Pwisovm(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Pwisovm"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesProcess_water_isolation_valve_command (IProcess_water_isolation_valve_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IProcess_water_isolation_valve_command> getUsesProcess_water_isolation_valve_command (){
		Set<IProcess_water_isolation_valve_command> UsesProcess_water_isolation_valve_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Process_water_isolation_valve_command) {
				UsesProcess_water_isolation_valve_command.add((Process_water_isolation_valve_command)action);
			}
		});
		return UsesProcess_water_isolation_valve_command;
	}

	public static Set<IPwisovm> getAllPwisovmsObjectsCreated(){
		Set<IPwisovm> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Pwisovm")).subjects().stream()
		.map(mapper->(IPwisovm)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}