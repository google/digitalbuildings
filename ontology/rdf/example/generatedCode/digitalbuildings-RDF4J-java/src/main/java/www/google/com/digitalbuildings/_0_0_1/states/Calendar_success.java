package www.google.com.digitalbuildings._0_0_1.states;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Calendar_success 
* The calendar events synchronization was successful.
*/
@SuppressWarnings("serial")
public class Calendar_success extends www.google.com.digitalbuildings._0_0_1.states.State implements ICalendar_success{

	IRI newInstance;
	public Calendar_success(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/states#Calendar_success"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<ICalendar_success> getAllCalendar_successsObjectsCreated(){
		Set<ICalendar_success> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/states#Calendar_success")).subjects().stream()
		.map(mapper->(ICalendar_success)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}