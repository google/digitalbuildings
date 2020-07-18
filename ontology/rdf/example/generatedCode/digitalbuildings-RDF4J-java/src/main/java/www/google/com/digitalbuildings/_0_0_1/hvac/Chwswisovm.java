package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.Monitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IRefrigerant_condenser_saturation_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Refrigerant_condenser_saturation_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICondenser_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Condenser_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_supply_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Chilled_supply_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_water_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_return_water_isolation_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Chilled_return_water_isolation_valve_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_supply_water_isolation_valve_command;
import www.google.com.digitalbuildings._0_0_1.fields.Chilled_supply_water_isolation_valve_command;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_supply_water_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Chilled_supply_water_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_return_water_isolation_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Chilled_return_water_isolation_valve_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.Compressor_run_command;
import www.google.com.digitalbuildings._0_0_1.fields.IRefrigerant_evaporator_saturation_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Refrigerant_evaporator_saturation_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IDifferential_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Differential_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IEvaporator_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Evaporator_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICompressor_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.Compressor_run_status;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_supply_water_isolation_valve_status;
import www.google.com.digitalbuildings._0_0_1.fields.Chilled_supply_water_isolation_valve_status;

/**
* Class Chwswisovm 
* Supply side isolation valve monitoring.
*/
@SuppressWarnings("serial")
public class Chwswisovm extends www.google.com.digitalbuildings._0_0_1.Monitoring implements IChwswisovm{

