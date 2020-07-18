package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IShade_extent_percentage_command;
/**
* Class Sepm 
* Shade extent monitoring.
*/
public interface ISepm extends IFunctionality, IMonitoring{

	public IRI iri();

    public void addUsesShade_extent_percentage_command (IShade_extent_percentage_command parameter);

	public Set<IShade_extent_percentage_command> getUsesShade_extent_percentage_command();

}