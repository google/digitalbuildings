package www.google.com.digitalbuildings._0_0_1.fields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.subfields.IDial;
import www.google.com.digitalbuildings._0_0_1.subfields.Dial;
import www.google.com.digitalbuildings._0_0_1.subfields.IResistance;
import www.google.com.digitalbuildings._0_0_1.subfields.Resistance;
import www.google.com.digitalbuildings._0_0_1.subfields.ISensor;
import www.google.com.digitalbuildings._0_0_1.subfields.Sensor;


@SuppressWarnings("serial")
public class Dial_resistance_sensor extends www.google.com.digitalbuildings._0_0_1.fields.Field implements IDial_resistance_sensor{

	IRI newInstance;
	public Dial_resistance_sensor(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Dial_resistance_sensor"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addComposedOfDial (IDial parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IDial> getComposedOfDial (){
		Set<IDial> ComposedOfDial = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Dial) {
				ComposedOfDial.add((Dial)action);
			}
		});
		return ComposedOfDial;
	}


  public void addComposedOfResistance (IResistance parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IResistance> getComposedOfResistance (){
		Set<IResistance> ComposedOfResistance = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Resistance) {
				ComposedOfResistance.add((Resistance)action);
			}
		});
		return ComposedOfResistance;
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

	public static Set<IDial_resistance_sensor> getAllDial_resistance_sensorsObjectsCreated(){
		Set<IDial_resistance_sensor> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Dial_resistance_sensor")).subjects().stream()
		.map(mapper->(IDial_resistance_sensor)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}