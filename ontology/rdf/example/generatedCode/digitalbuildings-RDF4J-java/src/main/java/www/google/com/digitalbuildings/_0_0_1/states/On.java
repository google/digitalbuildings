package www.google.com.digitalbuildings._0_0_1.states;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class On 
* Powered on.
*/
@SuppressWarnings("serial")
public class On extends www.google.com.digitalbuildings._0_0_1.states.State implements IOn{

	IRI newInstance;
	public On(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/states#On"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IOn> getAllOnsObjectsCreated(){
		Set<IOn> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/states#On")).subjects().stream()
		.map(mapper->(IOn)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}