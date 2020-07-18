package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Tertiary 
* Associated with the tertiary (peripheral) loops of a production process.
*/
@SuppressWarnings("serial")
public class Tertiary extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements ITertiary{

	IRI newInstance;
	public Tertiary(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Tertiary"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<ITertiary> getAllTertiarysObjectsCreated(){
		Set<ITertiary> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Tertiary")).subjects().stream()
		.map(mapper->(ITertiary)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}