package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_co_concentration_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_co_concentration_sensor;
/**
* Class Coc 
* Carbon monoxide control.
*/
public interface ICoc extends IFunctionality, IOperational{

	public IRI iri();

    public void addUsesZone_air_co_concentration_sensor (IZone_air_co_concentration_sensor parameter);

	public Set<IZone_air_co_concentration_sensor> getUsesZone_air_co_concentration_sensor();

    public void addUsesZone_air_co_concentration_setpoint (IZone_air_co_concentration_setpoint parameter);

	public Set<IZone_air_co_concentration_setpoint> getUsesZone_air_co_concentration_setpoint();

}