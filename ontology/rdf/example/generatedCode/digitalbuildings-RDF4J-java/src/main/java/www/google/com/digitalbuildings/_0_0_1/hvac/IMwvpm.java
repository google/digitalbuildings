package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IMakeup_water_valve_percentage_command;
/**
* Class Mwvpm 
* Make-up water valve percentage monitoring.
*/
public interface IMwvpm extends IFunctionality, IMonitoring{

	public IRI iri();

    public void addUsesMakeup_water_valve_percentage_command (IMakeup_water_valve_percentage_command parameter);

	public Set<IMakeup_water_valve_percentage_command> getUsesMakeup_water_valve_percentage_command();

}