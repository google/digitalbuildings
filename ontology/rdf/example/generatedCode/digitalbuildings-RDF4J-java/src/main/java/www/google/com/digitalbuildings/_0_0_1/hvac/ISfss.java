package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_current_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_power_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_flowrate_capacity;
/**
* Class Sfss 
* Basic combination of supply fan run command and status (start/stop).
*/
public interface ISfss extends IFunctionality, IOperational{

	public IRI iri();

    public void addUsesSupply_fan_run_command (ISupply_fan_run_command parameter);

	public Set<ISupply_fan_run_command> getUsesSupply_fan_run_command();

    public void addUsesSupply_fan_run_status (ISupply_fan_run_status parameter);

	public Set<ISupply_fan_run_status> getUsesSupply_fan_run_status();

    public void addUsesOptionalsSupply_air_flowrate_capacity (ISupply_air_flowrate_capacity parameter);

	public Set<ISupply_air_flowrate_capacity> getUsesOptionalsSupply_air_flowrate_capacity();

    public void addUsesOptionalsSupply_fan_current_sensor (ISupply_fan_current_sensor parameter);

	public Set<ISupply_fan_current_sensor> getUsesOptionalsSupply_fan_current_sensor();

    public void addUsesOptionalsSupply_fan_power_capacity (ISupply_fan_power_capacity parameter);

	public Set<ISupply_fan_power_capacity> getUsesOptionalsSupply_fan_power_capacity();

    public void addUsesOptionalsSupply_fan_power_sensor (ISupply_fan_power_sensor parameter);

	public Set<ISupply_fan_power_sensor> getUsesOptionalsSupply_fan_power_sensor();

}