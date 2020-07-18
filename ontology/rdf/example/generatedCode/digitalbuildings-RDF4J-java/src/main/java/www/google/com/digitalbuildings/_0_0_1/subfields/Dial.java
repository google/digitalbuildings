package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Dial 
* Adjustment device (e.g. setpoint dial).
*/
@SuppressWarnings("serial")
public class Dial extends www.google.com.digitalbuildings._0_0_1.subfields.Component implements IDial{

	IRI newInstance;
	public Dial(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Dial"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IDial> getAllDialsObjectsCreated(){
		Set<IDial> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Dial")).subjects().stream()
		.map(mapper->(IDial)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}