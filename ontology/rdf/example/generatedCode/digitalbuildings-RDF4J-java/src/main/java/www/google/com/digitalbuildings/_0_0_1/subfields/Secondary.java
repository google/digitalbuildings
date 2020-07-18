package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Secondary 
* Associated with the secondary (distribution) loop of a produciton process.
*/
@SuppressWarnings("serial")
public class Secondary extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements ISecondary{

	IRI newInstance;
	public Secondary(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Secondary"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<ISecondary> getAllSecondarysObjectsCreated(){
		Set<ISecondary> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Secondary")).subjects().stream()
		.map(mapper->(ISecondary)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}