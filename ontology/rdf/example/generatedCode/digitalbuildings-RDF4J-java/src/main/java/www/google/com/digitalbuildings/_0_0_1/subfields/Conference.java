package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Conference 
* An instance of speaking or meeting among multiple people.
*/
@SuppressWarnings("serial")
public class Conference extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IConference{

	IRI newInstance;
	public Conference(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Conference"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IConference> getAllConferencesObjectsCreated(){
		Set<IConference> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Conference")).subjects().stream()
		.map(mapper->(IConference)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}