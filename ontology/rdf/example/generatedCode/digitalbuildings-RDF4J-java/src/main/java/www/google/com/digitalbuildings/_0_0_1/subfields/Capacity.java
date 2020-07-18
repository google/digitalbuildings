package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Capacity 
* A design parameter quantity. Ex: design motor power capacity. Is always a maximum limit.
*/
@SuppressWarnings("serial")
public class Capacity extends www.google.com.digitalbuildings._0_0_1.subfields.Point_type implements ICapacity{

	IRI newInstance;
	public Capacity(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Capacity"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<ICapacity> getAllCapacitysObjectsCreated(){
		Set<ICapacity> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Capacity")).subjects().stream()
		.map(mapper->(ICapacity)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}