package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_damper_command;
/**
* Class Oadm 
* Outside air damper monitoring.
*/
public interface IOadm extends IFunctionality{

	public IRI iri();

    public void addUsesOutside_air_damper_command (IOutside_air_damper_command parameter);

	public Set<IOutside_air_damper_command> getUsesOutside_air_damper_command();

}