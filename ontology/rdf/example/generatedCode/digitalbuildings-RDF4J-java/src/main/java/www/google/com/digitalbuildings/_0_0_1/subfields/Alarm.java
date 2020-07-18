package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Alarm 
* Signal that an alarm is present.
*/
@SuppressWarnings("serial")
public class Alarm extends www.google.com.digitalbuildings._0_0_1.subfields.Measurement_descriptor implements IAlarm{

	IRI newInstance;
	public Alarm(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Alarm"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IAlarm> getAllAlarmsObjectsCreated(){
		Set<IAlarm> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Alarm")).subjects().stream()
		.map(mapper->(IAlarm)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}