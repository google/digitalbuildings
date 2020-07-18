package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Exhaust 
* Process or component used in the removal of air from a conditioned system to the outside atmosphere.
*/
@SuppressWarnings("serial")
public class Exhaust extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IExhaust{

	IRI newInstance;
	public Exhaust(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Exhaust"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IExhaust> getAllExhaustsObjectsCreated(){
		Set<IExhaust> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Exhaust")).subjects().stream()
		.map(mapper->(IExhaust)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}