package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IControl;
import www.google.com.digitalbuildings._0_0_1.fields.IDehumidification_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_relative_humidity_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IHumidification_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_relative_humidity_sensor;
/**
* Class Zhdhc 
* Zone humidification/dehumidification control.
*/
public interface IZhdhc extends IFunctionality, IControl{

	public IRI iri();

    public void addUsesDehumidification_run_command (IDehumidification_run_command parameter);

	public Set<IDehumidification_run_command> getUsesDehumidification_run_command();

    public void addUsesHumidification_run_command (IHumidification_run_command parameter);

	public Set<IHumidification_run_command> getUsesHumidification_run_command();

    public void addUsesZone_air_relative_humidity_sensor (IZone_air_relative_humidity_sensor parameter);

	public Set<IZone_air_relative_humidity_sensor> getUsesZone_air_relative_humidity_sensor();

    public void addUsesZone_air_relative_humidity_setpoint (IZone_air_relative_humidity_setpoint parameter);

	public Set<IZone_air_relative_humidity_setpoint> getUsesZone_air_relative_humidity_setpoint();

}