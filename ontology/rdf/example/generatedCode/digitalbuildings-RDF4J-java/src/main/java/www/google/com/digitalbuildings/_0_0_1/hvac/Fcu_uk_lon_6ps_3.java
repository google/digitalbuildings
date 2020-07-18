package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_water_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Chilled_water_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_speed_percentage_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_fan_speed_percentage_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_speed_percentage_command_3;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_fan_speed_percentage_command_3;
import www.google.com.digitalbuildings._0_0_1.fields.IExercise_mode;
import www.google.com.digitalbuildings._0_0_1.fields.Exercise_mode;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_temperature_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_air_temperature_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_speed_percentage_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_fan_speed_percentage_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_temperature_setpoint_1;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_air_temperature_setpoint_1;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_temperature_setpoint_2;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_air_temperature_setpoint_2;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_temperature_setpoint_3;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_air_temperature_setpoint_3;
import www.google.com.digitalbuildings._0_0_1.fields.IMaster_alarm_status;
import www.google.com.digitalbuildings._0_0_1.fields.Master_alarm_status;
import www.google.com.digitalbuildings._0_0_1.fields.IRun_mode;
import www.google.com.digitalbuildings._0_0_1.fields.Run_mode;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_occupancy_status_1;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_occupancy_status_1;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_occupancy_status_2;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_occupancy_status_2;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_occupancy_status_3;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_occupancy_status_3;
import www.google.com.digitalbuildings._0_0_1.fields.IFabric_protection_alarm_status;
import www.google.com.digitalbuildings._0_0_1.fields.Fabric_protection_alarm_status;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_air_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_water_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Heating_water_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IFilter_alarm_status;
import www.google.com.digitalbuildings._0_0_1.fields.Filter_alarm_status;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_temperature_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_air_temperature_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_temperature_sensor_3;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_air_temperature_sensor_3;

/**
* Class Fcu_uk_lon_6ps_3 
* Non-standard type for 6PS
*/
@SuppressWarnings("serial")
public class Fcu_uk_lon_6ps_3 extends www.google.com.digitalbuildings._0_0_1.hvac.Fcu implements IFcu_uk_lon_6ps_3{

