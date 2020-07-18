package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Cdws_swtc 
* Simple condenser water system with supply control.
*/
@SuppressWarnings("serial")
public class Cdws_swtc extends www.google.com.digitalbuildings._0_0_1.hvac.Swtc implements ICdws_swtc{

	IRI newInstance;
	public Cdws_swtc(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Cdws_swtc"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<ICdws_swtc> getAllCdws_swtcsObjectsCreated(){
		Set<ICdws_swtc> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Cdws_swtc")).subjects().stream()
		.map(mapper->(ICdws_swtc)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}