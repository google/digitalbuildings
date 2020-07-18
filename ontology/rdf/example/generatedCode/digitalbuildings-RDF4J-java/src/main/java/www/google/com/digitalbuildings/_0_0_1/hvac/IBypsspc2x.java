package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IControl;
import www.google.com.digitalbuildings._0_0_1.fields.IMixed_air_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IBypass_air_damper_percentage_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.IBypass_air_damper_percentage_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_run_status_2;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_run_status_1;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_water_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_flowrate_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.IVentilation_outside_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IBuilding_air_static_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IHeater_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_heating_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_cooling_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IBuilding_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_speed_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_status_4;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_status_3;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_command_4;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_command_3;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_status_2;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_status_1;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IPressurization_request_count;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_water_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_speed_percentage_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_speed_percentage_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.IHeater_run_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IMixed_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICooling_request_count;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_command_4;
import www.google.com.digitalbuildings._0_0_1.fields.IVentilation_outside_air_flowrate_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_flowrate_requirement;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.IHeater_run_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_command_3;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_command_4;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_command_3;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.IFilter_differential_pressure_sensor_4;
import www.google.com.digitalbuildings._0_0_1.fields.IFilter_differential_pressure_sensor_3;
import www.google.com.digitalbuildings._0_0_1.fields.IFilter_differential_pressure_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IFilter_differential_pressure_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_run_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.IEconomizer_mode;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_static_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_run_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.IVentilation_outside_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_status_4;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_speed_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_status_1;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_status_3;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_status_2;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_flowrate_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_run_command;
/**
* Class Bypsspc2x 
* Supply static pressure control with bypass damper.
*/
public interface IBypsspc2x extends IFunctionality, IControl{

	public IRI iri();

    public void addUsesBypass_air_damper_percentage_command_1 (IBypass_air_damper_percentage_command_1 parameter);

	public Set<IBypass_air_damper_percentage_command_1> getUsesBypass_air_damper_percentage_command_1();

    public void addUsesBypass_air_damper_percentage_command_2 (IBypass_air_damper_percentage_command_2 parameter);

	public Set<IBypass_air_damper_percentage_command_2> getUsesBypass_air_damper_percentage_command_2();

    public void addUsesSupply_air_static_pressure_sensor (ISupply_air_static_pressure_sensor parameter);

	public Set<ISupply_air_static_pressure_sensor> getUsesSupply_air_static_pressure_sensor();

    public void addUsesSupply_air_static_pressure_setpoint (ISupply_air_static_pressure_setpoint parameter);

	public Set<ISupply_air_static_pressure_setpoint> getUsesSupply_air_static_pressure_setpoint();

    public void addUsesSupply_fan_run_command (ISupply_fan_run_command parameter);

	public Set<ISupply_fan_run_command> getUsesSupply_fan_run_command();

    public void addUsesSupply_fan_run_status (ISupply_fan_run_status parameter);

	public Set<ISupply_fan_run_status> getUsesSupply_fan_run_status();

    public void addUsesCompressor_run_command_1 (ICompressor_run_command_1 parameter);

	public Set<ICompressor_run_command_1> getUsesCompressor_run_command_1();

    public void addUsesCompressor_run_command_2 (ICompressor_run_command_2 parameter);

	public Set<ICompressor_run_command_2> getUsesCompressor_run_command_2();

    public void addUsesCompressor_run_status_1 (ICompressor_run_status_1 parameter);

	public Set<ICompressor_run_status_1> getUsesCompressor_run_status_1();

    public void addUsesCompressor_run_status_2 (ICompressor_run_status_2 parameter);

	public Set<ICompressor_run_status_2> getUsesCompressor_run_status_2();

    public void addUsesSupply_air_temperature_sensor (ISupply_air_temperature_sensor parameter);

	public Set<ISupply_air_temperature_sensor> getUsesSupply_air_temperature_sensor();

    public void addUsesSupply_air_temperature_setpoint (ISupply_air_temperature_setpoint parameter);

