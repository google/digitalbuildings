package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Saturation 
* Point at which no more of a material can be absorbed into another material.
*/
@SuppressWarnings("serial")
public class Saturation extends www.google.com.digitalbuildings._0_0_1.subfields.Measurement_descriptor implements ISaturation{

	IRI newInstance;
	public Saturation(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Saturation"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<ISaturation> getAllSaturationsObjectsCreated(){
		Set<ISaturation> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Saturation")).subjects().stream()
		.map(mapper->(ISaturation)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}