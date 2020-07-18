package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Wheel 
* Component used for transfer of heat from incoming to outgoing air streams. 
*/
@SuppressWarnings("serial")
public class Wheel extends www.google.com.digitalbuildings._0_0_1.subfields.Component implements IWheel{

	IRI newInstance;
	public Wheel(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Wheel"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IWheel> getAllWheelsObjectsCreated(){
		Set<IWheel> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Wheel")).subjects().stream()
		.map(mapper->(IWheel)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}