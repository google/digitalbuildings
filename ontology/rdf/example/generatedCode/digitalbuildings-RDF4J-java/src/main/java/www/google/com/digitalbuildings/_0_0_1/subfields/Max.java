package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Max 
* Maximum value (e.g. Max_Cooling_Air_Flow_Setpoint)
*/
@SuppressWarnings("serial")
public class Max extends www.google.com.digitalbuildings._0_0_1.subfields.Aggregation implements IMax{

	IRI newInstance;
	public Max(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Max"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IMax> getAllMaxsObjectsCreated(){
		Set<IMax> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Max")).subjects().stream()
		.map(mapper->(IMax)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}