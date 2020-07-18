package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IControl;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_water_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ILeaving_cooling_coil_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.ICooling_thermal_power_capacity;
/**
* Class Chwsc 
* Chilled water valve monitoring on supply side.
*/
public interface IChwsc extends IFunctionality, IControl{

	public IRI iri();

    public void addUsesOptionalsCooling_thermal_power_capacity (ICooling_thermal_power_capacity parameter);

	public Set<ICooling_thermal_power_capacity> getUsesOptionalsCooling_thermal_power_capacity();

    public void addUsesOptionalsLeaving_cooling_coil_temperature_sensor (ILeaving_cooling_coil_temperature_sensor parameter);

	public Set<ILeaving_cooling_coil_temperature_sensor> getUsesOptionalsLeaving_cooling_coil_temperature_sensor();

    public void addUsesChilled_water_valve_percentage_command (IChilled_water_valve_percentage_command parameter);

	public Set<IChilled_water_valve_percentage_command> getUsesChilled_water_valve_percentage_command();

    public void addUsesSupply_air_temperature_sensor (ISupply_air_temperature_sensor parameter);

	public Set<ISupply_air_temperature_sensor> getUsesSupply_air_temperature_sensor();

    public void addUsesSupply_air_temperature_setpoint (ISupply_air_temperature_setpoint parameter);

	public Set<ISupply_air_temperature_setpoint> getUsesSupply_air_temperature_setpoint();

}