package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Dewpoint 
* The thermodynamic point at which water condenses from standing air.
*/
@SuppressWarnings("serial")
public class Dewpoint extends www.google.com.digitalbuildings._0_0_1.subfields.Measurement_descriptor implements IDewpoint{

	IRI newInstance;
	public Dewpoint(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Dewpoint"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IDewpoint> getAllDewpointsObjectsCreated(){
		Set<IDewpoint> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Dewpoint")).subjects().stream()
		.map(mapper->(IDewpoint)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}