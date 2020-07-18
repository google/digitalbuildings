package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Side 
* Position relative to an an object.
*/
@SuppressWarnings("serial")
public class Side extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements ISide{

	IRI newInstance;
	public Side(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Side"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<ISide> getAllSidesObjectsCreated(){
		Set<ISide> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Side")).subjects().stream()
		.map(mapper->(ISide)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}