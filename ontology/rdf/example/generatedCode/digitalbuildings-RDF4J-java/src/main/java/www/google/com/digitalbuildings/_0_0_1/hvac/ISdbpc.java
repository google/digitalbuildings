package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_static_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_damper_percentage_sensor;
/**
* Class Sdbpc 
* Back-pressure controlling supply damper.
*/
public interface ISdbpc extends IFunctionality, IMonitoring{

	public IRI iri();

    public void addUsesOptionalsSupply_air_flowrate_sensor (ISupply_air_flowrate_sensor parameter);

	public Set<ISupply_air_flowrate_sensor> getUsesOptionalsSupply_air_flowrate_sensor();

    public void addUsesSupply_air_damper_percentage_command (ISupply_air_damper_percentage_command parameter);

	public Set<ISupply_air_damper_percentage_command> getUsesSupply_air_damper_percentage_command();

    public void addUsesSupply_air_damper_percentage_sensor (ISupply_air_damper_percentage_sensor parameter);

	public Set<ISupply_air_damper_percentage_sensor> getUsesSupply_air_damper_percentage_sensor();

    public void addUsesSupply_air_static_pressure_sensor (ISupply_air_static_pressure_sensor parameter);

	public Set<ISupply_air_static_pressure_sensor> getUsesSupply_air_static_pressure_sensor();

    public void addUsesSupply_air_static_pressure_setpoint (ISupply_air_static_pressure_setpoint parameter);

	public Set<ISupply_air_static_pressure_setpoint> getUsesSupply_air_static_pressure_setpoint();

}