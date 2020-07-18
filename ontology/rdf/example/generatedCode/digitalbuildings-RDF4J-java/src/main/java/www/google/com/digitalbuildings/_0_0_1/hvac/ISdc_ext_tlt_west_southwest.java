package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.fields.ISouthwest_illuminance_sensor;
/**
* Class Sdc_ext_tlt_west_southwest 
* Multi-directional shade (West and Southwest).
*/
public interface ISdc_ext_tlt_west_southwest extends ISdc_ext_tlt_west{

	public IRI iri();

    public void addUsesSouthwest_illuminance_sensor (ISouthwest_illuminance_sensor parameter);

	public Set<ISouthwest_illuminance_sensor> getUsesSouthwest_illuminance_sensor();

}