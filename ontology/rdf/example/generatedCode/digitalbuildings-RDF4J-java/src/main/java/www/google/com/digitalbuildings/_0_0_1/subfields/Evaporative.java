package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Evaporative 
* Process associated with the evaporation of water.
*/
@SuppressWarnings("serial")
public class Evaporative extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IEvaporative{

	IRI newInstance;
	public Evaporative(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Evaporative"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IEvaporative> getAllEvaporativesObjectsCreated(){
		Set<IEvaporative> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Evaporative")).subjects().stream()
		.map(mapper->(IEvaporative)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}