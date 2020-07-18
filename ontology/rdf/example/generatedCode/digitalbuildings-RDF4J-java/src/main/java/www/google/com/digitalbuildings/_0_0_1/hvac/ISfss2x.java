package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_run_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_run_status_2;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_run_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_run_status_1;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_power_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_power_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_current_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_flowrate_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_current_sensor_2;
/**
* Class Sfss2x 
* Supply fan start-stop and feedback for two fans.
*/
public interface ISfss2x extends IFunctionality, IOperational{

	public IRI iri();

    public void addUsesSupply_fan_run_command_1 (ISupply_fan_run_command_1 parameter);

	public Set<ISupply_fan_run_command_1> getUsesSupply_fan_run_command_1();

    public void addUsesSupply_fan_run_command_2 (ISupply_fan_run_command_2 parameter);

	public Set<ISupply_fan_run_command_2> getUsesSupply_fan_run_command_2();

    public void addUsesSupply_fan_run_status_1 (ISupply_fan_run_status_1 parameter);

	public Set<ISupply_fan_run_status_1> getUsesSupply_fan_run_status_1();

    public void addUsesSupply_fan_run_status_2 (ISupply_fan_run_status_2 parameter);

	public Set<ISupply_fan_run_status_2> getUsesSupply_fan_run_status_2();

    public void addUsesOptionalsSupply_air_flowrate_capacity (ISupply_air_flowrate_capacity parameter);

	public Set<ISupply_air_flowrate_capacity> getUsesOptionalsSupply_air_flowrate_capacity();

    public void addUsesOptionalsSupply_fan_current_sensor_1 (ISupply_fan_current_sensor_1 parameter);

	public Set<ISupply_fan_current_sensor_1> getUsesOptionalsSupply_fan_current_sensor_1();

    public void addUsesOptionalsSupply_fan_current_sensor_2 (ISupply_fan_current_sensor_2 parameter);

	public Set<ISupply_fan_current_sensor_2> getUsesOptionalsSupply_fan_current_sensor_2();

    public void addUsesOptionalsSupply_fan_power_capacity (ISupply_fan_power_capacity parameter);

	public Set<ISupply_fan_power_capacity> getUsesOptionalsSupply_fan_power_capacity();

    public void addUsesOptionalsSupply_fan_power_sensor_1 (ISupply_fan_power_sensor_1 parameter);

	public Set<ISupply_fan_power_sensor_1> getUsesOptionalsSupply_fan_power_sensor_1();

    public void addUsesOptionalsSupply_fan_power_sensor_2 (ISupply_fan_power_sensor_2 parameter);

	public Set<ISupply_fan_power_sensor_2> getUsesOptionalsSupply_fan_power_sensor_2();

}