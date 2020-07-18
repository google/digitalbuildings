package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Reversing 
* Reverses direction of flow (e.g. reversing valve on heat pump).
*/
@SuppressWarnings("serial")
public class Reversing extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IReversing{

	IRI newInstance;
	public Reversing(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Reversing"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IReversing> getAllReversingsObjectsCreated(){
		Set<IReversing> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Reversing")).subjects().stream()
		.map(mapper->(IReversing)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}