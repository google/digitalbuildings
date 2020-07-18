package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_current_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_power_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_frequency_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_command;
/**
* Class Efvsc 
* Variable speed control for exhaust fans.
*/
public interface IEfvsc extends IFunctionality, IOperational{

	public IRI iri();

    public void addUsesOptionalsExhaust_fan_current_sensor (IExhaust_fan_current_sensor parameter);

	public Set<IExhaust_fan_current_sensor> getUsesOptionalsExhaust_fan_current_sensor();

    public void addUsesOptionalsExhaust_fan_power_sensor (IExhaust_fan_power_sensor parameter);

	public Set<IExhaust_fan_power_sensor> getUsesOptionalsExhaust_fan_power_sensor();

    public void addUsesOptionalsExhaust_fan_speed_frequency_sensor (IExhaust_fan_speed_frequency_sensor parameter);

	public Set<IExhaust_fan_speed_frequency_sensor> getUsesOptionalsExhaust_fan_speed_frequency_sensor();

    public void addUsesOptionalsExhaust_fan_speed_percentage_sensor (IExhaust_fan_speed_percentage_sensor parameter);

	public Set<IExhaust_fan_speed_percentage_sensor> getUsesOptionalsExhaust_fan_speed_percentage_sensor();

    public void addUsesExhaust_fan_run_command (IExhaust_fan_run_command parameter);

	public Set<IExhaust_fan_run_command> getUsesExhaust_fan_run_command();

    public void addUsesExhaust_fan_run_status (IExhaust_fan_run_status parameter);

	public Set<IExhaust_fan_run_status> getUsesExhaust_fan_run_status();

    public void addUsesExhaust_fan_speed_percentage_command (IExhaust_fan_speed_percentage_command parameter);

	public Set<IExhaust_fan_speed_percentage_command> getUsesExhaust_fan_speed_percentage_command();

}