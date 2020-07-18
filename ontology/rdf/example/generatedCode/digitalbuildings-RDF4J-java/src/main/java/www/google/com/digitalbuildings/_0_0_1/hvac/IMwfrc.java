package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.fields.IFlowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ILow_limit_flowrate_setpoint;
/**
* Class Mwfrc 
* Minimum water flowrate control.
*/
public interface IMwfrc extends IFunctionality, IOperational{

	public IRI iri();

    public void addUsesFlowrate_sensor (IFlowrate_sensor parameter);

	public Set<IFlowrate_sensor> getUsesFlowrate_sensor();

    public void addUsesLow_limit_flowrate_setpoint (ILow_limit_flowrate_setpoint parameter);

	public Set<ILow_limit_flowrate_setpoint> getUsesLow_limit_flowrate_setpoint();

}