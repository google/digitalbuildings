package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Aggregation 
*/
@SuppressWarnings("serial")
public class Aggregation extends www.google.com.digitalbuildings._0_0_1.subfields.SubField implements IAggregation{

	IRI newInstance;
	public Aggregation(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Aggregation"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IAggregation> getAllAggregationsObjectsCreated(){
		Set<IAggregation> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Aggregation")).subjects().stream()
		.map(mapper->(IAggregation)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}