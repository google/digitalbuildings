package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Coil 
* Component that exchanges heat between two media streams.
*/
@SuppressWarnings("serial")
public class Coil extends www.google.com.digitalbuildings._0_0_1.subfields.Component implements ICoil{

	IRI newInstance;
	public Coil(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Coil"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<ICoil> getAllCoilsObjectsCreated(){
		Set<ICoil> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Coil")).subjects().stream()
		.map(mapper->(ICoil)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}