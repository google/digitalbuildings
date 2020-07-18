package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Spray 
* Spray of water through air.
*/
@SuppressWarnings("serial")
public class Spray extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements ISpray{

	IRI newInstance;
	public Spray(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Spray"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<ISpray> getAllSpraysObjectsCreated(){
		Set<ISpray> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Spray")).subjects().stream()
		.map(mapper->(ISpray)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}