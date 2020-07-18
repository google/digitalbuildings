package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.fields.IDial_resistance_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Dial_resistance_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IThermal_power_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Thermal_power_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IMaster_alarm_status;
import www.google.com.digitalbuildings._0_0_1.fields.Master_alarm_status;
import www.google.com.digitalbuildings._0_0_1.fields.IRun_mode;
import www.google.com.digitalbuildings._0_0_1.fields.Run_mode;
import www.google.com.digitalbuildings._0_0_1.fields.IFilter_alarm_status;
import www.google.com.digitalbuildings._0_0_1.fields.Filter_alarm_status;

/**
* Class Fcu_uk_lon_6ps_1 
* Non-standard type for 6PS
*/
@SuppressWarnings("serial")
public class Fcu_uk_lon_6ps_1 extends www.google.com.digitalbuildings._0_0_1.hvac.Fcu_dfss_dfvsc_ztc_chwztc_hwztc implements IFcu_uk_lon_6ps_1{

	IRI newInstance;
	public Fcu_uk_lon_6ps_1(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Fcu_uk_lon_6ps_1"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesDial_resistance_sensor (IDial_resistance_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IDial_resistance_sensor> getUsesDial_resistance_sensor (){
		Set<IDial_resistance_sensor> UsesDial_resistance_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Dial_resistance_sensor) {
				UsesDial_resistance_sensor.add((Dial_resistance_sensor)action);
			}
		});
		return UsesDial_resistance_sensor;
	}


  public void addUsesDischarge_air_flowrate_sensor (IDischarge_air_flowrate_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IDischarge_air_flowrate_sensor> getUsesDischarge_air_flowrate_sensor (){
		Set<IDischarge_air_flowrate_sensor> UsesDischarge_air_flowrate_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Discharge_air_flowrate_sensor) {
				UsesDischarge_air_flowrate_sensor.add((Discharge_air_flowrate_sensor)action);
			}
		});
		return UsesDischarge_air_flowrate_sensor;
	}


  public void addUsesFilter_alarm_status (IFilter_alarm_status parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IFilter_alarm_status> getUsesFilter_alarm_status (){
		Set<IFilter_alarm_status> UsesFilter_alarm_status = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Filter_alarm_status) {
				UsesFilter_alarm_status.add((Filter_alarm_status)action);
			}
		});
		return UsesFilter_alarm_status;
	}


  public void addUsesMaster_alarm_status (IMaster_alarm_status parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IMaster_alarm_status> getUsesMaster_alarm_status (){
		Set<IMaster_alarm_status> UsesMaster_alarm_status = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Master_alarm_status) {
				UsesMaster_alarm_status.add((Master_alarm_status)action);
			}
		});
		return UsesMaster_alarm_status;
	}


  public void addUsesRun_mode (IRun_mode parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IRun_mode> getUsesRun_mode (){
		Set<IRun_mode> UsesRun_mode = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Run_mode) {
				UsesRun_mode.add((Run_mode)action);
			}
		});
		return UsesRun_mode;
	}


  public void addUsesThermal_power_sensor (IThermal_power_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IThermal_power_sensor> getUsesThermal_power_sensor (){
		Set<IThermal_power_sensor> UsesThermal_power_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Thermal_power_sensor) {
				UsesThermal_power_sensor.add((Thermal_power_sensor)action);
			}
		});
		return UsesThermal_power_sensor;
	}

	public static Set<IFcu_uk_lon_6ps_1> getAllFcu_uk_lon_6ps_1sObjectsCreated(){
		Set<IFcu_uk_lon_6ps_1> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Fcu_uk_lon_6ps_1")).subjects().stream()
		.map(mapper->(IFcu_uk_lon_6ps_1)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}