package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Glycol 
* Liquid mixture consisting of glycol and water 
*/
@SuppressWarnings("serial")
public class Glycol extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IGlycol{

	IRI newInstance;
	public Glycol(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Glycol"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IGlycol> getAllGlycolsObjectsCreated(){
		Set<IGlycol> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Glycol")).subjects().stream()
		.map(mapper->(IGlycol)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}