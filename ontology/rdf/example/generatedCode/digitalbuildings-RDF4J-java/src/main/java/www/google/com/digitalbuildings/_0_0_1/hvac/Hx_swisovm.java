package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Hx_swisovm 
* Simple supply water isolating heat exchanger.
*/
@SuppressWarnings("serial")
public class Hx_swisovm extends www.google.com.digitalbuildings._0_0_1.hvac.Swisovm implements IHx_swisovm{

	IRI newInstance;
	public Hx_swisovm(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Hx_swisovm"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IHx_swisovm> getAllHx_swisovmsObjectsCreated(){
		Set<IHx_swisovm> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Hx_swisovm")).subjects().stream()
		.map(mapper->(IHx_swisovm)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}