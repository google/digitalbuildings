package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.facilities.IPhysicalLocation;
/**
* Class Fan_ss 
* Basic fan with start/stop and status.
*/
public interface IFan_ss extends IFan, ISs{

	public IRI iri();

    public void addPhysicalLocation (IPhysicalLocation parameter);

	public Set<IPhysicalLocation> getPhysicalLocation();

}