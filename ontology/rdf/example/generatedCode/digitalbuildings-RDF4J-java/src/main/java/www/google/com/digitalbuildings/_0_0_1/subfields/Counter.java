package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Counter 
* Special case of accumulator that assumes integer values and non-dimensional units
*/
@SuppressWarnings("serial")
public class Counter extends www.google.com.digitalbuildings._0_0_1.subfields.Point_type implements ICounter{

	IRI newInstance;
	public Counter(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Counter"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<ICounter> getAllCountersObjectsCreated(){
		Set<ICounter> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Counter")).subjects().stream()
		.map(mapper->(ICounter)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}