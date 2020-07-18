package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.Operational;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_cooling_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_air_cooling_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_co2_concentration_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_air_co2_concentration_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_co2_concentration_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_air_co2_concentration_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.Compressor_run_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_status_2;
import www.google.com.digitalbuildings._0_0_1.fields.Compressor_run_status_2;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_status_1;
import www.google.com.digitalbuildings._0_0_1.fields.Compressor_run_status_1;
import www.google.com.digitalbuildings._0_0_1.fields.IBoost_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.Boost_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.Compressor_run_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IHeater_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.Heater_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IBoost_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.Boost_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_heating_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_air_heating_temperature_setpoint;

/**
* Class Co2c 
* Carbon dioxide control.
*/
@SuppressWarnings("serial")
public class Co2c extends www.google.com.digitalbuildings._0_0_1.Operational implements ICo2c{

	IRI newInstance;
	public Co2c(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Co2c"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesZone_air_co2_concentration_sensor (IZone_air_co2_concentration_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IZone_air_co2_concentration_sensor> getUsesZone_air_co2_concentration_sensor (){
		Set<IZone_air_co2_concentration_sensor> UsesZone_air_co2_concentration_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Zone_air_co2_concentration_sensor) {
				UsesZone_air_co2_concentration_sensor.add((Zone_air_co2_concentration_sensor)action);
			}
		});
		return UsesZone_air_co2_concentration_sensor;
	}


  public void addUsesZone_air_co2_concentration_setpoint (IZone_air_co2_concentration_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IZone_air_co2_concentration_setpoint> getUsesZone_air_co2_concentration_setpoint (){
		Set<IZone_air_co2_concentration_setpoint> UsesZone_air_co2_concentration_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Zone_air_co2_concentration_setpoint) {
				UsesZone_air_co2_concentration_setpoint.add((Zone_air_co2_concentration_setpoint)action);
			}
		});
		return UsesZone_air_co2_concentration_setpoint;
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


  public void addUsesZone_air_heating_temperature_setpoint (IZone_air_heating_temperature_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IZone_air_heating_temperature_setpoint> getUsesZone_air_heating_temperature_setpoint (){
		Set<IZone_air_heating_temperature_setpoint> UsesZone_air_heating_temperature_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Zone_air_heating_temperature_setpoint) {
				UsesZone_air_heating_temperature_setpoint.add((Zone_air_heating_temperature_setpoint)action);
			}
		});
		return UsesZone_air_heating_temperature_setpoint;
	}


  public void addUsesZone_air_temperature_sensor (IZone_air_temperature_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IZone_air_temperature_sensor> getUsesZone_air_temperature_sensor (){
		Set<IZone_air_temperature_sensor> UsesZone_air_temperature_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Zone_air_temperature_sensor) {
				UsesZone_air_temperature_sensor.add((Zone_air_temperature_sensor)action);
			}
		});
		return UsesZone_air_temperature_sensor;
	}


  public void addUsesDischarge_fan_run_command (IDischarge_fan_run_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IDischarge_fan_run_command> getUsesDischarge_fan_run_command (){
		Set<IDischarge_fan_run_command> UsesDischarge_fan_run_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Discharge_fan_run_command) {
				UsesDischarge_fan_run_command.add((Discharge_fan_run_command)action);
			}
		});
		return UsesDischarge_fan_run_command;
	}


  public void addUsesDischarge_fan_run_status (IDischarge_fan_run_status parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IDischarge_fan_run_status> getUsesDischarge_fan_run_status (){
		Set<IDischarge_fan_run_status> UsesDischarge_fan_run_status = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Discharge_fan_run_status) {
				UsesDischarge_fan_run_status.add((Discharge_fan_run_status)action);
			}
		});
		return UsesDischarge_fan_run_status;
	}


  public void addUsesCompressor_run_command_1 (ICompressor_run_command_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ICompressor_run_command_1> getUsesCompressor_run_command_1 (){
		Set<ICompressor_run_command_1> UsesCompressor_run_command_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Compressor_run_command_1) {
				UsesCompressor_run_command_1.add((Compressor_run_command_1)action);
			}
		});
		return UsesCompressor_run_command_1;
	}


  public void addUsesCompressor_run_command_2 (ICompressor_run_command_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ICompressor_run_command_2> getUsesCompressor_run_command_2 (){
		Set<ICompressor_run_command_2> UsesCompressor_run_command_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Compressor_run_command_2) {
				UsesCompressor_run_command_2.add((Compressor_run_command_2)action);
			}
		});
		return UsesCompressor_run_command_2;
	}


  public void addUsesCompressor_run_status_1 (ICompressor_run_status_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ICompressor_run_status_1> getUsesCompressor_run_status_1 (){
		Set<ICompressor_run_status_1> UsesCompressor_run_status_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Compressor_run_status_1) {
				UsesCompressor_run_status_1.add((Compressor_run_status_1)action);
			}
		});
		return UsesCompressor_run_status_1;
	}


  public void addUsesCompressor_run_status_2 (ICompressor_run_status_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ICompressor_run_status_2> getUsesCompressor_run_status_2 (){
		Set<ICompressor_run_status_2> UsesCompressor_run_status_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Compressor_run_status_2) {
				UsesCompressor_run_status_2.add((Compressor_run_status_2)action);
			}
		});
		return UsesCompressor_run_status_2;
	}


  public void addUsesZone_air_cooling_temperature_setpoint (IZone_air_cooling_temperature_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IZone_air_cooling_temperature_setpoint> getUsesZone_air_cooling_temperature_setpoint (){
		Set<IZone_air_cooling_temperature_setpoint> UsesZone_air_cooling_temperature_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Zone_air_cooling_temperature_setpoint) {
				UsesZone_air_cooling_temperature_setpoint.add((Zone_air_cooling_temperature_setpoint)action);
			}
		});
		return UsesZone_air_cooling_temperature_setpoint;
	}


  public void addUsesBoost_fan_run_command (IBoost_fan_run_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IBoost_fan_run_command> getUsesBoost_fan_run_command (){
		Set<IBoost_fan_run_command> UsesBoost_fan_run_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Boost_fan_run_command) {
				UsesBoost_fan_run_command.add((Boost_fan_run_command)action);
			}
		});
		return UsesBoost_fan_run_command;
	}


  public void addUsesBoost_fan_run_status (IBoost_fan_run_status parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IBoost_fan_run_status> getUsesBoost_fan_run_status (){
		Set<IBoost_fan_run_status> UsesBoost_fan_run_status = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Boost_fan_run_status) {
				UsesBoost_fan_run_status.add((Boost_fan_run_status)action);
			}
		});
		return UsesBoost_fan_run_status;
	}

	public static Set<ICo2c> getAllCo2csObjectsCreated(){
		Set<ICo2c> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Co2c")).subjects().stream()
		.map(mapper->(ICo2c)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}