	IRI newInstance;
	public Fcu_uk_lon_6ps_3(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Fcu_uk_lon_6ps_3"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesChilled_water_valve_percentage_command (IChilled_water_valve_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IChilled_water_valve_percentage_command> getUsesChilled_water_valve_percentage_command (){
		Set<IChilled_water_valve_percentage_command> UsesChilled_water_valve_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Chilled_water_valve_percentage_command) {
				UsesChilled_water_valve_percentage_command.add((Chilled_water_valve_percentage_command)action);
			}
		});
		return UsesChilled_water_valve_percentage_command;
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


  public void addUsesDischarge_fan_speed_percentage_command_1 (IDischarge_fan_speed_percentage_command_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IDischarge_fan_speed_percentage_command_1> getUsesDischarge_fan_speed_percentage_command_1 (){
		Set<IDischarge_fan_speed_percentage_command_1> UsesDischarge_fan_speed_percentage_command_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Discharge_fan_speed_percentage_command_1) {
				UsesDischarge_fan_speed_percentage_command_1.add((Discharge_fan_speed_percentage_command_1)action);
			}
		});
		return UsesDischarge_fan_speed_percentage_command_1;
	}


  public void addUsesDischarge_fan_speed_percentage_command_2 (IDischarge_fan_speed_percentage_command_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IDischarge_fan_speed_percentage_command_2> getUsesDischarge_fan_speed_percentage_command_2 (){
		Set<IDischarge_fan_speed_percentage_command_2> UsesDischarge_fan_speed_percentage_command_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Discharge_fan_speed_percentage_command_2) {
				UsesDischarge_fan_speed_percentage_command_2.add((Discharge_fan_speed_percentage_command_2)action);
			}
		});
		return UsesDischarge_fan_speed_percentage_command_2;
	}


  public void addUsesDischarge_fan_speed_percentage_command_3 (IDischarge_fan_speed_percentage_command_3 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IDischarge_fan_speed_percentage_command_3> getUsesDischarge_fan_speed_percentage_command_3 (){
		Set<IDischarge_fan_speed_percentage_command_3> UsesDischarge_fan_speed_percentage_command_3 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Discharge_fan_speed_percentage_command_3) {
				UsesDischarge_fan_speed_percentage_command_3.add((Discharge_fan_speed_percentage_command_3)action);
			}
		});
		return UsesDischarge_fan_speed_percentage_command_3;
	}


  public void addUsesExercise_mode (IExercise_mode parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IExercise_mode> getUsesExercise_mode (){
		Set<IExercise_mode> UsesExercise_mode = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Exercise_mode) {
				UsesExercise_mode.add((Exercise_mode)action);
			}
		});
		return UsesExercise_mode;
	}


  public void addUsesFabric_protection_alarm_status (IFabric_protection_alarm_status parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IFabric_protection_alarm_status> getUsesFabric_protection_alarm_status (){
		Set<IFabric_protection_alarm_status> UsesFabric_protection_alarm_status = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Fabric_protection_alarm_status) {
				UsesFabric_protection_alarm_status.add((Fabric_protection_alarm_status)action);
			}
		});
		return UsesFabric_protection_alarm_status;
	}


  public void addUsesFilter_alarm_status (IFilter_alarm_status parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IFilter_alarm_status> getUsesFilter_alarm_status (){
		Set<IFilter_alarm_status> UsesFilter_alarm_status = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Filter_alarm_status) {
				UsesFilter_alarm_status.add((Filter_alarm_status)action);
			}
		});
		return UsesFilter_alarm_status;
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


  public void addUsesMaster_alarm_status (IMaster_alarm_status parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IMaster_alarm_status> getUsesMaster_alarm_status (){
		Set<IMaster_alarm_status> UsesMaster_alarm_status = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Master_alarm_status) {
				UsesMaster_alarm_status.add((Master_alarm_status)action);
			}
		});
		return UsesMaster_alarm_status;
	}


  public void addUsesRun_mode (IRun_mode parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IRun_mode> getUsesRun_mode (){
		Set<IRun_mode> UsesRun_mode = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Run_mode) {
				UsesRun_mode.add((Run_mode)action);
			}
		});
		return UsesRun_mode;
	}


  public void addUsesZone_air_temperature_sensor_1 (IZone_air_temperature_sensor_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IZone_air_temperature_sensor_1> getUsesZone_air_temperature_sensor_1 (){
		Set<IZone_air_temperature_sensor_1> UsesZone_air_temperature_sensor_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Zone_air_temperature_sensor_1) {
				UsesZone_air_temperature_sensor_1.add((Zone_air_temperature_sensor_1)action);
			}
		});
		return UsesZone_air_temperature_sensor_1;
	}


  public void addUsesZone_air_temperature_sensor_2 (IZone_air_temperature_sensor_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IZone_air_temperature_sensor_2> getUsesZone_air_temperature_sensor_2 (){
		Set<IZone_air_temperature_sensor_2> UsesZone_air_temperature_sensor_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Zone_air_temperature_sensor_2) {
				UsesZone_air_temperature_sensor_2.add((Zone_air_temperature_sensor_2)action);
			}
		});
		return UsesZone_air_temperature_sensor_2;
	}


  public void addUsesZone_air_temperature_sensor_3 (IZone_air_temperature_sensor_3 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IZone_air_temperature_sensor_3> getUsesZone_air_temperature_sensor_3 (){
		Set<IZone_air_temperature_sensor_3> UsesZone_air_temperature_sensor_3 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Zone_air_temperature_sensor_3) {
				UsesZone_air_temperature_sensor_3.add((Zone_air_temperature_sensor_3)action);
			}
		});
		return UsesZone_air_temperature_sensor_3;
	}


  public void addUsesZone_air_temperature_setpoint (IZone_air_temperature_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IZone_air_temperature_setpoint> getUsesZone_air_temperature_setpoint (){
		Set<IZone_air_temperature_setpoint> UsesZone_air_temperature_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Zone_air_temperature_setpoint) {
				UsesZone_air_temperature_setpoint.add((Zone_air_temperature_setpoint)action);
			}
		});
		return UsesZone_air_temperature_setpoint;
	}


  public void addUsesZone_air_temperature_setpoint_1 (IZone_air_temperature_setpoint_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IZone_air_temperature_setpoint_1> getUsesZone_air_temperature_setpoint_1 (){
		Set<IZone_air_temperature_setpoint_1> UsesZone_air_temperature_setpoint_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Zone_air_temperature_setpoint_1) {
				UsesZone_air_temperature_setpoint_1.add((Zone_air_temperature_setpoint_1)action);
			}
		});
		return UsesZone_air_temperature_setpoint_1;
	}


  public void addUsesZone_air_temperature_setpoint_2 (IZone_air_temperature_setpoint_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IZone_air_temperature_setpoint_2> getUsesZone_air_temperature_setpoint_2 (){
		Set<IZone_air_temperature_setpoint_2> UsesZone_air_temperature_setpoint_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Zone_air_temperature_setpoint_2) {
				UsesZone_air_temperature_setpoint_2.add((Zone_air_temperature_setpoint_2)action);
			}
		});
		return UsesZone_air_temperature_setpoint_2;
	}


  public void addUsesZone_air_temperature_setpoint_3 (IZone_air_temperature_setpoint_3 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IZone_air_temperature_setpoint_3> getUsesZone_air_temperature_setpoint_3 (){
		Set<IZone_air_temperature_setpoint_3> UsesZone_air_temperature_setpoint_3 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Zone_air_temperature_setpoint_3) {
				UsesZone_air_temperature_setpoint_3.add((Zone_air_temperature_setpoint_3)action);
			}
		});
		return UsesZone_air_temperature_setpoint_3;
	}


  public void addUsesZone_occupancy_status_1 (IZone_occupancy_status_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IZone_occupancy_status_1> getUsesZone_occupancy_status_1 (){
		Set<IZone_occupancy_status_1> UsesZone_occupancy_status_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Zone_occupancy_status_1) {
				UsesZone_occupancy_status_1.add((Zone_occupancy_status_1)action);
			}
		});
		return UsesZone_occupancy_status_1;
	}


  public void addUsesZone_occupancy_status_2 (IZone_occupancy_status_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IZone_occupancy_status_2> getUsesZone_occupancy_status_2 (){
		Set<IZone_occupancy_status_2> UsesZone_occupancy_status_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Zone_occupancy_status_2) {
				UsesZone_occupancy_status_2.add((Zone_occupancy_status_2)action);
			}
		});
		return UsesZone_occupancy_status_2;
	}


  public void addUsesZone_occupancy_status_3 (IZone_occupancy_status_3 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IZone_occupancy_status_3> getUsesZone_occupancy_status_3 (){
		Set<IZone_occupancy_status_3> UsesZone_occupancy_status_3 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Zone_occupancy_status_3) {
				UsesZone_occupancy_status_3.add((Zone_occupancy_status_3)action);
			}
		});
		return UsesZone_occupancy_status_3;
	}

	public static Set<IFcu_uk_lon_6ps_3> getAllFcu_uk_lon_6ps_3sObjectsCreated(){
		Set<IFcu_uk_lon_6ps_3> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Fcu_uk_lon_6ps_3")).subjects().stream()
		.map(mapper->(IFcu_uk_lon_6ps_3)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}