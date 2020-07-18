package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IControl;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ICooling_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_thermal_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_heating_flowrate_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_air_flowrate_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICooling_thermal_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.ICooling_air_flowrate_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IRun_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_ventilation_flowrate_requirement;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_cooling_flowrate_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICooling_air_damper_percentage_command;
/**
* Class Dd 
* Dual duct flow control (hot deck, cold deck).
*/
public interface IDd extends IFunctionality, IControl{

	public IRI iri();

    public void addUsesCooling_air_damper_percentage_command (ICooling_air_damper_percentage_command parameter);

	public Set<ICooling_air_damper_percentage_command> getUsesCooling_air_damper_percentage_command();

    public void addUsesCooling_air_flowrate_sensor (ICooling_air_flowrate_sensor parameter);

	public Set<ICooling_air_flowrate_sensor> getUsesCooling_air_flowrate_sensor();

    public void addUsesCooling_air_flowrate_setpoint (ICooling_air_flowrate_setpoint parameter);

	public Set<ICooling_air_flowrate_setpoint> getUsesCooling_air_flowrate_setpoint();

    public void addUsesHeating_air_damper_percentage_command (IHeating_air_damper_percentage_command parameter);

	public Set<IHeating_air_damper_percentage_command> getUsesHeating_air_damper_percentage_command();

    public void addUsesHeating_air_flowrate_sensor (IHeating_air_flowrate_sensor parameter);

	public Set<IHeating_air_flowrate_sensor> getUsesHeating_air_flowrate_sensor();

    public void addUsesHeating_air_flowrate_setpoint (IHeating_air_flowrate_setpoint parameter);

	public Set<IHeating_air_flowrate_setpoint> getUsesHeating_air_flowrate_setpoint();

    public void addUsesOptionalsCooling_thermal_power_capacity (ICooling_thermal_power_capacity parameter);

	public Set<ICooling_thermal_power_capacity> getUsesOptionalsCooling_thermal_power_capacity();

    public void addUsesOptionalsDischarge_air_temperature_sensor (IDischarge_air_temperature_sensor parameter);

	public Set<IDischarge_air_temperature_sensor> getUsesOptionalsDischarge_air_temperature_sensor();

    public void addUsesOptionalsHeating_thermal_power_capacity (IHeating_thermal_power_capacity parameter);

	public Set<IHeating_thermal_power_capacity> getUsesOptionalsHeating_thermal_power_capacity();

    public void addUsesOptionalsRun_command (IRun_command parameter);

	public Set<IRun_command> getUsesOptionalsRun_command();

    public void addUsesOptionalsSupply_air_cooling_flowrate_capacity (ISupply_air_cooling_flowrate_capacity parameter);

	public Set<ISupply_air_cooling_flowrate_capacity> getUsesOptionalsSupply_air_cooling_flowrate_capacity();

    public void addUsesOptionalsSupply_air_heating_flowrate_capacity (ISupply_air_heating_flowrate_capacity parameter);

	public Set<ISupply_air_heating_flowrate_capacity> getUsesOptionalsSupply_air_heating_flowrate_capacity();

    public void addUsesOptionalsSupply_air_ventilation_flowrate_requirement (ISupply_air_ventilation_flowrate_requirement parameter);

	public Set<ISupply_air_ventilation_flowrate_requirement> getUsesOptionalsSupply_air_ventilation_flowrate_requirement();

}