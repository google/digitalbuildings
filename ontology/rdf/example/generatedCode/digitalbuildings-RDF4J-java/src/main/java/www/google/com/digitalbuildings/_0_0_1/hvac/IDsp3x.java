package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_cooling_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_temperature_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_heating_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_temperature_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_temperature_sensor_3;
/**
* Class Dsp3x 
* Dual setpoint zone temp control with 3 temp sensors.
*/
public interface IDsp3x extends IFunctionality, IOperational{

	public IRI iri();

    public void addUsesOptionalsDischarge_air_temperature_sensor (IDischarge_air_temperature_sensor parameter);

	public Set<IDischarge_air_temperature_sensor> getUsesOptionalsDischarge_air_temperature_sensor();

    public void addUsesZone_air_cooling_temperature_setpoint (IZone_air_cooling_temperature_setpoint parameter);

	public Set<IZone_air_cooling_temperature_setpoint> getUsesZone_air_cooling_temperature_setpoint();

    public void addUsesZone_air_heating_temperature_setpoint (IZone_air_heating_temperature_setpoint parameter);

	public Set<IZone_air_heating_temperature_setpoint> getUsesZone_air_heating_temperature_setpoint();

    public void addUsesZone_air_temperature_sensor_1 (IZone_air_temperature_sensor_1 parameter);

	public Set<IZone_air_temperature_sensor_1> getUsesZone_air_temperature_sensor_1();

    public void addUsesZone_air_temperature_sensor_2 (IZone_air_temperature_sensor_2 parameter);

	public Set<IZone_air_temperature_sensor_2> getUsesZone_air_temperature_sensor_2();

    public void addUsesZone_air_temperature_sensor_3 (IZone_air_temperature_sensor_3 parameter);

	public Set<IZone_air_temperature_sensor_3> getUsesZone_air_temperature_sensor_3();

}