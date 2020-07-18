package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.fields.ICondensing_supply_water_isolation_valve_command;
import www.google.com.digitalbuildings._0_0_1.fields.IHeater_run_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_isolation_valve_status;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_isolation_valve_status;
import www.google.com.digitalbuildings._0_0_1.fields.ICondenser_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_supply_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IRun_status;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_return_water_isolation_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IHeater_run_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_supply_water_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_return_water_isolation_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.ICondensing_supply_water_isolation_valve_status;
import www.google.com.digitalbuildings._0_0_1.fields.IDifferential_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_isolation_valve_command;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_return_water_isolation_valve_status;
import www.google.com.digitalbuildings._0_0_1.fields.IRun_command;
import www.google.com.digitalbuildings._0_0_1.fields.IEvaporator_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_return_water_isolation_valve_command;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_isolation_valve_command;
/**
* Class Cwsisovm 
* Condensing water supply isolation monitoring.
*/
public interface ICwsisovm extends IFunctionality, IMonitoring{

	public IRI iri();

    public void addUsesCondensing_supply_water_isolation_valve_command (ICondensing_supply_water_isolation_valve_command parameter);

	public Set<ICondensing_supply_water_isolation_valve_command> getUsesCondensing_supply_water_isolation_valve_command();

    public void addUsesCondensing_supply_water_isolation_valve_status (ICondensing_supply_water_isolation_valve_status parameter);

	public Set<ICondensing_supply_water_isolation_valve_status> getUsesCondensing_supply_water_isolation_valve_status();

    public void addUsesChilled_return_water_isolation_valve_command (IChilled_return_water_isolation_valve_command parameter);

	public Set<IChilled_return_water_isolation_valve_command> getUsesChilled_return_water_isolation_valve_command();

    public void addUsesChilled_return_water_isolation_valve_status (IChilled_return_water_isolation_valve_status parameter);

	public Set<IChilled_return_water_isolation_valve_status> getUsesChilled_return_water_isolation_valve_status();

    public void addUsesRun_command (IRun_command parameter);

	public Set<IRun_command> getUsesRun_command();

    public void addUsesRun_status (IRun_status parameter);

	public Set<IRun_status> getUsesRun_status();

    public void addUsesHeater_run_command_1 (IHeater_run_command_1 parameter);

	public Set<IHeater_run_command_1> getUsesHeater_run_command_1();

    public void addUsesHeater_run_command_2 (IHeater_run_command_2 parameter);

	public Set<IHeater_run_command_2> getUsesHeater_run_command_2();

    public void addUsesSupply_water_temperature_sensor (ISupply_water_temperature_sensor parameter);

	public Set<ISupply_water_temperature_sensor> getUsesSupply_water_temperature_sensor();

    public void addUsesSupply_water_temperature_setpoint (ISupply_water_temperature_setpoint parameter);

	public Set<ISupply_water_temperature_setpoint> getUsesSupply_water_temperature_setpoint();

    public void addUsesReturn_water_isolation_valve_command (IReturn_water_isolation_valve_command parameter);

	public Set<IReturn_water_isolation_valve_command> getUsesReturn_water_isolation_valve_command();

    public void addUsesReturn_water_isolation_valve_status (IReturn_water_isolation_valve_status parameter);

	public Set<IReturn_water_isolation_valve_status> getUsesReturn_water_isolation_valve_status();

    public void addUsesSupply_water_isolation_valve_command (ISupply_water_isolation_valve_command parameter);

	public Set<ISupply_water_isolation_valve_command> getUsesSupply_water_isolation_valve_command();

    public void addUsesSupply_water_isolation_valve_status (ISupply_water_isolation_valve_status parameter);

	public Set<ISupply_water_isolation_valve_status> getUsesSupply_water_isolation_valve_status();

    public void addUsesChilled_supply_water_temperature_sensor (IChilled_supply_water_temperature_sensor parameter);

	public Set<IChilled_supply_water_temperature_sensor> getUsesChilled_supply_water_temperature_sensor();

    public void addUsesChilled_supply_water_temperature_setpoint (IChilled_supply_water_temperature_setpoint parameter);

	public Set<IChilled_supply_water_temperature_setpoint> getUsesChilled_supply_water_temperature_setpoint();

    public void addUsesChilled_return_water_isolation_valve_percentage_command (IChilled_return_water_isolation_valve_percentage_command parameter);

	public Set<IChilled_return_water_isolation_valve_percentage_command> getUsesChilled_return_water_isolation_valve_percentage_command();

    public void addUsesChilled_return_water_isolation_valve_percentage_sensor (IChilled_return_water_isolation_valve_percentage_sensor parameter);

	public Set<IChilled_return_water_isolation_valve_percentage_sensor> getUsesChilled_return_water_isolation_valve_percentage_sensor();

    public void addUsesCompressor_run_command (ICompressor_run_command parameter);

	public Set<ICompressor_run_command> getUsesCompressor_run_command();

    public void addUsesCompressor_run_status (ICompressor_run_status parameter);

	public Set<ICompressor_run_status> getUsesCompressor_run_status();

    public void addUsesCondenser_pressure_sensor (ICondenser_pressure_sensor parameter);

	public Set<ICondenser_pressure_sensor> getUsesCondenser_pressure_sensor();

    public void addUsesDifferential_pressure_sensor (IDifferential_pressure_sensor parameter);

	public Set<IDifferential_pressure_sensor> getUsesDifferential_pressure_sensor();

    public void addUsesEvaporator_pressure_sensor (IEvaporator_pressure_sensor parameter);

	public Set<IEvaporator_pressure_sensor> getUsesEvaporator_pressure_sensor();

}