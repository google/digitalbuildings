package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Phase1 
* The first (nominally A) phase of three-phase power distribution systems.
*/
@SuppressWarnings("serial")
public class Phase1 extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IPhase1{

	IRI newInstance;
	public Phase1(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Phase1"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IPhase1> getAllPhase1sObjectsCreated(){
		Set<IPhase1> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Phase1")).subjects().stream()
		.map(mapper->(IPhase1)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}