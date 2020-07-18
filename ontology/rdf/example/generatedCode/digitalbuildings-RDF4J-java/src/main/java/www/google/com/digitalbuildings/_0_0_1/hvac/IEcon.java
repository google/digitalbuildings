package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IControl;
import www.google.com.digitalbuildings._0_0_1.fields.IEconomizer_mode;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IMixed_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_flowrate_setpoint;
/**
* Class Econ 
* Economizer mode control
*/
public interface IEcon extends IFunctionality, IControl{

	public IRI iri();

    public void addUsesOptionalsOutside_air_flowrate_sensor (IOutside_air_flowrate_sensor parameter);

	public Set<IOutside_air_flowrate_sensor> getUsesOptionalsOutside_air_flowrate_sensor();

    public void addUsesOptionalsOutside_air_flowrate_setpoint (IOutside_air_flowrate_setpoint parameter);

	public Set<IOutside_air_flowrate_setpoint> getUsesOptionalsOutside_air_flowrate_setpoint();

    public void addUsesOptionalsSupply_air_temperature_sensor (ISupply_air_temperature_sensor parameter);

	public Set<ISupply_air_temperature_sensor> getUsesOptionalsSupply_air_temperature_sensor();

    public void addUsesEconomizer_mode (IEconomizer_mode parameter);

	public Set<IEconomizer_mode> getUsesEconomizer_mode();

    public void addUsesMixed_air_temperature_sensor (IMixed_air_temperature_sensor parameter);

	public Set<IMixed_air_temperature_sensor> getUsesMixed_air_temperature_sensor();

    public void addUsesOutside_air_damper_percentage_command (IOutside_air_damper_percentage_command parameter);

	public Set<IOutside_air_damper_percentage_command> getUsesOutside_air_damper_percentage_command();

    public void addUsesOutside_air_temperature_sensor (IOutside_air_temperature_sensor parameter);

	public Set<IOutside_air_temperature_sensor> getUsesOutside_air_temperature_sensor();

    public void addUsesReturn_air_temperature_sensor (IReturn_air_temperature_sensor parameter);

	public Set<IReturn_air_temperature_sensor> getUsesReturn_air_temperature_sensor();

    public void addUsesSupply_air_temperature_setpoint (ISupply_air_temperature_setpoint parameter);

	public Set<ISupply_air_temperature_setpoint> getUsesSupply_air_temperature_setpoint();

}