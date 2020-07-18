package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_air_relative_humidity_sensor;
/**
* Class Rhm 
* Return air humidity monitoring.
*/
public interface IRhm extends IFunctionality, IMonitoring{

	public IRI iri();

    public void addUsesReturn_air_relative_humidity_sensor (IReturn_air_relative_humidity_sensor parameter);

	public Set<IReturn_air_relative_humidity_sensor> getUsesReturn_air_relative_humidity_sensor();

}