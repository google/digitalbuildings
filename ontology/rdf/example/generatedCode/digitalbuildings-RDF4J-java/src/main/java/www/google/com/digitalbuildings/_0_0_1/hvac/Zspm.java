package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.Monitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_air_static_pressure_sensor;

/**
* Class Zspm 
* Zone static pressure monitoring.
*/
@SuppressWarnings("serial")
public class Zspm extends www.google.com.digitalbuildings._0_0_1.Monitoring implements IZspm{

	IRI newInstance;
	public Zspm(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Zspm"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesZone_air_static_pressure_sensor (IZone_air_static_pressure_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IZone_air_static_pressure_sensor> getUsesZone_air_static_pressure_sensor (){
		Set<IZone_air_static_pressure_sensor> UsesZone_air_static_pressure_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Zone_air_static_pressure_sensor) {
				UsesZone_air_static_pressure_sensor.add((Zone_air_static_pressure_sensor)action);
			}
		});
		return UsesZone_air_static_pressure_sensor;
	}

	public static Set<IZspm> getAllZspmsObjectsCreated(){
		Set<IZspm> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Zspm")).subjects().stream()
		.map(mapper->(IZspm)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}