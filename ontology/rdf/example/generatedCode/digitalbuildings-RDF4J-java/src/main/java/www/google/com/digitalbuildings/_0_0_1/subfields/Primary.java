package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Primary 
* Associated with the primary (production) loop of a production process.
*/
@SuppressWarnings("serial")
public class Primary extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IPrimary{

	IRI newInstance;
	public Primary(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Primary"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IPrimary> getAllPrimarysObjectsCreated(){
		Set<IPrimary> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Primary")).subjects().stream()
		.map(mapper->(IPrimary)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}