package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_refrigerant_concentration_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_refrigerant_concentration_setpoint;
/**
* Class Refc 
* Refrigerant leak control.
*/
public interface IRefc extends IFunctionality, IOperational{

	public IRI iri();

    public void addUsesZone_air_refrigerant_concentration_sensor (IZone_air_refrigerant_concentration_sensor parameter);

	public Set<IZone_air_refrigerant_concentration_sensor> getUsesZone_air_refrigerant_concentration_sensor();

    public void addUsesZone_air_refrigerant_concentration_setpoint (IZone_air_refrigerant_concentration_setpoint parameter);

	public Set<IZone_air_refrigerant_concentration_setpoint> getUsesZone_air_refrigerant_concentration_setpoint();

}