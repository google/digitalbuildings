package www.google.com.digitalbuildings._0_0_1.states;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Disabled 
* Something is disabled.
*/
@SuppressWarnings("serial")
public class Disabled extends www.google.com.digitalbuildings._0_0_1.states.State implements IDisabled{

	IRI newInstance;
	public Disabled(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/states#Disabled"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IDisabled> getAllDisabledsObjectsCreated(){
		Set<IDisabled> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/states#Disabled")).subjects().stream()
		.map(mapper->(IDisabled)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}