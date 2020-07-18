package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Hws_rwtc 
* Simple heating water system with return temp control.
*/
@SuppressWarnings("serial")
public class Hws_rwtc extends www.google.com.digitalbuildings._0_0_1.hvac.Rwtc implements IHws_rwtc{

	IRI newInstance;
	public Hws_rwtc(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Hws_rwtc"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IHws_rwtc> getAllHws_rwtcsObjectsCreated(){
		Set<IHws_rwtc> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Hws_rwtc")).subjects().stream()
		.map(mapper->(IHws_rwtc)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}