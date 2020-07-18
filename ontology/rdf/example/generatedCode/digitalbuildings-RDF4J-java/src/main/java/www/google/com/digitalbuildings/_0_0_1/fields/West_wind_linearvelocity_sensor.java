package www.google.com.digitalbuildings._0_0_1.fields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.subfields.IWind;
import www.google.com.digitalbuildings._0_0_1.subfields.Wind;
import www.google.com.digitalbuildings._0_0_1.subfields.IWest;
import www.google.com.digitalbuildings._0_0_1.subfields.West;
import www.google.com.digitalbuildings._0_0_1.subfields.ILinearvelocity;
import www.google.com.digitalbuildings._0_0_1.subfields.Linearvelocity;
import www.google.com.digitalbuildings._0_0_1.subfields.ISensor;
import www.google.com.digitalbuildings._0_0_1.subfields.Sensor;


@SuppressWarnings("serial")
public class West_wind_linearvelocity_sensor extends www.google.com.digitalbuildings._0_0_1.fields.Field implements IWest_wind_linearvelocity_sensor{

	IRI newInstance;
	public West_wind_linearvelocity_sensor(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#West_wind_linearvelocity_sensor"));
	}

	public IRI iri()
	{
		return newInstance;
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


  public void addComposedOfWest (IWest parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), parameter);
	}

	public Set<IWest> getComposedOfWest (){
		Set<IWest> ComposedOfWest = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#isComposedOf"), null)
		.objects().forEach(action->{
			if(action instanceof West) {
				ComposedOfWest.add((West)action);
			}
		});
		return ComposedOfWest;
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

	public static Set<IWest_wind_linearvelocity_sensor> getAllWest_wind_linearvelocity_sensorsObjectsCreated(){
		Set<IWest_wind_linearvelocity_sensor> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/fields#West_wind_linearvelocity_sensor")).subjects().stream()
		.map(mapper->(IWest_wind_linearvelocity_sensor)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}