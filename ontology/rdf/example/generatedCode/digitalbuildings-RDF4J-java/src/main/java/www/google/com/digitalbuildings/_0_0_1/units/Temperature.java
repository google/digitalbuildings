package www.google.com.digitalbuildings._0_0_1.units;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Temperature 
*/
@SuppressWarnings("serial")
public class Temperature extends www.google.com.digitalbuildings._0_0_1.units.Unit implements ITemperature{

	IRI newInstance;
	public Temperature(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/units#Temperature"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<ITemperature> getAllTemperaturesObjectsCreated(){
		Set<ITemperature> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/units#Temperature")).subjects().stream()
		.map(mapper->(ITemperature)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}