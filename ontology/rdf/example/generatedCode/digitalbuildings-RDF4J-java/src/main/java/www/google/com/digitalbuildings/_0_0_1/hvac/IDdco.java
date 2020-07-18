package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.IControl;
import www.google.com.digitalbuildings._0_0_1.fields.ICooling_air_damper_percentage_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.ICooling_air_flowrate_setpoint_1;
import www.google.com.digitalbuildings._0_0_1.fields.ICooling_air_flowrate_setpoint_2;
import www.google.com.digitalbuildings._0_0_1.fields.ICooling_air_damper_percentage_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.ICooling_air_flowrate_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.ICooling_air_flowrate_sensor_1;
/**
* Class Ddco 
* Flow control - dual duct, but only cooling.
*/
public interface IDdco extends IFunctionality, IControl{

	public IRI iri();

    public void addUsesCooling_air_damper_percentage_command_1 (ICooling_air_damper_percentage_command_1 parameter);

	public Set<ICooling_air_damper_percentage_command_1> getUsesCooling_air_damper_percentage_command_1();

    public void addUsesCooling_air_damper_percentage_command_2 (ICooling_air_damper_percentage_command_2 parameter);

	public Set<ICooling_air_damper_percentage_command_2> getUsesCooling_air_damper_percentage_command_2();

    public void addUsesCooling_air_flowrate_sensor_1 (ICooling_air_flowrate_sensor_1 parameter);

	public Set<ICooling_air_flowrate_sensor_1> getUsesCooling_air_flowrate_sensor_1();

    public void addUsesCooling_air_flowrate_sensor_2 (ICooling_air_flowrate_sensor_2 parameter);

	public Set<ICooling_air_flowrate_sensor_2> getUsesCooling_air_flowrate_sensor_2();

    public void addUsesCooling_air_flowrate_setpoint_1 (ICooling_air_flowrate_setpoint_1 parameter);

	public Set<ICooling_air_flowrate_setpoint_1> getUsesCooling_air_flowrate_setpoint_1();

    public void addUsesCooling_air_flowrate_setpoint_2 (ICooling_air_flowrate_setpoint_2 parameter);

	public Set<ICooling_air_flowrate_setpoint_2> getUsesCooling_air_flowrate_setpoint_2();

}