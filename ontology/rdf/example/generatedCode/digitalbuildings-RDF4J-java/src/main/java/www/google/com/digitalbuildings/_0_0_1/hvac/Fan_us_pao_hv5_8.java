package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_static_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_air_static_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_damper_percentage_command;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_air_damper_percentage_command;

/**
* Class Fan_us_pao_hv5_8 
* Non-standard type for HV5 EFs
*/
@SuppressWarnings("serial")
public class Fan_us_pao_hv5_8 extends www.google.com.digitalbuildings._0_0_1.hvac.Fan_ss_vsc implements IFan_us_pao_hv5_8{

	IRI newInstance;
	public Fan_us_pao_hv5_8(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Fan_us_pao_hv5_8"));
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


  public void addUsesExhaust_air_static_pressure_sensor (IExhaust_air_static_pressure_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IExhaust_air_static_pressure_sensor> getUsesExhaust_air_static_pressure_sensor (){
		Set<IExhaust_air_static_pressure_sensor> UsesExhaust_air_static_pressure_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_air_static_pressure_sensor) {
				UsesExhaust_air_static_pressure_sensor.add((Exhaust_air_static_pressure_sensor)action);
			}
		});
		return UsesExhaust_air_static_pressure_sensor;
	}


  public void addUsesExhaust_air_static_pressure_setpoint (IExhaust_air_static_pressure_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IExhaust_air_static_pressure_setpoint> getUsesExhaust_air_static_pressure_setpoint (){
		Set<IExhaust_air_static_pressure_setpoint> UsesExhaust_air_static_pressure_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_air_static_pressure_setpoint) {
				UsesExhaust_air_static_pressure_setpoint.add((Exhaust_air_static_pressure_setpoint)action);
			}
		});
		return UsesExhaust_air_static_pressure_setpoint;
	}

	public static Set<IFan_us_pao_hv5_8> getAllFan_us_pao_hv5_8sObjectsCreated(){
		Set<IFan_us_pao_hv5_8> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Fan_us_pao_hv5_8")).subjects().stream()
		.map(mapper->(IFan_us_pao_hv5_8)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}