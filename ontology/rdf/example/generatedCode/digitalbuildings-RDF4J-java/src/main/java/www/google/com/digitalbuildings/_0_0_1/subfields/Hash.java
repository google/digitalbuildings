package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Hash 
* A computed value that is converted from an original value.
*/
@SuppressWarnings("serial")
public class Hash extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IHash{

	IRI newInstance;
	public Hash(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Hash"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IHash> getAllHashsObjectsCreated(){
		Set<IHash> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Hash")).subjects().stream()
		.map(mapper->(IHash)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}