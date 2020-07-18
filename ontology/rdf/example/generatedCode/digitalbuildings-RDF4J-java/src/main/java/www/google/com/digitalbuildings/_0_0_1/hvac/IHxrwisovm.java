package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IHeat_exchange_return_water_isolation_valve_status;
import www.google.com.digitalbuildings._0_0_1.fields.IHeat_exchange_return_water_isolation_valve_command;
/**
* Class Hxrwisovm 
* Heat exchanger return isolation water valve monitoring.
*/
public interface IHxrwisovm extends IFunctionality, IMonitoring{

	public IRI iri();

    public void addUsesHeat_exchange_return_water_isolation_valve_command (IHeat_exchange_return_water_isolation_valve_command parameter);

	public Set<IHeat_exchange_return_water_isolation_valve_command> getUsesHeat_exchange_return_water_isolation_valve_command();

    public void addUsesHeat_exchange_return_water_isolation_valve_status (IHeat_exchange_return_water_isolation_valve_status parameter);

	public Set<IHeat_exchange_return_water_isolation_valve_status> getUsesHeat_exchange_return_water_isolation_valve_status();

}