package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Setpoint 
* Control target of process or system.
*/
@SuppressWarnings("serial")
public class Setpoint extends www.google.com.digitalbuildings._0_0_1.subfields.Point_type implements ISetpoint{

	IRI newInstance;
	public Setpoint(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Setpoint"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<ISetpoint> getAllSetpointsObjectsCreated(){
		Set<ISetpoint> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Setpoint")).subjects().stream()
		.map(mapper->(ISetpoint)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}