package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Hws_swtc 
* Simple heating water system with supply temp control.
*/
@SuppressWarnings("serial")
public class Hws_swtc extends www.google.com.digitalbuildings._0_0_1.hvac.Swtc implements IHws_swtc{

	IRI newInstance;
	public Hws_swtc(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Hws_swtc"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IHws_swtc> getAllHws_swtcsObjectsCreated(){
		Set<IHws_swtc> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Hws_swtc")).subjects().stream()
		.map(mapper->(IHws_swtc)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}