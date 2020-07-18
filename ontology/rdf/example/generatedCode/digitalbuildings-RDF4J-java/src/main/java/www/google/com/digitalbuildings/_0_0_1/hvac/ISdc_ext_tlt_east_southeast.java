package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.fields.ISoutheast_illuminance_sensor;
/**
* Class Sdc_ext_tlt_east_southeast 
* Multi-directional shade (East and Southeast).
*/
public interface ISdc_ext_tlt_east_southeast extends ISdc_ext_tlt_east{

	public IRI iri();

    public void addUsesSoutheast_illuminance_sensor (ISoutheast_illuminance_sensor parameter);

	public Set<ISoutheast_illuminance_sensor> getUsesSoutheast_illuminance_sensor();

}