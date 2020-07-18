package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Aisle 
* Passage between two rows of server racks.
*/
@SuppressWarnings("serial")
public class Aisle extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IAisle{

	IRI newInstance;
	public Aisle(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Aisle"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IAisle> getAllAislesObjectsCreated(){
		Set<IAisle> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Aisle")).subjects().stream()
		.map(mapper->(IAisle)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}