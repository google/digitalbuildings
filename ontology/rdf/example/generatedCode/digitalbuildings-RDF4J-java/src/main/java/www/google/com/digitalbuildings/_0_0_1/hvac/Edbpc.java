package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IControl;
import www.google.com.digitalbuildings._0_0_1.Control;
import www.google.com.digitalbuildings._0_0_1.fields.IBuilding_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Building_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IBuilding_air_static_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Building_air_static_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_air_damper_percentage_command;

/**
* Class Edbpc 
* Building static control with exhaust damper.
*/
@SuppressWarnings("serial")
public class Edbpc extends www.google.com.digitalbuildings._0_0_1.Control implements IEdbpc{

	IRI newInstance;
	public Edbpc(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Edbpc"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesBuilding_air_static_pressure_sensor (IBuilding_air_static_pressure_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IBuilding_air_static_pressure_sensor> getUsesBuilding_air_static_pressure_sensor (){
		Set<IBuilding_air_static_pressure_sensor> UsesBuilding_air_static_pressure_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Building_air_static_pressure_sensor) {
				UsesBuilding_air_static_pressure_sensor.add((Building_air_static_pressure_sensor)action);
			}
		});
		return UsesBuilding_air_static_pressure_sensor;
	}


  public void addUsesBuilding_air_static_pressure_setpoint (IBuilding_air_static_pressure_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IBuilding_air_static_pressure_setpoint> getUsesBuilding_air_static_pressure_setpoint (){
		Set<IBuilding_air_static_pressure_setpoint> UsesBuilding_air_static_pressure_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Building_air_static_pressure_setpoint) {
				UsesBuilding_air_static_pressure_setpoint.add((Building_air_static_pressure_setpoint)action);
			}
		});
		return UsesBuilding_air_static_pressure_setpoint;
	}


  public void addUsesExhaust_air_damper_percentage_command (IExhaust_air_damper_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IExhaust_air_damper_percentage_command> getUsesExhaust_air_damper_percentage_command (){
		Set<IExhaust_air_damper_percentage_command> UsesExhaust_air_damper_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_air_damper_percentage_command) {
				UsesExhaust_air_damper_percentage_command.add((Exhaust_air_damper_percentage_command)action);
			}
		});
		return UsesExhaust_air_damper_percentage_command;
	}

	public static Set<IEdbpc> getAllEdbpcsObjectsCreated(){
		Set<IEdbpc> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Edbpc")).subjects().stream()
		.map(mapper->(IEdbpc)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}