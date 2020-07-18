package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.fields.IFlowrate_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IFlowrate_sensor;
/**
* Class Wfrc 
* Water flowrate control.
*/
public interface IWfrc extends IFunctionality, IOperational{

	public IRI iri();

    public void addUsesFlowrate_sensor (IFlowrate_sensor parameter);

	public Set<IFlowrate_sensor> getUsesFlowrate_sensor();

    public void addUsesFlowrate_setpoint (IFlowrate_setpoint parameter);

	public Set<IFlowrate_setpoint> getUsesFlowrate_setpoint();

}