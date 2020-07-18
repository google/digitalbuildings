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
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_supply_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Process_supply_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_return_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Process_return_water_temperature_sensor;

/**
* Class Prwdt 
* Temperature differential across process water.
*/
@SuppressWarnings("serial")
public class Prwdt extends www.google.com.digitalbuildings._0_0_1.Monitoring implements IPrwdt{

	IRI newInstance;
	public Prwdt(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Prwdt"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesOptionalsProcess_cooling_thermal_power_sensor (IProcess_cooling_thermal_power_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IProcess_cooling_thermal_power_sensor> getUsesOptionalsProcess_cooling_thermal_power_sensor (){
		Set<IProcess_cooling_thermal_power_sensor> UsesOptionalsProcess_cooling_thermal_power_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Process_cooling_thermal_power_sensor) {
				UsesOptionalsProcess_cooling_thermal_power_sensor.add((Process_cooling_thermal_power_sensor)action);
			}
		});
		return UsesOptionalsProcess_cooling_thermal_power_sensor;
	}


  public void addUsesProcess_return_water_temperature_sensor (IProcess_return_water_temperature_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IProcess_return_water_temperature_sensor> getUsesProcess_return_water_temperature_sensor (){
		Set<IProcess_return_water_temperature_sensor> UsesProcess_return_water_temperature_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Process_return_water_temperature_sensor) {
				UsesProcess_return_water_temperature_sensor.add((Process_return_water_temperature_sensor)action);
			}
		});
		return UsesProcess_return_water_temperature_sensor;
	}


  public void addUsesProcess_supply_water_temperature_sensor (IProcess_supply_water_temperature_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IProcess_supply_water_temperature_sensor> getUsesProcess_supply_water_temperature_sensor (){
		Set<IProcess_supply_water_temperature_sensor> UsesProcess_supply_water_temperature_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Process_supply_water_temperature_sensor) {
				UsesProcess_supply_water_temperature_sensor.add((Process_supply_water_temperature_sensor)action);
			}
		});
		return UsesProcess_supply_water_temperature_sensor;
	}

	public static Set<IPrwdt> getAllPrwdtsObjectsCreated(){
		Set<IPrwdt> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Prwdt")).subjects().stream()
		.map(mapper->(IPrwdt)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}