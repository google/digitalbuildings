package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IRun_command;
import www.google.com.digitalbuildings._0_0_1.fields.ICondensing_water_isolation_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ICondensing_water_isolation_valve_percentage_sensor;
/**
* Class Cdwisovpm 
* Condensing water isolation valve percentage monitoring.
*/
public interface ICdwisovpm extends IFunctionality, IMonitoring{

	public IRI iri();

    public void addUsesOptionalsRun_command (IRun_command parameter);

	public Set<IRun_command> getUsesOptionalsRun_command();

    public void addUsesCondensing_water_isolation_valve_percentage_command (ICondensing_water_isolation_valve_percentage_command parameter);

	public Set<ICondensing_water_isolation_valve_percentage_command> getUsesCondensing_water_isolation_valve_percentage_command();

    public void addUsesCondensing_water_isolation_valve_percentage_sensor (ICondensing_water_isolation_valve_percentage_sensor parameter);

	public Set<ICondensing_water_isolation_valve_percentage_sensor> getUsesCondensing_water_isolation_valve_percentage_sensor();

}