package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Deadband 
* Represents a range in which the controller does not do anything.
*/
@SuppressWarnings("serial")
public class Deadband extends www.google.com.digitalbuildings._0_0_1.subfields.Measurement_descriptor implements IDeadband{

	IRI newInstance;
	public Deadband(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Deadband"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IDeadband> getAllDeadbandsObjectsCreated(){
		Set<IDeadband> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Deadband")).subjects().stream()
		.map(mapper->(IDeadband)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}