package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Vane 
* Component for guiding media flow.
*/
@SuppressWarnings("serial")
public class Vane extends www.google.com.digitalbuildings._0_0_1.subfields.Component implements IVane{

	IRI newInstance;
	public Vane(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Vane"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IVane> getAllVanesObjectsCreated(){
		Set<IVane> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Vane")).subjects().stream()
		.map(mapper->(IVane)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}