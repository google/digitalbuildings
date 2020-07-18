package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.fields.IWest_illuminance_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.West_illuminance_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IWest_wind_linearvelocity_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.West_wind_linearvelocity_sensor;

/**
* Class Sdc_ext_tlt_west 
* Directional shade (West).
*/
@SuppressWarnings("serial")
public class Sdc_ext_tlt_west extends www.google.com.digitalbuildings._0_0_1.hvac.Sdc_ext_tlt implements ISdc_ext_tlt_west{

	IRI newInstance;
	public Sdc_ext_tlt_west(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Sdc_ext_tlt_west"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesWest_illuminance_sensor (IWest_illuminance_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IWest_illuminance_sensor> getUsesWest_illuminance_sensor (){
		Set<IWest_illuminance_sensor> UsesWest_illuminance_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof West_illuminance_sensor) {
				UsesWest_illuminance_sensor.add((West_illuminance_sensor)action);
			}
		});
		return UsesWest_illuminance_sensor;
	}


  public void addUsesWest_wind_linearvelocity_sensor (IWest_wind_linearvelocity_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IWest_wind_linearvelocity_sensor> getUsesWest_wind_linearvelocity_sensor (){
		Set<IWest_wind_linearvelocity_sensor> UsesWest_wind_linearvelocity_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof West_wind_linearvelocity_sensor) {
				UsesWest_wind_linearvelocity_sensor.add((West_wind_linearvelocity_sensor)action);
			}
		});
		return UsesWest_wind_linearvelocity_sensor;
	}

	public static Set<ISdc_ext_tlt_west> getAllSdc_ext_tlt_westsObjectsCreated(){
		Set<ISdc_ext_tlt_west> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Sdc_ext_tlt_west")).subjects().stream()
		.map(mapper->(ISdc_ext_tlt_west)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}