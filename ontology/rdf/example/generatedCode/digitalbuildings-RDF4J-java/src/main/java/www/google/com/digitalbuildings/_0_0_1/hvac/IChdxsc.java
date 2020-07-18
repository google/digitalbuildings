package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_speed_frequency_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_speed_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_supply_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_return_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_speed_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ICooling_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_supply_water_temperature_setpoint;
/**
* Class Chdxsc 
* Chiller control single stage.
*/
public interface IChdxsc extends IFunctionality{

	public IRI iri();

    public void addUsesChilled_supply_water_temperature_sensor (IChilled_supply_water_temperature_sensor parameter);

	public Set<IChilled_supply_water_temperature_sensor> getUsesChilled_supply_water_temperature_sensor();

    public void addUsesChilled_supply_water_temperature_setpoint (IChilled_supply_water_temperature_setpoint parameter);

	public Set<IChilled_supply_water_temperature_setpoint> getUsesChilled_supply_water_temperature_setpoint();

    public void addUsesCompressor_run_command (ICompressor_run_command parameter);

	public Set<ICompressor_run_command> getUsesCompressor_run_command();

    public void addUsesCompressor_run_status (ICompressor_run_status parameter);

	public Set<ICompressor_run_status> getUsesCompressor_run_status();

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

}