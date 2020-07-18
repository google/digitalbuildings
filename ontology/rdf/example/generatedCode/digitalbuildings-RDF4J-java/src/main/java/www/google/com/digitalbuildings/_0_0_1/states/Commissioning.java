package www.google.com.digitalbuildings._0_0_1.states;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Commissioning 
* The fan speed and valve positions are set to preconfigured parameters.
*/
@SuppressWarnings("serial")
public class Commissioning extends www.google.com.digitalbuildings._0_0_1.states.State implements ICommissioning{

	IRI newInstance;
	public Commissioning(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/states#Commissioning"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<ICommissioning> getAllCommissioningsObjectsCreated(){
		Set<ICommissioning> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/states#Commissioning")).subjects().stream()
		.map(mapper->(ICommissioning)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}