package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_cooling_thermal_power_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_supply_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_return_water_temperature_sensor;
/**
* Class Prwdt 
* Temperature differential across process water.
*/
public interface IPrwdt extends IFunctionality, IMonitoring{

	public IRI iri();

    public void addUsesOptionalsProcess_cooling_thermal_power_sensor (IProcess_cooling_thermal_power_sensor parameter);

	public Set<IProcess_cooling_thermal_power_sensor> getUsesOptionalsProcess_cooling_thermal_power_sensor();

    public void addUsesProcess_return_water_temperature_sensor (IProcess_return_water_temperature_sensor parameter);

	public Set<IProcess_return_water_temperature_sensor> getUsesProcess_return_water_temperature_sensor();

    public void addUsesProcess_supply_water_temperature_sensor (IProcess_supply_water_temperature_sensor parameter);

	public Set<IProcess_supply_water_temperature_sensor> getUsesProcess_supply_water_temperature_sensor();

}