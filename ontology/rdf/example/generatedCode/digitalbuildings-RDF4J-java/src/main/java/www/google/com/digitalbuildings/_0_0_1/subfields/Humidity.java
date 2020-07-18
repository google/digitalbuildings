package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Humidity 
* Concentration of water vapor in air (conditioned or unconditioned).
*/
@SuppressWarnings("serial")
public class Humidity extends www.google.com.digitalbuildings._0_0_1.subfields.Measurement implements IHumidity{

	IRI newInstance;
	public Humidity(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Humidity"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IHumidity> getAllHumiditysObjectsCreated(){
		Set<IHumidity> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Humidity")).subjects().stream()
		.map(mapper->(IHumidity)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}