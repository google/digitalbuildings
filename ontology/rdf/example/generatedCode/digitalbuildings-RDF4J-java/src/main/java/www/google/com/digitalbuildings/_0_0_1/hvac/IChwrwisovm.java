package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_return_water_isolation_valve_status;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_return_water_isolation_valve_command;
/**
* Class Chwrwisovm 
* Return side isolation valve monitoring.
*/
public interface IChwrwisovm extends IFunctionality, IMonitoring{

	public IRI iri();

    public void addUsesChilled_return_water_isolation_valve_command (IChilled_return_water_isolation_valve_command parameter);

	public Set<IChilled_return_water_isolation_valve_command> getUsesChilled_return_water_isolation_valve_command();

    public void addUsesChilled_return_water_isolation_valve_status (IChilled_return_water_isolation_valve_status parameter);

	public Set<IChilled_return_water_isolation_valve_status> getUsesChilled_return_water_isolation_valve_status();

}