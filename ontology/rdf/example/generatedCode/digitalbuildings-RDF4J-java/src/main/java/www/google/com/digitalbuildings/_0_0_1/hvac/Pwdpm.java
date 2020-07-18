package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.Monitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_water_differential_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Process_water_differential_pressure_sensor;

/**
* Class Pwdpm 
* Differential pressure monitoring for process water.
*/
@SuppressWarnings("serial")
public class Pwdpm extends www.google.com.digitalbuildings._0_0_1.Monitoring implements IPwdpm{

	IRI newInstance;
	public Pwdpm(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Pwdpm"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesProcess_water_differential_pressure_sensor (IProcess_water_differential_pressure_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IProcess_water_differential_pressure_sensor> getUsesProcess_water_differential_pressure_sensor (){
		Set<IProcess_water_differential_pressure_sensor> UsesProcess_water_differential_pressure_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Process_water_differential_pressure_sensor) {
				UsesProcess_water_differential_pressure_sensor.add((Process_water_differential_pressure_sensor)action);
			}
		});
		return UsesProcess_water_differential_pressure_sensor;
	}

	public static Set<IPwdpm> getAllPwdpmsObjectsCreated(){
		Set<IPwdpm> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Pwdpm")).subjects().stream()
		.map(mapper->(IPwdpm)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}