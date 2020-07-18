package www.google.com.digitalbuildings._0_0_1;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Control 
*/
@SuppressWarnings("serial")
public class Control extends www.google.com.digitalbuildings._0_0_1.Application implements IControl{

	IRI newInstance;
	public Control(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#Control"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IControl> getAllControlsObjectsCreated(){
		Set<IControl> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1#Control")).subjects().stream()
		.map(mapper->(IControl)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}