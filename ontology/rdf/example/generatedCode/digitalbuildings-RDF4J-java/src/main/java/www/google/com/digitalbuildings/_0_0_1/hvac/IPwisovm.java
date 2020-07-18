package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_water_isolation_valve_command;
/**
* Class Pwisovm 
* Process water iso valve monitoring.
*/
public interface IPwisovm extends IFunctionality, IMonitoring{

	public IRI iri();

    public void addUsesProcess_water_isolation_valve_command (IProcess_water_isolation_valve_command parameter);

	public Set<IProcess_water_isolation_valve_command> getUsesProcess_water_isolation_valve_command();

}