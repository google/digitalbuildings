package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Override 
* An action that interrupts, cancels, or changes the current action or status.
*/
@SuppressWarnings("serial")
public class Override extends www.google.com.digitalbuildings._0_0_1.subfields.Measurement_descriptor implements IOverride{

	IRI newInstance;
	public Override(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Override"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IOverride> getAllOverridesObjectsCreated(){
		Set<IOverride> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Override")).subjects().stream()
		.map(mapper->(IOverride)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}