package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Accumulator 
* The total accumulated quantity (e.g. total energy accumulated).
*/
@SuppressWarnings("serial")
public class Accumulator extends www.google.com.digitalbuildings._0_0_1.subfields.Point_type implements IAccumulator{

	IRI newInstance;
	public Accumulator(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Accumulator"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IAccumulator> getAllAccumulatorsObjectsCreated(){
		Set<IAccumulator> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Accumulator")).subjects().stream()
		.map(mapper->(IAccumulator)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}