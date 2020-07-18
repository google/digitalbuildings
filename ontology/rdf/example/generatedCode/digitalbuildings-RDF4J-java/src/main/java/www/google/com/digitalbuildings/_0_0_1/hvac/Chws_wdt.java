package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Chws_wdt 
* Chilled water system with only basic delta-T monitoring.
*/
@SuppressWarnings("serial")
public class Chws_wdt extends www.google.com.digitalbuildings._0_0_1.hvac.Wdt implements IChws_wdt{

	IRI newInstance;
	public Chws_wdt(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Chws_wdt"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IChws_wdt> getAllChws_wdtsObjectsCreated(){
		Set<IChws_wdt> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Chws_wdt")).subjects().stream()
		.map(mapper->(IChws_wdt)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}