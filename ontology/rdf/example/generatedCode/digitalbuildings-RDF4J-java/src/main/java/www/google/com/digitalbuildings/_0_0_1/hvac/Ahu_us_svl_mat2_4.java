package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_air_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_static_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_air_static_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_speed_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_speed_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IMixed_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Mixed_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IMixed_air_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Mixed_air_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Outside_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_speed_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Compressor_speed_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_speed_frequency_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_speed_frequency_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ILeaving_heating_coil_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Leaving_heating_coil_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Return_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_damper_command;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_air_damper_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_water_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Heating_water_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_damper_status;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_air_damper_status;

/**
* Class Ahu_us_svl_mat2_4 
* Non-standard type for MAT2 ACs
*/
@SuppressWarnings("serial")
public class Ahu_us_svl_mat2_4 extends www.google.com.digitalbuildings._0_0_1.hvac.Ahu implements IAhu_us_svl_mat2_4{

	IRI newInstance;
	public Ahu_us_svl_mat2_4(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Ahu_us_svl_mat2_4"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesCompressor_speed_percentage_command (ICompressor_speed_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ICompressor_speed_percentage_command> getUsesCompressor_speed_percentage_command (){
		Set<ICompressor_speed_percentage_command> UsesCompressor_speed_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Compressor_speed_percentage_command) {
				UsesCompressor_speed_percentage_command.add((Compressor_speed_percentage_command)action);
			}
		});
		return UsesCompressor_speed_percentage_command;
	}


  public void addUsesHeating_water_valve_percentage_command (IHeating_water_valve_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IHeating_water_valve_percentage_command> getUsesHeating_water_valve_percentage_command (){
		Set<IHeating_water_valve_percentage_command> UsesHeating_water_valve_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Heating_water_valve_percentage_command) {
				UsesHeating_water_valve_percentage_command.add((Heating_water_valve_percentage_command)action);
			}
		});
		return UsesHeating_water_valve_percentage_command;
	}


  public void addUsesLeaving_heating_coil_temperature_sensor (ILeaving_heating_coil_temperature_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ILeaving_heating_coil_temperature_sensor> getUsesLeaving_heating_coil_temperature_sensor (){
		Set<ILeaving_heating_coil_temperature_sensor> UsesLeaving_heating_coil_temperature_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Leaving_heating_coil_temperature_sensor) {
				UsesLeaving_heating_coil_temperature_sensor.add((Leaving_heating_coil_temperature_sensor)action);
			}
		});
		return UsesLeaving_heating_coil_temperature_sensor;
	}


  public void addUsesMixed_air_temperature_sensor (IMixed_air_temperature_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IMixed_air_temperature_sensor> getUsesMixed_air_temperature_sensor (){
		Set<IMixed_air_temperature_sensor> UsesMixed_air_temperature_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Mixed_air_temperature_sensor) {
				UsesMixed_air_temperature_sensor.add((Mixed_air_temperature_sensor)action);
			}
		});
		return UsesMixed_air_temperature_sensor;
	}


  public void addUsesMixed_air_temperature_setpoint (IMixed_air_temperature_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IMixed_air_temperature_setpoint> getUsesMixed_air_temperature_setpoint (){
		Set<IMixed_air_temperature_setpoint> UsesMixed_air_temperature_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Mixed_air_temperature_setpoint) {
				UsesMixed_air_temperature_setpoint.add((Mixed_air_temperature_setpoint)action);
			}
		});
		return UsesMixed_air_temperature_setpoint;
	}


  public void addUsesOutside_air_damper_percentage_command (IOutside_air_damper_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IOutside_air_damper_percentage_command> getUsesOutside_air_damper_percentage_command (){
		Set<IOutside_air_damper_percentage_command> UsesOutside_air_damper_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Outside_air_damper_percentage_command) {
				UsesOutside_air_damper_percentage_command.add((Outside_air_damper_percentage_command)action);
			}
		});
		return UsesOutside_air_damper_percentage_command;
	}


  public void addUsesReturn_air_temperature_sensor (IReturn_air_temperature_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IReturn_air_temperature_sensor> getUsesReturn_air_temperature_sensor (){
		Set<IReturn_air_temperature_sensor> UsesReturn_air_temperature_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Return_air_temperature_sensor) {
				UsesReturn_air_temperature_sensor.add((Return_air_temperature_sensor)action);
			}
		});
		return UsesReturn_air_temperature_sensor;
	}


  public void addUsesSupply_air_damper_command (ISupply_air_damper_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_air_damper_command> getUsesSupply_air_damper_command (){
		Set<ISupply_air_damper_command> UsesSupply_air_damper_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_air_damper_command) {
				UsesSupply_air_damper_command.add((Supply_air_damper_command)action);
			}
		});
		return UsesSupply_air_damper_command;
	}


  public void addUsesSupply_air_damper_status (ISupply_air_damper_status parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_air_damper_status> getUsesSupply_air_damper_status (){
		Set<ISupply_air_damper_status> UsesSupply_air_damper_status = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_air_damper_status) {
				UsesSupply_air_damper_status.add((Supply_air_damper_status)action);
			}
		});
		return UsesSupply_air_damper_status;
	}


  public void addUsesSupply_air_flowrate_sensor (ISupply_air_flowrate_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_air_flowrate_sensor> getUsesSupply_air_flowrate_sensor (){
		Set<ISupply_air_flowrate_sensor> UsesSupply_air_flowrate_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_air_flowrate_sensor) {
				UsesSupply_air_flowrate_sensor.add((Supply_air_flowrate_sensor)action);
			}
		});
		return UsesSupply_air_flowrate_sensor;
	}


  public void addUsesSupply_air_static_pressure_sensor (ISupply_air_static_pressure_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_air_static_pressure_sensor> getUsesSupply_air_static_pressure_sensor (){
		Set<ISupply_air_static_pressure_sensor> UsesSupply_air_static_pressure_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_air_static_pressure_sensor) {
				UsesSupply_air_static_pressure_sensor.add((Supply_air_static_pressure_sensor)action);
			}
		});
		return UsesSupply_air_static_pressure_sensor;
	}


  public void addUsesSupply_air_static_pressure_setpoint (ISupply_air_static_pressure_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_air_static_pressure_setpoint> getUsesSupply_air_static_pressure_setpoint (){
		Set<ISupply_air_static_pressure_setpoint> UsesSupply_air_static_pressure_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_air_static_pressure_setpoint) {
				UsesSupply_air_static_pressure_setpoint.add((Supply_air_static_pressure_setpoint)action);
			}
		});
		return UsesSupply_air_static_pressure_setpoint;
	}


  public void addUsesSupply_air_temperature_sensor (ISupply_air_temperature_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_air_temperature_sensor> getUsesSupply_air_temperature_sensor (){
		Set<ISupply_air_temperature_sensor> UsesSupply_air_temperature_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_air_temperature_sensor) {
				UsesSupply_air_temperature_sensor.add((Supply_air_temperature_sensor)action);
			}
		});
		return UsesSupply_air_temperature_sensor;
	}


  public void addUsesSupply_air_temperature_setpoint (ISupply_air_temperature_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_air_temperature_setpoint> getUsesSupply_air_temperature_setpoint (){
		Set<ISupply_air_temperature_setpoint> UsesSupply_air_temperature_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_air_temperature_setpoint) {
				UsesSupply_air_temperature_setpoint.add((Supply_air_temperature_setpoint)action);
			}
		});
		return UsesSupply_air_temperature_setpoint;
	}


  public void addUsesSupply_fan_run_command (ISupply_fan_run_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_fan_run_command> getUsesSupply_fan_run_command (){
		Set<ISupply_fan_run_command> UsesSupply_fan_run_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_fan_run_command) {
				UsesSupply_fan_run_command.add((Supply_fan_run_command)action);
			}
		});
		return UsesSupply_fan_run_command;
	}


  public void addUsesSupply_fan_speed_frequency_sensor (ISupply_fan_speed_frequency_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_fan_speed_frequency_sensor> getUsesSupply_fan_speed_frequency_sensor (){
		Set<ISupply_fan_speed_frequency_sensor> UsesSupply_fan_speed_frequency_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_fan_speed_frequency_sensor) {
				UsesSupply_fan_speed_frequency_sensor.add((Supply_fan_speed_frequency_sensor)action);
			}
		});
		return UsesSupply_fan_speed_frequency_sensor;
	}


  public void addUsesSupply_fan_speed_percentage_command (ISupply_fan_speed_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_fan_speed_percentage_command> getUsesSupply_fan_speed_percentage_command (){
		Set<ISupply_fan_speed_percentage_command> UsesSupply_fan_speed_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_fan_speed_percentage_command) {
				UsesSupply_fan_speed_percentage_command.add((Supply_fan_speed_percentage_command)action);
			}
		});
		return UsesSupply_fan_speed_percentage_command;
	}

	public static Set<IAhu_us_svl_mat2_4> getAllAhu_us_svl_mat2_4sObjectsCreated(){
		Set<IAhu_us_svl_mat2_4> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Ahu_us_svl_mat2_4")).subjects().stream()
		.map(mapper->(IAhu_us_svl_mat2_4)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}