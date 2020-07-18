package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Count 
* Total count of actions or requests.
*/
@SuppressWarnings("serial")
public class Count extends www.google.com.digitalbuildings._0_0_1.subfields.Point_type implements ICount{

	IRI newInstance;
	public Count(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Count"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<ICount> getAllCountsObjectsCreated(){
		Set<ICount> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Count")).subjects().stream()
		.map(mapper->(ICount)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}