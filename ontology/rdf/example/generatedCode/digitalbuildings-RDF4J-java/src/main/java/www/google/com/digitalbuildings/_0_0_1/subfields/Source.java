package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Source 
* The upstream source of conditioning (used specifically for heat exchangers).
*/
@SuppressWarnings("serial")
public class Source extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements ISource{

	IRI newInstance;
	public Source(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Source"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<ISource> getAllSourcesObjectsCreated(){
		Set<ISource> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Source")).subjects().stream()
		.map(mapper->(ISource)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}