package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_static_pressure_sensor;
/**
* Class Zspm 
* Zone static pressure monitoring.
*/
public interface IZspm extends IFunctionality, IMonitoring{

	public IRI iri();

    public void addUsesZone_air_static_pressure_sensor (IZone_air_static_pressure_sensor parameter);

	public Set<IZone_air_static_pressure_sensor> getUsesZone_air_static_pressure_sensor();

}