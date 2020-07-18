package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.fields.IDishwasher_run_status;
/**
* Class Fan_us_svl_mp7_2 
* Non-standard type for MP7
*/
public interface IFan_us_svl_mp7_2 extends IFan_ss_vsc{

	public IRI iri();

    public void addUsesDishwasher_run_status (IDishwasher_run_status parameter);

	public Set<IDishwasher_run_status> getUsesDishwasher_run_status();

}