package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Loop 
* Recirculating loop.
*/
@SuppressWarnings("serial")
public class Loop extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements ILoop{

	IRI newInstance;
	public Loop(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Loop"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<ILoop> getAllLoopsObjectsCreated(){
		Set<ILoop> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Loop")).subjects().stream()
		.map(mapper->(ILoop)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}