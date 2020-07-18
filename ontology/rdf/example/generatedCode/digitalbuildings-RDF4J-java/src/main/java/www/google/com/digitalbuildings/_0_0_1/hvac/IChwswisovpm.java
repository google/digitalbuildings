package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_supply_water_isolation_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_supply_water_isolation_valve_percentage_command;
/**
* Class Chwswisovpm 
* Supply side isolation valve monitoring.
*/
public interface IChwswisovpm extends IFunctionality, IMonitoring{

	public IRI iri();

    public void addUsesChilled_supply_water_isolation_valve_percentage_command (IChilled_supply_water_isolation_valve_percentage_command parameter);

	public Set<IChilled_supply_water_isolation_valve_percentage_command> getUsesChilled_supply_water_isolation_valve_percentage_command();

    public void addUsesChilled_supply_water_isolation_valve_percentage_sensor (IChilled_supply_water_isolation_valve_percentage_sensor parameter);

	public Set<IChilled_supply_water_isolation_valve_percentage_sensor> getUsesChilled_supply_water_isolation_valve_percentage_sensor();

}