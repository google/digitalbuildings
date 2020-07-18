package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Pump 
* Component used for the distribution of liquid media.
*/
@SuppressWarnings("serial")
public class Pump extends www.google.com.digitalbuildings._0_0_1.subfields.Component implements IPump{

	IRI newInstance;
	public Pump(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Pump"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IPump> getAllPumpsObjectsCreated(){
		Set<IPump> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Pump")).subjects().stream()
		.map(mapper->(IPump)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}