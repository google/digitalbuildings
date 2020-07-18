package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class South 
* Cardinal direction; opposite of north
*/
@SuppressWarnings("serial")
public class South extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements ISouth{

	IRI newInstance;
	public South(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#South"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<ISouth> getAllSouthsObjectsCreated(){
		Set<ISouth> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#South")).subjects().stream()
		.map(mapper->(ISouth)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}