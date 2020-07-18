package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_air_flowrate_setpoint;
/**
* Class Rfc 
* Return air flow control.
*/
public interface IRfc extends IFunctionality, IOperational{

	public IRI iri();

    public void addUsesReturn_air_flowrate_sensor (IReturn_air_flowrate_sensor parameter);

	public Set<IReturn_air_flowrate_sensor> getUsesReturn_air_flowrate_sensor();

    public void addUsesReturn_air_flowrate_setpoint (IReturn_air_flowrate_setpoint parameter);

	public Set<IReturn_air_flowrate_setpoint> getUsesReturn_air_flowrate_setpoint();

}