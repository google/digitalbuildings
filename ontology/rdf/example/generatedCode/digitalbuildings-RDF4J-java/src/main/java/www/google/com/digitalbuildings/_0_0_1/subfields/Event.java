package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Event 
* A thing of occassion that happens.
*/
@SuppressWarnings("serial")
public class Event extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IEvent{

	IRI newInstance;
	public Event(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Event"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IEvent> getAllEventsObjectsCreated(){
		Set<IEvent> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Event")).subjects().stream()
		.map(mapper->(IEvent)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}