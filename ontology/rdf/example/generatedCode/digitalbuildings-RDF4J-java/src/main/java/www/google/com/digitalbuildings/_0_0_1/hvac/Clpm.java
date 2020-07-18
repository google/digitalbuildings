package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.Monitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_cooling_thermal_power_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Process_cooling_thermal_power_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICooling_thermal_power_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Cooling_thermal_power_sensor;

/**
* Class Clpm 
* Cooling thermal monitoring.
*/
@SuppressWarnings("serial")
public class Clpm extends www.google.com.digitalbuildings._0_0_1.Monitoring implements IClpm{

	IRI newInstance;
	public Clpm(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Clpm"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesCooling_thermal_power_sensor (ICooling_thermal_power_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ICooling_thermal_power_sensor> getUsesCooling_thermal_power_sensor (){
		Set<ICooling_thermal_power_sensor> UsesCooling_thermal_power_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Cooling_thermal_power_sensor) {
				UsesCooling_thermal_power_sensor.add((Cooling_thermal_power_sensor)action);
			}
		});
		return UsesCooling_thermal_power_sensor;
	}


  public void addUsesProcess_cooling_thermal_power_sensor (IProcess_cooling_thermal_power_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IProcess_cooling_thermal_power_sensor> getUsesProcess_cooling_thermal_power_sensor (){
		Set<IProcess_cooling_thermal_power_sensor> UsesProcess_cooling_thermal_power_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Process_cooling_thermal_power_sensor) {
				UsesProcess_cooling_thermal_power_sensor.add((Process_cooling_thermal_power_sensor)action);
			}
		});
		return UsesProcess_cooling_thermal_power_sensor;
	}

	public static Set<IClpm> getAllClpmsObjectsCreated(){
		Set<IClpm> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Clpm")).subjects().stream()
		.map(mapper->(IClpm)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}