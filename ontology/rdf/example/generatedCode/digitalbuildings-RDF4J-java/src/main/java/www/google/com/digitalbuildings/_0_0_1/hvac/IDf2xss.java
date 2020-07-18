package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_run_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_run_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_run_status_2;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_run_status_1;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_current_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_power_sensor;
/**
* Class Df2xss 
* Discharge fan start-stop and feedback (2 pts).
*/
public interface IDf2xss extends IFunctionality, IOperational{

	public IRI iri();

    public void addUsesDischarge_fan_run_command_1 (IDischarge_fan_run_command_1 parameter);

	public Set<IDischarge_fan_run_command_1> getUsesDischarge_fan_run_command_1();

    public void addUsesDischarge_fan_run_command_2 (IDischarge_fan_run_command_2 parameter);

	public Set<IDischarge_fan_run_command_2> getUsesDischarge_fan_run_command_2();

    public void addUsesDischarge_fan_run_status_1 (IDischarge_fan_run_status_1 parameter);

	public Set<IDischarge_fan_run_status_1> getUsesDischarge_fan_run_status_1();

    public void addUsesDischarge_fan_run_status_2 (IDischarge_fan_run_status_2 parameter);

	public Set<IDischarge_fan_run_status_2> getUsesDischarge_fan_run_status_2();

    public void addUsesOptionalsDischarge_fan_current_sensor (IDischarge_fan_current_sensor parameter);

	public Set<IDischarge_fan_current_sensor> getUsesOptionalsDischarge_fan_current_sensor();

    public void addUsesOptionalsDischarge_fan_power_sensor (IDischarge_fan_power_sensor parameter);

	public Set<IDischarge_fan_power_sensor> getUsesOptionalsDischarge_fan_power_sensor();

}