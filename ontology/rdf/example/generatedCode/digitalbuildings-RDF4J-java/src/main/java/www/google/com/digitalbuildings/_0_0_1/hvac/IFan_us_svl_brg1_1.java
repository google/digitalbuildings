package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_occupancy_status;
/**
* Class Fan_us_svl_brg1_1 
* Non-standard type for BRG1
*/
public interface IFan_us_svl_brg1_1 extends IFan_ss{

	public IRI iri();

    public void addUsesZone_occupancy_status (IZone_occupancy_status parameter);

	public Set<IZone_occupancy_status> getUsesZone_occupancy_status();

}