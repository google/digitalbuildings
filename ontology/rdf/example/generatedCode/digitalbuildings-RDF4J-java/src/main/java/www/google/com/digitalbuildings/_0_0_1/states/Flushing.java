package www.google.com.digitalbuildings._0_0_1.states;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Flushing 
* The heating and cooling valves are fully open.
*/
@SuppressWarnings("serial")
public class Flushing extends www.google.com.digitalbuildings._0_0_1.states.State implements IFlushing{

	IRI newInstance;
	public Flushing(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/states#Flushing"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IFlushing> getAllFlushingsObjectsCreated(){
		Set<IFlushing> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/states#Flushing")).subjects().stream()
		.map(mapper->(IFlushing)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}