package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Requirement 
* A lower limit design parameter (e.g. minimum flowrate requirement). Is always a lower limit.
*/
@SuppressWarnings("serial")
public class Requirement extends www.google.com.digitalbuildings._0_0_1.subfields.Point_type implements IRequirement{

	IRI newInstance;
	public Requirement(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Requirement"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IRequirement> getAllRequirementsObjectsCreated(){
		Set<IRequirement> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Requirement")).subjects().stream()
		.map(mapper->(IRequirement)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}