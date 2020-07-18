package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Occupancy 
* State of being occupied.
*/
@SuppressWarnings("serial")
public class Occupancy extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IOccupancy{

	IRI newInstance;
	public Occupancy(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Occupancy"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IOccupancy> getAllOccupancysObjectsCreated(){
		Set<IOccupancy> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Occupancy")).subjects().stream()
		.map(mapper->(IOccupancy)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}