package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Static 
* Resting or stagnant value (e.g. static_pressure_sensor).
*/
@SuppressWarnings("serial")
public class Static extends www.google.com.digitalbuildings._0_0_1.subfields.Measurement_descriptor implements IStatic{

	IRI newInstance;
	public Static(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Static"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IStatic> getAllStaticsObjectsCreated(){
		Set<IStatic> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Static")).subjects().stream()
		.map(mapper->(IStatic)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}