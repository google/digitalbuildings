package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_current_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_power_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_air_flowrate_capacity;
/**
* Class Dfss 
* Basic combination of discharge fan run command and status (start/stop).
*/
public interface IDfss extends IFunctionality, IOperational{

	public IRI iri();

    public void addUsesDischarge_fan_run_command (IDischarge_fan_run_command parameter);

	public Set<IDischarge_fan_run_command> getUsesDischarge_fan_run_command();

    public void addUsesDischarge_fan_run_status (IDischarge_fan_run_status parameter);

	public Set<IDischarge_fan_run_status> getUsesDischarge_fan_run_status();

    public void addUsesOptionalsDischarge_air_flowrate_capacity (IDischarge_air_flowrate_capacity parameter);

	public Set<IDischarge_air_flowrate_capacity> getUsesOptionalsDischarge_air_flowrate_capacity();

    public void addUsesOptionalsDischarge_fan_current_sensor (IDischarge_fan_current_sensor parameter);

	public Set<IDischarge_fan_current_sensor> getUsesOptionalsDischarge_fan_current_sensor();

    public void addUsesOptionalsDischarge_fan_power_capacity (IDischarge_fan_power_capacity parameter);

	public Set<IDischarge_fan_power_capacity> getUsesOptionalsDischarge_fan_power_capacity();

    public void addUsesOptionalsDischarge_fan_power_sensor (IDischarge_fan_power_sensor parameter);

	public Set<IDischarge_fan_power_sensor> getUsesOptionalsDischarge_fan_power_sensor();

}