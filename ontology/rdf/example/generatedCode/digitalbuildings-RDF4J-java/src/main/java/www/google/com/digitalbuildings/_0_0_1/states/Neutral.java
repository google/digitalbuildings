package www.google.com.digitalbuildings._0_0_1.states;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Neutral 
* Neither the heating valve nor cooling valve is open.
*/
@SuppressWarnings("serial")
public class Neutral extends www.google.com.digitalbuildings._0_0_1.states.State implements INeutral{

	IRI newInstance;
	public Neutral(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/states#Neutral"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<INeutral> getAllNeutralsObjectsCreated(){
		Set<INeutral> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/states#Neutral")).subjects().stream()
		.map(mapper->(INeutral)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}