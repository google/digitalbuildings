package www.google.com.digitalbuildings._0_0_1.fields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.subfields.IChilled;
import www.google.com.digitalbuildings._0_0_1.subfields.Chilled;
import www.google.com.digitalbuildings._0_0_1.subfields.IWater;
import www.google.com.digitalbuildings._0_0_1.subfields.Water;
import www.google.com.digitalbuildings._0_0_1.subfields.ITemperature;
import www.google.com.digitalbuildings._0_0_1.subfields.Temperature;
import www.google.com.digitalbuildings._0_0_1.subfields.IReturn;
import www.google.com.digitalbuildings._0_0_1.subfields.Return;
import www.google.com.digitalbuildings._0_0_1.subfields.ISensor;
import www.google.com.digitalbuildings._0_0_1.subfields.Sensor;


@SuppressWarnings("serial")
public class Chilled_return_water_temperature_sensor extends www.google.com.digitalbuildings._0_0_1.fields.Field implements IChilled_return_water_temperature_sensor{

	IRI newInstance;
	public Chilled_return_water_temperature_sensor(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Chilled_return_water_temperature_sensor"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addComposedOfChilled (IChilled parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IChilled> getComposedOfChilled (){
		Set<IChilled> ComposedOfChilled = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Chilled) {
				ComposedOfChilled.add((Chilled)action);
			}
		});
		return ComposedOfChilled;
	}


  public void addComposedOfReturn (IReturn parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IReturn> getComposedOfReturn (){
		Set<IReturn> ComposedOfReturn = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Return) {
				ComposedOfReturn.add((Return)action);
			}
		});
		return ComposedOfReturn;
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


  public void addComposedOfWater (IWater parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IWater> getComposedOfWater (){
		Set<IWater> ComposedOfWater = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Water) {
				ComposedOfWater.add((Water)action);
			}
		});
		return ComposedOfWater;
	}

	public static Set<IChilled_return_water_temperature_sensor> getAllChilled_return_water_temperature_sensorsObjectsCreated(){
		Set<IChilled_return_water_temperature_sensor> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Chilled_return_water_temperature_sensor")).subjects().stream()
		.map(mapper->(IChilled_return_water_temperature_sensor)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}