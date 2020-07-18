package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.fields.ICondensing_return_water_isolation_valve_status;
import www.google.com.digitalbuildings._0_0_1.fields.ICondensing_return_water_isolation_valve_command;
/**
* Class Cwrisovm 
* Condensing water return isolation monitoring.
*/
public interface ICwrisovm extends IFunctionality, IMonitoring{

	public IRI iri();

    public void addUsesCondensing_return_water_isolation_valve_command (ICondensing_return_water_isolation_valve_command parameter);

	public Set<ICondensing_return_water_isolation_valve_command> getUsesCondensing_return_water_isolation_valve_command();

    public void addUsesCondensing_return_water_isolation_valve_status (ICondensing_return_water_isolation_valve_status parameter);

	public Set<ICondensing_return_water_isolation_valve_status> getUsesCondensing_return_water_isolation_valve_status();

}