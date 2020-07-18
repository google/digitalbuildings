package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.fields.IEast_illuminance_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IEast_wind_linearvelocity_sensor;
/**
* Class Sdc_ext_tlt_east 
* Directional shade (East).
*/
public interface ISdc_ext_tlt_east extends ISdc_ext_tlt{

	public IRI iri();

    public void addUsesEast_illuminance_sensor (IEast_illuminance_sensor parameter);

	public Set<IEast_illuminance_sensor> getUsesEast_illuminance_sensor();

    public void addUsesEast_wind_linearvelocity_sensor (IEast_wind_linearvelocity_sensor parameter);

	public Set<IEast_wind_linearvelocity_sensor> getUsesEast_wind_linearvelocity_sensor();

}