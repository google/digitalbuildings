package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Hx_hwswc 
* Heating outlet control heat exchanger.
*/
@SuppressWarnings("serial")
public class Hx_hwswc extends www.google.com.digitalbuildings._0_0_1.hvac.Hwswc implements IHx_hwswc{

	IRI newInstance;
	public Hx_hwswc(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Hx_hwswc"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IHx_hwswc> getAllHx_hwswcsObjectsCreated(){
		Set<IHx_hwswc> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Hx_hwswc")).subjects().stream()
		.map(mapper->(IHx_hwswc)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}