package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IControl;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_cooling_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_power_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_speed_frequency_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_run_status_2;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_run_status_1;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_request_count;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_water_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_water_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_flowrate_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.IVentilation_outside_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_speed_frequency_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IBuilding_air_static_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_speed_frequency_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_current_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_speed_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_speed_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IPressurization_request_count;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_speed_percentage_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_speed_percentage_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_water_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_relative_humidity_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_frequency_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_frequency_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_frequency_sensor_4;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_frequency_sensor_3;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_command_4;
import www.google.com.digitalbuildings._0_0_1.fields.ILeaving_cooling_coil_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_command_3;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_current_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.IFilter_differential_pressure_sensor_4;
import www.google.com.digitalbuildings._0_0_1.fields.IFilter_differential_pressure_sensor_3;
import www.google.com.digitalbuildings._0_0_1.fields.IFilter_differential_pressure_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IFilter_differential_pressure_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_air_flowrate_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IBypass_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_static_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IVentilation_outside_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_status_4;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_frequency_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_status_1;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_status_3;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_status_2;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_power_sensor_3;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_power_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_power_sensor_4;
import www.google.com.digitalbuildings._0_0_1.fields.IHeater_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_flowrate_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_sensor_4;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_sensor_3;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.ICooling_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_power_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IMixed_air_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_speed_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IHeater_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_heating_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_cooling_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IBuilding_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_power_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_power_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_power_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_status_4;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_status_3;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_current_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_command_4;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_current_sensor_3;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_command_3;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_current_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_status_2;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_status_1;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_speed_frequency_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_current_sensor_4;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.ICooling_thermal_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_flowrate_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_speed_percentage_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.IHeater_run_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_speed_percentage_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_current_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IMixed_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICooling_request_count;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_command_4;
import www.google.com.digitalbuildings._0_0_1.fields.IVentilation_outside_air_flowrate_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_flowrate_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IHeater_run_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_command_3;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_damper_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_run_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.IEconomizer_mode;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_run_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_thermal_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_speed_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_current_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_current_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_power_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_fan_speed_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_heating_temperature_setpoint;
/**
* Class Dx2sdc 
* Two compressor run control on supply air side (dual temp setpoint).
*/
public interface IDx2sdc extends IFunctionality, IControl{

	public IRI iri();

    public void addUsesCompressor_run_command_1 (ICompressor_run_command_1 parameter);

	public Set<ICompressor_run_command_1> getUsesCompressor_run_command_1();

    public void addUsesCompressor_run_command_2 (ICompressor_run_command_2 parameter);

	public Set<ICompressor_run_command_2> getUsesCompressor_run_command_2();

    public void addUsesCompressor_run_status_1 (ICompressor_run_status_1 parameter);

	public Set<ICompressor_run_status_1> getUsesCompressor_run_status_1();

    public void addUsesCompressor_run_status_2 (ICompressor_run_status_2 parameter);

	public Set<ICompressor_run_status_2> getUsesCompressor_run_status_2();

    public void addUsesSupply_air_cooling_temperature_setpoint (ISupply_air_cooling_temperature_setpoint parameter);

	public Set<ISupply_air_cooling_temperature_setpoint> getUsesSupply_air_cooling_temperature_setpoint();

    public void addUsesSupply_air_heating_temperature_setpoint (ISupply_air_heating_temperature_setpoint parameter);

	public Set<ISupply_air_heating_temperature_setpoint> getUsesSupply_air_heating_temperature_setpoint();

    public void addUsesSupply_air_temperature_sensor (ISupply_air_temperature_sensor parameter);

	public Set<ISupply_air_temperature_sensor> getUsesSupply_air_temperature_sensor();

    public void addUsesHeater_run_command_1 (IHeater_run_command_1 parameter);

	public Set<IHeater_run_command_1> getUsesHeater_run_command_1();

    public void addUsesHeater_run_command_2 (IHeater_run_command_2 parameter);

	public Set<IHeater_run_command_2> getUsesHeater_run_command_2();

    public void addUsesSupply_fan_run_command (ISupply_fan_run_command parameter);

	public Set<ISupply_fan_run_command> getUsesSupply_fan_run_command();

    public void addUsesSupply_fan_run_status (ISupply_fan_run_status parameter);

	public Set<ISupply_fan_run_status> getUsesSupply_fan_run_status();

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

