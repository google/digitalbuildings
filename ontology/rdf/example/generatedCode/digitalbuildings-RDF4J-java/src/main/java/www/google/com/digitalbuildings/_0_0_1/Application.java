package www.google.com.digitalbuildings._0_0_1;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Application 
* The class of all applications
*/
@SuppressWarnings("serial")
public class Application extends www.google.com.digitalbuildings._0_0_1.EntityType implements IApplication{

	IRI newInstance;
	public Application(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#Application"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IApplication> getAllApplicationsObjectsCreated(){
		Set<IApplication> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1#Application")).subjects().stream()
		.map(mapper->(IApplication)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}