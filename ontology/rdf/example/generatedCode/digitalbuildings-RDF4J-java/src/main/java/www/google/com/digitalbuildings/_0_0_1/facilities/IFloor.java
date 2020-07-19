package www.google.com.digitalbuildings._0_0_1.facilities;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
/**
* Class Floor 
* This is a type for FLOOR facilities object
*/
public interface IFloor extends IPhysicalLocation{

	public IRI iri();

    public void addRoom(IRoom parameter);

	public Set<IRoom> getRooms();

}