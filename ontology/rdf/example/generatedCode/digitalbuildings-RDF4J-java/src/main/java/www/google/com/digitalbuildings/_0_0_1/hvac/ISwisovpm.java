package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_isolation_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_isolation_valve_percentage_sensor;
/**
* Class Swisovpm 
* Supply side isolation valve monitoring.
*/
public interface ISwisovpm extends IFunctionality, IMonitoring{

	public IRI iri();

    public void addUsesSupply_water_isolation_valve_percentage_command (ISupply_water_isolation_valve_percentage_command parameter);

	public Set<ISupply_water_isolation_valve_percentage_command> getUsesSupply_water_isolation_valve_percentage_command();

    public void addUsesSupply_water_isolation_valve_percentage_sensor (ISupply_water_isolation_valve_percentage_sensor parameter);

	public Set<ISupply_water_isolation_valve_percentage_sensor> getUsesSupply_water_isolation_valve_percentage_sensor();

}