package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.fields.IDehumidification_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_dehumidification_relative_humidity_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IHumidification_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_relative_humidity_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_humidification_relative_humidity_setpoint;
/**
* Class Shc 
* Supply air relative humidity control.
*/
public interface IShc extends IFunctionality, IOperational{

	public IRI iri();

    public void addUsesDehumidification_run_command (IDehumidification_run_command parameter);

	public Set<IDehumidification_run_command> getUsesDehumidification_run_command();

    public void addUsesHumidification_run_command (IHumidification_run_command parameter);

	public Set<IHumidification_run_command> getUsesHumidification_run_command();

    public void addUsesSupply_air_dehumidification_relative_humidity_setpoint (ISupply_air_dehumidification_relative_humidity_setpoint parameter);

	public Set<ISupply_air_dehumidification_relative_humidity_setpoint> getUsesSupply_air_dehumidification_relative_humidity_setpoint();

    public void addUsesSupply_air_humidification_relative_humidity_setpoint (ISupply_air_humidification_relative_humidity_setpoint parameter);

	public Set<ISupply_air_humidification_relative_humidity_setpoint> getUsesSupply_air_humidification_relative_humidity_setpoint();

    public void addUsesSupply_air_relative_humidity_sensor (ISupply_air_relative_humidity_sensor parameter);

	public Set<ISupply_air_relative_humidity_sensor> getUsesSupply_air_relative_humidity_sensor();

}