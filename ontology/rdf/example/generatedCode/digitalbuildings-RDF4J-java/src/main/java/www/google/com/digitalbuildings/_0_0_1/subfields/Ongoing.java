package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Ongoing 
* Hapenning currently, right now.
*/
@SuppressWarnings("serial")
public class Ongoing extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IOngoing{

	IRI newInstance;
	public Ongoing(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Ongoing"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IOngoing> getAllOngoingsObjectsCreated(){
		Set<IOngoing> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Ongoing")).subjects().stream()
		.map(mapper->(IOngoing)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}