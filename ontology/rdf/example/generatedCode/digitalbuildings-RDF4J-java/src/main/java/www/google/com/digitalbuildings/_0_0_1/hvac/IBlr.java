package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IEquipment;
import www.google.com.digitalbuildings._0_0_1.fields.IFlowrate_requirement;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_thermal_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IEfficiency_percentage_specification;
import www.google.com.digitalbuildings._0_0_1.fields.IHeating_input_thermal_power_capacity;
/**
* Class Blr 
* Tag for boilers.
*/
public interface IBlr extends IEquipment{

	public IRI iri();

    public void addUsesOptionalsEfficiency_percentage_specification (IEfficiency_percentage_specification parameter);

	public Set<IEfficiency_percentage_specification> getUsesOptionalsEfficiency_percentage_specification();

    public void addUsesOptionalsFlowrate_requirement (IFlowrate_requirement parameter);

	public Set<IFlowrate_requirement> getUsesOptionalsFlowrate_requirement();

    public void addUsesOptionalsHeating_input_thermal_power_capacity (IHeating_input_thermal_power_capacity parameter);

	public Set<IHeating_input_thermal_power_capacity> getUsesOptionalsHeating_input_thermal_power_capacity();

    public void addUsesOptionalsHeating_thermal_power_capacity (IHeating_thermal_power_capacity parameter);

	public Set<IHeating_thermal_power_capacity> getUsesOptionalsHeating_thermal_power_capacity();

}