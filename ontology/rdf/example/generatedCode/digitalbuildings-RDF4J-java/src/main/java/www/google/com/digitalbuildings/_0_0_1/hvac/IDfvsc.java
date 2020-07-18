package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_speed_frequency_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_speed_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_speed_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_current_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_power_sensor;
/**
* Class Dfvsc 
* Variable speed control for discharge fans.
*/
public interface IDfvsc extends IFunctionality, IOperational{

	public IRI iri();

    public void addUsesOptionalsDischarge_fan_current_sensor (IDischarge_fan_current_sensor parameter);

	public Set<IDischarge_fan_current_sensor> getUsesOptionalsDischarge_fan_current_sensor();

    public void addUsesOptionalsDischarge_fan_power_sensor (IDischarge_fan_power_sensor parameter);

	public Set<IDischarge_fan_power_sensor> getUsesOptionalsDischarge_fan_power_sensor();

    public void addUsesOptionalsDischarge_fan_speed_frequency_sensor (IDischarge_fan_speed_frequency_sensor parameter);

	public Set<IDischarge_fan_speed_frequency_sensor> getUsesOptionalsDischarge_fan_speed_frequency_sensor();

    public void addUsesOptionalsDischarge_fan_speed_percentage_sensor (IDischarge_fan_speed_percentage_sensor parameter);

	public Set<IDischarge_fan_speed_percentage_sensor> getUsesOptionalsDischarge_fan_speed_percentage_sensor();

    public void addUsesDischarge_fan_run_command (IDischarge_fan_run_command parameter);

	public Set<IDischarge_fan_run_command> getUsesDischarge_fan_run_command();

    public void addUsesDischarge_fan_run_status (IDischarge_fan_run_status parameter);

	public Set<IDischarge_fan_run_status> getUsesDischarge_fan_run_status();

    public void addUsesDischarge_fan_speed_percentage_command (IDischarge_fan_speed_percentage_command parameter);

	public Set<IDischarge_fan_speed_percentage_command> getUsesDischarge_fan_speed_percentage_command();

}