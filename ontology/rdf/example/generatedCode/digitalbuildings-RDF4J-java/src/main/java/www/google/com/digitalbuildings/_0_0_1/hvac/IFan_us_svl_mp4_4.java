package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_static_pressure_sensor;
/**
* Class Fan_us_svl_mp4_4 
* Hash:b0ca60c549d1ba9493310cb1e832003a645a704cb4e659e28312336fc8048222; Entities: US-SVL-MP4:FAN:KEF-1 SF
*/
public interface IFan_us_svl_mp4_4 extends IFan_ss_vsc{

	public IRI iri();

    public void addUsesExhaust_air_static_pressure_sensor (IExhaust_air_static_pressure_sensor parameter);

	public Set<IExhaust_air_static_pressure_sensor> getUsesExhaust_air_static_pressure_sensor();

}