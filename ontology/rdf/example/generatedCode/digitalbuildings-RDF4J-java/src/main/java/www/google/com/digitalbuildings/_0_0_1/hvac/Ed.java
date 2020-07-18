package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IControl;
import www.google.com.digitalbuildings._0_0_1.Control;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_flowrate_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_air_flowrate_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_air_damper_percentage_command;

/**
* Class Ed 
* Exhaust air flow control.
*/
@SuppressWarnings("serial")
public class Ed extends www.google.com.digitalbuildings._0_0_1.Control implements IEd{

	IRI newInstance;
	public Ed(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Ed"));
	}

	public IRI iri()
	{
		return newInstance;
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


  public void addUsesExhaust_air_flowrate_sensor (IExhaust_air_flowrate_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IExhaust_air_flowrate_sensor> getUsesExhaust_air_flowrate_sensor (){
		Set<IExhaust_air_flowrate_sensor> UsesExhaust_air_flowrate_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_air_flowrate_sensor) {
				UsesExhaust_air_flowrate_sensor.add((Exhaust_air_flowrate_sensor)action);
			}
		});
		return UsesExhaust_air_flowrate_sensor;
	}


  public void addUsesExhaust_air_flowrate_setpoint (IExhaust_air_flowrate_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IExhaust_air_flowrate_setpoint> getUsesExhaust_air_flowrate_setpoint (){
		Set<IExhaust_air_flowrate_setpoint> UsesExhaust_air_flowrate_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_air_flowrate_setpoint) {
				UsesExhaust_air_flowrate_setpoint.add((Exhaust_air_flowrate_setpoint)action);
			}
		});
		return UsesExhaust_air_flowrate_setpoint;
	}

	public static Set<IEd> getAllEdsObjectsCreated(){
		Set<IEd> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Ed")).subjects().stream()
		.map(mapper->(IEd)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}