    public void addUsesSupply_air_temperature_setpoint (ISupply_air_temperature_setpoint parameter);

	public Set<ISupply_air_temperature_setpoint> getUsesSupply_air_temperature_setpoint();

    public void addUsesSupply_air_static_pressure_sensor (ISupply_air_static_pressure_sensor parameter);

	public Set<ISupply_air_static_pressure_sensor> getUsesSupply_air_static_pressure_sensor();

    public void addUsesSupply_air_static_pressure_setpoint (ISupply_air_static_pressure_setpoint parameter);

	public Set<ISupply_air_static_pressure_setpoint> getUsesSupply_air_static_pressure_setpoint();

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

    public void addUsesBypass_air_damper_percentage_command (IBypass_air_damper_percentage_command parameter);

	public Set<IBypass_air_damper_percentage_command> getUsesBypass_air_damper_percentage_command();

    public void addUsesOptionalsCompressor_speed_percentage_command (ICompressor_speed_percentage_command parameter);

	public Set<ICompressor_speed_percentage_command> getUsesOptionalsCompressor_speed_percentage_command();

    public void addUsesOptionalsCooling_percentage_command (ICooling_percentage_command parameter);

	public Set<ICooling_percentage_command> getUsesOptionalsCooling_percentage_command();

    public void addUsesOptionalsCooling_thermal_power_capacity (ICooling_thermal_power_capacity parameter);

	public Set<ICooling_thermal_power_capacity> getUsesOptionalsCooling_thermal_power_capacity();

    public void addUsesOptionalsLeaving_cooling_coil_temperature_sensor (ILeaving_cooling_coil_temperature_sensor parameter);

	public Set<ILeaving_cooling_coil_temperature_sensor> getUsesOptionalsLeaving_cooling_coil_temperature_sensor();

    public void addUsesOptionalsHeating_percentage_command (IHeating_percentage_command parameter);

	public Set<IHeating_percentage_command> getUsesOptionalsHeating_percentage_command();

    public void addUsesOptionalsHeating_thermal_power_capacity (IHeating_thermal_power_capacity parameter);

	public Set<IHeating_thermal_power_capacity> getUsesOptionalsHeating_thermal_power_capacity();

    public void addUsesOptionalsSupply_air_flowrate_capacity (ISupply_air_flowrate_capacity parameter);

	public Set<ISupply_air_flowrate_capacity> getUsesOptionalsSupply_air_flowrate_capacity();

    public void addUsesOptionalsSupply_fan_current_sensor (ISupply_fan_current_sensor parameter);

	public Set<ISupply_fan_current_sensor> getUsesOptionalsSupply_fan_current_sensor();

    public void addUsesOptionalsSupply_fan_power_capacity (ISupply_fan_power_capacity parameter);

	public Set<ISupply_fan_power_capacity> getUsesOptionalsSupply_fan_power_capacity();

    public void addUsesOptionalsSupply_fan_power_sensor (ISupply_fan_power_sensor parameter);

	public Set<ISupply_fan_power_sensor> getUsesOptionalsSupply_fan_power_sensor();

    public void addUsesOptionalsExhaust_air_damper_percentage_command (IExhaust_air_damper_percentage_command parameter);

	public Set<IExhaust_air_damper_percentage_command> getUsesOptionalsExhaust_air_damper_percentage_command();

    public void addUsesOptionalsExhaust_fan_run_status (IExhaust_fan_run_status parameter);

	public Set<IExhaust_fan_run_status> getUsesOptionalsExhaust_fan_run_status();

    public void addUsesOptionalsSupply_fan_speed_frequency_sensor (ISupply_fan_speed_frequency_sensor parameter);

	public Set<ISupply_fan_speed_frequency_sensor> getUsesOptionalsSupply_fan_speed_frequency_sensor();

    public void addUsesOptionalsSupply_fan_speed_percentage_sensor (ISupply_fan_speed_percentage_sensor parameter);

	public Set<ISupply_fan_speed_percentage_sensor> getUsesOptionalsSupply_fan_speed_percentage_sensor();

    public void addUsesOptionalsPressurization_request_count (IPressurization_request_count parameter);

	public Set<IPressurization_request_count> getUsesOptionalsPressurization_request_count();

    public void addUsesOptionalsSupply_air_damper_percentage_command (ISupply_air_damper_percentage_command parameter);

