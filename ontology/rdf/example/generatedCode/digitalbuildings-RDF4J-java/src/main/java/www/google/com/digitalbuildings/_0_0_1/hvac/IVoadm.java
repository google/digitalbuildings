package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IEconomizer_mode;
import www.google.com.digitalbuildings._0_0_1.fields.IMixed_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_damper_percentage_sensor;
/**
* Class Voadm 
* Variable outside air damper monitoring.
*/
public interface IVoadm extends IFunctionality, IMonitoring{

	public IRI iri();

    public void addUsesOutside_air_damper_percentage_command (IOutside_air_damper_percentage_command parameter);

	public Set<IOutside_air_damper_percentage_command> getUsesOutside_air_damper_percentage_command();

    public void addUsesOutside_air_temperature_sensor (IOutside_air_temperature_sensor parameter);

	public Set<IOutside_air_temperature_sensor> getUsesOutside_air_temperature_sensor();

    public void addUsesOptionalsEconomizer_mode (IEconomizer_mode parameter);

	public Set<IEconomizer_mode> getUsesOptionalsEconomizer_mode();

    public void addUsesOptionalsMixed_air_temperature_sensor (IMixed_air_temperature_sensor parameter);

	public Set<IMixed_air_temperature_sensor> getUsesOptionalsMixed_air_temperature_sensor();

    public void addUsesOptionalsOutside_air_damper_percentage_sensor (IOutside_air_damper_percentage_sensor parameter);

	public Set<IOutside_air_damper_percentage_sensor> getUsesOptionalsOutside_air_damper_percentage_sensor();

}