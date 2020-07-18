package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Southwest 
* Inter-cardinal direction between South and West.
*/
@SuppressWarnings("serial")
public class Southwest extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements ISouthwest{

	IRI newInstance;
	public Southwest(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Southwest"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<ISouthwest> getAllSouthwestsObjectsCreated(){
		Set<ISouthwest> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Southwest")).subjects().stream()
		.map(mapper->(ISouthwest)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}