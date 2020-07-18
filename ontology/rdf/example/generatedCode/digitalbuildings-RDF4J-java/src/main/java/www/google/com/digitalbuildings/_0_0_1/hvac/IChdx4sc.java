package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_supply_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_status_4;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_status_3;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_speed_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_status_2;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_supply_water_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_status_1;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_command_4;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_command_3;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_speed_frequency_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_speed_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_return_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICooling_percentage_command;
/**
* Class Chdx4sc 
* Chiller control.
*/
public interface IChdx4sc extends IFunctionality{

	public IRI iri();

    public void addUsesOptionalsChilled_return_water_temperature_sensor (IChilled_return_water_temperature_sensor parameter);

	public Set<IChilled_return_water_temperature_sensor> getUsesOptionalsChilled_return_water_temperature_sensor();

    public void addUsesOptionalsCompressor_speed_frequency_sensor (ICompressor_speed_frequency_sensor parameter);

	public Set<ICompressor_speed_frequency_sensor> getUsesOptionalsCompressor_speed_frequency_sensor();

    public void addUsesOptionalsCompressor_speed_percentage_command (ICompressor_speed_percentage_command parameter);

	public Set<ICompressor_speed_percentage_command> getUsesOptionalsCompressor_speed_percentage_command();

    public void addUsesOptionalsCompressor_speed_percentage_sensor (ICompressor_speed_percentage_sensor parameter);

	public Set<ICompressor_speed_percentage_sensor> getUsesOptionalsCompressor_speed_percentage_sensor();

    public void addUsesOptionalsCooling_percentage_command (ICooling_percentage_command parameter);

	public Set<ICooling_percentage_command> getUsesOptionalsCooling_percentage_command();

    public void addUsesChilled_supply_water_temperature_sensor (IChilled_supply_water_temperature_sensor parameter);

	public Set<IChilled_supply_water_temperature_sensor> getUsesChilled_supply_water_temperature_sensor();

    public void addUsesChilled_supply_water_temperature_setpoint (IChilled_supply_water_temperature_setpoint parameter);

	public Set<IChilled_supply_water_temperature_setpoint> getUsesChilled_supply_water_temperature_setpoint();

    public void addUsesCompressor_run_command_1 (ICompressor_run_command_1 parameter);

	public Set<ICompressor_run_command_1> getUsesCompressor_run_command_1();

    public void addUsesCompressor_run_command_2 (ICompressor_run_command_2 parameter);

	public Set<ICompressor_run_command_2> getUsesCompressor_run_command_2();

    public void addUsesCompressor_run_command_3 (ICompressor_run_command_3 parameter);

	public Set<ICompressor_run_command_3> getUsesCompressor_run_command_3();

    public void addUsesCompressor_run_command_4 (ICompressor_run_command_4 parameter);

	public Set<ICompressor_run_command_4> getUsesCompressor_run_command_4();

    public void addUsesCompressor_run_status_1 (ICompressor_run_status_1 parameter);

	public Set<ICompressor_run_status_1> getUsesCompressor_run_status_1();

    public void addUsesCompressor_run_status_2 (ICompressor_run_status_2 parameter);

	public Set<ICompressor_run_status_2> getUsesCompressor_run_status_2();

    public void addUsesCompressor_run_status_3 (ICompressor_run_status_3 parameter);

	public Set<ICompressor_run_status_3> getUsesCompressor_run_status_3();

    public void addUsesCompressor_run_status_4 (ICompressor_run_status_4 parameter);

	public Set<ICompressor_run_status_4> getUsesCompressor_run_status_4();

}