	IRI newInstance;
	public Chwswisovm(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Chwswisovm"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesChilled_supply_water_isolation_valve_command (IChilled_supply_water_isolation_valve_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IChilled_supply_water_isolation_valve_command> getUsesChilled_supply_water_isolation_valve_command (){
		Set<IChilled_supply_water_isolation_valve_command> UsesChilled_supply_water_isolation_valve_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Chilled_supply_water_isolation_valve_command) {
				UsesChilled_supply_water_isolation_valve_command.add((Chilled_supply_water_isolation_valve_command)action);
			}
		});
		return UsesChilled_supply_water_isolation_valve_command;
	}


  public void addUsesChilled_supply_water_isolation_valve_status (IChilled_supply_water_isolation_valve_status parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IChilled_supply_water_isolation_valve_status> getUsesChilled_supply_water_isolation_valve_status (){
		Set<IChilled_supply_water_isolation_valve_status> UsesChilled_supply_water_isolation_valve_status = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Chilled_supply_water_isolation_valve_status) {
				UsesChilled_supply_water_isolation_valve_status.add((Chilled_supply_water_isolation_valve_status)action);
			}
		});
		return UsesChilled_supply_water_isolation_valve_status;
	}


  public void addUsesRefrigerant_condenser_saturation_temperature_sensor (IRefrigerant_condenser_saturation_temperature_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IRefrigerant_condenser_saturation_temperature_sensor> getUsesRefrigerant_condenser_saturation_temperature_sensor (){
		Set<IRefrigerant_condenser_saturation_temperature_sensor> UsesRefrigerant_condenser_saturation_temperature_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Refrigerant_condenser_saturation_temperature_sensor) {
				UsesRefrigerant_condenser_saturation_temperature_sensor.add((Refrigerant_condenser_saturation_temperature_sensor)action);
			}
		});
		return UsesRefrigerant_condenser_saturation_temperature_sensor;
	}


  public void addUsesRefrigerant_evaporator_saturation_temperature_sensor (IRefrigerant_evaporator_saturation_temperature_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IRefrigerant_evaporator_saturation_temperature_sensor> getUsesRefrigerant_evaporator_saturation_temperature_sensor (){
		Set<IRefrigerant_evaporator_saturation_temperature_sensor> UsesRefrigerant_evaporator_saturation_temperature_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Refrigerant_evaporator_saturation_temperature_sensor) {
				UsesRefrigerant_evaporator_saturation_temperature_sensor.add((Refrigerant_evaporator_saturation_temperature_sensor)action);
			}
		});
		return UsesRefrigerant_evaporator_saturation_temperature_sensor;
	}


  public void addUsesChilled_supply_water_temperature_sensor (IChilled_supply_water_temperature_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IChilled_supply_water_temperature_sensor> getUsesChilled_supply_water_temperature_sensor (){
		Set<IChilled_supply_water_temperature_sensor> UsesChilled_supply_water_temperature_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Chilled_supply_water_temperature_sensor) {
				UsesChilled_supply_water_temperature_sensor.add((Chilled_supply_water_temperature_sensor)action);
			}
		});
		return UsesChilled_supply_water_temperature_sensor;
	}


  public void addUsesChilled_supply_water_temperature_setpoint (IChilled_supply_water_temperature_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IChilled_supply_water_temperature_setpoint> getUsesChilled_supply_water_temperature_setpoint (){
		Set<IChilled_supply_water_temperature_setpoint> UsesChilled_supply_water_temperature_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Chilled_supply_water_temperature_setpoint) {
				UsesChilled_supply_water_temperature_setpoint.add((Chilled_supply_water_temperature_setpoint)action);
			}
		});
		return UsesChilled_supply_water_temperature_setpoint;
	}


  public void addUsesChilled_return_water_isolation_valve_percentage_command (IChilled_return_water_isolation_valve_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IChilled_return_water_isolation_valve_percentage_command> getUsesChilled_return_water_isolation_valve_percentage_command (){
		Set<IChilled_return_water_isolation_valve_percentage_command> UsesChilled_return_water_isolation_valve_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Chilled_return_water_isolation_valve_percentage_command) {
				UsesChilled_return_water_isolation_valve_percentage_command.add((Chilled_return_water_isolation_valve_percentage_command)action);
			}
		});
		return UsesChilled_return_water_isolation_valve_percentage_command;
	}


  public void addUsesChilled_return_water_isolation_valve_percentage_sensor (IChilled_return_water_isolation_valve_percentage_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IChilled_return_water_isolation_valve_percentage_sensor> getUsesChilled_return_water_isolation_valve_percentage_sensor (){
		Set<IChilled_return_water_isolation_valve_percentage_sensor> UsesChilled_return_water_isolation_valve_percentage_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Chilled_return_water_isolation_valve_percentage_sensor) {
				UsesChilled_return_water_isolation_valve_percentage_sensor.add((Chilled_return_water_isolation_valve_percentage_sensor)action);
			}
		});
		return UsesChilled_return_water_isolation_valve_percentage_sensor;
	}


  public void addUsesCondenser_pressure_sensor (ICondenser_pressure_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ICondenser_pressure_sensor> getUsesCondenser_pressure_sensor (){
		Set<ICondenser_pressure_sensor> UsesCondenser_pressure_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Condenser_pressure_sensor) {
				UsesCondenser_pressure_sensor.add((Condenser_pressure_sensor)action);
			}
		});
		return UsesCondenser_pressure_sensor;
	}


  public void addUsesDifferential_pressure_sensor (IDifferential_pressure_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IDifferential_pressure_sensor> getUsesDifferential_pressure_sensor (){
		Set<IDifferential_pressure_sensor> UsesDifferential_pressure_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Differential_pressure_sensor) {
				UsesDifferential_pressure_sensor.add((Differential_pressure_sensor)action);
			}
		});
		return UsesDifferential_pressure_sensor;
	}


  public void addUsesEvaporator_pressure_sensor (IEvaporator_pressure_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IEvaporator_pressure_sensor> getUsesEvaporator_pressure_sensor (){
		Set<IEvaporator_pressure_sensor> UsesEvaporator_pressure_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Evaporator_pressure_sensor) {
				UsesEvaporator_pressure_sensor.add((Evaporator_pressure_sensor)action);
			}
		});
		return UsesEvaporator_pressure_sensor;
	}


  public void addUsesCompressor_run_command (ICompressor_run_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ICompressor_run_command> getUsesCompressor_run_command (){
		Set<ICompressor_run_command> UsesCompressor_run_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Compressor_run_command) {
				UsesCompressor_run_command.add((Compressor_run_command)action);
			}
		});
		return UsesCompressor_run_command;
	}


  public void addUsesCompressor_run_status (ICompressor_run_status parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ICompressor_run_status> getUsesCompressor_run_status (){
		Set<ICompressor_run_status> UsesCompressor_run_status = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Compressor_run_status) {
				UsesCompressor_run_status.add((Compressor_run_status)action);
			}
		});
		return UsesCompressor_run_status;
	}


  public void addUsesSupply_water_temperature_sensor (ISupply_water_temperature_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_water_temperature_sensor> getUsesSupply_water_temperature_sensor (){
		Set<ISupply_water_temperature_sensor> UsesSupply_water_temperature_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_water_temperature_sensor) {
				UsesSupply_water_temperature_sensor.add((Supply_water_temperature_sensor)action);
			}
		});
		return UsesSupply_water_temperature_sensor;
	}


  public void addUsesSupply_water_temperature_setpoint (ISupply_water_temperature_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_water_temperature_setpoint> getUsesSupply_water_temperature_setpoint (){
		Set<ISupply_water_temperature_setpoint> UsesSupply_water_temperature_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_water_temperature_setpoint) {
				UsesSupply_water_temperature_setpoint.add((Supply_water_temperature_setpoint)action);
			}
		});
		return UsesSupply_water_temperature_setpoint;
	}

	public static Set<IChwswisovm> getAllChwswisovmsObjectsCreated(){
		Set<IChwswisovm> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Chwswisovm")).subjects().stream()
		.map(mapper->(IChwswisovm)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}