package www.google.com.digitalbuildings._0_0_1.fields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.subfields.IEast;
import www.google.com.digitalbuildings._0_0_1.subfields.East;
import www.google.com.digitalbuildings._0_0_1.subfields.IIlluminance;
import www.google.com.digitalbuildings._0_0_1.subfields.Illuminance;
import www.google.com.digitalbuildings._0_0_1.subfields.ISensor;
import www.google.com.digitalbuildings._0_0_1.subfields.Sensor;


@SuppressWarnings("serial")
public class East_illuminance_sensor extends www.google.com.digitalbuildings._0_0_1.fields.Field implements IEast_illuminance_sensor{

	IRI newInstance;
	public East_illuminance_sensor(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#East_illuminance_sensor"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addComposedOfEast (IEast parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IEast> getComposedOfEast (){
		Set<IEast> ComposedOfEast = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof East) {
				ComposedOfEast.add((East)action);
			}
		});
		return ComposedOfEast;
	}


  public void addComposedOfIlluminance (IIlluminance parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IIlluminance> getComposedOfIlluminance (){
		Set<IIlluminance> ComposedOfIlluminance = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Illuminance) {
				ComposedOfIlluminance.add((Illuminance)action);
			}
		});
		return ComposedOfIlluminance;
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

	public static Set<IEast_illuminance_sensor> getAllEast_illuminance_sensorsObjectsCreated(){
		Set<IEast_illuminance_sensor> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#East_illuminance_sensor")).subjects().stream()
		.map(mapper->(IEast_illuminance_sensor)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}