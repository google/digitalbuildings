package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IBypass_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IBypass_valve_percentage_sensor;
/**
* Class Bypvpm 
* Bypass water valve percentage monitoring.
*/
public interface IBypvpm extends IFunctionality, IMonitoring{

	public IRI iri();

    public void addUsesOptionalsBypass_valve_percentage_sensor (IBypass_valve_percentage_sensor parameter);

	public Set<IBypass_valve_percentage_sensor> getUsesOptionalsBypass_valve_percentage_sensor();

    public void addUsesBypass_valve_percentage_command (IBypass_valve_percentage_command parameter);

	public Set<IBypass_valve_percentage_command> getUsesBypass_valve_percentage_command();

}