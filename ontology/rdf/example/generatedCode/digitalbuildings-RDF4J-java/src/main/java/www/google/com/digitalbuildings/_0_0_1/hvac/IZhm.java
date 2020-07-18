package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_relative_humidity_sensor;
/**
* Class Zhm 
* Zone humidity monitoring.
*/
public interface IZhm extends IFunctionality, IMonitoring{

	public IRI iri();

    public void addUsesZone_air_relative_humidity_sensor (IZone_air_relative_humidity_sensor parameter);

	public Set<IZone_air_relative_humidity_sensor> getUsesZone_air_relative_humidity_sensor();

}