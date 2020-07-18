package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Min 
* Minimum value (e.g. Min_Ventilation_Air_Flow_Setpoint)
*/
@SuppressWarnings("serial")
public class Min extends www.google.com.digitalbuildings._0_0_1.subfields.Aggregation implements IMin{

	IRI newInstance;
	public Min(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Min"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IMin> getAllMinsObjectsCreated(){
		Set<IMin> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Min")).subjects().stream()
		.map(mapper->(IMin)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}