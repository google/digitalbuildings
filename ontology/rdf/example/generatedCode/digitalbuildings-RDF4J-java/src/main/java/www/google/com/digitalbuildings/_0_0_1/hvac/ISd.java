package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IControl;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICooling_thermal_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IRun_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_flowrate_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_ventilation_flowrate_requirement;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_cooling_flowrate_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_heating_flowrate_capacity;
/**
* Class Sd 
* Single duct VAV type, with basic airflow control.
*/
public interface ISd extends IFunctionality, IControl{

	public IRI iri();

    public void addUsesSupply_air_damper_percentage_command (ISupply_air_damper_percentage_command parameter);

	public Set<ISupply_air_damper_percentage_command> getUsesSupply_air_damper_percentage_command();

    public void addUsesSupply_air_flowrate_sensor (ISupply_air_flowrate_sensor parameter);

	public Set<ISupply_air_flowrate_sensor> getUsesSupply_air_flowrate_sensor();

    public void addUsesSupply_air_flowrate_setpoint (ISupply_air_flowrate_setpoint parameter);

	public Set<ISupply_air_flowrate_setpoint> getUsesSupply_air_flowrate_setpoint();

    public void addUsesOptionalsCooling_thermal_power_capacity (ICooling_thermal_power_capacity parameter);

	public Set<ICooling_thermal_power_capacity> getUsesOptionalsCooling_thermal_power_capacity();

    public void addUsesOptionalsRun_command (IRun_command parameter);

	public Set<IRun_command> getUsesOptionalsRun_command();

    public void addUsesOptionalsSupply_air_cooling_flowrate_capacity (ISupply_air_cooling_flowrate_capacity parameter);

	public Set<ISupply_air_cooling_flowrate_capacity> getUsesOptionalsSupply_air_cooling_flowrate_capacity();

    public void addUsesOptionalsSupply_air_heating_flowrate_capacity (ISupply_air_heating_flowrate_capacity parameter);

	public Set<ISupply_air_heating_flowrate_capacity> getUsesOptionalsSupply_air_heating_flowrate_capacity();

    public void addUsesOptionalsSupply_air_temperature_sensor (ISupply_air_temperature_sensor parameter);

	public Set<ISupply_air_temperature_sensor> getUsesOptionalsSupply_air_temperature_sensor();

    public void addUsesOptionalsSupply_air_ventilation_flowrate_requirement (ISupply_air_ventilation_flowrate_requirement parameter);

	public Set<ISupply_air_ventilation_flowrate_requirement> getUsesOptionalsSupply_air_ventilation_flowrate_requirement();

}