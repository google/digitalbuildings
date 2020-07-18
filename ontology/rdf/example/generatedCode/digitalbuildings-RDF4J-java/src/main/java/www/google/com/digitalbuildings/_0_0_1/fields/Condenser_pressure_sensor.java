package www.google.com.digitalbuildings._0_0_1.fields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.subfields.ICondenser;
import www.google.com.digitalbuildings._0_0_1.subfields.Condenser;
import www.google.com.digitalbuildings._0_0_1.subfields.IPressure;
import www.google.com.digitalbuildings._0_0_1.subfields.Pressure;
import www.google.com.digitalbuildings._0_0_1.subfields.ISensor;
import www.google.com.digitalbuildings._0_0_1.subfields.Sensor;


@SuppressWarnings("serial")
public class Condenser_pressure_sensor extends www.google.com.digitalbuildings._0_0_1.fields.Field implements ICondenser_pressure_sensor{

	IRI newInstance;
	public Condenser_pressure_sensor(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Condenser_pressure_sensor"));
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


  public void addComposedOfPressure (IPressure parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IPressure> getComposedOfPressure (){
		Set<IPressure> ComposedOfPressure = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Pressure) {
				ComposedOfPressure.add((Pressure)action);
			}
		});
		return ComposedOfPressure;
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

	public static Set<ICondenser_pressure_sensor> getAllCondenser_pressure_sensorsObjectsCreated(){
		Set<ICondenser_pressure_sensor> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Condenser_pressure_sensor")).subjects().stream()
		.map(mapper->(ICondenser_pressure_sensor)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}