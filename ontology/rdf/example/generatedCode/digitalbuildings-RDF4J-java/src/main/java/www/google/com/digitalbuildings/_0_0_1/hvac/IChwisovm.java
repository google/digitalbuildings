package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_water_isolation_valve_status;
import www.google.com.digitalbuildings._0_0_1.fields.IRun_command;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_water_isolation_valve_command;
/**
* Class Chwisovm 
* Chilled water isolation valve monitoring.
*/
public interface IChwisovm extends IFunctionality, IMonitoring{

	public IRI iri();

    public void addUsesOptionalsRun_command (IRun_command parameter);

	public Set<IRun_command> getUsesOptionalsRun_command();

    public void addUsesChilled_water_isolation_valve_command (IChilled_water_isolation_valve_command parameter);

	public Set<IChilled_water_isolation_valve_command> getUsesChilled_water_isolation_valve_command();

    public void addUsesChilled_water_isolation_valve_status (IChilled_water_isolation_valve_status parameter);

	public Set<IChilled_water_isolation_valve_status> getUsesChilled_water_isolation_valve_status();

}