	public Set<ISupply_air_temperature_setpoint> getUsesSupply_air_temperature_setpoint();

    public void addUsesBuilding_air_static_pressure_sensor (IBuilding_air_static_pressure_sensor parameter);

	public Set<IBuilding_air_static_pressure_sensor> getUsesBuilding_air_static_pressure_sensor();

    public void addUsesBuilding_air_static_pressure_setpoint (IBuilding_air_static_pressure_setpoint parameter);

	public Set<IBuilding_air_static_pressure_setpoint> getUsesBuilding_air_static_pressure_setpoint();

    public void addUsesExhaust_fan_run_command (IExhaust_fan_run_command parameter);

	public Set<IExhaust_fan_run_command> getUsesExhaust_fan_run_command();

    public void addUsesSupply_fan_speed_percentage_command (ISupply_fan_speed_percentage_command parameter);

	public Set<ISupply_fan_speed_percentage_command> getUsesSupply_fan_speed_percentage_command();

    public void addUsesChilled_water_valve_percentage_command (IChilled_water_valve_percentage_command parameter);

	public Set<IChilled_water_valve_percentage_command> getUsesChilled_water_valve_percentage_command();

    public void addUsesExhaust_fan_run_status (IExhaust_fan_run_status parameter);

	public Set<IExhaust_fan_run_status> getUsesExhaust_fan_run_status();

    public void addUsesExhaust_fan_speed_percentage_command (IExhaust_fan_speed_percentage_command parameter);

	public Set<IExhaust_fan_speed_percentage_command> getUsesExhaust_fan_speed_percentage_command();

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

    public void addUsesHeating_water_valve_percentage_command (IHeating_water_valve_percentage_command parameter);

	public Set<IHeating_water_valve_percentage_command> getUsesHeating_water_valve_percentage_command();

    public void addUsesExhaust_fan_run_command_1 (IExhaust_fan_run_command_1 parameter);

	public Set<IExhaust_fan_run_command_1> getUsesExhaust_fan_run_command_1();

    public void addUsesExhaust_fan_run_command_2 (IExhaust_fan_run_command_2 parameter);

	public Set<IExhaust_fan_run_command_2> getUsesExhaust_fan_run_command_2();

    public void addUsesExhaust_fan_run_command_3 (IExhaust_fan_run_command_3 parameter);

	public Set<IExhaust_fan_run_command_3> getUsesExhaust_fan_run_command_3();

    public void addUsesExhaust_fan_run_command_4 (IExhaust_fan_run_command_4 parameter);

	public Set<IExhaust_fan_run_command_4> getUsesExhaust_fan_run_command_4();

    public void addUsesExhaust_fan_run_status_1 (IExhaust_fan_run_status_1 parameter);

	public Set<IExhaust_fan_run_status_1> getUsesExhaust_fan_run_status_1();

    public void addUsesExhaust_fan_run_status_2 (IExhaust_fan_run_status_2 parameter);

	public Set<IExhaust_fan_run_status_2> getUsesExhaust_fan_run_status_2();

    public void addUsesExhaust_fan_run_status_3 (IExhaust_fan_run_status_3 parameter);

	public Set<IExhaust_fan_run_status_3> getUsesExhaust_fan_run_status_3();

    public void addUsesExhaust_fan_run_status_4 (IExhaust_fan_run_status_4 parameter);

	public Set<IExhaust_fan_run_status_4> getUsesExhaust_fan_run_status_4();

    public void addUsesVentilation_outside_air_damper_percentage_command (IVentilation_outside_air_damper_percentage_command parameter);

	public Set<IVentilation_outside_air_damper_percentage_command> getUsesVentilation_outside_air_damper_percentage_command();

    public void addUsesVentilation_outside_air_flowrate_sensor (IVentilation_outside_air_flowrate_sensor parameter);

	public Set<IVentilation_outside_air_flowrate_sensor> getUsesVentilation_outside_air_flowrate_sensor();

