package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Condenser 
* The component of a refrigeration system that condenses refrigerant.
*/
@SuppressWarnings("serial")
public class Condenser extends www.google.com.digitalbuildings._0_0_1.subfields.Component implements ICondenser{

	IRI newInstance;
	public Condenser(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Condenser"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<ICondenser> getAllCondensersObjectsCreated(){
		Set<ICondenser> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Condenser")).subjects().stream()
		.map(mapper->(ICondenser)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}