package www.google.com.digitalbuildings._0_0_1.fields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.subfields.IWind;
import www.google.com.digitalbuildings._0_0_1.subfields.Wind;
import www.google.com.digitalbuildings._0_0_1.subfields.ILinearvelocity;
import www.google.com.digitalbuildings._0_0_1.subfields.Linearvelocity;
import www.google.com.digitalbuildings._0_0_1.subfields.IEast;
import www.google.com.digitalbuildings._0_0_1.subfields.East;
import www.google.com.digitalbuildings._0_0_1.subfields.ISensor;
import www.google.com.digitalbuildings._0_0_1.subfields.Sensor;


@SuppressWarnings("serial")
public class East_wind_linearvelocity_sensor extends www.google.com.digitalbuildings._0_0_1.fields.Field implements IEast_wind_linearvelocity_sensor{

	IRI newInstance;
	public East_wind_linearvelocity_sensor(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#East_wind_linearvelocity_sensor"));
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


  public void addComposedOfLinearvelocity (ILinearvelocity parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<ILinearvelocity> getComposedOfLinearvelocity (){
		Set<ILinearvelocity> ComposedOfLinearvelocity = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Linearvelocity) {
				ComposedOfLinearvelocity.add((Linearvelocity)action);
			}
		});
		return ComposedOfLinearvelocity;
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


  public void addComposedOfWind (IWind parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IWind> getComposedOfWind (){
		Set<IWind> ComposedOfWind = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof Wind) {
				ComposedOfWind.add((Wind)action);
			}
		});
		return ComposedOfWind;
	}

	public static Set<IEast_wind_linearvelocity_sensor> getAllEast_wind_linearvelocity_sensorsObjectsCreated(){
		Set<IEast_wind_linearvelocity_sensor> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#East_wind_linearvelocity_sensor")).subjects().stream()
		.map(mapper->(IEast_wind_linearvelocity_sensor)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}