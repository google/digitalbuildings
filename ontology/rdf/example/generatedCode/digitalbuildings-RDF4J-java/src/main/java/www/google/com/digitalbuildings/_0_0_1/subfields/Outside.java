package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Outside 
* Process or measurement of local atmospheric conditions.
*/
@SuppressWarnings("serial")
public class Outside extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IOutside{

	IRI newInstance;
	public Outside(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Outside"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IOutside> getAllOutsidesObjectsCreated(){
		Set<IOutside> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Outside")).subjects().stream()
		.map(mapper->(IOutside)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}