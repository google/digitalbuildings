package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IMixing_valve_percentage_command;
/**
* Class Mxvpm 
* Mixing valve percent monitoring.
*/
public interface IMxvpm extends IFunctionality, IMonitoring{

	public IRI iri();

    public void addUsesMixing_valve_percentage_command (IMixing_valve_percentage_command parameter);

	public Set<IMixing_valve_percentage_command> getUsesMixing_valve_percentage_command();

}