package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.fields.ICondensing_water_isolation_valve_command;
import www.google.com.digitalbuildings._0_0_1.fields.ICondensing_water_isolation_valve_status;
import www.google.com.digitalbuildings._0_0_1.fields.IRun_command;
/**
* Class Cdwisovm 
* Condensing water isolation valve monitoring.
*/
public interface ICdwisovm extends IFunctionality, IMonitoring{

	public IRI iri();

    public void addUsesOptionalsRun_command (IRun_command parameter);

	public Set<IRun_command> getUsesOptionalsRun_command();

    public void addUsesCondensing_water_isolation_valve_command (ICondensing_water_isolation_valve_command parameter);

	public Set<ICondensing_water_isolation_valve_command> getUsesCondensing_water_isolation_valve_command();

    public void addUsesCondensing_water_isolation_valve_status (ICondensing_water_isolation_valve_status parameter);

	public Set<ICondensing_water_isolation_valve_status> getUsesCondensing_water_isolation_valve_status();

}