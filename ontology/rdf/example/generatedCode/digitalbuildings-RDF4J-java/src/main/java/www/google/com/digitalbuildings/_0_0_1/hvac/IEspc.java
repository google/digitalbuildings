package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_static_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_command;
/**
* Class Espc 
* Exhaust air static pressure control.
*/
public interface IEspc extends IFunctionality, IOperational{

	public IRI iri();

    public void addUsesExhaust_air_damper_percentage_command (IExhaust_air_damper_percentage_command parameter);

	public Set<IExhaust_air_damper_percentage_command> getUsesExhaust_air_damper_percentage_command();

    public void addUsesExhaust_air_static_pressure_sensor (IExhaust_air_static_pressure_sensor parameter);

	public Set<IExhaust_air_static_pressure_sensor> getUsesExhaust_air_static_pressure_sensor();

    public void addUsesExhaust_air_static_pressure_setpoint (IExhaust_air_static_pressure_setpoint parameter);

	public Set<IExhaust_air_static_pressure_setpoint> getUsesExhaust_air_static_pressure_setpoint();

    public void addUsesExhaust_fan_run_command (IExhaust_fan_run_command parameter);

	public Set<IExhaust_fan_run_command> getUsesExhaust_fan_run_command();

    public void addUsesExhaust_fan_run_status (IExhaust_fan_run_status parameter);

	public Set<IExhaust_fan_run_status> getUsesExhaust_fan_run_status();

    public void addUsesExhaust_fan_speed_percentage_command (IExhaust_fan_speed_percentage_command parameter);

	public Set<IExhaust_fan_speed_percentage_command> getUsesExhaust_fan_speed_percentage_command();

}