package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Total 
* Sum total of some set of values (e.g. total_request_heating_count)
*/
@SuppressWarnings("serial")
public class Total extends www.google.com.digitalbuildings._0_0_1.subfields.Aggregation implements ITotal{

	IRI newInstance;
	public Total(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Total"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<ITotal> getAllTotalsObjectsCreated(){
		Set<ITotal> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Total")).subjects().stream()
		.map(mapper->(ITotal)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}