    public void addUsesVentilation_outside_air_flowrate_setpoint (IVentilation_outside_air_flowrate_setpoint parameter);

	public Set<IVentilation_outside_air_flowrate_setpoint> getUsesVentilation_outside_air_flowrate_setpoint();

    public void addUsesSupply_fan_run_command_1 (ISupply_fan_run_command_1 parameter);

	public Set<ISupply_fan_run_command_1> getUsesSupply_fan_run_command_1();

    public void addUsesSupply_fan_run_command_2 (ISupply_fan_run_command_2 parameter);

	public Set<ISupply_fan_run_command_2> getUsesSupply_fan_run_command_2();

    public void addUsesSupply_fan_run_status_1 (ISupply_fan_run_status_1 parameter);

	public Set<ISupply_fan_run_status_1> getUsesSupply_fan_run_status_1();

    public void addUsesSupply_fan_run_status_2 (ISupply_fan_run_status_2 parameter);

	public Set<ISupply_fan_run_status_2> getUsesSupply_fan_run_status_2();

    public void addUsesExhaust_fan_speed_percentage_command_1 (IExhaust_fan_speed_percentage_command_1 parameter);

	public Set<IExhaust_fan_speed_percentage_command_1> getUsesExhaust_fan_speed_percentage_command_1();

    public void addUsesExhaust_fan_speed_percentage_command_2 (IExhaust_fan_speed_percentage_command_2 parameter);

	public Set<IExhaust_fan_speed_percentage_command_2> getUsesExhaust_fan_speed_percentage_command_2();

    public void addUsesExhaust_fan_speed_percentage_command_3 (IExhaust_fan_speed_percentage_command_3 parameter);

	public Set<IExhaust_fan_speed_percentage_command_3> getUsesExhaust_fan_speed_percentage_command_3();

    public void addUsesSupply_fan_speed_percentage_command_1 (ISupply_fan_speed_percentage_command_1 parameter);

	public Set<ISupply_fan_speed_percentage_command_1> getUsesSupply_fan_speed_percentage_command_1();

    public void addUsesSupply_fan_speed_percentage_command_2 (ISupply_fan_speed_percentage_command_2 parameter);

	public Set<ISupply_fan_speed_percentage_command_2> getUsesSupply_fan_speed_percentage_command_2();

    public void addUsesCooling_request_count (ICooling_request_count parameter);

	public Set<ICooling_request_count> getUsesCooling_request_count();

    public void addUsesPressurization_request_count (IPressurization_request_count parameter);

	public Set<IPressurization_request_count> getUsesPressurization_request_count();

    public void addUsesExhaust_fan_speed_percentage_command_4 (IExhaust_fan_speed_percentage_command_4 parameter);

	public Set<IExhaust_fan_speed_percentage_command_4> getUsesExhaust_fan_speed_percentage_command_4();

    public void addUsesOutside_air_flowrate_sensor (IOutside_air_flowrate_sensor parameter);

	public Set<IOutside_air_flowrate_sensor> getUsesOutside_air_flowrate_sensor();

    public void addUsesZone_air_cooling_temperature_setpoint (IZone_air_cooling_temperature_setpoint parameter);

	public Set<IZone_air_cooling_temperature_setpoint> getUsesZone_air_cooling_temperature_setpoint();

    public void addUsesZone_air_temperature_sensor (IZone_air_temperature_sensor parameter);

	public Set<IZone_air_temperature_sensor> getUsesZone_air_temperature_sensor();

    public void addUsesDischarge_fan_run_command (IDischarge_fan_run_command parameter);

	public Set<IDischarge_fan_run_command> getUsesDischarge_fan_run_command();

    public void addUsesDischarge_fan_run_status (IDischarge_fan_run_status parameter);

	public Set<IDischarge_fan_run_status> getUsesDischarge_fan_run_status();

    public void addUsesZone_air_heating_temperature_setpoint (IZone_air_heating_temperature_setpoint parameter);

