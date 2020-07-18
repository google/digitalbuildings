package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_air_relative_humidity_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_air_heating_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_air_cooling_temperature_setpoint;
/**
* Class Dsprtc 
* Dual setpoint return air temp control.
*/
public interface IDsprtc extends IFunctionality, IOperational{

	public IRI iri();

    public void addUsesReturn_air_cooling_temperature_setpoint (IReturn_air_cooling_temperature_setpoint parameter);

	public Set<IReturn_air_cooling_temperature_setpoint> getUsesReturn_air_cooling_temperature_setpoint();

    public void addUsesReturn_air_heating_temperature_setpoint (IReturn_air_heating_temperature_setpoint parameter);

	public Set<IReturn_air_heating_temperature_setpoint> getUsesReturn_air_heating_temperature_setpoint();

    public void addUsesReturn_air_temperature_sensor (IReturn_air_temperature_sensor parameter);

	public Set<IReturn_air_temperature_sensor> getUsesReturn_air_temperature_sensor();

    public void addUsesOptionalsDischarge_air_temperature_sensor (IDischarge_air_temperature_sensor parameter);

	public Set<IDischarge_air_temperature_sensor> getUsesOptionalsDischarge_air_temperature_sensor();

    public void addUsesOptionalsReturn_air_relative_humidity_sensor (IReturn_air_relative_humidity_sensor parameter);

	public Set<IReturn_air_relative_humidity_sensor> getUsesOptionalsReturn_air_relative_humidity_sensor();

}