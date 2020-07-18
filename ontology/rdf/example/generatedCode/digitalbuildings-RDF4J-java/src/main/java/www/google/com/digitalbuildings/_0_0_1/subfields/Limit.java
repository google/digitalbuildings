package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Limit 
* A boundary condition for a control (e.g. low limit).
*/
@SuppressWarnings("serial")
public class Limit extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements ILimit{

	IRI newInstance;
	public Limit(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Limit"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<ILimit> getAllLimitsObjectsCreated(){
		Set<ILimit> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Limit")).subjects().stream()
		.map(mapper->(ILimit)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}