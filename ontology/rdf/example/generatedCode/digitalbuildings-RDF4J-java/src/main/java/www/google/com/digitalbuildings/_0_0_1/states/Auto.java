package www.google.com.digitalbuildings._0_0_1.states;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Auto 
* Running under automatic control.
*/
@SuppressWarnings("serial")
public class Auto extends www.google.com.digitalbuildings._0_0_1.states.State implements IAuto{

	IRI newInstance;
	public Auto(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/states#Auto"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IAuto> getAllAutosObjectsCreated(){
		Set<IAuto> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/states#Auto")).subjects().stream()
		.map(mapper->(IAuto)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}