package www.google.com.digitalbuildings._0_0_1.fields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.subfields.ISoutheast;
import www.google.com.digitalbuildings._0_0_1.subfields.Southeast;
import www.google.com.digitalbuildings._0_0_1.subfields.IIlluminance;
import www.google.com.digitalbuildings._0_0_1.subfields.Illuminance;
import www.google.com.digitalbuildings._0_0_1.subfields.ISensor;
import www.google.com.digitalbuildings._0_0_1.subfields.Sensor;


@SuppressWarnings("serial")
public class Southeast_illuminance_sensor extends www.google.com.digitalbuildings._0_0_1.fields.Field implements ISoutheast_illuminance_sensor{

	IRI newInstance;
	public Southeast_illuminance_sensor(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Southeast_illuminance_sensor"));
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


  public void addComposedOfSoutheast (ISoutheast parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<ISoutheast> getComposedOfSoutheast (){
		Set<ISoutheast> ComposedOfSoutheast = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Southeast) {
				ComposedOfSoutheast.add((Southeast)action);
			}
		});
		return ComposedOfSoutheast;
	}

	public static Set<ISoutheast_illuminance_sensor> getAllSoutheast_illuminance_sensorsObjectsCreated(){
		Set<ISoutheast_illuminance_sensor> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Southeast_illuminance_sensor")).subjects().stream()
		.map(mapper->(ISoutheast_illuminance_sensor)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}