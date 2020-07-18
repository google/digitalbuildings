package www.google.com.digitalbuildings._0_0_1.states;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Unoccupied 
* Unoccupied sensor state or operation mode.
*/
@SuppressWarnings("serial")
public class Unoccupied extends www.google.com.digitalbuildings._0_0_1.states.State implements IUnoccupied{

	IRI newInstance;
	public Unoccupied(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/states#Unoccupied"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IUnoccupied> getAllUnoccupiedsObjectsCreated(){
		Set<IUnoccupied> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/states#Unoccupied")).subjects().stream()
		.map(mapper->(IUnoccupied)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}