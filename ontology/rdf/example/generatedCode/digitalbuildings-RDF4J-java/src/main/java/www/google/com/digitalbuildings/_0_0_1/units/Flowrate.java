package www.google.com.digitalbuildings._0_0_1.units;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Flowrate 
*/
@SuppressWarnings("serial")
public class Flowrate extends www.google.com.digitalbuildings._0_0_1.units.Unit implements IFlowrate{

	IRI newInstance;
	public Flowrate(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/units#Flowrate"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IFlowrate> getAllFlowratesObjectsCreated(){
		Set<IFlowrate> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/units#Flowrate")).subjects().stream()
		.map(mapper->(IFlowrate)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}