package www.google.com.digitalbuildings._0_0_1.states;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Calendar_startup 
* The calendar events synchronization is starting up.
*/
@SuppressWarnings("serial")
public class Calendar_startup extends www.google.com.digitalbuildings._0_0_1.states.State implements ICalendar_startup{

	IRI newInstance;
	public Calendar_startup(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/states#Calendar_startup"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<ICalendar_startup> getAllCalendar_startupsObjectsCreated(){
		Set<ICalendar_startup> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/states#Calendar_startup")).subjects().stream()
		.map(mapper->(ICalendar_startup)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}