package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Zone_hvac 
* A zone entity representing the area served by connected HVAC entities.
*/
@SuppressWarnings("serial")
public class Zone_hvac extends www.google.com.digitalbuildings._0_0_1.hvac.Zone implements IZone_hvac{

	IRI newInstance;
	public Zone_hvac(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Zone_hvac"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IZone_hvac> getAllZone_hvacsObjectsCreated(){
		Set<IZone_hvac> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Zone_hvac")).subjects().stream()
		.map(mapper->(IZone_hvac)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}