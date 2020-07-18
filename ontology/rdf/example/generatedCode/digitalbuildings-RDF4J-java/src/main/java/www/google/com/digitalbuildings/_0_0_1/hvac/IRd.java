package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IControl;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_air_flowrate_setpoint;
/**
* Class Rd 
* Return damper flow control.
*/
public interface IRd extends IFunctionality, IControl{

	public IRI iri();

    public void addUsesReturn_air_damper_percentage_command (IReturn_air_damper_percentage_command parameter);

	public Set<IReturn_air_damper_percentage_command> getUsesReturn_air_damper_percentage_command();

    public void addUsesReturn_air_flowrate_sensor (IReturn_air_flowrate_sensor parameter);

	public Set<IReturn_air_flowrate_sensor> getUsesReturn_air_flowrate_sensor();

    public void addUsesReturn_air_flowrate_setpoint (IReturn_air_flowrate_setpoint parameter);

	public Set<IReturn_air_flowrate_setpoint> getUsesReturn_air_flowrate_setpoint();

}