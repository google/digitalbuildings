package www.google.com.digitalbuildings._0_0_1.fields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.subfields.ISouthwest;
import www.google.com.digitalbuildings._0_0_1.subfields.Southwest;
import www.google.com.digitalbuildings._0_0_1.subfields.IIlluminance;
import www.google.com.digitalbuildings._0_0_1.subfields.Illuminance;
import www.google.com.digitalbuildings._0_0_1.subfields.ISensor;
import www.google.com.digitalbuildings._0_0_1.subfields.Sensor;


@SuppressWarnings("serial")
public class Southwest_illuminance_sensor extends www.google.com.digitalbuildings._0_0_1.fields.Field implements ISouthwest_illuminance_sensor{

	IRI newInstance;
	public Southwest_illuminance_sensor(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Southwest_illuminance_sensor"));
	}

	public IRI iri()
	{
		return newInstance;
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


  public void addComposedOfSouthwest (ISouthwest parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<ISouthwest> getComposedOfSouthwest (){
		Set<ISouthwest> ComposedOfSouthwest = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Southwest) {
				ComposedOfSouthwest.add((Southwest)action);
			}
		});
		return ComposedOfSouthwest;
	}

	public static Set<ISouthwest_illuminance_sensor> getAllSouthwest_illuminance_sensorsObjectsCreated(){
		Set<ISouthwest_illuminance_sensor> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Southwest_illuminance_sensor")).subjects().stream()
		.map(mapper->(ISouthwest_illuminance_sensor)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}