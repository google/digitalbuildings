package www.google.com.digitalbuildings._0_0_1.facilities;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
/**
* Class Building 
* This is a type for BUILDING facilities object
*/
public interface IBuilding extends IPhysicalLocation{

	public IRI iri();

    public void addFloor(IFloor parameter);

	public Set<IFloor> getFloors();

}