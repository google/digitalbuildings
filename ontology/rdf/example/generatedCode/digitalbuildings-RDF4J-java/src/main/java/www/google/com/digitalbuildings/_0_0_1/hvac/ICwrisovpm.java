package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.fields.ICondensing_return_water_isolation_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ICondensing_return_water_isolation_valve_percentage_sensor;
/**
* Class Cwrisovpm 
* Condensing water return isolation monitoring.
*/
public interface ICwrisovpm extends IFunctionality, IMonitoring{

	public IRI iri();

    public void addUsesCondensing_return_water_isolation_valve_percentage_command (ICondensing_return_water_isolation_valve_percentage_command parameter);

	public Set<ICondensing_return_water_isolation_valve_percentage_command> getUsesCondensing_return_water_isolation_valve_percentage_command();

    public void addUsesCondensing_return_water_isolation_valve_percentage_sensor (ICondensing_return_water_isolation_valve_percentage_sensor parameter);

	public Set<ICondensing_return_water_isolation_valve_percentage_sensor> getUsesCondensing_return_water_isolation_valve_percentage_sensor();

}