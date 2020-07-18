package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Extent 
* Distance travelled.
*/
@SuppressWarnings("serial")
public class Extent extends www.google.com.digitalbuildings._0_0_1.subfields.Measurement_descriptor implements IExtent{

	IRI newInstance;
	public Extent(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Extent"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IExtent> getAllExtentsObjectsCreated(){
		Set<IExtent> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Extent")).subjects().stream()
		.map(mapper->(IExtent)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}