package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IEconomizer_mode;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_relative_humidity_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_flowrate_requirement;
/**
* Class Ztm 
* Zone temperature monitoring.
*/
public interface IZtm extends IFunctionality, IMonitoring{

	public IRI iri();

    public void addUsesOptionalsOutside_air_flowrate_requirement (IOutside_air_flowrate_requirement parameter);

	public Set<IOutside_air_flowrate_requirement> getUsesOptionalsOutside_air_flowrate_requirement();

    public void addUsesOptionalsEconomizer_mode (IEconomizer_mode parameter);

	public Set<IEconomizer_mode> getUsesOptionalsEconomizer_mode();

    public void addUsesZone_air_relative_humidity_sensor (IZone_air_relative_humidity_sensor parameter);

	public Set<IZone_air_relative_humidity_sensor> getUsesZone_air_relative_humidity_sensor();

}