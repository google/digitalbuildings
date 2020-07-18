package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IHeater_run_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_isolation_valve_status;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_isolation_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IRun_command;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_isolation_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IRun_status;
import www.google.com.digitalbuildings._0_0_1.fields.IHeater_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IHeater_run_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_isolation_valve_command;
/**
* Class Rwisovpm 
* Return side isolation valve monitoring.
*/
public interface IRwisovpm extends IFunctionality, IMonitoring{

	public IRI iri();

    public void addUsesReturn_water_isolation_valve_percentage_command (IReturn_water_isolation_valve_percentage_command parameter);

	public Set<IReturn_water_isolation_valve_percentage_command> getUsesReturn_water_isolation_valve_percentage_command();

    public void addUsesReturn_water_isolation_valve_percentage_sensor (IReturn_water_isolation_valve_percentage_sensor parameter);

	public Set<IReturn_water_isolation_valve_percentage_sensor> getUsesReturn_water_isolation_valve_percentage_sensor();

    public void addUsesHeater_run_command (IHeater_run_command parameter);

	public Set<IHeater_run_command> getUsesHeater_run_command();

    public void addUsesSupply_water_temperature_sensor (ISupply_water_temperature_sensor parameter);

	public Set<ISupply_water_temperature_sensor> getUsesSupply_water_temperature_sensor();

    public void addUsesSupply_water_temperature_setpoint (ISupply_water_temperature_setpoint parameter);

	public Set<ISupply_water_temperature_setpoint> getUsesSupply_water_temperature_setpoint();

    public void addUsesRun_command (IRun_command parameter);

	public Set<IRun_command> getUsesRun_command();

    public void addUsesRun_status (IRun_status parameter);

	public Set<IRun_status> getUsesRun_status();

    public void addUsesHeater_run_command_1 (IHeater_run_command_1 parameter);

	public Set<IHeater_run_command_1> getUsesHeater_run_command_1();

    public void addUsesHeater_run_command_2 (IHeater_run_command_2 parameter);

	public Set<IHeater_run_command_2> getUsesHeater_run_command_2();

    public void addUsesReturn_water_isolation_valve_command (IReturn_water_isolation_valve_command parameter);

	public Set<IReturn_water_isolation_valve_command> getUsesReturn_water_isolation_valve_command();

    public void addUsesReturn_water_isolation_valve_status (IReturn_water_isolation_valve_status parameter);

	public Set<IReturn_water_isolation_valve_status> getUsesReturn_water_isolation_valve_status();

}