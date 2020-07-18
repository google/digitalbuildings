package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Southeast 
* Inter-cardinal direction between South and East.
*/
@SuppressWarnings("serial")
public class Southeast extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements ISoutheast{

	IRI newInstance;
	public Southeast(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Southeast"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<ISoutheast> getAllSoutheastsObjectsCreated(){
		Set<ISoutheast> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Southeast")).subjects().stream()
		.map(mapper->(ISoutheast)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}