	public Set<IZone_air_heating_temperature_setpoint> getUsesZone_air_heating_temperature_setpoint();

    public void addUsesDischarge_fan_speed_percentage_command (IDischarge_fan_speed_percentage_command parameter);

	public Set<IDischarge_fan_speed_percentage_command> getUsesDischarge_fan_speed_percentage_command();

    public void addUsesHeater_run_command (IHeater_run_command parameter);

	public Set<IHeater_run_command> getUsesHeater_run_command();

    public void addUsesOutside_air_flowrate_setpoint (IOutside_air_flowrate_setpoint parameter);

	public Set<IOutside_air_flowrate_setpoint> getUsesOutside_air_flowrate_setpoint();

    public void addUsesFilter_differential_pressure_sensor_1 (IFilter_differential_pressure_sensor_1 parameter);

	public Set<IFilter_differential_pressure_sensor_1> getUsesFilter_differential_pressure_sensor_1();

    public void addUsesFilter_differential_pressure_sensor_2 (IFilter_differential_pressure_sensor_2 parameter);

	public Set<IFilter_differential_pressure_sensor_2> getUsesFilter_differential_pressure_sensor_2();

    public void addUsesFilter_differential_pressure_sensor_3 (IFilter_differential_pressure_sensor_3 parameter);

	public Set<IFilter_differential_pressure_sensor_3> getUsesFilter_differential_pressure_sensor_3();

    public void addUsesFilter_differential_pressure_sensor_4 (IFilter_differential_pressure_sensor_4 parameter);

	public Set<IFilter_differential_pressure_sensor_4> getUsesFilter_differential_pressure_sensor_4();

    public void addUsesCompressor_run_command_3 (ICompressor_run_command_3 parameter);

	public Set<ICompressor_run_command_3> getUsesCompressor_run_command_3();

    public void addUsesCompressor_run_command_4 (ICompressor_run_command_4 parameter);

	public Set<ICompressor_run_command_4> getUsesCompressor_run_command_4();

    public void addUsesCompressor_run_status_3 (ICompressor_run_status_3 parameter);

	public Set<ICompressor_run_status_3> getUsesCompressor_run_status_3();

    public void addUsesCompressor_run_status_4 (ICompressor_run_status_4 parameter);

	public Set<ICompressor_run_status_4> getUsesCompressor_run_status_4();

    public void addUsesMixed_air_temperature_setpoint (IMixed_air_temperature_setpoint parameter);

	public Set<IMixed_air_temperature_setpoint> getUsesMixed_air_temperature_setpoint();

    public void addUsesSupply_air_flowrate_sensor (ISupply_air_flowrate_sensor parameter);

	public Set<ISupply_air_flowrate_sensor> getUsesSupply_air_flowrate_sensor();

    public void addUsesSupply_air_flowrate_setpoint (ISupply_air_flowrate_setpoint parameter);

	public Set<ISupply_air_flowrate_setpoint> getUsesSupply_air_flowrate_setpoint();

    public void addUsesCompressor_run_command (ICompressor_run_command parameter);

	public Set<ICompressor_run_command> getUsesCompressor_run_command();

    public void addUsesCompressor_run_status (ICompressor_run_status parameter);

	public Set<ICompressor_run_status> getUsesCompressor_run_status();

    public void addUsesHeater_run_command_1 (IHeater_run_command_1 parameter);

	public Set<IHeater_run_command_1> getUsesHeater_run_command_1();

    public void addUsesHeater_run_command_2 (IHeater_run_command_2 parameter);

	public Set<IHeater_run_command_2> getUsesHeater_run_command_2();

    public void addUsesOptionalsOutside_air_flowrate_requirement (IOutside_air_flowrate_requirement parameter);

	public Set<IOutside_air_flowrate_requirement> getUsesOptionalsOutside_air_flowrate_requirement();

    public void addUsesOptionalsEconomizer_mode (IEconomizer_mode parameter);

	public Set<IEconomizer_mode> getUsesOptionalsEconomizer_mode();

}