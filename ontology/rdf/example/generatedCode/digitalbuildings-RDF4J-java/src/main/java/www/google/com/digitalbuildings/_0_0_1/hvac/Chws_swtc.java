package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Chws_swtc 
* Chilled water system with basic supply water temperature control. 
*/
@SuppressWarnings("serial")
public class Chws_swtc extends www.google.com.digitalbuildings._0_0_1.hvac.Swtc implements IChws_swtc{

	IRI newInstance;
	public Chws_swtc(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Chws_swtc"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IChws_swtc> getAllChws_swtcsObjectsCreated(){
		Set<IChws_swtc> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Chws_swtc")).subjects().stream()
		.map(mapper->(IChws_swtc)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}