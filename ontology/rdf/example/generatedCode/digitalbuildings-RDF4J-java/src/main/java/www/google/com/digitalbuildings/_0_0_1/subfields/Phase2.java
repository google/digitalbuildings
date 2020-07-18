package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Phase2 
* The second (nominally B) phase of three-phase power distribution systems.
*/
@SuppressWarnings("serial")
public class Phase2 extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IPhase2{

	IRI newInstance;
	public Phase2(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Phase2"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IPhase2> getAllPhase2sObjectsCreated(){
		Set<IPhase2> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Phase2")).subjects().stream()
		.map(mapper->(IPhase2)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}