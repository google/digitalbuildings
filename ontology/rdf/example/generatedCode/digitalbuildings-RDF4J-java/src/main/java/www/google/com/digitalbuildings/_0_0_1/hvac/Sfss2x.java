package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.Operational;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_run_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_run_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_run_status_2;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_run_status_2;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_run_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_run_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_run_status_1;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_run_status_1;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_power_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_power_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_power_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_power_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_current_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_current_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_flowrate_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_air_flowrate_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_current_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_current_sensor_2;

/**
* Class Sfss2x 
* Supply fan start-stop and feedback for two fans.
*/
@SuppressWarnings("serial")
public class Sfss2x extends www.google.com.digitalbuildings._0_0_1.Operational implements ISfss2x{

	IRI newInstance;
	public Sfss2x(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Sfss2x"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesSupply_fan_run_command_1 (ISupply_fan_run_command_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_fan_run_command_1> getUsesSupply_fan_run_command_1 (){
		Set<ISupply_fan_run_command_1> UsesSupply_fan_run_command_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_fan_run_command_1) {
				UsesSupply_fan_run_command_1.add((Supply_fan_run_command_1)action);
			}
		});
		return UsesSupply_fan_run_command_1;
	}


  public void addUsesSupply_fan_run_command_2 (ISupply_fan_run_command_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_fan_run_command_2> getUsesSupply_fan_run_command_2 (){
		Set<ISupply_fan_run_command_2> UsesSupply_fan_run_command_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_fan_run_command_2) {
				UsesSupply_fan_run_command_2.add((Supply_fan_run_command_2)action);
			}
		});
		return UsesSupply_fan_run_command_2;
	}


  public void addUsesSupply_fan_run_status_1 (ISupply_fan_run_status_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_fan_run_status_1> getUsesSupply_fan_run_status_1 (){
		Set<ISupply_fan_run_status_1> UsesSupply_fan_run_status_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_fan_run_status_1) {
				UsesSupply_fan_run_status_1.add((Supply_fan_run_status_1)action);
			}
		});
		return UsesSupply_fan_run_status_1;
	}


  public void addUsesSupply_fan_run_status_2 (ISupply_fan_run_status_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_fan_run_status_2> getUsesSupply_fan_run_status_2 (){
		Set<ISupply_fan_run_status_2> UsesSupply_fan_run_status_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_fan_run_status_2) {
				UsesSupply_fan_run_status_2.add((Supply_fan_run_status_2)action);
			}
		});
		return UsesSupply_fan_run_status_2;
	}


  public void addUsesOptionalsSupply_air_flowrate_capacity (ISupply_air_flowrate_capacity parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<ISupply_air_flowrate_capacity> getUsesOptionalsSupply_air_flowrate_capacity (){
		Set<ISupply_air_flowrate_capacity> UsesOptionalsSupply_air_flowrate_capacity = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_air_flowrate_capacity) {
				UsesOptionalsSupply_air_flowrate_capacity.add((Supply_air_flowrate_capacity)action);
			}
		});
		return UsesOptionalsSupply_air_flowrate_capacity;
	}


  public void addUsesOptionalsSupply_fan_current_sensor_1 (ISupply_fan_current_sensor_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<ISupply_fan_current_sensor_1> getUsesOptionalsSupply_fan_current_sensor_1 (){
		Set<ISupply_fan_current_sensor_1> UsesOptionalsSupply_fan_current_sensor_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_fan_current_sensor_1) {
				UsesOptionalsSupply_fan_current_sensor_1.add((Supply_fan_current_sensor_1)action);
			}
		});
		return UsesOptionalsSupply_fan_current_sensor_1;
	}


  public void addUsesOptionalsSupply_fan_current_sensor_2 (ISupply_fan_current_sensor_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<ISupply_fan_current_sensor_2> getUsesOptionalsSupply_fan_current_sensor_2 (){
		Set<ISupply_fan_current_sensor_2> UsesOptionalsSupply_fan_current_sensor_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_fan_current_sensor_2) {
				UsesOptionalsSupply_fan_current_sensor_2.add((Supply_fan_current_sensor_2)action);
			}
		});
		return UsesOptionalsSupply_fan_current_sensor_2;
	}


  public void addUsesOptionalsSupply_fan_power_capacity (ISupply_fan_power_capacity parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<ISupply_fan_power_capacity> getUsesOptionalsSupply_fan_power_capacity (){
		Set<ISupply_fan_power_capacity> UsesOptionalsSupply_fan_power_capacity = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_fan_power_capacity) {
				UsesOptionalsSupply_fan_power_capacity.add((Supply_fan_power_capacity)action);
			}
		});
		return UsesOptionalsSupply_fan_power_capacity;
	}


  public void addUsesOptionalsSupply_fan_power_sensor_1 (ISupply_fan_power_sensor_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<ISupply_fan_power_sensor_1> getUsesOptionalsSupply_fan_power_sensor_1 (){
		Set<ISupply_fan_power_sensor_1> UsesOptionalsSupply_fan_power_sensor_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_fan_power_sensor_1) {
				UsesOptionalsSupply_fan_power_sensor_1.add((Supply_fan_power_sensor_1)action);
			}
		});
		return UsesOptionalsSupply_fan_power_sensor_1;
	}


  public void addUsesOptionalsSupply_fan_power_sensor_2 (ISupply_fan_power_sensor_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<ISupply_fan_power_sensor_2> getUsesOptionalsSupply_fan_power_sensor_2 (){
		Set<ISupply_fan_power_sensor_2> UsesOptionalsSupply_fan_power_sensor_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_fan_power_sensor_2) {
				UsesOptionalsSupply_fan_power_sensor_2.add((Supply_fan_power_sensor_2)action);
			}
		});
		return UsesOptionalsSupply_fan_power_sensor_2;
	}

	public static Set<ISfss2x> getAllSfss2xsObjectsCreated(){
		Set<ISfss2x> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Sfss2x")).subjects().stream()
		.map(mapper->(ISfss2x)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}