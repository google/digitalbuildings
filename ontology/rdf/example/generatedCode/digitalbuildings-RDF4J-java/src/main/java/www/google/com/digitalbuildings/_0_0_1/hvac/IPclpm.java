package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_cooling_thermal_power_sensor;
/**
* Class Pclpm 
* Process cooling thermal monitoring.
*/
public interface IPclpm extends IFunctionality, IMonitoring{

	public IRI iri();

    public void addUsesProcess_cooling_thermal_power_sensor (IProcess_cooling_thermal_power_sensor parameter);

	public Set<IProcess_cooling_thermal_power_sensor> getUsesProcess_cooling_thermal_power_sensor();

}