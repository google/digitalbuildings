package www.google.com.digitalbuildings._0_0_1.facilities;

import org.eclipse.rdf4j.model.IRI;
import www.google.com.digitalbuildings._0_0_1.IEntityType;
/**
* Class PhysicalLocation 
* The class of all physical locations
*/
public interface IPhysicalLocation extends IEntityType{

	public IRI iri();


	public void setCode (String parameter);

	public String getCode ();

	public void setFriendlyName (String parameter);

	public String getFriendlyName ();
}