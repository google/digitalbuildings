package www.google.com.digitalbuildings._0_0_1;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Operational 
*/
@SuppressWarnings("serial")
public class Operational extends www.google.com.digitalbuildings._0_0_1.Application implements IOperational{

	IRI newInstance;
	public Operational(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#Operational"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IOperational> getAllOperationalsObjectsCreated(){
		Set<IOperational> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1#Operational")).subjects().stream()
		.map(mapper->(IOperational)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}