package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.IRemap_required;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.ILow_discharge_fan_speed_command;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.IHigh_discharge_fan_speed_command;
/**
* Class Dfhlc 
* Discharge fan three-speed (high/low/off) speed control.
*/
public interface IDfhlc extends IFunctionality, IOperational, IRemap_required{

	public IRI iri();

    public void addUsesHigh_discharge_fan_speed_command (IHigh_discharge_fan_speed_command parameter);

	public Set<IHigh_discharge_fan_speed_command> getUsesHigh_discharge_fan_speed_command();

    public void addUsesLow_discharge_fan_speed_command (ILow_discharge_fan_speed_command parameter);

	public Set<ILow_discharge_fan_speed_command> getUsesLow_discharge_fan_speed_command();

    public void addUsesOptionalsDischarge_fan_run_command (IDischarge_fan_run_command parameter);

	public Set<IDischarge_fan_run_command> getUsesOptionalsDischarge_fan_run_command();

    public void addUsesOptionalsDischarge_fan_run_status (IDischarge_fan_run_status parameter);

	public Set<IDischarge_fan_run_status> getUsesOptionalsDischarge_fan_run_status();

}