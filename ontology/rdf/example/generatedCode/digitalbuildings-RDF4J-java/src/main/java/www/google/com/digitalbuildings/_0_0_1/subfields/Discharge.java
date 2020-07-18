package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Discharge 
* Media leaving system to enter ambient conditioned space. Typically applies only to air-side systems.
*/
@SuppressWarnings("serial")
public class Discharge extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IDischarge{

	IRI newInstance;
	public Discharge(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Discharge"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IDischarge> getAllDischargesObjectsCreated(){
		Set<IDischarge> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Discharge")).subjects().stream()
		.map(mapper->(IDischarge)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}