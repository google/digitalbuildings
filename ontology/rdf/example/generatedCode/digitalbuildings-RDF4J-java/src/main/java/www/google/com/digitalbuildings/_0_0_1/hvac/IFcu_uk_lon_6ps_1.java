package www.google.com.digitalbuildings._0_0_1.hvac;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.fields.IDial_resistance_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IThermal_power_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IMaster_alarm_status;
import www.google.com.digitalbuildings._0_0_1.fields.IRun_mode;
import www.google.com.digitalbuildings._0_0_1.fields.IFilter_alarm_status;
/**
* Class Fcu_uk_lon_6ps_1 
* Non-standard type for 6PS
*/
public interface IFcu_uk_lon_6ps_1 extends IFcu_dfss_dfvsc_ztc_chwztc_hwztc{

	public IRI iri();

    public void addUsesDial_resistance_sensor (IDial_resistance_sensor parameter);

	public Set<IDial_resistance_sensor> getUsesDial_resistance_sensor();

    public void addUsesDischarge_air_flowrate_sensor (IDischarge_air_flowrate_sensor parameter);

	public Set<IDischarge_air_flowrate_sensor> getUsesDischarge_air_flowrate_sensor();

    public void addUsesFilter_alarm_status (IFilter_alarm_status parameter);

	public Set<IFilter_alarm_status> getUsesFilter_alarm_status();

    public void addUsesMaster_alarm_status (IMaster_alarm_status parameter);

	public Set<IMaster_alarm_status> getUsesMaster_alarm_status();

    public void addUsesRun_mode (IRun_mode parameter);

	public Set<IRun_mode> getUsesRun_mode();

    public void addUsesThermal_power_sensor (IThermal_power_sensor parameter);

	public Set<IThermal_power_sensor> getUsesThermal_power_sensor();

}