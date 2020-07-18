package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Speed 
* Numeric setting of how fast to run a device, in the specified untis. Typically used to describe revolutions of a motor as a fraction of nominal or maximum.
*/
@SuppressWarnings("serial")
public class Speed extends www.google.com.digitalbuildings._0_0_1.subfields.Measurement_descriptor implements ISpeed{

	IRI newInstance;
	public Speed(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Speed"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<ISpeed> getAllSpeedsObjectsCreated(){
		Set<ISpeed> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Speed")).subjects().stream()
		.map(mapper->(ISpeed)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}