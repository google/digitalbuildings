package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.Operational;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_run_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_fan_run_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_run_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_fan_run_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_run_status_2;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_fan_run_status_2;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_run_status_1;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_fan_run_status_1;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_current_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_fan_current_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_fan_power_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_fan_power_sensor;

/**
* Class Df2xss 
* Discharge fan start-stop and feedback (2 pts).
*/
@SuppressWarnings("serial")
public class Df2xss extends www.google.com.digitalbuildings._0_0_1.Operational implements IDf2xss{

	IRI newInstance;
	public Df2xss(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Df2xss"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesDischarge_fan_run_command_1 (IDischarge_fan_run_command_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IDischarge_fan_run_command_1> getUsesDischarge_fan_run_command_1 (){
		Set<IDischarge_fan_run_command_1> UsesDischarge_fan_run_command_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Discharge_fan_run_command_1) {
				UsesDischarge_fan_run_command_1.add((Discharge_fan_run_command_1)action);
			}
		});
		return UsesDischarge_fan_run_command_1;
	}


  public void addUsesDischarge_fan_run_command_2 (IDischarge_fan_run_command_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IDischarge_fan_run_command_2> getUsesDischarge_fan_run_command_2 (){
		Set<IDischarge_fan_run_command_2> UsesDischarge_fan_run_command_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Discharge_fan_run_command_2) {
				UsesDischarge_fan_run_command_2.add((Discharge_fan_run_command_2)action);
			}
		});
		return UsesDischarge_fan_run_command_2;
	}


  public void addUsesDischarge_fan_run_status_1 (IDischarge_fan_run_status_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IDischarge_fan_run_status_1> getUsesDischarge_fan_run_status_1 (){
		Set<IDischarge_fan_run_status_1> UsesDischarge_fan_run_status_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Discharge_fan_run_status_1) {
				UsesDischarge_fan_run_status_1.add((Discharge_fan_run_status_1)action);
			}
		});
		return UsesDischarge_fan_run_status_1;
	}


  public void addUsesDischarge_fan_run_status_2 (IDischarge_fan_run_status_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IDischarge_fan_run_status_2> getUsesDischarge_fan_run_status_2 (){
		Set<IDischarge_fan_run_status_2> UsesDischarge_fan_run_status_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Discharge_fan_run_status_2) {
				UsesDischarge_fan_run_status_2.add((Discharge_fan_run_status_2)action);
			}
		});
		return UsesDischarge_fan_run_status_2;
	}


  public void addUsesOptionalsDischarge_fan_current_sensor (IDischarge_fan_current_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IDischarge_fan_current_sensor> getUsesOptionalsDischarge_fan_current_sensor (){
		Set<IDischarge_fan_current_sensor> UsesOptionalsDischarge_fan_current_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Discharge_fan_current_sensor) {
				UsesOptionalsDischarge_fan_current_sensor.add((Discharge_fan_current_sensor)action);
			}
		});
		return UsesOptionalsDischarge_fan_current_sensor;
	}


  public void addUsesOptionalsDischarge_fan_power_sensor (IDischarge_fan_power_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IDischarge_fan_power_sensor> getUsesOptionalsDischarge_fan_power_sensor (){
		Set<IDischarge_fan_power_sensor> UsesOptionalsDischarge_fan_power_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Discharge_fan_power_sensor) {
				UsesOptionalsDischarge_fan_power_sensor.add((Discharge_fan_power_sensor)action);
			}
		});
		return UsesOptionalsDischarge_fan_power_sensor;
	}

	public static Set<IDf2xss> getAllDf2xsssObjectsCreated(){
		Set<IDf2xss> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Df2xss")).subjects().stream()
		.map(mapper->(IDf2xss)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}