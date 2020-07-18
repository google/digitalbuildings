package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.fields.IWest_illuminance_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IWest_wind_linearvelocity_sensor;
/**
* Class Sdc_ext_tlt_west 
* Directional shade (West).
*/
public interface ISdc_ext_tlt_west extends ISdc_ext_tlt{

	public IRI iri();

    public void addUsesWest_illuminance_sensor (IWest_illuminance_sensor parameter);

	public Set<IWest_illuminance_sensor> getUsesWest_illuminance_sensor();

    public void addUsesWest_wind_linearvelocity_sensor (IWest_wind_linearvelocity_sensor parameter);

	public Set<IWest_wind_linearvelocity_sensor> getUsesWest_wind_linearvelocity_sensor();

}