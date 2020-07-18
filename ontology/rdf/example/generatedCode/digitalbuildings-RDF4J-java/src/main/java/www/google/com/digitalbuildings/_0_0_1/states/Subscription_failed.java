package www.google.com.digitalbuildings._0_0_1.states;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Subscription_failed 
* The calendar events subscription has failed.
*/
@SuppressWarnings("serial")
public class Subscription_failed extends www.google.com.digitalbuildings._0_0_1.states.State implements ISubscription_failed{

	IRI newInstance;
	public Subscription_failed(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/states#Subscription_failed"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<ISubscription_failed> getAllSubscription_failedsObjectsCreated(){
		Set<ISubscription_failed> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/states#Subscription_failed")).subjects().stream()
		.map(mapper->(ISubscription_failed)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}