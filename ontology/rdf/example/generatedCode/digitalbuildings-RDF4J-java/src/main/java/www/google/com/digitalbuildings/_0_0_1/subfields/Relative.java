package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Relative 
* Quality of media with respect to theoretical minimum or maximum value for a given condition (e.g. relative humidity).
*/
@SuppressWarnings("serial")
public class Relative extends www.google.com.digitalbuildings._0_0_1.subfields.Measurement_descriptor implements IRelative{

	IRI newInstance;
	public Relative(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Relative"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IRelative> getAllRelativesObjectsCreated(){
		Set<IRelative> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Relative")).subjects().stream()
		.map(mapper->(IRelative)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}