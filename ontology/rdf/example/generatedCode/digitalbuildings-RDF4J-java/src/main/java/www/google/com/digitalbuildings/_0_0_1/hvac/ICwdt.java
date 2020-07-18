package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.fields.ICondensing_supply_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICondensing_return_water_temperature_sensor;
/**
* Class Cwdt 
* Temperature differential across condenser water.
*/
public interface ICwdt extends IFunctionality, IMonitoring{

	public IRI iri();

    public void addUsesCondensing_return_water_temperature_sensor (ICondensing_return_water_temperature_sensor parameter);

	public Set<ICondensing_return_water_temperature_sensor> getUsesCondensing_return_water_temperature_sensor();

    public void addUsesCondensing_supply_water_temperature_sensor (ICondensing_supply_water_temperature_sensor parameter);

	public Set<ICondensing_supply_water_temperature_sensor> getUsesCondensing_supply_water_temperature_sensor();

}