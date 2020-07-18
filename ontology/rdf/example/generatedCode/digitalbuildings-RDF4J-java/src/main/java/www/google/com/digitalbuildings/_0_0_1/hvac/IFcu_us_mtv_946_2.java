package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_cooling_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IHumidification_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IReversing_valve_command;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_air_relative_humidity_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_speed_mode;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IHumidification_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_water_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_air_humidification_relative_humidity_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_heating_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_air_dehumidification_relative_humidity_setpoint;
/**
* Class Fcu_us_mtv_946_2 
* Non-standard type for 946 FCs
*/
public interface IFcu_us_mtv_946_2 extends IFcu{

	public IRI iri();

    public void addUsesCompressor_run_status (ICompressor_run_status parameter);

	public Set<ICompressor_run_status> getUsesCompressor_run_status();

    public void addUsesDischarge_air_temperature_sensor (IDischarge_air_temperature_sensor parameter);

	public Set<IDischarge_air_temperature_sensor> getUsesDischarge_air_temperature_sensor();

    public void addUsesDischarge_fan_run_status (IDischarge_fan_run_status parameter);

	public Set<IDischarge_fan_run_status> getUsesDischarge_fan_run_status();

    public void addUsesDischarge_fan_speed_mode (IDischarge_fan_speed_mode parameter);

	public Set<IDischarge_fan_speed_mode> getUsesDischarge_fan_speed_mode();

    public void addUsesHeating_water_valve_percentage_command (IHeating_water_valve_percentage_command parameter);

	public Set<IHeating_water_valve_percentage_command> getUsesHeating_water_valve_percentage_command();

    public void addUsesHumidification_percentage_command (IHumidification_percentage_command parameter);

	public Set<IHumidification_percentage_command> getUsesHumidification_percentage_command();

    public void addUsesHumidification_run_command (IHumidification_run_command parameter);

	public Set<IHumidification_run_command> getUsesHumidification_run_command();

    public void addUsesReturn_air_dehumidification_relative_humidity_setpoint (IReturn_air_dehumidification_relative_humidity_setpoint parameter);

	public Set<IReturn_air_dehumidification_relative_humidity_setpoint> getUsesReturn_air_dehumidification_relative_humidity_setpoint();

    public void addUsesReturn_air_humidification_relative_humidity_setpoint (IReturn_air_humidification_relative_humidity_setpoint parameter);

	public Set<IReturn_air_humidification_relative_humidity_setpoint> getUsesReturn_air_humidification_relative_humidity_setpoint();

    public void addUsesReturn_air_relative_humidity_sensor (IReturn_air_relative_humidity_sensor parameter);

	public Set<IReturn_air_relative_humidity_sensor> getUsesReturn_air_relative_humidity_sensor();

    public void addUsesReturn_air_temperature_sensor (IReturn_air_temperature_sensor parameter);

	public Set<IReturn_air_temperature_sensor> getUsesReturn_air_temperature_sensor();

    public void addUsesReversing_valve_command (IReversing_valve_command parameter);

	public Set<IReversing_valve_command> getUsesReversing_valve_command();

    public void addUsesZone_air_cooling_temperature_setpoint (IZone_air_cooling_temperature_setpoint parameter);

	public Set<IZone_air_cooling_temperature_setpoint> getUsesZone_air_cooling_temperature_setpoint();

    public void addUsesZone_air_heating_temperature_setpoint (IZone_air_heating_temperature_setpoint parameter);

	public Set<IZone_air_heating_temperature_setpoint> getUsesZone_air_heating_temperature_setpoint();

    public void addUsesZone_air_temperature_sensor (IZone_air_temperature_sensor parameter);

	public Set<IZone_air_temperature_sensor> getUsesZone_air_temperature_sensor();

}