	public Set<ISupply_air_damper_percentage_command> getUsesOptionalsSupply_air_damper_percentage_command();

    public void addUsesOptionalsSupply_air_flowrate_sensor (ISupply_air_flowrate_sensor parameter);

	public Set<ISupply_air_flowrate_sensor> getUsesOptionalsSupply_air_flowrate_sensor();

    public void addUsesOptionalsSupply_fan_run_command (ISupply_fan_run_command parameter);

	public Set<ISupply_fan_run_command> getUsesOptionalsSupply_fan_run_command();

    public void addUsesOptionalsSupply_fan_run_status (ISupply_fan_run_status parameter);

	public Set<ISupply_fan_run_status> getUsesOptionalsSupply_fan_run_status();

    public void addUsesOptionalsSupply_fan_speed_percentage_command (ISupply_fan_speed_percentage_command parameter);

	public Set<ISupply_fan_speed_percentage_command> getUsesOptionalsSupply_fan_speed_percentage_command();

    public void addUsesOptionalsHeating_water_valve_percentage_sensor (IHeating_water_valve_percentage_sensor parameter);

	public Set<IHeating_water_valve_percentage_sensor> getUsesOptionalsHeating_water_valve_percentage_sensor();

    public void addUsesOptionalsExhaust_air_flowrate_capacity (IExhaust_air_flowrate_capacity parameter);

	public Set<IExhaust_air_flowrate_capacity> getUsesOptionalsExhaust_air_flowrate_capacity();

    public void addUsesOptionalsExhaust_fan_current_sensor_1 (IExhaust_fan_current_sensor_1 parameter);

	public Set<IExhaust_fan_current_sensor_1> getUsesOptionalsExhaust_fan_current_sensor_1();

    public void addUsesOptionalsExhaust_fan_current_sensor_2 (IExhaust_fan_current_sensor_2 parameter);

	public Set<IExhaust_fan_current_sensor_2> getUsesOptionalsExhaust_fan_current_sensor_2();

    public void addUsesOptionalsExhaust_fan_current_sensor_3 (IExhaust_fan_current_sensor_3 parameter);

	public Set<IExhaust_fan_current_sensor_3> getUsesOptionalsExhaust_fan_current_sensor_3();

    public void addUsesOptionalsExhaust_fan_current_sensor_4 (IExhaust_fan_current_sensor_4 parameter);

	public Set<IExhaust_fan_current_sensor_4> getUsesOptionalsExhaust_fan_current_sensor_4();

    public void addUsesOptionalsExhaust_fan_power_capacity (IExhaust_fan_power_capacity parameter);

	public Set<IExhaust_fan_power_capacity> getUsesOptionalsExhaust_fan_power_capacity();

    public void addUsesOptionalsExhaust_fan_power_sensor_1 (IExhaust_fan_power_sensor_1 parameter);

	public Set<IExhaust_fan_power_sensor_1> getUsesOptionalsExhaust_fan_power_sensor_1();

    public void addUsesOptionalsExhaust_fan_power_sensor_2 (IExhaust_fan_power_sensor_2 parameter);

	public Set<IExhaust_fan_power_sensor_2> getUsesOptionalsExhaust_fan_power_sensor_2();

    public void addUsesOptionalsExhaust_fan_power_sensor_3 (IExhaust_fan_power_sensor_3 parameter);

	public Set<IExhaust_fan_power_sensor_3> getUsesOptionalsExhaust_fan_power_sensor_3();

    public void addUsesOptionalsExhaust_fan_power_sensor_4 (IExhaust_fan_power_sensor_4 parameter);

	public Set<IExhaust_fan_power_sensor_4> getUsesOptionalsExhaust_fan_power_sensor_4();

    public void addUsesOptionalsExhaust_fan_current_sensor (IExhaust_fan_current_sensor parameter);

	public Set<IExhaust_fan_current_sensor> getUsesOptionalsExhaust_fan_current_sensor();

    public void addUsesOptionalsExhaust_fan_power_sensor (IExhaust_fan_power_sensor parameter);

	public Set<IExhaust_fan_power_sensor> getUsesOptionalsExhaust_fan_power_sensor();

    public void addUsesOptionalsExhaust_fan_speed_frequency_sensor (IExhaust_fan_speed_frequency_sensor parameter);

	public Set<IExhaust_fan_speed_frequency_sensor> getUsesOptionalsExhaust_fan_speed_frequency_sensor();

