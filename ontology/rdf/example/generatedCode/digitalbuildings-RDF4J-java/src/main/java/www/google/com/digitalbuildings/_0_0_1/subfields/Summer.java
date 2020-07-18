package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Summer 
* Method or process used during warmer weather (i.e. summer season).
*/
@SuppressWarnings("serial")
public class Summer extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements ISummer{

	IRI newInstance;
	public Summer(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Summer"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<ISummer> getAllSummersObjectsCreated(){
		Set<ISummer> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Summer")).subjects().stream()
		.map(mapper->(ISummer)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}