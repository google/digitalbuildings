package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Phase3 
* The third (nominally C) phase of three-phase power distribution systems.
*/
@SuppressWarnings("serial")
public class Phase3 extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IPhase3{

	IRI newInstance;
	public Phase3(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Phase3"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IPhase3> getAllPhase3sObjectsCreated(){
		Set<IPhase3> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Phase3")).subjects().stream()
		.map(mapper->(IPhase3)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}