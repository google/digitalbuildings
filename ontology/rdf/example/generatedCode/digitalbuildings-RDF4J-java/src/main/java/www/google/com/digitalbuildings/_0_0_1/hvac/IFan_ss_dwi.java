package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.fields.IDishwasher_run_status;
/**
* Class Fan_ss_dwi 
* Dishwasher-interlocked fan.
*/
public interface IFan_ss_dwi extends IFan, ISs{

	public IRI iri();

    public void addUsesDishwasher_run_status (IDishwasher_run_status parameter);

	public Set<IDishwasher_run_status> getUsesDishwasher_run_status();

}