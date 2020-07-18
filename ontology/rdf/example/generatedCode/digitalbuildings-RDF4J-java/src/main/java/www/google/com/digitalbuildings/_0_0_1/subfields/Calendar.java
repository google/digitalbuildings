package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Calendar 
* A system structured around the days, weeks, and the months, used to manage schedules.
*/
@SuppressWarnings("serial")
public class Calendar extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements ICalendar{

	IRI newInstance;
	public Calendar(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Calendar"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<ICalendar> getAllCalendarsObjectsCreated(){
		Set<ICalendar> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Calendar")).subjects().stream()
		.map(mapper->(ICalendar)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}