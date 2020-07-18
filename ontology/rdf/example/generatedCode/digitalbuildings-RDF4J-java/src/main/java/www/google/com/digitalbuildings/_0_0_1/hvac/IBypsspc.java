package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IControl;
import www.google.com.digitalbuildings._0_0_1.fields.IBypass_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_static_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_run_command;
/**
* Class Bypsspc 
* Supply static pressure control with bypass damper.
*/
public interface IBypsspc extends IFunctionality, IControl{

	public IRI iri();

    public void addUsesOptionalsSupply_air_flowrate_sensor (ISupply_air_flowrate_sensor parameter);

	public Set<ISupply_air_flowrate_sensor> getUsesOptionalsSupply_air_flowrate_sensor();

    public void addUsesBypass_air_damper_percentage_command (IBypass_air_damper_percentage_command parameter);

	public Set<IBypass_air_damper_percentage_command> getUsesBypass_air_damper_percentage_command();

    public void addUsesSupply_air_static_pressure_sensor (ISupply_air_static_pressure_sensor parameter);

	public Set<ISupply_air_static_pressure_sensor> getUsesSupply_air_static_pressure_sensor();

    public void addUsesSupply_air_static_pressure_setpoint (ISupply_air_static_pressure_setpoint parameter);

	public Set<ISupply_air_static_pressure_setpoint> getUsesSupply_air_static_pressure_setpoint();

    public void addUsesSupply_fan_run_command (ISupply_fan_run_command parameter);

	public Set<ISupply_fan_run_command> getUsesSupply_fan_run_command();

    public void addUsesSupply_fan_run_status (ISupply_fan_run_status parameter);

	public Set<ISupply_fan_run_status> getUsesSupply_fan_run_status();

}