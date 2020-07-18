package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class North 
* Cardinal direction; opposite of south
*/
@SuppressWarnings("serial")
public class North extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements INorth{

	IRI newInstance;
	public North(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#North"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<INorth> getAllNorthsObjectsCreated(){
		Set<INorth> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#North")).subjects().stream()
		.map(mapper->(INorth)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}