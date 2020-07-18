package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Co2 
* Measures carbon dioxide concentration.
*/
@SuppressWarnings("serial")
public class Co2 extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements ICo2{

	IRI newInstance;
	public Co2(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Co2"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<ICo2> getAllCo2sObjectsCreated(){
		Set<ICo2> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Co2")).subjects().stream()
		.map(mapper->(ICo2)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}