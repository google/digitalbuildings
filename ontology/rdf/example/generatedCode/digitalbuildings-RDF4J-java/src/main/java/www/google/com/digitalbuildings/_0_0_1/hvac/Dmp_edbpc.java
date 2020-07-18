package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Dmp_edbpc 
* Stand-alone building pressure control damper.
*/
@SuppressWarnings("serial")
public class Dmp_edbpc extends www.google.com.digitalbuildings._0_0_1.hvac.Edbpc implements IDmp_edbpc{

	IRI newInstance;
	public Dmp_edbpc(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Dmp_edbpc"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IDmp_edbpc> getAllDmp_edbpcsObjectsCreated(){
		Set<IDmp_edbpc> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Dmp_edbpc")).subjects().stream()
		.map(mapper->(IDmp_edbpc)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}