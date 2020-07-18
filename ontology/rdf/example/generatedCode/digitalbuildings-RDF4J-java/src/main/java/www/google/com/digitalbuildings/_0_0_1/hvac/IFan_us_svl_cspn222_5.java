package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_temperature_sensor;
/**
* Class Fan_us_svl_cspn222_5 
* Non-standard type for CSPN222 KEFs
*/
public interface IFan_us_svl_cspn222_5 extends IFan_ss_vsc{

	public IRI iri();

    public void addUsesExhaust_air_temperature_sensor (IExhaust_air_temperature_sensor parameter);

	public Set<IExhaust_air_temperature_sensor> getUsesExhaust_air_temperature_sensor();

}