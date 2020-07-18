package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Absolute 
* Quality of media with respect to non-relativistic boudaries (e.g. absolute temperature).
*/
@SuppressWarnings("serial")
public class Absolute extends www.google.com.digitalbuildings._0_0_1.subfields.Measurement_descriptor implements IAbsolute{

	IRI newInstance;
	public Absolute(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Absolute"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IAbsolute> getAllAbsolutesObjectsCreated(){
		Set<IAbsolute> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Absolute")).subjects().stream()
		.map(mapper->(IAbsolute)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}