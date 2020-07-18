package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IControl;
import www.google.com.digitalbuildings._0_0_1.fields.IBuilding_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.IBuilding_air_static_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_command;
/**
* Class Bspc 
* Building static pressure control (as part of a composite device).
*/
public interface IBspc extends IFunctionality, IControl{

	public IRI iri();

    public void addUsesOptionalsExhaust_air_damper_percentage_command (IExhaust_air_damper_percentage_command parameter);

	public Set<IExhaust_air_damper_percentage_command> getUsesOptionalsExhaust_air_damper_percentage_command();

    public void addUsesOptionalsExhaust_fan_run_status (IExhaust_fan_run_status parameter);

	public Set<IExhaust_fan_run_status> getUsesOptionalsExhaust_fan_run_status();

    public void addUsesBuilding_air_static_pressure_sensor (IBuilding_air_static_pressure_sensor parameter);

	public Set<IBuilding_air_static_pressure_sensor> getUsesBuilding_air_static_pressure_sensor();

    public void addUsesBuilding_air_static_pressure_setpoint (IBuilding_air_static_pressure_setpoint parameter);

	public Set<IBuilding_air_static_pressure_setpoint> getUsesBuilding_air_static_pressure_setpoint();

    public void addUsesExhaust_fan_run_command (IExhaust_fan_run_command parameter);

	public Set<IExhaust_fan_run_command> getUsesExhaust_fan_run_command();

}