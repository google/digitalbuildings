package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Sensor 
* Component used to measure some quality of a system or process. Can be feedback for an analog command.
*/
@SuppressWarnings("serial")
public class Sensor extends www.google.com.digitalbuildings._0_0_1.subfields.Point_type implements ISensor{

	IRI newInstance;
	public Sensor(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Sensor"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<ISensor> getAllSensorsObjectsCreated(){
		Set<ISensor> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Sensor")).subjects().stream()
		.map(mapper->(ISensor)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}