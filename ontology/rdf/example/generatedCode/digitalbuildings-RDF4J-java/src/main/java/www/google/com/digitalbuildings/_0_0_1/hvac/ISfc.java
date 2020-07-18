package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_flowrate_setpoint;
/**
* Class Sfc 
* Supply air flow control.
*/
public interface ISfc extends IFunctionality, IOperational{

	public IRI iri();

    public void addUsesSupply_air_flowrate_sensor (ISupply_air_flowrate_sensor parameter);

	public Set<ISupply_air_flowrate_sensor> getUsesSupply_air_flowrate_sensor();

    public void addUsesSupply_air_flowrate_setpoint (ISupply_air_flowrate_setpoint parameter);

	public Set<ISupply_air_flowrate_setpoint> getUsesSupply_air_flowrate_setpoint();

}