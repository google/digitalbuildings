package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IControl;
import www.google.com.digitalbuildings._0_0_1.fields.IBypass_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IFlowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IMin_flowrate_setpoint;
/**
* Class Minfc 
* Minimum flow control for entire loop.
*/
public interface IMinfc extends IFunctionality, IControl{

	public IRI iri();

    public void addUsesBypass_valve_percentage_command (IBypass_valve_percentage_command parameter);

	public Set<IBypass_valve_percentage_command> getUsesBypass_valve_percentage_command();

    public void addUsesFlowrate_sensor (IFlowrate_sensor parameter);

	public Set<IFlowrate_sensor> getUsesFlowrate_sensor();

    public void addUsesMin_flowrate_setpoint (IMin_flowrate_setpoint parameter);

	public Set<IMin_flowrate_setpoint> getUsesMin_flowrate_setpoint();

}