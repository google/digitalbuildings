package www.google.com.digitalbuildings._0_0_1.states;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Access_failed 
* The failure to access a resource.
*/
@SuppressWarnings("serial")
public class Access_failed extends www.google.com.digitalbuildings._0_0_1.states.State implements IAccess_failed{

	IRI newInstance;
	public Access_failed(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/states#Access_failed"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IAccess_failed> getAllAccess_failedsObjectsCreated(){
		Set<IAccess_failed> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/states#Access_failed")).subjects().stream()
		.map(mapper->(IAccess_failed)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}