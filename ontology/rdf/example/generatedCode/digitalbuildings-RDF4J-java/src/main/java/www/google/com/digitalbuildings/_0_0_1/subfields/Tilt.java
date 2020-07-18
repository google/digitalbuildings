package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Tilt 
* Degree of radial rotation.
*/
@SuppressWarnings("serial")
public class Tilt extends www.google.com.digitalbuildings._0_0_1.subfields.Measurement_descriptor implements ITilt{

	IRI newInstance;
	public Tilt(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Tilt"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<ITilt> getAllTiltsObjectsCreated(){
		Set<ITilt> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Tilt")).subjects().stream()
		.map(mapper->(ITilt)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}