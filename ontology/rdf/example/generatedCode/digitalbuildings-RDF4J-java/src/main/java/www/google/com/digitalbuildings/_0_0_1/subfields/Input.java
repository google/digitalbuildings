package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Input 
* The input to a system.
*/
@SuppressWarnings("serial")
public class Input extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IInput{

	IRI newInstance;
	public Input(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Input"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IInput> getAllInputsObjectsCreated(){
		Set<IInput> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Input")).subjects().stream()
		.map(mapper->(IInput)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}