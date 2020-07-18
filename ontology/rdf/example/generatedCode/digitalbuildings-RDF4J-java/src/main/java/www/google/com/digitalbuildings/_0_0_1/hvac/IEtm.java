package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_temperature_sensor;
/**
* Class Etm 
* Basic exhaust temperature monitoring.
*/
public interface IEtm extends IFunctionality, IMonitoring{

	public IRI iri();

    public void addUsesExhaust_air_temperature_sensor (IExhaust_air_temperature_sensor parameter);

	public Set<IExhaust_air_temperature_sensor> getUsesExhaust_air_temperature_sensor();

}