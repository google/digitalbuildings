package www.google.com.digitalbuildings._0_0_1.states;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Does_not_match 
* Two or more things do not match.
*/
@SuppressWarnings("serial")
public class Does_not_match extends www.google.com.digitalbuildings._0_0_1.states.State implements IDoes_not_match{

	IRI newInstance;
	public Does_not_match(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/states#Does_not_match"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IDoes_not_match> getAllDoes_not_matchsObjectsCreated(){
		Set<IDoes_not_match> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/states#Does_not_match")).subjects().stream()
		.map(mapper->(IDoes_not_match)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}