package www.google.com.digitalbuildings._0_0_1.fields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.subfields.ISpecificenthalpy;
import www.google.com.digitalbuildings._0_0_1.subfields.Specificenthalpy;
import www.google.com.digitalbuildings._0_0_1.subfields.IAir;
import www.google.com.digitalbuildings._0_0_1.subfields.Air;
import www.google.com.digitalbuildings._0_0_1.subfields.IOutside;
import www.google.com.digitalbuildings._0_0_1.subfields.Outside;
import www.google.com.digitalbuildings._0_0_1.subfields.ISensor;
import www.google.com.digitalbuildings._0_0_1.subfields.Sensor;


@SuppressWarnings("serial")
public class Outside_air_specificenthalpy_sensor extends www.google.com.digitalbuildings._0_0_1.fields.Field implements IOutside_air_specificenthalpy_sensor{

	IRI newInstance;
	public Outside_air_specificenthalpy_sensor(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Outside_air_specificenthalpy_sensor"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addComposedOfAir (IAir parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IAir> getComposedOfAir (){
		Set<IAir> ComposedOfAir = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Air) {
				ComposedOfAir.add((Air)action);
			}
		});
		return ComposedOfAir;
	}


  public void addComposedOfOutside (IOutside parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IOutside> getComposedOfOutside (){
		Set<IOutside> ComposedOfOutside = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Outside) {
				ComposedOfOutside.add((Outside)action);
			}
		});
		return ComposedOfOutside;
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


  public void addComposedOfSpecificenthalpy (ISpecificenthalpy parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<ISpecificenthalpy> getComposedOfSpecificenthalpy (){
		Set<ISpecificenthalpy> ComposedOfSpecificenthalpy = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Specificenthalpy) {
				ComposedOfSpecificenthalpy.add((Specificenthalpy)action);
			}
		});
		return ComposedOfSpecificenthalpy;
	}

	public static Set<IOutside_air_specificenthalpy_sensor> getAllOutside_air_specificenthalpy_sensorsObjectsCreated(){
		Set<IOutside_air_specificenthalpy_sensor> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Outside_air_specificenthalpy_sensor")).subjects().stream()
		.map(mapper->(IOutside_air_specificenthalpy_sensor)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}