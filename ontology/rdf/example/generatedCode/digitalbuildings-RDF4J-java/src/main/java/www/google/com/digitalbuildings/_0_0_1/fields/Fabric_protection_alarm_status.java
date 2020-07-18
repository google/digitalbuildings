package www.google.com.digitalbuildings._0_0_1.fields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.subfields.IStatus;
import www.google.com.digitalbuildings._0_0_1.subfields.Status;
import www.google.com.digitalbuildings._0_0_1.subfields.IAlarm;
import www.google.com.digitalbuildings._0_0_1.subfields.Alarm;
import www.google.com.digitalbuildings._0_0_1.subfields.IFabric;
import www.google.com.digitalbuildings._0_0_1.subfields.Fabric;
import www.google.com.digitalbuildings._0_0_1.subfields.IProtection;
import www.google.com.digitalbuildings._0_0_1.subfields.Protection;


@SuppressWarnings("serial")
public class Fabric_protection_alarm_status extends www.google.com.digitalbuildings._0_0_1.fields.Field implements IFabric_protection_alarm_status{

	IRI newInstance;
	public Fabric_protection_alarm_status(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Fabric_protection_alarm_status"));
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


  public void addComposedOfFabric (IFabric parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IFabric> getComposedOfFabric (){
		Set<IFabric> ComposedOfFabric = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Fabric) {
				ComposedOfFabric.add((Fabric)action);
			}
		});
		return ComposedOfFabric;
	}


  public void addComposedOfProtection (IProtection parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IProtection> getComposedOfProtection (){
		Set<IProtection> ComposedOfProtection = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Protection) {
				ComposedOfProtection.add((Protection)action);
			}
		});
		return ComposedOfProtection;
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

	public static Set<IFabric_protection_alarm_status> getAllFabric_protection_alarm_statussObjectsCreated(){
		Set<IFabric_protection_alarm_status> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Fabric_protection_alarm_status")).subjects().stream()
		.map(mapper->(IFabric_protection_alarm_status)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}