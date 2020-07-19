package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.facilities.IPhysicalLocation;
import www.google.com.digitalbuildings._0_0_1.fields.IDryer_run_status;
/**
* Class Fan_ss_dri 
* Dryer-interlocked fan.
*/
public interface IFan_ss_dri extends IFan, ISs{

	public IRI iri();

    public void addUsesDryer_run_status (IDryer_run_status parameter);

	public Set<IDryer_run_status> getUsesDryer_run_status();

    public void addPhysicalLocation(IPhysicalLocation parameter);

	public Set<IPhysicalLocation> getPhysicalLocation();

}