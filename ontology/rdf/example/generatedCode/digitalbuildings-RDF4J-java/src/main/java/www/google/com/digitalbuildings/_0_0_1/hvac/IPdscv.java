package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IControl;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_damper_percentage_sensor;
/**
* Class Pdscv 
* Pressure-dependent supply damper control for ventilation purposes (CO2 or VOC).
*/
public interface IPdscv extends IFunctionality, IControl{

	public IRI iri();

    public void addUsesSupply_air_damper_percentage_command (ISupply_air_damper_percentage_command parameter);

	public Set<ISupply_air_damper_percentage_command> getUsesSupply_air_damper_percentage_command();

    public void addUsesSupply_air_damper_percentage_sensor (ISupply_air_damper_percentage_sensor parameter);

	public Set<ISupply_air_damper_percentage_sensor> getUsesSupply_air_damper_percentage_sensor();

}