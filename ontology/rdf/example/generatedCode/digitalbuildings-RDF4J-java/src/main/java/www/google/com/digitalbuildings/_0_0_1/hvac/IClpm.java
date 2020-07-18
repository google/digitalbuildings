package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_cooling_thermal_power_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICooling_thermal_power_sensor;
/**
* Class Clpm 
* Cooling thermal monitoring.
*/
public interface IClpm extends IFunctionality, IMonitoring{

	public IRI iri();

    public void addUsesCooling_thermal_power_sensor (ICooling_thermal_power_sensor parameter);

	public Set<ICooling_thermal_power_sensor> getUsesCooling_thermal_power_sensor();

    public void addUsesProcess_cooling_thermal_power_sensor (IProcess_cooling_thermal_power_sensor parameter);

	public Set<IProcess_cooling_thermal_power_sensor> getUsesProcess_cooling_thermal_power_sensor();

}