package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.Monitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_cooling_thermal_power_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.Process_cooling_thermal_power_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_cooling_thermal_power_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.Process_cooling_thermal_power_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_supply_water_temperature_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.Process_supply_water_temperature_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_supply_water_temperature_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.Process_supply_water_temperature_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_return_water_temperature_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.Process_return_water_temperature_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_return_water_temperature_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.Process_return_water_temperature_sensor_2;

/**
* Class Prwdt2x 
* Temperature differential across 2 process water headers.
*/
@SuppressWarnings("serial")
public class Prwdt2x extends www.google.com.digitalbuildings._0_0_1.Monitoring implements IPrwdt2x{

	IRI newInstance;
	public Prwdt2x(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Prwdt2x"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesOptionalsProcess_cooling_thermal_power_sensor_1 (IProcess_cooling_thermal_power_sensor_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IProcess_cooling_thermal_power_sensor_1> getUsesOptionalsProcess_cooling_thermal_power_sensor_1 (){
		Set<IProcess_cooling_thermal_power_sensor_1> UsesOptionalsProcess_cooling_thermal_power_sensor_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Process_cooling_thermal_power_sensor_1) {
				UsesOptionalsProcess_cooling_thermal_power_sensor_1.add((Process_cooling_thermal_power_sensor_1)action);
			}
		});
		return UsesOptionalsProcess_cooling_thermal_power_sensor_1;
	}


  public void addUsesOptionalsProcess_cooling_thermal_power_sensor_2 (IProcess_cooling_thermal_power_sensor_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IProcess_cooling_thermal_power_sensor_2> getUsesOptionalsProcess_cooling_thermal_power_sensor_2 (){
		Set<IProcess_cooling_thermal_power_sensor_2> UsesOptionalsProcess_cooling_thermal_power_sensor_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Process_cooling_thermal_power_sensor_2) {
				UsesOptionalsProcess_cooling_thermal_power_sensor_2.add((Process_cooling_thermal_power_sensor_2)action);
			}
		});
		return UsesOptionalsProcess_cooling_thermal_power_sensor_2;
	}


  public void addUsesProcess_return_water_temperature_sensor_1 (IProcess_return_water_temperature_sensor_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IProcess_return_water_temperature_sensor_1> getUsesProcess_return_water_temperature_sensor_1 (){
		Set<IProcess_return_water_temperature_sensor_1> UsesProcess_return_water_temperature_sensor_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Process_return_water_temperature_sensor_1) {
				UsesProcess_return_water_temperature_sensor_1.add((Process_return_water_temperature_sensor_1)action);
			}
		});
		return UsesProcess_return_water_temperature_sensor_1;
	}


  public void addUsesProcess_return_water_temperature_sensor_2 (IProcess_return_water_temperature_sensor_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IProcess_return_water_temperature_sensor_2> getUsesProcess_return_water_temperature_sensor_2 (){
		Set<IProcess_return_water_temperature_sensor_2> UsesProcess_return_water_temperature_sensor_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Process_return_water_temperature_sensor_2) {
				UsesProcess_return_water_temperature_sensor_2.add((Process_return_water_temperature_sensor_2)action);
			}
		});
		return UsesProcess_return_water_temperature_sensor_2;
	}


  public void addUsesProcess_supply_water_temperature_sensor_1 (IProcess_supply_water_temperature_sensor_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IProcess_supply_water_temperature_sensor_1> getUsesProcess_supply_water_temperature_sensor_1 (){
		Set<IProcess_supply_water_temperature_sensor_1> UsesProcess_supply_water_temperature_sensor_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Process_supply_water_temperature_sensor_1) {
				UsesProcess_supply_water_temperature_sensor_1.add((Process_supply_water_temperature_sensor_1)action);
			}
		});
		return UsesProcess_supply_water_temperature_sensor_1;
	}


  public void addUsesProcess_supply_water_temperature_sensor_2 (IProcess_supply_water_temperature_sensor_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IProcess_supply_water_temperature_sensor_2> getUsesProcess_supply_water_temperature_sensor_2 (){
		Set<IProcess_supply_water_temperature_sensor_2> UsesProcess_supply_water_temperature_sensor_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Process_supply_water_temperature_sensor_2) {
				UsesProcess_supply_water_temperature_sensor_2.add((Process_supply_water_temperature_sensor_2)action);
			}
		});
		return UsesProcess_supply_water_temperature_sensor_2;
	}

	public static Set<IPrwdt2x> getAllPrwdt2xsObjectsCreated(){
		Set<IPrwdt2x> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Prwdt2x")).subjects().stream()
		.map(mapper->(IPrwdt2x)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}