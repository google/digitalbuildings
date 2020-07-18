package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Cold 
* Associated with cold area or process.
*/
@SuppressWarnings("serial")
public class Cold extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements ICold{

	IRI newInstance;
	public Cold(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Cold"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<ICold> getAllColdsObjectsCreated(){
		Set<ICold> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Cold")).subjects().stream()
		.map(mapper->(ICold)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}