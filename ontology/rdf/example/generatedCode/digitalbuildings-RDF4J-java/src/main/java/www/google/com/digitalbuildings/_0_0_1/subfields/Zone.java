package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Zone 
* Region of building which is conditioned.
*/
@SuppressWarnings("serial")
public class Zone extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IZone{

	IRI newInstance;
	public Zone(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Zone"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IZone> getAllZonesObjectsCreated(){
		Set<IZone> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Zone")).subjects().stream()
		.map(mapper->(IZone)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}