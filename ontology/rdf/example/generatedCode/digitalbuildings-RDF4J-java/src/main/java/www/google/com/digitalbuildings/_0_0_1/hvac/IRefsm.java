package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IRefrigerant_evaporator_saturation_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IRefrigerant_condenser_saturation_temperature_sensor;
/**
* Class Refsm 
* Refrigerant saturation monitoring.
*/
public interface IRefsm extends IFunctionality, IMonitoring{

	public IRI iri();

    public void addUsesRefrigerant_condenser_saturation_temperature_sensor (IRefrigerant_condenser_saturation_temperature_sensor parameter);

	public Set<IRefrigerant_condenser_saturation_temperature_sensor> getUsesRefrigerant_condenser_saturation_temperature_sensor();

    public void addUsesRefrigerant_evaporator_saturation_temperature_sensor (IRefrigerant_evaporator_saturation_temperature_sensor parameter);

	public Set<IRefrigerant_evaporator_saturation_temperature_sensor> getUsesRefrigerant_evaporator_saturation_temperature_sensor();

}