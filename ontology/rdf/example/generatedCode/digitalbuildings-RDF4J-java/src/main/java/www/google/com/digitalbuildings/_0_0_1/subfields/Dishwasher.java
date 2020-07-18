package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Dishwasher 
* Device that washes dishes.
*/
@SuppressWarnings("serial")
public class Dishwasher extends www.google.com.digitalbuildings._0_0_1.subfields.Component implements IDishwasher{

	IRI newInstance;
	public Dishwasher(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Dishwasher"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IDishwasher> getAllDishwashersObjectsCreated(){
		Set<IDishwasher> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Dishwasher")).subjects().stream()
		.map(mapper->(IDishwasher)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}