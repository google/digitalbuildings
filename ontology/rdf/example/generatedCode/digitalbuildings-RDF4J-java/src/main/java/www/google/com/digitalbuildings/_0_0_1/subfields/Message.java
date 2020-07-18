package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Message 
* A communication sent to or left for a recipient.
*/
@SuppressWarnings("serial")
public class Message extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IMessage{

	IRI newInstance;
	public Message(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Message"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IMessage> getAllMessagesObjectsCreated(){
		Set<IMessage> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Message")).subjects().stream()
		.map(mapper->(IMessage)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}