package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_damper_percentage_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_damper_percentage_command_2;
/**
* Class Fan_us_svl_mp4_3 
* Non-standard type for MP4
*/
public interface IFan_us_svl_mp4_3 extends IFan_ss_vsc_bspc{

	public IRI iri();

    public void addUsesExhaust_air_damper_percentage_command_1 (IExhaust_air_damper_percentage_command_1 parameter);

	public Set<IExhaust_air_damper_percentage_command_1> getUsesExhaust_air_damper_percentage_command_1();

    public void addUsesExhaust_air_damper_percentage_command_2 (IExhaust_air_damper_percentage_command_2 parameter);

	public Set<IExhaust_air_damper_percentage_command_2> getUsesExhaust_air_damper_percentage_command_2();

}