package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Winter 
* Method or process used during colder weather (i.e. winter season).
*/
@SuppressWarnings("serial")
public class Winter extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IWinter{

	IRI newInstance;
	public Winter(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Winter"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IWinter> getAllWintersObjectsCreated(){
		Set<IWinter> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Winter")).subjects().stream()
		.map(mapper->(IWinter)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}