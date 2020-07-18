package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Dryer 
* A component used for drying clothes.
*/
@SuppressWarnings("serial")
public class Dryer extends www.google.com.digitalbuildings._0_0_1.subfields.Component implements IDryer{

	IRI newInstance;
	public Dryer(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Dryer"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IDryer> getAllDryersObjectsCreated(){
		Set<IDryer> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Dryer")).subjects().stream()
		.map(mapper->(IDryer)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}