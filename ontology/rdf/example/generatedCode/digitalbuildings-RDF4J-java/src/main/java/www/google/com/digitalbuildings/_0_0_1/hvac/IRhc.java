package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_air_relative_humidity_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_air_relative_humidity_setpoint;
/**
* Class Rhc 
* Return air relative humidity control.
*/
public interface IRhc extends IFunctionality, IOperational{

	public IRI iri();

    public void addUsesReturn_air_relative_humidity_sensor (IReturn_air_relative_humidity_sensor parameter);

	public Set<IReturn_air_relative_humidity_sensor> getUsesReturn_air_relative_humidity_sensor();

    public void addUsesReturn_air_relative_humidity_setpoint (IReturn_air_relative_humidity_setpoint parameter);

	public Set<IReturn_air_relative_humidity_setpoint> getUsesReturn_air_relative_humidity_setpoint();

}