package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_air_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_air_temperature_sensor;
/**
* Class Rtc 
* Return air temperature control
*/
public interface IRtc extends IFunctionality, IOperational{

	public IRI iri();

    public void addUsesReturn_air_temperature_sensor (IReturn_air_temperature_sensor parameter);

	public Set<IReturn_air_temperature_sensor> getUsesReturn_air_temperature_sensor();

    public void addUsesReturn_air_temperature_setpoint (IReturn_air_temperature_setpoint parameter);

	public Set<IReturn_air_temperature_setpoint> getUsesReturn_air_temperature_setpoint();

}