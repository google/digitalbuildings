package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_water_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_speed_percentage_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_speed_percentage_command_3;
import www.google.com.digitalbuildings._0_0_1.fields.IExercise_mode;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_temperature_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_speed_percentage_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_temperature_setpoint_1;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_temperature_setpoint_2;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_temperature_setpoint_3;
import www.google.com.digitalbuildings._0_0_1.fields.IMaster_alarm_status;
import www.google.com.digitalbuildings._0_0_1.fields.IRun_mode;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_occupancy_status_1;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_occupancy_status_2;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_occupancy_status_3;
import www.google.com.digitalbuildings._0_0_1.fields.IFabric_protection_alarm_status;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_water_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IFilter_alarm_status;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_temperature_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_temperature_sensor_3;
/**
* Class Fcu_uk_lon_6ps_3 
* Non-standard type for 6PS
*/
public interface IFcu_uk_lon_6ps_3 extends IFcu{

	public IRI iri();

    public void addUsesChilled_water_valve_percentage_command (IChilled_water_valve_percentage_command parameter);

	public Set<IChilled_water_valve_percentage_command> getUsesChilled_water_valve_percentage_command();

    public void addUsesDischarge_fan_run_command (IDischarge_fan_run_command parameter);

	public Set<IDischarge_fan_run_command> getUsesDischarge_fan_run_command();

    public void addUsesDischarge_fan_speed_percentage_command_1 (IDischarge_fan_speed_percentage_command_1 parameter);

	public Set<IDischarge_fan_speed_percentage_command_1> getUsesDischarge_fan_speed_percentage_command_1();

    public void addUsesDischarge_fan_speed_percentage_command_2 (IDischarge_fan_speed_percentage_command_2 parameter);

	public Set<IDischarge_fan_speed_percentage_command_2> getUsesDischarge_fan_speed_percentage_command_2();

    public void addUsesDischarge_fan_speed_percentage_command_3 (IDischarge_fan_speed_percentage_command_3 parameter);

	public Set<IDischarge_fan_speed_percentage_command_3> getUsesDischarge_fan_speed_percentage_command_3();

    public void addUsesExercise_mode (IExercise_mode parameter);

	public Set<IExercise_mode> getUsesExercise_mode();

    public void addUsesFabric_protection_alarm_status (IFabric_protection_alarm_status parameter);

	public Set<IFabric_protection_alarm_status> getUsesFabric_protection_alarm_status();

    public void addUsesFilter_alarm_status (IFilter_alarm_status parameter);

	public Set<IFilter_alarm_status> getUsesFilter_alarm_status();

    public void addUsesHeating_water_valve_percentage_command (IHeating_water_valve_percentage_command parameter);

	public Set<IHeating_water_valve_percentage_command> getUsesHeating_water_valve_percentage_command();

    public void addUsesMaster_alarm_status (IMaster_alarm_status parameter);

	public Set<IMaster_alarm_status> getUsesMaster_alarm_status();

    public void addUsesRun_mode (IRun_mode parameter);

	public Set<IRun_mode> getUsesRun_mode();

    public void addUsesZone_air_temperature_sensor_1 (IZone_air_temperature_sensor_1 parameter);

	public Set<IZone_air_temperature_sensor_1> getUsesZone_air_temperature_sensor_1();

    public void addUsesZone_air_temperature_sensor_2 (IZone_air_temperature_sensor_2 parameter);

	public Set<IZone_air_temperature_sensor_2> getUsesZone_air_temperature_sensor_2();

    public void addUsesZone_air_temperature_sensor_3 (IZone_air_temperature_sensor_3 parameter);

	public Set<IZone_air_temperature_sensor_3> getUsesZone_air_temperature_sensor_3();

    public void addUsesZone_air_temperature_setpoint (IZone_air_temperature_setpoint parameter);

	public Set<IZone_air_temperature_setpoint> getUsesZone_air_temperature_setpoint();

    public void addUsesZone_air_temperature_setpoint_1 (IZone_air_temperature_setpoint_1 parameter);

	public Set<IZone_air_temperature_setpoint_1> getUsesZone_air_temperature_setpoint_1();

    public void addUsesZone_air_temperature_setpoint_2 (IZone_air_temperature_setpoint_2 parameter);

	public Set<IZone_air_temperature_setpoint_2> getUsesZone_air_temperature_setpoint_2();

    public void addUsesZone_air_temperature_setpoint_3 (IZone_air_temperature_setpoint_3 parameter);

	public Set<IZone_air_temperature_setpoint_3> getUsesZone_air_temperature_setpoint_3();

    public void addUsesZone_occupancy_status_1 (IZone_occupancy_status_1 parameter);

	public Set<IZone_occupancy_status_1> getUsesZone_occupancy_status_1();

    public void addUsesZone_occupancy_status_2 (IZone_occupancy_status_2 parameter);

	public Set<IZone_occupancy_status_2> getUsesZone_occupancy_status_2();

    public void addUsesZone_occupancy_status_3 (IZone_occupancy_status_3 parameter);

	public Set<IZone_occupancy_status_3> getUsesZone_occupancy_status_3();

}