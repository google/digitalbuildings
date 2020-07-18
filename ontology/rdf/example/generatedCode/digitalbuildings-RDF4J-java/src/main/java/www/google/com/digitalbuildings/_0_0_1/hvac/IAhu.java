package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IEquipment;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_flowrate_requirement;
/**
* Class Ahu 
* Tag for air-handling units.
*/
public interface IAhu extends IEquipment{

	public IRI iri();

    public void addUsesOptionalsOutside_air_flowrate_requirement (IOutside_air_flowrate_requirement parameter);

	public Set<IOutside_air_flowrate_requirement> getUsesOptionalsOutside_air_flowrate_requirement();

}