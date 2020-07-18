package www.google.com.digitalbuildings._0_0_1.states;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Active 
* An action, activity, event, or operation is currently hapenning.
*/
@SuppressWarnings("serial")
public class Active extends www.google.com.digitalbuildings._0_0_1.states.State implements IActive{

	IRI newInstance;
	public Active(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/states#Active"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IActive> getAllActivesObjectsCreated(){
		Set<IActive> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/states#Active")).subjects().stream()
		.map(mapper->(IActive)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}