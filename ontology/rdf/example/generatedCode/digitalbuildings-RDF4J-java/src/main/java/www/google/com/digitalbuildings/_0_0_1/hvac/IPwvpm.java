package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_water_valve_percentage_command;
/**
* Class Pwvpm 
* Process water valve percentage monitoring.
*/
public interface IPwvpm extends IFunctionality, IMonitoring{

	public IRI iri();

    public void addUsesProcess_water_valve_percentage_command (IProcess_water_valve_percentage_command parameter);

	public Set<IProcess_water_valve_percentage_command> getUsesProcess_water_valve_percentage_command();

}