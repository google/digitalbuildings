package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_damper_percentage_command_3;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_air_damper_percentage_command_3;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_damper_percentage_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_air_damper_percentage_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_damper_percentage_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_air_damper_percentage_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_static_pressure_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_air_static_pressure_setpoint;

/**
* Class Fan_us_pao_hv5_3 
* Non-standard type for HV5
*/
@SuppressWarnings("serial")
public class Fan_us_pao_hv5_3 extends www.google.com.digitalbuildings._0_0_1.hvac.Fan_ss_vsc_bspc implements IFan_us_pao_hv5_3{

	IRI newInstance;
	public Fan_us_pao_hv5_3(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Fan_us_pao_hv5_3"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesExhaust_air_damper_percentage_command_1 (IExhaust_air_damper_percentage_command_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IExhaust_air_damper_percentage_command_1> getUsesExhaust_air_damper_percentage_command_1 (){
		Set<IExhaust_air_damper_percentage_command_1> UsesExhaust_air_damper_percentage_command_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_air_damper_percentage_command_1) {
				UsesExhaust_air_damper_percentage_command_1.add((Exhaust_air_damper_percentage_command_1)action);
			}
		});
		return UsesExhaust_air_damper_percentage_command_1;
	}


  public void addUsesExhaust_air_damper_percentage_command_2 (IExhaust_air_damper_percentage_command_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IExhaust_air_damper_percentage_command_2> getUsesExhaust_air_damper_percentage_command_2 (){
		Set<IExhaust_air_damper_percentage_command_2> UsesExhaust_air_damper_percentage_command_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_air_damper_percentage_command_2) {
				UsesExhaust_air_damper_percentage_command_2.add((Exhaust_air_damper_percentage_command_2)action);
			}
		});
		return UsesExhaust_air_damper_percentage_command_2;
	}


  public void addUsesExhaust_air_damper_percentage_command_3 (IExhaust_air_damper_percentage_command_3 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IExhaust_air_damper_percentage_command_3> getUsesExhaust_air_damper_percentage_command_3 (){
		Set<IExhaust_air_damper_percentage_command_3> UsesExhaust_air_damper_percentage_command_3 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_air_damper_percentage_command_3) {
				UsesExhaust_air_damper_percentage_command_3.add((Exhaust_air_damper_percentage_command_3)action);
			}
		});
		return UsesExhaust_air_damper_percentage_command_3;
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

	public static Set<IFan_us_pao_hv5_3> getAllFan_us_pao_hv5_3sObjectsCreated(){
		Set<IFan_us_pao_hv5_3> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Fan_us_pao_hv5_3")).subjects().stream()
		.map(mapper->(IFan_us_pao_hv5_3)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}