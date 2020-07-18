package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Voltage 
* Electrical potential difference between two reference points.
*/
@SuppressWarnings("serial")
public class Voltage extends www.google.com.digitalbuildings._0_0_1.subfields.Measurement implements IVoltage{

	IRI newInstance;
	public Voltage(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Voltage"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IVoltage> getAllVoltagesObjectsCreated(){
		Set<IVoltage> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Voltage")).subjects().stream()
		.map(mapper->(IVoltage)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}