package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Return_water_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IReturn_water_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Return_water_temperature_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IRun_command;
import www.google.com.digitalbuildings._0_0_1.fields.Run_command;

/**
* Class Hws_rwtc_wdpc 
* Simple heating water system with return temp control and differential pressure control.
*/
@SuppressWarnings("serial")
public class Hws_rwtc_wdpc extends www.google.com.digitalbuildings._0_0_1.hvac.Wdpc implements IHws_rwtc_wdpc{

	IRI newInstance;
	public Hws_rwtc_wdpc(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Hws_rwtc_wdpc"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesOptionalsRun_command (IRun_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IRun_command> getUsesOptionalsRun_command (){
		Set<IRun_command> UsesOptionalsRun_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Run_command) {
				UsesOptionalsRun_command.add((Run_command)action);
			}
		});
		return UsesOptionalsRun_command;
	}


  public void addUsesOptionalsSupply_water_temperature_sensor (ISupply_water_temperature_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<ISupply_water_temperature_sensor> getUsesOptionalsSupply_water_temperature_sensor (){
		Set<ISupply_water_temperature_sensor> UsesOptionalsSupply_water_temperature_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_water_temperature_sensor) {
				UsesOptionalsSupply_water_temperature_sensor.add((Supply_water_temperature_sensor)action);
			}
		});
		return UsesOptionalsSupply_water_temperature_sensor;
	}


  public void addUsesReturn_water_temperature_sensor (IReturn_water_temperature_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IReturn_water_temperature_sensor> getUsesReturn_water_temperature_sensor (){
		Set<IReturn_water_temperature_sensor> UsesReturn_water_temperature_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Return_water_temperature_sensor) {
				UsesReturn_water_temperature_sensor.add((Return_water_temperature_sensor)action);
			}
		});
		return UsesReturn_water_temperature_sensor;
	}


  public void addUsesReturn_water_temperature_setpoint (IReturn_water_temperature_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IReturn_water_temperature_setpoint> getUsesReturn_water_temperature_setpoint (){
		Set<IReturn_water_temperature_setpoint> UsesReturn_water_temperature_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Return_water_temperature_setpoint) {
				UsesReturn_water_temperature_setpoint.add((Return_water_temperature_setpoint)action);
			}
		});
		return UsesReturn_water_temperature_setpoint;
	}

	public static Set<IHws_rwtc_wdpc> getAllHws_rwtc_wdpcsObjectsCreated(){
		Set<IHws_rwtc_wdpc> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Hws_rwtc_wdpc")).subjects().stream()
		.map(mapper->(IHws_rwtc_wdpc)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}