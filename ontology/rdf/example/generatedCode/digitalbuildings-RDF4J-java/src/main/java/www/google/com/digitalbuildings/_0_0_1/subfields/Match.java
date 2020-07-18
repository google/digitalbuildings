package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Match 
* A function that matches something against others.
*/
@SuppressWarnings("serial")
public class Match extends www.google.com.digitalbuildings._0_0_1.subfields.Measurement_descriptor implements IMatch{

	IRI newInstance;
	public Match(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Match"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IMatch> getAllMatchsObjectsCreated(){
		Set<IMatch> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Match")).subjects().stream()
		.map(mapper->(IMatch)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}