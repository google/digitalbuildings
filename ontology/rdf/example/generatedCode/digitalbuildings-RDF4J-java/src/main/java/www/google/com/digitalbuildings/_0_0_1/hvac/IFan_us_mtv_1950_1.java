package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.fields.IDryer_run_status_1;
import www.google.com.digitalbuildings._0_0_1.fields.IDryer_run_status_2;
/**
* Class Fan_us_mtv_1950_1 
* Non-standard type for 1950
*/
public interface IFan_us_mtv_1950_1 extends IFan_ss{

	public IRI iri();

    public void addUsesDryer_run_status_1 (IDryer_run_status_1 parameter);

	public Set<IDryer_run_status_1> getUsesDryer_run_status_1();

    public void addUsesDryer_run_status_2 (IDryer_run_status_2 parameter);

	public Set<IDryer_run_status_2> getUsesDryer_run_status_2();

}