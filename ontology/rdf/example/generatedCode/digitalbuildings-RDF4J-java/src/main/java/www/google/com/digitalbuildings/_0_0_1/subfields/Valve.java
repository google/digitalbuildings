package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Valve 
* Component which meters the flow of water within a system or device.
*/
@SuppressWarnings("serial")
public class Valve extends www.google.com.digitalbuildings._0_0_1.subfields.Component implements IValve{

	IRI newInstance;
	public Valve(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Valve"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IValve> getAllValvesObjectsCreated(){
		Set<IValve> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Valve")).subjects().stream()
		.map(mapper->(IValve)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}