package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IControl;
import www.google.com.digitalbuildings._0_0_1.Control;
import www.google.com.digitalbuildings._0_0_1.fields.ICooling_air_damper_percentage_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.Cooling_air_damper_percentage_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.ICooling_air_flowrate_setpoint_1;
import www.google.com.digitalbuildings._0_0_1.fields.Cooling_air_flowrate_setpoint_1;
import www.google.com.digitalbuildings._0_0_1.fields.ICooling_air_flowrate_setpoint_2;
import www.google.com.digitalbuildings._0_0_1.fields.Cooling_air_flowrate_setpoint_2;
import www.google.com.digitalbuildings._0_0_1.fields.ICooling_air_damper_percentage_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.Cooling_air_damper_percentage_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.ICooling_air_flowrate_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.Cooling_air_flowrate_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.ICooling_air_flowrate_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.Cooling_air_flowrate_sensor_1;

/**
* Class Ddco 
* Flow control - dual duct, but only cooling.
*/
@SuppressWarnings("serial")
public class Ddco extends www.google.com.digitalbuildings._0_0_1.Control implements IDdco{

	IRI newInstance;
	public Ddco(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Ddco"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesCooling_air_damper_percentage_command_1 (ICooling_air_damper_percentage_command_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ICooling_air_damper_percentage_command_1> getUsesCooling_air_damper_percentage_command_1 (){
		Set<ICooling_air_damper_percentage_command_1> UsesCooling_air_damper_percentage_command_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Cooling_air_damper_percentage_command_1) {
				UsesCooling_air_damper_percentage_command_1.add((Cooling_air_damper_percentage_command_1)action);
			}
		});
		return UsesCooling_air_damper_percentage_command_1;
	}


  public void addUsesCooling_air_damper_percentage_command_2 (ICooling_air_damper_percentage_command_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ICooling_air_damper_percentage_command_2> getUsesCooling_air_damper_percentage_command_2 (){
		Set<ICooling_air_damper_percentage_command_2> UsesCooling_air_damper_percentage_command_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Cooling_air_damper_percentage_command_2) {
				UsesCooling_air_damper_percentage_command_2.add((Cooling_air_damper_percentage_command_2)action);
			}
		});
		return UsesCooling_air_damper_percentage_command_2;
	}


  public void addUsesCooling_air_flowrate_sensor_1 (ICooling_air_flowrate_sensor_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ICooling_air_flowrate_sensor_1> getUsesCooling_air_flowrate_sensor_1 (){
		Set<ICooling_air_flowrate_sensor_1> UsesCooling_air_flowrate_sensor_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Cooling_air_flowrate_sensor_1) {
				UsesCooling_air_flowrate_sensor_1.add((Cooling_air_flowrate_sensor_1)action);
			}
		});
		return UsesCooling_air_flowrate_sensor_1;
	}


  public void addUsesCooling_air_flowrate_sensor_2 (ICooling_air_flowrate_sensor_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ICooling_air_flowrate_sensor_2> getUsesCooling_air_flowrate_sensor_2 (){
		Set<ICooling_air_flowrate_sensor_2> UsesCooling_air_flowrate_sensor_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Cooling_air_flowrate_sensor_2) {
				UsesCooling_air_flowrate_sensor_2.add((Cooling_air_flowrate_sensor_2)action);
			}
		});
		return UsesCooling_air_flowrate_sensor_2;
	}


  public void addUsesCooling_air_flowrate_setpoint_1 (ICooling_air_flowrate_setpoint_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ICooling_air_flowrate_setpoint_1> getUsesCooling_air_flowrate_setpoint_1 (){
		Set<ICooling_air_flowrate_setpoint_1> UsesCooling_air_flowrate_setpoint_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Cooling_air_flowrate_setpoint_1) {
				UsesCooling_air_flowrate_setpoint_1.add((Cooling_air_flowrate_setpoint_1)action);
			}
		});
		return UsesCooling_air_flowrate_setpoint_1;
	}


  public void addUsesCooling_air_flowrate_setpoint_2 (ICooling_air_flowrate_setpoint_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ICooling_air_flowrate_setpoint_2> getUsesCooling_air_flowrate_setpoint_2 (){
		Set<ICooling_air_flowrate_setpoint_2> UsesCooling_air_flowrate_setpoint_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Cooling_air_flowrate_setpoint_2) {
				UsesCooling_air_flowrate_setpoint_2.add((Cooling_air_flowrate_setpoint_2)action);
			}
		});
		return UsesCooling_air_flowrate_setpoint_2;
	}

	public static Set<IDdco> getAllDdcosObjectsCreated(){
		Set<IDdco> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Ddco")).subjects().stream()
		.map(mapper->(IDdco)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}