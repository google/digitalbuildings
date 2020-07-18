package www.google.com.digitalbuildings._0_0_1.states;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Enabled 
* Something is enabled.
*/
@SuppressWarnings("serial")
public class Enabled extends www.google.com.digitalbuildings._0_0_1.states.State implements IEnabled{

	IRI newInstance;
	public Enabled(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/states#Enabled"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IEnabled> getAllEnabledsObjectsCreated(){
		Set<IEnabled> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/states#Enabled")).subjects().stream()
		.map(mapper->(IEnabled)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}