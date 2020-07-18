package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_relative_humidity_sensor;
/**
* Class Shm 
* Supply air relative humidity monitoring.
*/
public interface IShm extends IFunctionality, IMonitoring{

	public IRI iri();

    public void addUsesSupply_air_relative_humidity_sensor (ISupply_air_relative_humidity_sensor parameter);

	public Set<ISupply_air_relative_humidity_sensor> getUsesSupply_air_relative_humidity_sensor();

}