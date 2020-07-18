package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IEquipment;
import www.google.com.digitalbuildings._0_0_1.fields.ICooling_thermal_power_capacity;
import www.google.com.digitalbuildings._0_0_1.fields.IFlowrate_requirement;
import www.google.com.digitalbuildings._0_0_1.fields.IEfficiency_percentage_specification;
import www.google.com.digitalbuildings._0_0_1.fields.IPower_capacity;
/**
* Class Ch 
* Tag for chillers.
*/
public interface ICh extends IEquipment{

	public IRI iri();

    public void addUsesOptionalsCooling_thermal_power_capacity (ICooling_thermal_power_capacity parameter);

	public Set<ICooling_thermal_power_capacity> getUsesOptionalsCooling_thermal_power_capacity();

    public void addUsesOptionalsEfficiency_percentage_specification (IEfficiency_percentage_specification parameter);

	public Set<IEfficiency_percentage_specification> getUsesOptionalsEfficiency_percentage_specification();

    public void addUsesOptionalsFlowrate_requirement (IFlowrate_requirement parameter);

	public Set<IFlowrate_requirement> getUsesOptionalsFlowrate_requirement();

    public void addUsesOptionalsPower_capacity (IPower_capacity parameter);

	public Set<IPower_capacity> getUsesOptionalsPower_capacity();

}