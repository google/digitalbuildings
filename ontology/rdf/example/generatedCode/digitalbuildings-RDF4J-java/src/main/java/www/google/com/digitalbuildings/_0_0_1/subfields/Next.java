package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Next 
* Something that occurs directly in time after the present or most recent one.
*/
@SuppressWarnings("serial")
public class Next extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements INext{

	IRI newInstance;
	public Next(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Next"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<INext> getAllNextsObjectsCreated(){
		Set<INext> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Next")).subjects().stream()
		.map(mapper->(INext)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}