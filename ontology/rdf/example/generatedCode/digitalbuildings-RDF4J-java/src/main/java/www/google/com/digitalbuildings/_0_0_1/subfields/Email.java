package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Email 
* A unique identifier address in the Internet.
*/
@SuppressWarnings("serial")
public class Email extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IEmail{

	IRI newInstance;
	public Email(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Email"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IEmail> getAllEmailsObjectsCreated(){
		Set<IEmail> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Email")).subjects().stream()
		.map(mapper->(IEmail)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}