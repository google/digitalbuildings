package www.google.com.digitalbuildings._0_0_1.fields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.subfields.IMaster;
import www.google.com.digitalbuildings._0_0_1.subfields.Master;
import www.google.com.digitalbuildings._0_0_1.subfields.IStatus;
import www.google.com.digitalbuildings._0_0_1.subfields.Status;
import www.google.com.digitalbuildings._0_0_1.subfields.IAlarm;
import www.google.com.digitalbuildings._0_0_1.subfields.Alarm;


@SuppressWarnings("serial")
public class Master_alarm_status extends www.google.com.digitalbuildings._0_0_1.fields.Field implements IMaster_alarm_status{

	IRI newInstance;
	public Master_alarm_status(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Master_alarm_status"));
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


  public void addComposedOfMaster (IMaster parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IMaster> getComposedOfMaster (){
		Set<IMaster> ComposedOfMaster = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Master) {
				ComposedOfMaster.add((Master)action);
			}
		});
		return ComposedOfMaster;
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

	public static Set<IMaster_alarm_status> getAllMaster_alarm_statussObjectsCreated(){
		Set<IMaster_alarm_status> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Master_alarm_status")).subjects().stream()
		.map(mapper->(IMaster_alarm_status)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}