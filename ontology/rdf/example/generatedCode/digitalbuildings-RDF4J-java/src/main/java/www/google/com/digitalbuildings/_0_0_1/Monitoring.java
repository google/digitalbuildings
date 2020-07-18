package www.google.com.digitalbuildings._0_0_1;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Monitoring 
*/
@SuppressWarnings("serial")
public class Monitoring extends www.google.com.digitalbuildings._0_0_1.Application implements IMonitoring{

	IRI newInstance;
	public Monitoring(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#Monitoring"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IMonitoring> getAllMonitoringsObjectsCreated(){
		Set<IMonitoring> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1#Monitoring")).subjects().stream()
		.map(mapper->(IMonitoring)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}