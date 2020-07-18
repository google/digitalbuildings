package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Production 
* The loop in a system that is responsible for the conditioning of fluid.
*/
@SuppressWarnings("serial")
public class Production extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IProduction{

	IRI newInstance;
	public Production(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Production"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IProduction> getAllProductionsObjectsCreated(){
		Set<IProduction> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Production")).subjects().stream()
		.map(mapper->(IProduction)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}