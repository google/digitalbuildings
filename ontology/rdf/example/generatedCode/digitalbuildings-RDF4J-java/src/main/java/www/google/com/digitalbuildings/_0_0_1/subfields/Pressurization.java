package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Pressurization 
* Relating to the level of pressure in a system or vessel.
*/
@SuppressWarnings("serial")
public class Pressurization extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IPressurization{

	IRI newInstance;
	public Pressurization(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Pressurization"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IPressurization> getAllPressurizationsObjectsCreated(){
		Set<IPressurization> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Pressurization")).subjects().stream()
		.map(mapper->(IPressurization)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}