package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Apparent 
* The combination of reactive and real components (power).
*/
@SuppressWarnings("serial")
public class Apparent extends www.google.com.digitalbuildings._0_0_1.subfields.Measurement_descriptor implements IApparent{

	IRI newInstance;
	public Apparent(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Apparent"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IApparent> getAllApparentsObjectsCreated(){
		Set<IApparent> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Apparent")).subjects().stream()
		.map(mapper->(IApparent)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}