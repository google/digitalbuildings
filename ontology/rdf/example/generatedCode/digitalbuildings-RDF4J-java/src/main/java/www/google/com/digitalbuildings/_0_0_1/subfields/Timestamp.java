package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Timestamp 
* An instant in time, represented as a numeric offset from the epoch.
*/
@SuppressWarnings("serial")
public class Timestamp extends www.google.com.digitalbuildings._0_0_1.subfields.Point_type implements ITimestamp{

	IRI newInstance;
	public Timestamp(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Timestamp"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<ITimestamp> getAllTimestampsObjectsCreated(){
		Set<ITimestamp> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Timestamp")).subjects().stream()
		.map(mapper->(ITimestamp)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}