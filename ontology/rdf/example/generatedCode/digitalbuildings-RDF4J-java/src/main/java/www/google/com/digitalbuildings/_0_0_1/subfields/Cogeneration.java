package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Cogeneration 
* Associated with a cogeneration process.
*/
@SuppressWarnings("serial")
public class Cogeneration extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements ICogeneration{

	IRI newInstance;
	public Cogeneration(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Cogeneration"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<ICogeneration> getAllCogenerationsObjectsCreated(){
		Set<ICogeneration> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Cogeneration")).subjects().stream()
		.map(mapper->(ICogeneration)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}