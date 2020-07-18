package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class No2 
* Nitrogen dioxide.
*/
@SuppressWarnings("serial")
public class No2 extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements INo2{

	IRI newInstance;
	public No2(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#No2"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<INo2> getAllNo2sObjectsCreated(){
		Set<INo2> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#No2")).subjects().stream()
		.map(mapper->(INo2)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}