package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Bypass 
* Route which fluid takes to bypass process.
*/
@SuppressWarnings("serial")
public class Bypass extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IBypass{

	IRI newInstance;
	public Bypass(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Bypass"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IBypass> getAllBypasssObjectsCreated(){
		Set<IBypass> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Bypass")).subjects().stream()
		.map(mapper->(IBypass)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}