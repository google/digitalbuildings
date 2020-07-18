package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.fields.ICogeneration_return_water_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.ICogeneration_supply_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICogeneration_return_water_temperature_sensor;
/**
* Class Cgrwtc 
* Cogeneration return water temperature control.
*/
public interface ICgrwtc extends IFunctionality, IOperational{

	public IRI iri();

    public void addUsesCogeneration_return_water_temperature_sensor (ICogeneration_return_water_temperature_sensor parameter);

	public Set<ICogeneration_return_water_temperature_sensor> getUsesCogeneration_return_water_temperature_sensor();

    public void addUsesCogeneration_return_water_temperature_setpoint (ICogeneration_return_water_temperature_setpoint parameter);

	public Set<ICogeneration_return_water_temperature_setpoint> getUsesCogeneration_return_water_temperature_setpoint();

    public void addUsesOptionalsCogeneration_supply_water_temperature_sensor (ICogeneration_supply_water_temperature_sensor parameter);

	public Set<ICogeneration_supply_water_temperature_sensor> getUsesOptionalsCogeneration_supply_water_temperature_sensor();

}