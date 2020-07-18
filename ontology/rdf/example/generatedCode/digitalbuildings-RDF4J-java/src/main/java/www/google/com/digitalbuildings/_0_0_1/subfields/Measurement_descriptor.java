package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Measurement_descriptor 
*/
@SuppressWarnings("serial")
public class Measurement_descriptor extends www.google.com.digitalbuildings._0_0_1.subfields.SubField implements IMeasurement_descriptor{

	IRI newInstance;
	public Measurement_descriptor(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Measurement_descriptor"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IMeasurement_descriptor> getAllMeasurement_descriptorsObjectsCreated(){
		Set<IMeasurement_descriptor> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Measurement_descriptor")).subjects().stream()
		.map(mapper->(IMeasurement_descriptor)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}