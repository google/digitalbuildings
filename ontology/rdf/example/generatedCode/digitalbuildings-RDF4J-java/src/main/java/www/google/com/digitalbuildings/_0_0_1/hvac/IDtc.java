package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_air_temperature_setpoint;
/**
* Class Dtc 
* Discharge air temperatore control
*/
public interface IDtc extends IFunctionality, IOperational{

	public IRI iri();

    public void addUsesDischarge_air_temperature_sensor (IDischarge_air_temperature_sensor parameter);

	public Set<IDischarge_air_temperature_sensor> getUsesDischarge_air_temperature_sensor();

    public void addUsesDischarge_air_temperature_setpoint (IDischarge_air_temperature_setpoint parameter);

	public Set<IDischarge_air_temperature_setpoint> getUsesDischarge_air_temperature_setpoint();

}