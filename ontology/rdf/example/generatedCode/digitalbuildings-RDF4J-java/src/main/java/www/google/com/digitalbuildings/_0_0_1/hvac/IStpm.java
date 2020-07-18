package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IShade_tilt_percentage_command;
/**
* Class Stpm 
* Shade tilt monitoring.
*/
public interface IStpm extends IFunctionality, IMonitoring{

	public IRI iri();

    public void addUsesShade_tilt_percentage_command (IShade_tilt_percentage_command parameter);

	public Set<IShade_tilt_percentage_command> getUsesShade_tilt_percentage_command();

}