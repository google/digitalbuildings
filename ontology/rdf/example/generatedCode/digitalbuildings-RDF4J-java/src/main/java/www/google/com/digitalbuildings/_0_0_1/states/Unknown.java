package www.google.com.digitalbuildings._0_0_1.states;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Unknown 
* The state is unknown.
*/
@SuppressWarnings("serial")
public class Unknown extends www.google.com.digitalbuildings._0_0_1.states.State implements IUnknown{

	IRI newInstance;
	public Unknown(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/states#Unknown"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IUnknown> getAllUnknownsObjectsCreated(){
		Set<IUnknown> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/states#Unknown")).subjects().stream()
		.map(mapper->(IUnknown)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}