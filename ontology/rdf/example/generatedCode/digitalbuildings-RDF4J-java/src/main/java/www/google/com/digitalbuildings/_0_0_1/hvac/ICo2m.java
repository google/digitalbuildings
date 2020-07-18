package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_co2_concentration_sensor;
/**
* Class Co2m 
* Basic carbon dioxide monitoring.
*/
public interface ICo2m extends IFunctionality, IMonitoring{

	public IRI iri();

    public void addUsesZone_air_co2_concentration_sensor (IZone_air_co2_concentration_sensor parameter);

	public Set<IZone_air_co2_concentration_sensor> getUsesZone_air_co2_concentration_sensor();

}