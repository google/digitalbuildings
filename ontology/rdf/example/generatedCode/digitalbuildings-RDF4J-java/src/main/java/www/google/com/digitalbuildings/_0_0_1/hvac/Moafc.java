package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IControl;
import www.google.com.digitalbuildings._0_0_1.Control;
import www.google.com.digitalbuildings._0_0_1.fields.IEconomizer_mode;
import www.google.com.digitalbuildings._0_0_1.fields.Economizer_mode;
import www.google.com.digitalbuildings._0_0_1.fields.IVentilation_outside_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Ventilation_outside_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.IVentilation_outside_air_flowrate_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Ventilation_outside_air_flowrate_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IVentilation_outside_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Ventilation_outside_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IOutside_air_flowrate_requirement;
import www.google.com.digitalbuildings._0_0_1.fields.Outside_air_flowrate_requirement;

/**
* Class Moafc 
* Minimum (ventilation) outside air flow control.
*/
@SuppressWarnings("serial")
public class Moafc extends www.google.com.digitalbuildings._0_0_1.Control implements IMoafc{

	IRI newInstance;
	public Moafc(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Moafc"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesVentilation_outside_air_damper_percentage_command (IVentilation_outside_air_damper_percentage_command parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IVentilation_outside_air_damper_percentage_command> getUsesVentilation_outside_air_damper_percentage_command (){
		Set<IVentilation_outside_air_damper_percentage_command> UsesVentilation_outside_air_damper_percentage_command = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Ventilation_outside_air_damper_percentage_command) {
				UsesVentilation_outside_air_damper_percentage_command.add((Ventilation_outside_air_damper_percentage_command)action);
			}
		});
		return UsesVentilation_outside_air_damper_percentage_command;
	}


  public void addUsesVentilation_outside_air_flowrate_sensor (IVentilation_outside_air_flowrate_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IVentilation_outside_air_flowrate_sensor> getUsesVentilation_outside_air_flowrate_sensor (){
		Set<IVentilation_outside_air_flowrate_sensor> UsesVentilation_outside_air_flowrate_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Ventilation_outside_air_flowrate_sensor) {
				UsesVentilation_outside_air_flowrate_sensor.add((Ventilation_outside_air_flowrate_sensor)action);
			}
		});
		return UsesVentilation_outside_air_flowrate_sensor;
	}


  public void addUsesVentilation_outside_air_flowrate_setpoint (IVentilation_outside_air_flowrate_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IVentilation_outside_air_flowrate_setpoint> getUsesVentilation_outside_air_flowrate_setpoint (){
		Set<IVentilation_outside_air_flowrate_setpoint> UsesVentilation_outside_air_flowrate_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Ventilation_outside_air_flowrate_setpoint) {
				UsesVentilation_outside_air_flowrate_setpoint.add((Ventilation_outside_air_flowrate_setpoint)action);
			}
		});
		return UsesVentilation_outside_air_flowrate_setpoint;
	}


  public void addUsesOptionalsEconomizer_mode (IEconomizer_mode parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IEconomizer_mode> getUsesOptionalsEconomizer_mode (){
		Set<IEconomizer_mode> UsesOptionalsEconomizer_mode = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Economizer_mode) {
				UsesOptionalsEconomizer_mode.add((Economizer_mode)action);
			}
		});
		return UsesOptionalsEconomizer_mode;
	}


  public void addUsesOptionalsOutside_air_flowrate_requirement (IOutside_air_flowrate_requirement parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IOutside_air_flowrate_requirement> getUsesOptionalsOutside_air_flowrate_requirement (){
		Set<IOutside_air_flowrate_requirement> UsesOptionalsOutside_air_flowrate_requirement = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Outside_air_flowrate_requirement) {
				UsesOptionalsOutside_air_flowrate_requirement.add((Outside_air_flowrate_requirement)action);
			}
		});
		return UsesOptionalsOutside_air_flowrate_requirement;
	}

	public static Set<IMoafc> getAllMoafcsObjectsCreated(){
		Set<IMoafc> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Moafc")).subjects().stream()
		.map(mapper->(IMoafc)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}