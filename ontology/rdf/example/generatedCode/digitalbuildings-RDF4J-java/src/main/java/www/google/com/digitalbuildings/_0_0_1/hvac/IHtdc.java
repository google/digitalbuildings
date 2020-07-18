package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IControl;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IHeater_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_thermal_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_air_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IHeater_run_command;
/**
* Class Htdc 
* Gas or electric heater control on discharge side.
*/
public interface IHtdc extends IFunctionality, IControl{

	public IRI iri();

    public void addUsesOptionalsHeater_run_status (IHeater_run_status parameter);

	public Set<IHeater_run_status> getUsesOptionalsHeater_run_status();

    public void addUsesOptionalsHeating_percentage_command (IHeating_percentage_command parameter);

	public Set<IHeating_percentage_command> getUsesOptionalsHeating_percentage_command();

    public void addUsesOptionalsHeating_thermal_power_capacity (IHeating_thermal_power_capacity parameter);

	public Set<IHeating_thermal_power_capacity> getUsesOptionalsHeating_thermal_power_capacity();

    public void addUsesDischarge_air_temperature_sensor (IDischarge_air_temperature_sensor parameter);

	public Set<IDischarge_air_temperature_sensor> getUsesDischarge_air_temperature_sensor();

    public void addUsesDischarge_air_temperature_setpoint (IDischarge_air_temperature_setpoint parameter);

	public Set<IDischarge_air_temperature_setpoint> getUsesDischarge_air_temperature_setpoint();

    public void addUsesHeater_run_command (IHeater_run_command parameter);

	public Set<IHeater_run_command> getUsesHeater_run_command();

}