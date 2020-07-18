package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Flowrate 
* Rate of fluid movement.
*/
@SuppressWarnings("serial")
public class Flowrate extends www.google.com.digitalbuildings._0_0_1.subfields.Measurement implements IFlowrate{

	IRI newInstance;
	public Flowrate(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Flowrate"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IFlowrate> getAllFlowratesObjectsCreated(){
		Set<IFlowrate> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Flowrate")).subjects().stream()
		.map(mapper->(IFlowrate)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}