    public void addUsesOptionalsExhaust_fan_speed_percentage_sensor (IExhaust_fan_speed_percentage_sensor parameter);

	public Set<IExhaust_fan_speed_percentage_sensor> getUsesOptionalsExhaust_fan_speed_percentage_sensor();

    public void addUsesOptionalsSupply_fan_current_sensor_1 (ISupply_fan_current_sensor_1 parameter);

	public Set<ISupply_fan_current_sensor_1> getUsesOptionalsSupply_fan_current_sensor_1();

    public void addUsesOptionalsSupply_fan_current_sensor_2 (ISupply_fan_current_sensor_2 parameter);

	public Set<ISupply_fan_current_sensor_2> getUsesOptionalsSupply_fan_current_sensor_2();

    public void addUsesOptionalsSupply_fan_power_sensor_1 (ISupply_fan_power_sensor_1 parameter);

	public Set<ISupply_fan_power_sensor_1> getUsesOptionalsSupply_fan_power_sensor_1();

    public void addUsesOptionalsSupply_fan_power_sensor_2 (ISupply_fan_power_sensor_2 parameter);

	public Set<ISupply_fan_power_sensor_2> getUsesOptionalsSupply_fan_power_sensor_2();

    public void addUsesOptionalsOutside_air_flowrate_sensor (IOutside_air_flowrate_sensor parameter);

	public Set<IOutside_air_flowrate_sensor> getUsesOptionalsOutside_air_flowrate_sensor();

    public void addUsesOptionalsOutside_air_flowrate_setpoint (IOutside_air_flowrate_setpoint parameter);

	public Set<IOutside_air_flowrate_setpoint> getUsesOptionalsOutside_air_flowrate_setpoint();

    public void addUsesOptionalsSupply_air_temperature_sensor (ISupply_air_temperature_sensor parameter);

	public Set<ISupply_air_temperature_sensor> getUsesOptionalsSupply_air_temperature_sensor();

    public void addUsesOptionalsExhaust_fan_speed_frequency_sensor_1 (IExhaust_fan_speed_frequency_sensor_1 parameter);

	public Set<IExhaust_fan_speed_frequency_sensor_1> getUsesOptionalsExhaust_fan_speed_frequency_sensor_1();

    public void addUsesOptionalsExhaust_fan_speed_frequency_sensor_2 (IExhaust_fan_speed_frequency_sensor_2 parameter);

	public Set<IExhaust_fan_speed_frequency_sensor_2> getUsesOptionalsExhaust_fan_speed_frequency_sensor_2();

    public void addUsesOptionalsExhaust_fan_speed_frequency_sensor_3 (IExhaust_fan_speed_frequency_sensor_3 parameter);

	public Set<IExhaust_fan_speed_frequency_sensor_3> getUsesOptionalsExhaust_fan_speed_frequency_sensor_3();

    public void addUsesOptionalsExhaust_fan_speed_percentage_sensor_1 (IExhaust_fan_speed_percentage_sensor_1 parameter);

	public Set<IExhaust_fan_speed_percentage_sensor_1> getUsesOptionalsExhaust_fan_speed_percentage_sensor_1();

    public void addUsesOptionalsExhaust_fan_speed_percentage_sensor_2 (IExhaust_fan_speed_percentage_sensor_2 parameter);

	public Set<IExhaust_fan_speed_percentage_sensor_2> getUsesOptionalsExhaust_fan_speed_percentage_sensor_2();

    public void addUsesOptionalsExhaust_fan_speed_percentage_sensor_3 (IExhaust_fan_speed_percentage_sensor_3 parameter);

	public Set<IExhaust_fan_speed_percentage_sensor_3> getUsesOptionalsExhaust_fan_speed_percentage_sensor_3();

    public void addUsesOptionalsSupply_fan_speed_frequency_sensor_1 (ISupply_fan_speed_frequency_sensor_1 parameter);

	public Set<ISupply_fan_speed_frequency_sensor_1> getUsesOptionalsSupply_fan_speed_frequency_sensor_1();

    public void addUsesOptionalsSupply_fan_speed_frequency_sensor_2 (ISupply_fan_speed_frequency_sensor_2 parameter);

	public Set<ISupply_fan_speed_frequency_sensor_2> getUsesOptionalsSupply_fan_speed_frequency_sensor_2();

