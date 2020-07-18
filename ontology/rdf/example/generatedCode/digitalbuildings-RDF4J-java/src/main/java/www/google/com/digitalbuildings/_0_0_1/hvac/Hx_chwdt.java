package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Hx_chwdt 
* Condenser/chilled water heat exchanger.
*/
@SuppressWarnings("serial")
public class Hx_chwdt extends www.google.com.digitalbuildings._0_0_1.hvac.Chwdt implements IHx_chwdt{

	IRI newInstance;
	public Hx_chwdt(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Hx_chwdt"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IHx_chwdt> getAllHx_chwdtsObjectsCreated(){
		Set<IHx_chwdt> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Hx_chwdt")).subjects().stream()
		.map(mapper->(IHx_chwdt)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}