package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_temperature_sensor;
/**
* Class Wdt 
* Temperature differential across water.
*/
public interface IWdt extends IFunctionality, IMonitoring{

	public IRI iri();

    public void addUsesReturn_water_temperature_sensor (IReturn_water_temperature_sensor parameter);

	public Set<IReturn_water_temperature_sensor> getUsesReturn_water_temperature_sensor();

    public void addUsesSupply_water_temperature_sensor (ISupply_water_temperature_sensor parameter);

	public Set<ISupply_water_temperature_sensor> getUsesSupply_water_temperature_sensor();

}