package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Pmp_ss 
* Typical pump.
*/
@SuppressWarnings("serial")
public class Pmp_ss extends www.google.com.digitalbuildings._0_0_1.hvac.Ss implements IPmp_ss{

	IRI newInstance;
	public Pmp_ss(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Pmp_ss"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IPmp_ss> getAllPmp_sssObjectsCreated(){
		Set<IPmp_ss> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Pmp_ss")).subjects().stream()
		.map(mapper->(IPmp_ss)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}