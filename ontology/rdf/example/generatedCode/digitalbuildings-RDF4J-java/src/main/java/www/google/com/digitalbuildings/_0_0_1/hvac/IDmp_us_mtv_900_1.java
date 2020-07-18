package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_damper_percentage_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_damper_percentage_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.IWest_building_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IEast_building_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_air_damper_command;
/**
* Class Dmp_us_mtv_900_1 
* Non-standard type for SBO-900
*/
public interface IDmp_us_mtv_900_1 extends IDmp{

	public IRI iri();

    public void addUsesEast_building_air_static_pressure_sensor (IEast_building_air_static_pressure_sensor parameter);

	public Set<IEast_building_air_static_pressure_sensor> getUsesEast_building_air_static_pressure_sensor();

    public void addUsesReturn_air_damper_command (IReturn_air_damper_command parameter);

	public Set<IReturn_air_damper_command> getUsesReturn_air_damper_command();

    public void addUsesSupply_air_damper_percentage_command_1 (ISupply_air_damper_percentage_command_1 parameter);

	public Set<ISupply_air_damper_percentage_command_1> getUsesSupply_air_damper_percentage_command_1();

    public void addUsesSupply_air_damper_percentage_command_2 (ISupply_air_damper_percentage_command_2 parameter);

	public Set<ISupply_air_damper_percentage_command_2> getUsesSupply_air_damper_percentage_command_2();

    public void addUsesWest_building_air_static_pressure_sensor (IWest_building_air_static_pressure_sensor parameter);

	public Set<IWest_building_air_static_pressure_sensor> getUsesWest_building_air_static_pressure_sensor();

}