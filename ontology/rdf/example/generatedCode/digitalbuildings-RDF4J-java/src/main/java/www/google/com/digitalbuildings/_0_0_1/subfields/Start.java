package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Start 
* Indicates a point in time or space at which something has its origin or beginning.
*/
@SuppressWarnings("serial")
public class Start extends www.google.com.digitalbuildings._0_0_1.subfields.Measurement_descriptor implements IStart{

	IRI newInstance;
	public Start(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Start"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IStart> getAllStartsObjectsCreated(){
		Set<IStart> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Start")).subjects().stream()
		.map(mapper->(IStart)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}