package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Mixed 
* Process or component used to mix multiple streams of air.
*/
@SuppressWarnings("serial")
public class Mixed extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IMixed{

	IRI newInstance;
	public Mixed(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Mixed"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IMixed> getAllMixedsObjectsCreated(){
		Set<IMixed> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Mixed")).subjects().stream()
		.map(mapper->(IMixed)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}