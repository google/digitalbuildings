package www.google.com.digitalbuildings._0_0_1.fields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.subfields.IStatus;
import www.google.com.digitalbuildings._0_0_1.subfields.Status;
import www.google.com.digitalbuildings._0_0_1.subfields.IFilter;
import www.google.com.digitalbuildings._0_0_1.subfields.Filter;
import www.google.com.digitalbuildings._0_0_1.subfields.IAlarm;
import www.google.com.digitalbuildings._0_0_1.subfields.Alarm;


@SuppressWarnings("serial")
public class Filter_alarm_status extends www.google.com.digitalbuildings._0_0_1.fields.Field implements IFilter_alarm_status{

	IRI newInstance;
	public Filter_alarm_status(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Filter_alarm_status"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addComposedOfAlarm (IAlarm parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IAlarm> getComposedOfAlarm (){
		Set<IAlarm> ComposedOfAlarm = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Alarm) {
				ComposedOfAlarm.add((Alarm)action);
			}
		});
		return ComposedOfAlarm;
	}


  public void addComposedOfFilter (IFilter parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IFilter> getComposedOfFilter (){
		Set<IFilter> ComposedOfFilter = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Filter) {
				ComposedOfFilter.add((Filter)action);
			}
		});
		return ComposedOfFilter;
	}


  public void addComposedOfStatus (IStatus parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IStatus> getComposedOfStatus (){
		Set<IStatus> ComposedOfStatus = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Status) {
				ComposedOfStatus.add((Status)action);
			}
		});
		return ComposedOfStatus;
	}

	public static Set<IFilter_alarm_status> getAllFilter_alarm_statussObjectsCreated(){
		Set<IFilter_alarm_status> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Filter_alarm_status")).subjects().stream()
		.map(mapper->(IFilter_alarm_status)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}