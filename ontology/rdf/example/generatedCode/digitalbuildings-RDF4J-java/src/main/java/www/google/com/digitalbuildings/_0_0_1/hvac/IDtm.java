package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_air_temperature_sensor;
/**
* Class Dtm 
* Discharge temperature monitoring.
*/
public interface IDtm extends IFunctionality, IMonitoring{

	public IRI iri();

    public void addUsesDischarge_air_temperature_sensor (IDischarge_air_temperature_sensor parameter);

	public Set<IDischarge_air_temperature_sensor> getUsesDischarge_air_temperature_sensor();

}