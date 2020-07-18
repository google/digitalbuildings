package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_cooling_thermal_power_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_cooling_thermal_power_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_supply_water_temperature_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_supply_water_temperature_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_return_water_temperature_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_return_water_temperature_sensor_2;
/**
* Class Prwdt2x 
* Temperature differential across 2 process water headers.
*/
public interface IPrwdt2x extends IFunctionality, IMonitoring{

	public IRI iri();

    public void addUsesOptionalsProcess_cooling_thermal_power_sensor_1 (IProcess_cooling_thermal_power_sensor_1 parameter);

	public Set<IProcess_cooling_thermal_power_sensor_1> getUsesOptionalsProcess_cooling_thermal_power_sensor_1();

    public void addUsesOptionalsProcess_cooling_thermal_power_sensor_2 (IProcess_cooling_thermal_power_sensor_2 parameter);

	public Set<IProcess_cooling_thermal_power_sensor_2> getUsesOptionalsProcess_cooling_thermal_power_sensor_2();

    public void addUsesProcess_return_water_temperature_sensor_1 (IProcess_return_water_temperature_sensor_1 parameter);

	public Set<IProcess_return_water_temperature_sensor_1> getUsesProcess_return_water_temperature_sensor_1();

    public void addUsesProcess_return_water_temperature_sensor_2 (IProcess_return_water_temperature_sensor_2 parameter);

	public Set<IProcess_return_water_temperature_sensor_2> getUsesProcess_return_water_temperature_sensor_2();

    public void addUsesProcess_supply_water_temperature_sensor_1 (IProcess_supply_water_temperature_sensor_1 parameter);

	public Set<IProcess_supply_water_temperature_sensor_1> getUsesProcess_supply_water_temperature_sensor_1();

    public void addUsesProcess_supply_water_temperature_sensor_2 (IProcess_supply_water_temperature_sensor_2 parameter);

	public Set<IProcess_supply_water_temperature_sensor_2> getUsesProcess_supply_water_temperature_sensor_2();

}