    public void addUsesOptionalsSupply_fan_speed_percentage_sensor_1 (ISupply_fan_speed_percentage_sensor_1 parameter);

	public Set<ISupply_fan_speed_percentage_sensor_1> getUsesOptionalsSupply_fan_speed_percentage_sensor_1();

    public void addUsesOptionalsSupply_fan_speed_percentage_sensor_2 (ISupply_fan_speed_percentage_sensor_2 parameter);

	public Set<ISupply_fan_speed_percentage_sensor_2> getUsesOptionalsSupply_fan_speed_percentage_sensor_2();

    public void addUsesOptionalsHeating_request_count (IHeating_request_count parameter);

	public Set<IHeating_request_count> getUsesOptionalsHeating_request_count();

    public void addUsesOptionalsExhaust_fan_speed_frequency_sensor_4 (IExhaust_fan_speed_frequency_sensor_4 parameter);

	public Set<IExhaust_fan_speed_frequency_sensor_4> getUsesOptionalsExhaust_fan_speed_frequency_sensor_4();

    public void addUsesOptionalsExhaust_fan_speed_percentage_sensor_4 (IExhaust_fan_speed_percentage_sensor_4 parameter);

	public Set<IExhaust_fan_speed_percentage_sensor_4> getUsesOptionalsExhaust_fan_speed_percentage_sensor_4();

    public void addUsesOptionalsMixed_air_temperature_sensor (IMixed_air_temperature_sensor parameter);

	public Set<IMixed_air_temperature_sensor> getUsesOptionalsMixed_air_temperature_sensor();

    public void addUsesOptionalsDischarge_air_temperature_sensor (IDischarge_air_temperature_sensor parameter);

	public Set<IDischarge_air_temperature_sensor> getUsesOptionalsDischarge_air_temperature_sensor();

    public void addUsesOptionalsDischarge_air_flowrate_capacity (IDischarge_air_flowrate_capacity parameter);

	public Set<IDischarge_air_flowrate_capacity> getUsesOptionalsDischarge_air_flowrate_capacity();

    public void addUsesOptionalsDischarge_fan_current_sensor (IDischarge_fan_current_sensor parameter);

	public Set<IDischarge_fan_current_sensor> getUsesOptionalsDischarge_fan_current_sensor();

    public void addUsesOptionalsDischarge_fan_power_capacity (IDischarge_fan_power_capacity parameter);

	public Set<IDischarge_fan_power_capacity> getUsesOptionalsDischarge_fan_power_capacity();

    public void addUsesOptionalsDischarge_fan_power_sensor (IDischarge_fan_power_sensor parameter);

	public Set<IDischarge_fan_power_sensor> getUsesOptionalsDischarge_fan_power_sensor();

    public void addUsesOptionalsOutside_air_damper_percentage_sensor (IOutside_air_damper_percentage_sensor parameter);

	public Set<IOutside_air_damper_percentage_sensor> getUsesOptionalsOutside_air_damper_percentage_sensor();

    public void addUsesOptionalsReturn_air_temperature_sensor (IReturn_air_temperature_sensor parameter);

	public Set<IReturn_air_temperature_sensor> getUsesOptionalsReturn_air_temperature_sensor();

    public void addUsesOptionalsZone_air_relative_humidity_sensor (IZone_air_relative_humidity_sensor parameter);

	public Set<IZone_air_relative_humidity_sensor> getUsesOptionalsZone_air_relative_humidity_sensor();

    public void addUsesOptionalsDischarge_fan_speed_frequency_sensor (IDischarge_fan_speed_frequency_sensor parameter);

	public Set<IDischarge_fan_speed_frequency_sensor> getUsesOptionalsDischarge_fan_speed_frequency_sensor();

    public void addUsesOptionalsDischarge_fan_speed_percentage_sensor (IDischarge_fan_speed_percentage_sensor parameter);

	public Set<IDischarge_fan_speed_percentage_sensor> getUsesOptionalsDischarge_fan_speed_percentage_sensor();

    public void addUsesOptionalsHeater_run_status (IHeater_run_status parameter);

	public Set<IHeater_run_status> getUsesOptionalsHeater_run_status();

    public void addUsesOptionalsCooling_request_count (ICooling_request_count parameter);

	public Set<ICooling_request_count> getUsesOptionalsCooling_request_count();

}