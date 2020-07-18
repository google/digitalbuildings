package www.google.com.digitalbuildings._0_0_1.fields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.subfields.IExhaust;
import www.google.com.digitalbuildings._0_0_1.subfields.Exhaust;
import www.google.com.digitalbuildings._0_0_1.subfields.ISpeed;
import www.google.com.digitalbuildings._0_0_1.subfields.Speed;
import www.google.com.digitalbuildings._0_0_1.subfields.IFan;
import www.google.com.digitalbuildings._0_0_1.subfields.Fan;
import www.google.com.digitalbuildings._0_0_1.subfields.IFrequency;
import www.google.com.digitalbuildings._0_0_1.subfields.Frequency;
import www.google.com.digitalbuildings._0_0_1.subfields.ISensor;
import www.google.com.digitalbuildings._0_0_1.subfields.Sensor;


@SuppressWarnings("serial")
public class Exhaust_fan_speed_frequency_sensor_1 extends www.google.com.digitalbuildings._0_0_1.fields.Field implements IExhaust_fan_speed_frequency_sensor_1{

	IRI newInstance;
	public Exhaust_fan_speed_frequency_sensor_1(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Exhaust_fan_speed_frequency_sensor_1"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addComposedOfExhaust (IExhaust parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IExhaust> getComposedOfExhaust (){
		Set<IExhaust> ComposedOfExhaust = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust) {
				ComposedOfExhaust.add((Exhaust)action);
			}
		});
		return ComposedOfExhaust;
	}


  public void addComposedOfFan (IFan parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IFan> getComposedOfFan (){
		Set<IFan> ComposedOfFan = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Fan) {
				ComposedOfFan.add((Fan)action);
			}
		});
		return ComposedOfFan;
	}


  public void addComposedOfFrequency (IFrequency parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IFrequency> getComposedOfFrequency (){
		Set<IFrequency> ComposedOfFrequency = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Frequency) {
				ComposedOfFrequency.add((Frequency)action);
			}
		});
		return ComposedOfFrequency;
	}


  public void addComposedOfSensor (ISensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<ISensor> getComposedOfSensor (){
		Set<ISensor> ComposedOfSensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Sensor) {
				ComposedOfSensor.add((Sensor)action);
			}
		});
		return ComposedOfSensor;
	}


  public void addComposedOfSpeed (ISpeed parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<ISpeed> getComposedOfSpeed (){
		Set<ISpeed> ComposedOfSpeed = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Speed) {
				ComposedOfSpeed.add((Speed)action);
			}
		});
		return ComposedOfSpeed;
	}

	public static Set<IExhaust_fan_speed_frequency_sensor_1> getAllExhaust_fan_speed_frequency_sensor_1sObjectsCreated(){
		Set<IExhaust_fan_speed_frequency_sensor_1> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Exhaust_fan_speed_frequency_sensor_1")).subjects().stream()
		.map(mapper->(IExhaust_fan_speed_frequency_sensor_1)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}