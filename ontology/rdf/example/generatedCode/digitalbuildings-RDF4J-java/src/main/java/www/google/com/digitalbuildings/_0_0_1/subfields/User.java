package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class User 
* A person who uses or operates something.
*/
@SuppressWarnings("serial")
public class User extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IUser{

	IRI newInstance;
	public User(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#User"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IUser> getAllUsersObjectsCreated(){
		Set<IUser> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#User")).subjects().stream()
		.map(mapper->(IUser)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}