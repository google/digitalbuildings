package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.fields.IShade_extent_percentage_command;
/**
* Class Sdc_ext 
* Simple shade with extension control only.
*/
public interface ISdc_ext extends ISdc{

	public IRI iri();

    public void addUsesShade_extent_percentage_command (IShade_extent_percentage_command parameter);

	public Set<IShade_extent_percentage_command> getUsesShade_extent_percentage_command();

}