package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IControl;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IHeater_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_thermal_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IHeater_run_command;
/**
* Class Htvsc 
* Variable gas to electric control on supply air side.
*/
public interface IHtvsc extends IFunctionality, IControl{

	public IRI iri();

    public void addUsesHeater_run_command (IHeater_run_command parameter);

	public Set<IHeater_run_command> getUsesHeater_run_command();

    public void addUsesHeater_run_status (IHeater_run_status parameter);

	public Set<IHeater_run_status> getUsesHeater_run_status();

    public void addUsesHeating_percentage_command (IHeating_percentage_command parameter);

	public Set<IHeating_percentage_command> getUsesHeating_percentage_command();

    public void addUsesSupply_air_temperature_sensor (ISupply_air_temperature_sensor parameter);

	public Set<ISupply_air_temperature_sensor> getUsesSupply_air_temperature_sensor();

    public void addUsesSupply_air_temperature_setpoint (ISupply_air_temperature_setpoint parameter);

	public Set<ISupply_air_temperature_setpoint> getUsesSupply_air_temperature_setpoint();

    public void addUsesOptionalsHeating_thermal_power_capacity (IHeating_thermal_power_capacity parameter);

	public Set<IHeating_thermal_power_capacity> getUsesOptionalsHeating_thermal_power_capacity();

}