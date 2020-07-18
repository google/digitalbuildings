package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Evaporator 
* The component of a refrigeration system that evaporates refrigerant.
*/
@SuppressWarnings("serial")
public class Evaporator extends www.google.com.digitalbuildings._0_0_1.subfields.Component implements IEvaporator{

	IRI newInstance;
	public Evaporator(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Evaporator"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IEvaporator> getAllEvaporatorsObjectsCreated(){
		Set<IEvaporator> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Evaporator")).subjects().stream()
		.map(mapper->(IEvaporator)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}