package www.google.com.digitalbuildings._0_0_1.fields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.subfields.IPower;
import www.google.com.digitalbuildings._0_0_1.subfields.Power;
import www.google.com.digitalbuildings._0_0_1.subfields.ISensor;
import www.google.com.digitalbuildings._0_0_1.subfields.Sensor;
import www.google.com.digitalbuildings._0_0_1.subfields.IThermal;
import www.google.com.digitalbuildings._0_0_1.subfields.Thermal;


@SuppressWarnings("serial")
public class Thermal_power_sensor extends www.google.com.digitalbuildings._0_0_1.fields.Field implements IThermal_power_sensor{

	IRI newInstance;
	public Thermal_power_sensor(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Thermal_power_sensor"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addComposedOfPower (IPower parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IPower> getComposedOfPower (){
		Set<IPower> ComposedOfPower = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Power) {
				ComposedOfPower.add((Power)action);
			}
		});
		return ComposedOfPower;
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


  public void addComposedOfThermal (IThermal parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IThermal> getComposedOfThermal (){
		Set<IThermal> ComposedOfThermal = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Thermal) {
				ComposedOfThermal.add((Thermal)action);
			}
		});
		return ComposedOfThermal;
	}

	public static Set<IThermal_power_sensor> getAllThermal_power_sensorsObjectsCreated(){
		Set<IThermal_power_sensor> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Thermal_power_sensor")).subjects().stream()
		.map(mapper->(IThermal_power_sensor)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}