package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Protection 
* Act of preventing damage to object.
*/
@SuppressWarnings("serial")
public class Protection extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IProtection{

	IRI newInstance;
	public Protection(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Protection"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IProtection> getAllProtectionsObjectsCreated(){
		Set<IProtection> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Protection")).subjects().stream()
		.map(mapper->(IProtection)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}