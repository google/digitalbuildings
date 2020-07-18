package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Average 
* Average value (e.g. average_zone_air_temperature_sensor)
*/
@SuppressWarnings("serial")
public class Average extends www.google.com.digitalbuildings._0_0_1.subfields.Aggregation implements IAverage{

	IRI newInstance;
	public Average(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Average"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IAverage> getAllAveragesObjectsCreated(){
		Set<IAverage> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Average")).subjects().stream()
		.map(mapper->(IAverage)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}