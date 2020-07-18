package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Point_type 
*/
@SuppressWarnings("serial")
public class Point_type extends www.google.com.digitalbuildings._0_0_1.subfields.SubField implements IPoint_type{

	IRI newInstance;
	public Point_type(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Point_type"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IPoint_type> getAllPoint_typesObjectsCreated(){
		Set<IPoint_type> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Point_type")).subjects().stream()
		.map(mapper->(IPoint_type)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}