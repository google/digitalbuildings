package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Isolation 
* Process of isolating one component or process from another.
*/
@SuppressWarnings("serial")
public class Isolation extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IIsolation{

	IRI newInstance;
	public Isolation(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Isolation"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IIsolation> getAllIsolationsObjectsCreated(){
		Set<IIsolation> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Isolation")).subjects().stream()
		.map(mapper->(IIsolation)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}