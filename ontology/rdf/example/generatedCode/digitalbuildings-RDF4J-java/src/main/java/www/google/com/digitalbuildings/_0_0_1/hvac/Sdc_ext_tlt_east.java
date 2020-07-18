package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.fields.IEast_illuminance_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.East_illuminance_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IEast_wind_linearvelocity_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.East_wind_linearvelocity_sensor;

/**
* Class Sdc_ext_tlt_east 
* Directional shade (East).
*/
@SuppressWarnings("serial")
public class Sdc_ext_tlt_east extends www.google.com.digitalbuildings._0_0_1.hvac.Sdc_ext_tlt implements ISdc_ext_tlt_east{

	IRI newInstance;
	public Sdc_ext_tlt_east(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Sdc_ext_tlt_east"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesEast_illuminance_sensor (IEast_illuminance_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IEast_illuminance_sensor> getUsesEast_illuminance_sensor (){
		Set<IEast_illuminance_sensor> UsesEast_illuminance_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof East_illuminance_sensor) {
				UsesEast_illuminance_sensor.add((East_illuminance_sensor)action);
			}
		});
		return UsesEast_illuminance_sensor;
	}


  public void addUsesEast_wind_linearvelocity_sensor (IEast_wind_linearvelocity_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IEast_wind_linearvelocity_sensor> getUsesEast_wind_linearvelocity_sensor (){
		Set<IEast_wind_linearvelocity_sensor> UsesEast_wind_linearvelocity_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof East_wind_linearvelocity_sensor) {
				UsesEast_wind_linearvelocity_sensor.add((East_wind_linearvelocity_sensor)action);
			}
		});
		return UsesEast_wind_linearvelocity_sensor;
	}

	public static Set<ISdc_ext_tlt_east> getAllSdc_ext_tlt_eastsObjectsCreated(){
		Set<ISdc_ext_tlt_east> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Sdc_ext_tlt_east")).subjects().stream()
		.map(mapper->(ISdc_ext_tlt_east)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}