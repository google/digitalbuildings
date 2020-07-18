package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import www.google.com.digitalbuildings._0_0_1.INo_analysis;
import www.google.com.digitalbuildings._0_0_1.IEquipment;
/**
* Class Ignore 
* Tag to ignore things. To be applied to devices which should not be onboarded.
*/
public interface IIgnore extends IEquipment, INo_analysis{

	public IRI iri();

}