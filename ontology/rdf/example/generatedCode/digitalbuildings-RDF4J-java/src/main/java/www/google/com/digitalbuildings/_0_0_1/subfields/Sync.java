package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Sync 
* The simultaneous operation or activity of two or more things.
*/
@SuppressWarnings("serial")
public class Sync extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements ISync{

	IRI newInstance;
	public Sync(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Sync"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<ISync> getAllSyncsObjectsCreated(){
		Set<ISync> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Sync")).subjects().stream()
		.map(mapper->(ISync)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}