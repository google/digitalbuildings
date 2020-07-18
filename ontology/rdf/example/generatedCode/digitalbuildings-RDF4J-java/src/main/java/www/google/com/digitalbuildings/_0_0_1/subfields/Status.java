package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Status 
* The multistate value indicating an observed state in a piece of equipment, often indicating if a command was effected.
*/
@SuppressWarnings("serial")
public class Status extends www.google.com.digitalbuildings._0_0_1.subfields.Point_type implements IStatus{

	IRI newInstance;
	public Status(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Status"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IStatus> getAllStatussObjectsCreated(){
		Set<IStatus> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Status")).subjects().stream()
		.map(mapper->(IStatus)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}