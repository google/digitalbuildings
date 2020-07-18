package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Damper 
* Component which meters the flow of air within a system or device.
*/
@SuppressWarnings("serial")
public class Damper extends www.google.com.digitalbuildings._0_0_1.subfields.Component implements IDamper{

	IRI newInstance;
	public Damper(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Damper"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IDamper> getAllDampersObjectsCreated(){
		Set<IDamper> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Damper")).subjects().stream()
		.map(mapper->(IDamper)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}