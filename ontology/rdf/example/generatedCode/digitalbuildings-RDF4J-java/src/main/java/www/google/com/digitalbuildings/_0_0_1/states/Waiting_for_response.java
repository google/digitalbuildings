package www.google.com.digitalbuildings._0_0_1.states;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Waiting_for_response 
* The calendar events synchronization process is awaiting response.
*/
@SuppressWarnings("serial")
public class Waiting_for_response extends www.google.com.digitalbuildings._0_0_1.states.State implements IWaiting_for_response{

	IRI newInstance;
	public Waiting_for_response(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/states#Waiting_for_response"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IWaiting_for_response> getAllWaiting_for_responsesObjectsCreated(){
		Set<IWaiting_for_response> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/states#Waiting_for_response")).subjects().stream()
		.map(mapper->(IWaiting_for_response)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}