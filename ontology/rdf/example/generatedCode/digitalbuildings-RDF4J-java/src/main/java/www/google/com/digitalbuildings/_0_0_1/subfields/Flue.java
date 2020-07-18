package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Flue 
* Chimney for conveying exhaust gas.
*/
@SuppressWarnings("serial")
public class Flue extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IFlue{

	IRI newInstance;
	public Flue(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Flue"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IFlue> getAllFluesObjectsCreated(){
		Set<IFlue> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Flue")).subjects().stream()
		.map(mapper->(IFlue)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}