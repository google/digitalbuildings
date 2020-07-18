package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.Monitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_air_temperature_sensor;

/**
* Class Etm 
* Basic exhaust temperature monitoring.
*/
@SuppressWarnings("serial")
public class Etm extends www.google.com.digitalbuildings._0_0_1.Monitoring implements IEtm{

	IRI newInstance;
	public Etm(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Etm"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesExhaust_air_temperature_sensor (IExhaust_air_temperature_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IExhaust_air_temperature_sensor> getUsesExhaust_air_temperature_sensor (){
		Set<IExhaust_air_temperature_sensor> UsesExhaust_air_temperature_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_air_temperature_sensor) {
				UsesExhaust_air_temperature_sensor.add((Exhaust_air_temperature_sensor)action);
			}
		});
		return UsesExhaust_air_temperature_sensor;
	}

	public static Set<IEtm> getAllEtmsObjectsCreated(){
		Set<IEtm> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Etm")).subjects().stream()
		.map(mapper->(IEtm)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}