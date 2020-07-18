package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Medium 
* Level of control or measurement; between high and low.
*/
@SuppressWarnings("serial")
public class Medium extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IMedium{

	IRI newInstance;
	public Medium(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Medium"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IMedium> getAllMediumsObjectsCreated(){
		Set<IMedium> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Medium")).subjects().stream()
		.map(mapper->(IMedium)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}