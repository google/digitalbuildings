package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IControl;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_flowrate_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_damper_percentage_command;
/**
* Class Ed 
* Exhaust air flow control.
*/
public interface IEd extends IFunctionality, IControl{

	public IRI iri();

    public void addUsesExhaust_air_damper_percentage_command (IExhaust_air_damper_percentage_command parameter);

	public Set<IExhaust_air_damper_percentage_command> getUsesExhaust_air_damper_percentage_command();

    public void addUsesExhaust_air_flowrate_sensor (IExhaust_air_flowrate_sensor parameter);

	public Set<IExhaust_air_flowrate_sensor> getUsesExhaust_air_flowrate_sensor();

    public void addUsesExhaust_air_flowrate_setpoint (IExhaust_air_flowrate_setpoint parameter);

	public Set<IExhaust_air_flowrate_setpoint> getUsesExhaust_air_flowrate_setpoint();

}