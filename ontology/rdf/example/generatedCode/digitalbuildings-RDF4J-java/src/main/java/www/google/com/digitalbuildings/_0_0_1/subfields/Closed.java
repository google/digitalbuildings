package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Closed 
* Indicates full closed (for two-position actuators)
*/
@SuppressWarnings("serial")
public class Closed extends www.google.com.digitalbuildings._0_0_1.subfields.Measurement_descriptor implements IClosed{

	IRI newInstance;
	public Closed(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Closed"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IClosed> getAllClosedsObjectsCreated(){
		Set<IClosed> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Closed")).subjects().stream()
		.map(mapper->(IClosed)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}