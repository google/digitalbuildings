package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Dmp_sdbpc 
* Exhaust control damper.
*/
@SuppressWarnings("serial")
public class Dmp_sdbpc extends www.google.com.digitalbuildings._0_0_1.hvac.Sdbpc implements IDmp_sdbpc{

	IRI newInstance;
	public Dmp_sdbpc(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Dmp_sdbpc"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IDmp_sdbpc> getAllDmp_sdbpcsObjectsCreated(){
		Set<IDmp_sdbpc> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Dmp_sdbpc")).subjects().stream()
		.map(mapper->(IDmp_sdbpc)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}