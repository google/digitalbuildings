package www.google.com.digitalbuildings._0_0_1.units;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Volume 
*/
@SuppressWarnings("serial")
public class Volume extends www.google.com.digitalbuildings._0_0_1.units.Unit implements IVolume{

	IRI newInstance;
	public Volume(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/units#Volume"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IVolume> getAllVolumesObjectsCreated(){
		Set<IVolume> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/units#Volume")).subjects().stream()
		.map(mapper->(IVolume)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}