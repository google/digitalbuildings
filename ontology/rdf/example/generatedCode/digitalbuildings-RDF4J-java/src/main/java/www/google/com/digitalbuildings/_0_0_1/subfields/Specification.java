package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Specification 
* The specified design value for a particular operating condition (differential pressure specification).
*/
@SuppressWarnings("serial")
public class Specification extends www.google.com.digitalbuildings._0_0_1.subfields.Point_type implements ISpecification{

	IRI newInstance;
	public Specification(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Specification"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<ISpecification> getAllSpecificationsObjectsCreated(){
		Set<ISpecification> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Specification")).subjects().stream()
		.map(mapper->(ISpecification)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}