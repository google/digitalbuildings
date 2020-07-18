package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IHeat_exchange_return_water_isolation_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IHeat_exchange_return_water_isolation_valve_percentage_sensor;
/**
* Class Hxrwisovpm 
* Heat exchanger return isolation water valve percentage monitoring.
*/
public interface IHxrwisovpm extends IFunctionality, IMonitoring{

	public IRI iri();

    public void addUsesHeat_exchange_return_water_isolation_valve_percentage_command (IHeat_exchange_return_water_isolation_valve_percentage_command parameter);

	public Set<IHeat_exchange_return_water_isolation_valve_percentage_command> getUsesHeat_exchange_return_water_isolation_valve_percentage_command();

    public void addUsesHeat_exchange_return_water_isolation_valve_percentage_sensor (IHeat_exchange_return_water_isolation_valve_percentage_sensor parameter);

	public Set<IHeat_exchange_return_water_isolation_valve_percentage_sensor> getUsesHeat_exchange_return_water_isolation_valve_percentage_sensor();

}