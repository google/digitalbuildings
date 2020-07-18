package www.google.com.digitalbuildings._0_0_1.fields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.subfields.IDifferential;
import www.google.com.digitalbuildings._0_0_1.subfields.Differential;
import www.google.com.digitalbuildings._0_0_1.subfields.IFilter;
import www.google.com.digitalbuildings._0_0_1.subfields.Filter;
import www.google.com.digitalbuildings._0_0_1.subfields.IPressure;
import www.google.com.digitalbuildings._0_0_1.subfields.Pressure;
import www.google.com.digitalbuildings._0_0_1.subfields.ISensor;
import www.google.com.digitalbuildings._0_0_1.subfields.Sensor;


@SuppressWarnings("serial")
public class Filter_differential_pressure_sensor_4 extends www.google.com.digitalbuildings._0_0_1.fields.Field implements IFilter_differential_pressure_sensor_4{

	IRI newInstance;
	public Filter_differential_pressure_sensor_4(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Filter_differential_pressure_sensor_4"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addComposedOfDifferential (IDifferential parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IDifferential> getComposedOfDifferential (){
		Set<IDifferential> ComposedOfDifferential = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Differential) {
				ComposedOfDifferential.add((Differential)action);
			}
		});
		return ComposedOfDifferential;
	}


  public void addComposedOfFilter (IFilter parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IFilter> getComposedOfFilter (){
		Set<IFilter> ComposedOfFilter = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Filter) {
				ComposedOfFilter.add((Filter)action);
			}
		});
		return ComposedOfFilter;
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

	public static Set<IFilter_differential_pressure_sensor_4> getAllFilter_differential_pressure_sensor_4sObjectsCreated(){
		Set<IFilter_differential_pressure_sensor_4> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#Filter_differential_pressure_sensor_4")).subjects().stream()
		.map(mapper->(IFilter_differential_pressure_sensor_4)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}