package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_speed_mode;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_run_status;
/**
* Class Dfmsc 
* Discharge fan multi-speed control.
*/
public interface IDfmsc extends IFunctionality{

	public IRI iri();

    public void addUsesDischarge_fan_run_command (IDischarge_fan_run_command parameter);

	public Set<IDischarge_fan_run_command> getUsesDischarge_fan_run_command();

    public void addUsesDischarge_fan_run_status (IDischarge_fan_run_status parameter);

	public Set<IDischarge_fan_run_status> getUsesDischarge_fan_run_status();

    public void addUsesDischarge_fan_speed_mode (IDischarge_fan_speed_mode parameter);

	public Set<IDischarge_fan_speed_mode> getUsesDischarge_fan_speed_mode();

}