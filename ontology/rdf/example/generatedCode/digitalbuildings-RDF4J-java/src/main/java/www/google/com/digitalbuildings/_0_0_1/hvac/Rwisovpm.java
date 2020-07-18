package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.Monitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IHeater_run_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.Heater_run_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_isolation_valve_status;
import www.google.com.digitalbuildings._0_0_1.fields.Return_water_isolation_valve_status;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_isolation_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Return_water_isolation_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IRun_command;
import www.google.com.digitalbuildings._0_0_1.fields.Run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_isolation_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Return_water_isolation_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_water_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IRun_status;
import www.google.com.digitalbuildings._0_0_1.fields.Run_status;
import www.google.com.digitalbuildings._0_0_1.fields.IHeater_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.Heater_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IHeater_run_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.Heater_run_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_isolation_valve_command;
import www.google.com.digitalbuildings._0_0_1.fields.Return_water_isolation_valve_command;

/**
* Class Rwisovpm 
* Return side isolation valve monitoring.
*/
@SuppressWarnings("serial")
public class Rwisovpm extends www.google.com.digitalbuildings._0_0_1.Monitoring implements IRwisovpm{

	IRI newInstance;
	public Rwisovpm(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Rwisovpm"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesReturn_water_isolation_valve_percentage_command (IReturn_water_isolation_valve_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IReturn_water_isolation_valve_percentage_command> getUsesReturn_water_isolation_valve_percentage_command (){
		Set<IReturn_water_isolation_valve_percentage_command> UsesReturn_water_isolation_valve_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Return_water_isolation_valve_percentage_command) {
				UsesReturn_water_isolation_valve_percentage_command.add((Return_water_isolation_valve_percentage_command)action);
			}
		});
		return UsesReturn_water_isolation_valve_percentage_command;
	}


  public void addUsesReturn_water_isolation_valve_percentage_sensor (IReturn_water_isolation_valve_percentage_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IReturn_water_isolation_valve_percentage_sensor> getUsesReturn_water_isolation_valve_percentage_sensor (){
		Set<IReturn_water_isolation_valve_percentage_sensor> UsesReturn_water_isolation_valve_percentage_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Return_water_isolation_valve_percentage_sensor) {
				UsesReturn_water_isolation_valve_percentage_sensor.add((Return_water_isolation_valve_percentage_sensor)action);
			}
		});
		return UsesReturn_water_isolation_valve_percentage_sensor;
	}


  public void addUsesHeater_run_command (IHeater_run_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IHeater_run_command> getUsesHeater_run_command (){
		Set<IHeater_run_command> UsesHeater_run_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Heater_run_command) {
				UsesHeater_run_command.add((Heater_run_command)action);
			}
		});
		return UsesHeater_run_command;
	}


  public void addUsesSupply_water_temperature_sensor (ISupply_water_temperature_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_water_temperature_sensor> getUsesSupply_water_temperature_sensor (){
		Set<ISupply_water_temperature_sensor> UsesSupply_water_temperature_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_water_temperature_sensor) {
				UsesSupply_water_temperature_sensor.add((Supply_water_temperature_sensor)action);
			}
		});
		return UsesSupply_water_temperature_sensor;
	}


  public void addUsesSupply_water_temperature_setpoint (ISupply_water_temperature_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_water_temperature_setpoint> getUsesSupply_water_temperature_setpoint (){
		Set<ISupply_water_temperature_setpoint> UsesSupply_water_temperature_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_water_temperature_setpoint) {
				UsesSupply_water_temperature_setpoint.add((Supply_water_temperature_setpoint)action);
			}
		});
		return UsesSupply_water_temperature_setpoint;
	}


  public void addUsesRun_command (IRun_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IRun_command> getUsesRun_command (){
		Set<IRun_command> UsesRun_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Run_command) {
				UsesRun_command.add((Run_command)action);
			}
		});
		return UsesRun_command;
	}


  public void addUsesRun_status (IRun_status parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IRun_status> getUsesRun_status (){
		Set<IRun_status> UsesRun_status = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Run_status) {
				UsesRun_status.add((Run_status)action);
			}
		});
		return UsesRun_status;
	}


  public void addUsesHeater_run_command_1 (IHeater_run_command_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IHeater_run_command_1> getUsesHeater_run_command_1 (){
		Set<IHeater_run_command_1> UsesHeater_run_command_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Heater_run_command_1) {
				UsesHeater_run_command_1.add((Heater_run_command_1)action);
			}
		});
		return UsesHeater_run_command_1;
	}


  public void addUsesHeater_run_command_2 (IHeater_run_command_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IHeater_run_command_2> getUsesHeater_run_command_2 (){
		Set<IHeater_run_command_2> UsesHeater_run_command_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Heater_run_command_2) {
				UsesHeater_run_command_2.add((Heater_run_command_2)action);
			}
		});
		return UsesHeater_run_command_2;
	}


  public void addUsesReturn_water_isolation_valve_command (IReturn_water_isolation_valve_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IReturn_water_isolation_valve_command> getUsesReturn_water_isolation_valve_command (){
		Set<IReturn_water_isolation_valve_command> UsesReturn_water_isolation_valve_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Return_water_isolation_valve_command) {
				UsesReturn_water_isolation_valve_command.add((Return_water_isolation_valve_command)action);
			}
		});
		return UsesReturn_water_isolation_valve_command;
	}


  public void addUsesReturn_water_isolation_valve_status (IReturn_water_isolation_valve_status parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IReturn_water_isolation_valve_status> getUsesReturn_water_isolation_valve_status (){
		Set<IReturn_water_isolation_valve_status> UsesReturn_water_isolation_valve_status = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Return_water_isolation_valve_status) {
				UsesReturn_water_isolation_valve_status.add((Return_water_isolation_valve_status)action);
			}
		});
		return UsesReturn_water_isolation_valve_status;
	}

	public static Set<IRwisovpm> getAllRwisovpmsObjectsCreated(){
		Set<IRwisovpm> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Rwisovpm")).subjects().stream()
		.map(mapper->(IRwisovpm)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}