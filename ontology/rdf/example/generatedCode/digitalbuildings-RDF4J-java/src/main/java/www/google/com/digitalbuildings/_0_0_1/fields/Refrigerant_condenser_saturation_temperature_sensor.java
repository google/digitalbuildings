package www.google.com.digitalbuildings._0_0_1.fields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.subfields.ITemperature;
import www.google.com.digitalbuildings._0_0_1.subfields.Temperature;
import www.google.com.digitalbuildings._0_0_1.subfields.ICondenser;
import www.google.com.digitalbuildings._0_0_1.subfields.Condenser;
import www.google.com.digitalbuildings._0_0_1.subfields.IRefrigerant;
import www.google.com.digitalbuildings._0_0_1.subfields.Refrigerant;
import www.google.com.digitalbuildings._0_0_1.subfields.ISaturation;
import www.google.com.digitalbuildings._0_0_1.subfields.Saturation;
import www.google.com.digitalbuildings._0_0_1.subfields.ISensor;
import www.google.com.digitalbuildings._0_0_1.subfields.Sensor;


@SuppressWarnings("serial")
public class Refrigerant_condenser_saturation_temperature_sensor extends www.google.com.digitalbuildings._0_0_1.fields.Field implements IRefrigerant_condenser_saturation_temperature_sensor{

	IRI newInstance;
	public Refrigerant_condenser_saturation_temperature_sensor(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Refrigerant_condenser_saturation_temperature_sensor"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addComposedOfCondenser (ICondenser parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<ICondenser> getComposedOfCondenser (){
		Set<ICondenser> ComposedOfCondenser = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Condenser) {
				ComposedOfCondenser.add((Condenser)action);
			}
		});
		return ComposedOfCondenser;
	}


  public void addComposedOfRefrigerant (IRefrigerant parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IRefrigerant> getComposedOfRefrigerant (){
		Set<IRefrigerant> ComposedOfRefrigerant = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Refrigerant) {
				ComposedOfRefrigerant.add((Refrigerant)action);
			}
		});
		return ComposedOfRefrigerant;
	}


  public void addComposedOfSaturation (ISaturation parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<ISaturation> getComposedOfSaturation (){
		Set<ISaturation> ComposedOfSaturation = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Saturation) {
				ComposedOfSaturation.add((Saturation)action);
			}
		});
		return ComposedOfSaturation;
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


  public void addComposedOfTemperature (ITemperature parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<ITemperature> getComposedOfTemperature (){
		Set<ITemperature> ComposedOfTemperature = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Temperature) {
				ComposedOfTemperature.add((Temperature)action);
			}
		});
		return ComposedOfTemperature;
	}

	public static Set<IRefrigerant_condenser_saturation_temperature_sensor> getAllRefrigerant_condenser_saturation_temperature_sensorsObjectsCreated(){
		Set<IRefrigerant_condenser_saturation_temperature_sensor> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Refrigerant_condenser_saturation_temperature_sensor")).subjects().stream()
		.map(mapper->(IRefrigerant_condenser_saturation_temperature_sensor)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}