package www.google.com.digitalbuildings._0_0_1.units;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Illuminance 
*/
@SuppressWarnings("serial")
public class Illuminance extends www.google.com.digitalbuildings._0_0_1.units.Unit implements IIlluminance{

	IRI newInstance;
	public Illuminance(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/units#Illuminance"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IIlluminance> getAllIlluminancesObjectsCreated(){
		Set<IIlluminance> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/units#Illuminance")).subjects().stream()
		.map(mapper->(IIlluminance)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}