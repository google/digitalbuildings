package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_current_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_status_1;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_frequency_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_current_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_frequency_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_status_2;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_power_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_power_sensor_1;
/**
* Class Efvsc2x 
* Exhaust fan variable speed control with feedback and sensoring for two fans.
*/
public interface IEfvsc2x extends IFunctionality, IOperational{

	public IRI iri();

    public void addUsesExhaust_fan_run_command_1 (IExhaust_fan_run_command_1 parameter);

	public Set<IExhaust_fan_run_command_1> getUsesExhaust_fan_run_command_1();

    public void addUsesExhaust_fan_run_command_2 (IExhaust_fan_run_command_2 parameter);

	public Set<IExhaust_fan_run_command_2> getUsesExhaust_fan_run_command_2();

    public void addUsesExhaust_fan_run_status_1 (IExhaust_fan_run_status_1 parameter);

	public Set<IExhaust_fan_run_status_1> getUsesExhaust_fan_run_status_1();

    public void addUsesExhaust_fan_run_status_2 (IExhaust_fan_run_status_2 parameter);

	public Set<IExhaust_fan_run_status_2> getUsesExhaust_fan_run_status_2();

    public void addUsesExhaust_fan_speed_percentage_command_1 (IExhaust_fan_speed_percentage_command_1 parameter);

	public Set<IExhaust_fan_speed_percentage_command_1> getUsesExhaust_fan_speed_percentage_command_1();

    public void addUsesExhaust_fan_speed_percentage_command_2 (IExhaust_fan_speed_percentage_command_2 parameter);

	public Set<IExhaust_fan_speed_percentage_command_2> getUsesExhaust_fan_speed_percentage_command_2();

    public void addUsesOptionalsExhaust_fan_current_sensor_1 (IExhaust_fan_current_sensor_1 parameter);

	public Set<IExhaust_fan_current_sensor_1> getUsesOptionalsExhaust_fan_current_sensor_1();

    public void addUsesOptionalsExhaust_fan_current_sensor_2 (IExhaust_fan_current_sensor_2 parameter);

	public Set<IExhaust_fan_current_sensor_2> getUsesOptionalsExhaust_fan_current_sensor_2();

    public void addUsesOptionalsExhaust_fan_power_sensor_1 (IExhaust_fan_power_sensor_1 parameter);

	public Set<IExhaust_fan_power_sensor_1> getUsesOptionalsExhaust_fan_power_sensor_1();

    public void addUsesOptionalsExhaust_fan_power_sensor_2 (IExhaust_fan_power_sensor_2 parameter);

	public Set<IExhaust_fan_power_sensor_2> getUsesOptionalsExhaust_fan_power_sensor_2();

    public void addUsesOptionalsExhaust_fan_speed_frequency_sensor_1 (IExhaust_fan_speed_frequency_sensor_1 parameter);

	public Set<IExhaust_fan_speed_frequency_sensor_1> getUsesOptionalsExhaust_fan_speed_frequency_sensor_1();

    public void addUsesOptionalsExhaust_fan_speed_frequency_sensor_2 (IExhaust_fan_speed_frequency_sensor_2 parameter);

	public Set<IExhaust_fan_speed_frequency_sensor_2> getUsesOptionalsExhaust_fan_speed_frequency_sensor_2();

    public void addUsesOptionalsExhaust_fan_speed_percentage_sensor_1 (IExhaust_fan_speed_percentage_sensor_1 parameter);

	public Set<IExhaust_fan_speed_percentage_sensor_1> getUsesOptionalsExhaust_fan_speed_percentage_sensor_1();

    public void addUsesOptionalsExhaust_fan_speed_percentage_sensor_2 (IExhaust_fan_speed_percentage_sensor_2 parameter);

	public Set<IExhaust_fan_speed_percentage_sensor_2> getUsesOptionalsExhaust_fan_speed_percentage_sensor_2();

}