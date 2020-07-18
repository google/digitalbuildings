package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Leaving 
* Area where media leaves process.
*/
@SuppressWarnings("serial")
public class Leaving extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements ILeaving{

	IRI newInstance;
	public Leaving(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Leaving"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<ILeaving> getAllLeavingsObjectsCreated(){
		Set<ILeaving> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Leaving")).subjects().stream()
		.map(mapper->(ILeaving)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}