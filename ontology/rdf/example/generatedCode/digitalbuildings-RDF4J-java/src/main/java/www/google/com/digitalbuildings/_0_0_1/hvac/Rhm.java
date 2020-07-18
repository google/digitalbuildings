package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.Monitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_air_relative_humidity_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Return_air_relative_humidity_sensor;

/**
* Class Rhm 
* Return air humidity monitoring.
*/
@SuppressWarnings("serial")
public class Rhm extends www.google.com.digitalbuildings._0_0_1.Monitoring implements IRhm{

	IRI newInstance;
	public Rhm(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Rhm"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesReturn_air_relative_humidity_sensor (IReturn_air_relative_humidity_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IReturn_air_relative_humidity_sensor> getUsesReturn_air_relative_humidity_sensor (){
		Set<IReturn_air_relative_humidity_sensor> UsesReturn_air_relative_humidity_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Return_air_relative_humidity_sensor) {
				UsesReturn_air_relative_humidity_sensor.add((Return_air_relative_humidity_sensor)action);
			}
		});
		return UsesReturn_air_relative_humidity_sensor;
	}

	public static Set<IRhm> getAllRhmsObjectsCreated(){
		Set<IRhm> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Rhm")).subjects().stream()
		.map(mapper->(IRhm)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}