package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class End 
* Indicates a final part of something, especially a period of time.
*/
@SuppressWarnings("serial")
public class End extends www.google.com.digitalbuildings._0_0_1.subfields.Measurement_descriptor implements IEnd{

	IRI newInstance;
	public End(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#End"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IEnd> getAllEndsObjectsCreated(){
		Set<IEnd> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#End")).subjects().stream()
		.map(mapper->(IEnd)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}