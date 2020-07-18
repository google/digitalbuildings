package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_supply_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_return_water_temperature_sensor;
/**
* Class Chwdt 
* Temperature differential across chilled water.
*/
public interface IChwdt extends IFunctionality, IMonitoring{

	public IRI iri();

    public void addUsesChilled_return_water_temperature_sensor (IChilled_return_water_temperature_sensor parameter);

	public Set<IChilled_return_water_temperature_sensor> getUsesChilled_return_water_temperature_sensor();

    public void addUsesChilled_supply_water_temperature_sensor (IChilled_supply_water_temperature_sensor parameter);

	public Set<IChilled_supply_water_temperature_sensor> getUsesChilled_supply_water_temperature_sensor();

}