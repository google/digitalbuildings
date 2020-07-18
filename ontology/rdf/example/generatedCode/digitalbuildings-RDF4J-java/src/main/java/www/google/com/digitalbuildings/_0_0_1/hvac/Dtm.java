package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.Monitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_air_temperature_sensor;

/**
* Class Dtm 
* Discharge temperature monitoring.
*/
@SuppressWarnings("serial")
public class Dtm extends www.google.com.digitalbuildings._0_0_1.Monitoring implements IDtm{

	IRI newInstance;
	public Dtm(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Dtm"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesDischarge_air_temperature_sensor (IDischarge_air_temperature_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IDischarge_air_temperature_sensor> getUsesDischarge_air_temperature_sensor (){
		Set<IDischarge_air_temperature_sensor> UsesDischarge_air_temperature_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Discharge_air_temperature_sensor) {
				UsesDischarge_air_temperature_sensor.add((Discharge_air_temperature_sensor)action);
			}
		});
		return UsesDischarge_air_temperature_sensor;
	}

	public static Set<IDtm> getAllDtmsObjectsCreated(){
		Set<IDtm> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Dtm")).subjects().stream()
		.map(mapper->(IDtm)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}