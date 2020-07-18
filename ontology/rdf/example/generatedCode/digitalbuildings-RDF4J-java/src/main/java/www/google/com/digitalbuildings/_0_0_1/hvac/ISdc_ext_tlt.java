package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.fields.IShade_tilt_percentage_command;
/**
* Class Sdc_ext_tlt 
* Simple shade with extension and tilt control.
*/
public interface ISdc_ext_tlt extends ISdc_ext{

	public IRI iri();

    public void addUsesShade_tilt_percentage_command (IShade_tilt_percentage_command parameter);

	public Set<IShade_tilt_percentage_command> getUsesShade_tilt_percentage_command();

}