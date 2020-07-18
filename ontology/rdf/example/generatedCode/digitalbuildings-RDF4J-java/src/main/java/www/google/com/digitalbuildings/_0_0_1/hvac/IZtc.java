package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_deadband_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_relative_humidity_sensor;
/**
* Class Ztc 
* Single control setpoint with deadband.
*/
public interface IZtc extends IFunctionality, IOperational{

	public IRI iri();

    public void addUsesOptionalsZone_air_deadband_temperature_setpoint (IZone_air_deadband_temperature_setpoint parameter);

	public Set<IZone_air_deadband_temperature_setpoint> getUsesOptionalsZone_air_deadband_temperature_setpoint();

    public void addUsesOptionalsZone_air_relative_humidity_sensor (IZone_air_relative_humidity_sensor parameter);

	public Set<IZone_air_relative_humidity_sensor> getUsesOptionalsZone_air_relative_humidity_sensor();

    public void addUsesZone_air_temperature_sensor (IZone_air_temperature_sensor parameter);

	public Set<IZone_air_temperature_sensor> getUsesZone_air_temperature_sensor();

    public void addUsesZone_air_temperature_setpoint (IZone_air_temperature_setpoint parameter);

	public Set<IZone_air_temperature_setpoint> getUsesZone_air_temperature_setpoint();

}