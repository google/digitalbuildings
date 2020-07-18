package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Fabric 
* Textile material.
*/
@SuppressWarnings("serial")
public class Fabric extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IFabric{

	IRI newInstance;
	public Fabric(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Fabric"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IFabric> getAllFabricsObjectsCreated(){
		Set<IFabric> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Fabric")).subjects().stream()
		.map(mapper->(IFabric)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}