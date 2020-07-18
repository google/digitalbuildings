package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Reactive 
* Power that is returned to the source (not consumed by the load).
*/
@SuppressWarnings("serial")
public class Reactive extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IReactive{

	IRI newInstance;
	public Reactive(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Reactive"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IReactive> getAllReactivesObjectsCreated(){
		Set<IReactive> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Reactive")).subjects().stream()
		.map(mapper->(IReactive)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}