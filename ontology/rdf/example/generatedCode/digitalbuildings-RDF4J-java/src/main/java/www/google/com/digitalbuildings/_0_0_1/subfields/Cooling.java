package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Cooling 
* Process, measured effect or requirement for cooling.
*/
@SuppressWarnings("serial")
public class Cooling extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements ICooling{

	IRI newInstance;
	public Cooling(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Cooling"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<ICooling> getAllCoolingsObjectsCreated(){
		Set<ICooling> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Cooling")).subjects().stream()
		.map(mapper->(ICooling)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}