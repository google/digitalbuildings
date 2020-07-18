package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_current_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_flowrate_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_power_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_command;
/**
* Class Efss 
* Basic combination of exhaust fan run command and status (start/stop).
*/
public interface IEfss extends IFunctionality, IOperational{

	public IRI iri();

    public void addUsesExhaust_fan_run_command (IExhaust_fan_run_command parameter);

	public Set<IExhaust_fan_run_command> getUsesExhaust_fan_run_command();

    public void addUsesExhaust_fan_run_status (IExhaust_fan_run_status parameter);

	public Set<IExhaust_fan_run_status> getUsesExhaust_fan_run_status();

    public void addUsesOptionalsExhaust_air_flowrate_capacity (IExhaust_air_flowrate_capacity parameter);

	public Set<IExhaust_air_flowrate_capacity> getUsesOptionalsExhaust_air_flowrate_capacity();

    public void addUsesOptionalsExhaust_fan_current_sensor (IExhaust_fan_current_sensor parameter);

	public Set<IExhaust_fan_current_sensor> getUsesOptionalsExhaust_fan_current_sensor();

    public void addUsesOptionalsExhaust_fan_power_capacity (IExhaust_fan_power_capacity parameter);

	public Set<IExhaust_fan_power_capacity> getUsesOptionalsExhaust_fan_power_capacity();

    public void addUsesOptionalsExhaust_fan_power_sensor (IExhaust_fan_power_sensor parameter);

	public Set<IExhaust_fan_power_sensor> getUsesOptionalsExhaust_fan_power_sensor();

}