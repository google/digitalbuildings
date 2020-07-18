package www.google.com.digitalbuildings._0_0_1.states;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Inactive 
* An action, activity, event, or operation is not currently hapenning.
*/
@SuppressWarnings("serial")
public class Inactive extends www.google.com.digitalbuildings._0_0_1.states.State implements IInactive{

	IRI newInstance;
	public Inactive(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/states#Inactive"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IInactive> getAllInactivesObjectsCreated(){
		Set<IInactive> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/states#Inactive")).subjects().stream()
		.map(mapper->(IInactive)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}