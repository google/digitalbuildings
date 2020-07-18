package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class East 
* Cardinal direction; opposite of west
*/
@SuppressWarnings("serial")
public class East extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IEast{

	IRI newInstance;
	public East(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#East"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IEast> getAllEastsObjectsCreated(){
		Set<IEast> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#East")).subjects().stream()
		.map(mapper->(IEast)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}