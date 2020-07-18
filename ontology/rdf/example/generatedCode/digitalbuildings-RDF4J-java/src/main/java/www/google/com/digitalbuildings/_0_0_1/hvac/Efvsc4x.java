package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.Operational;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_command_4;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_speed_percentage_command_4;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_frequency_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_speed_frequency_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_frequency_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_speed_frequency_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_speed_percentage_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_frequency_sensor_4;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_speed_frequency_sensor_4;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_speed_percentage_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_frequency_sensor_3;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_speed_frequency_sensor_3;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_command_3;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_speed_percentage_command_3;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_status_4;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_run_status_4;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_current_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_current_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_current_sensor_3;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_current_sensor_3;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_command_4;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_run_command_4;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_status_1;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_run_status_1;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_current_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_current_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_command_3;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_run_command_3;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_run_command_2;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_status_3;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_run_status_3;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_current_sensor_4;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_current_sensor_4;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_run_command_1;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_run_status_2;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_run_status_2;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_power_sensor_3;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_power_sensor_3;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_power_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_power_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_power_sensor_4;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_power_sensor_4;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_speed_percentage_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_speed_percentage_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_sensor_4;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_speed_percentage_sensor_4;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_speed_percentage_sensor_3;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_speed_percentage_sensor_3;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_fan_power_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_fan_power_sensor_1;

/**
* Class Efvsc4x 
* Exhaust fan variable speed control with feedback and sensoring for four fans.
*/
@SuppressWarnings("serial")
public class Efvsc4x extends www.google.com.digitalbuildings._0_0_1.Operational implements IEfvsc4x{

	IRI newInstance;
	public Efvsc4x(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Efvsc4x"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesOptionalsExhaust_fan_current_sensor_1 (IExhaust_fan_current_sensor_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IExhaust_fan_current_sensor_1> getUsesOptionalsExhaust_fan_current_sensor_1 (){
		Set<IExhaust_fan_current_sensor_1> UsesOptionalsExhaust_fan_current_sensor_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_current_sensor_1) {
				UsesOptionalsExhaust_fan_current_sensor_1.add((Exhaust_fan_current_sensor_1)action);
			}
		});
		return UsesOptionalsExhaust_fan_current_sensor_1;
	}


  public void addUsesOptionalsExhaust_fan_current_sensor_2 (IExhaust_fan_current_sensor_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IExhaust_fan_current_sensor_2> getUsesOptionalsExhaust_fan_current_sensor_2 (){
		Set<IExhaust_fan_current_sensor_2> UsesOptionalsExhaust_fan_current_sensor_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_current_sensor_2) {
				UsesOptionalsExhaust_fan_current_sensor_2.add((Exhaust_fan_current_sensor_2)action);
			}
		});
		return UsesOptionalsExhaust_fan_current_sensor_2;
	}


  public void addUsesOptionalsExhaust_fan_current_sensor_3 (IExhaust_fan_current_sensor_3 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IExhaust_fan_current_sensor_3> getUsesOptionalsExhaust_fan_current_sensor_3 (){
		Set<IExhaust_fan_current_sensor_3> UsesOptionalsExhaust_fan_current_sensor_3 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_current_sensor_3) {
				UsesOptionalsExhaust_fan_current_sensor_3.add((Exhaust_fan_current_sensor_3)action);
			}
		});
		return UsesOptionalsExhaust_fan_current_sensor_3;
	}


  public void addUsesOptionalsExhaust_fan_current_sensor_4 (IExhaust_fan_current_sensor_4 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IExhaust_fan_current_sensor_4> getUsesOptionalsExhaust_fan_current_sensor_4 (){
		Set<IExhaust_fan_current_sensor_4> UsesOptionalsExhaust_fan_current_sensor_4 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_current_sensor_4) {
				UsesOptionalsExhaust_fan_current_sensor_4.add((Exhaust_fan_current_sensor_4)action);
			}
		});
		return UsesOptionalsExhaust_fan_current_sensor_4;
	}


  public void addUsesOptionalsExhaust_fan_power_sensor_1 (IExhaust_fan_power_sensor_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IExhaust_fan_power_sensor_1> getUsesOptionalsExhaust_fan_power_sensor_1 (){
		Set<IExhaust_fan_power_sensor_1> UsesOptionalsExhaust_fan_power_sensor_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_power_sensor_1) {
				UsesOptionalsExhaust_fan_power_sensor_1.add((Exhaust_fan_power_sensor_1)action);
			}
		});
		return UsesOptionalsExhaust_fan_power_sensor_1;
	}


  public void addUsesOptionalsExhaust_fan_power_sensor_2 (IExhaust_fan_power_sensor_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IExhaust_fan_power_sensor_2> getUsesOptionalsExhaust_fan_power_sensor_2 (){
		Set<IExhaust_fan_power_sensor_2> UsesOptionalsExhaust_fan_power_sensor_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_power_sensor_2) {
				UsesOptionalsExhaust_fan_power_sensor_2.add((Exhaust_fan_power_sensor_2)action);
			}
		});
		return UsesOptionalsExhaust_fan_power_sensor_2;
	}


  public void addUsesOptionalsExhaust_fan_power_sensor_3 (IExhaust_fan_power_sensor_3 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IExhaust_fan_power_sensor_3> getUsesOptionalsExhaust_fan_power_sensor_3 (){
		Set<IExhaust_fan_power_sensor_3> UsesOptionalsExhaust_fan_power_sensor_3 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_power_sensor_3) {
				UsesOptionalsExhaust_fan_power_sensor_3.add((Exhaust_fan_power_sensor_3)action);
			}
		});
		return UsesOptionalsExhaust_fan_power_sensor_3;
	}


  public void addUsesOptionalsExhaust_fan_power_sensor_4 (IExhaust_fan_power_sensor_4 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IExhaust_fan_power_sensor_4> getUsesOptionalsExhaust_fan_power_sensor_4 (){
		Set<IExhaust_fan_power_sensor_4> UsesOptionalsExhaust_fan_power_sensor_4 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_power_sensor_4) {
				UsesOptionalsExhaust_fan_power_sensor_4.add((Exhaust_fan_power_sensor_4)action);
			}
		});
		return UsesOptionalsExhaust_fan_power_sensor_4;
	}


  public void addUsesOptionalsExhaust_fan_speed_frequency_sensor_1 (IExhaust_fan_speed_frequency_sensor_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IExhaust_fan_speed_frequency_sensor_1> getUsesOptionalsExhaust_fan_speed_frequency_sensor_1 (){
		Set<IExhaust_fan_speed_frequency_sensor_1> UsesOptionalsExhaust_fan_speed_frequency_sensor_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_speed_frequency_sensor_1) {
				UsesOptionalsExhaust_fan_speed_frequency_sensor_1.add((Exhaust_fan_speed_frequency_sensor_1)action);
			}
		});
		return UsesOptionalsExhaust_fan_speed_frequency_sensor_1;
	}


  public void addUsesOptionalsExhaust_fan_speed_frequency_sensor_2 (IExhaust_fan_speed_frequency_sensor_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IExhaust_fan_speed_frequency_sensor_2> getUsesOptionalsExhaust_fan_speed_frequency_sensor_2 (){
		Set<IExhaust_fan_speed_frequency_sensor_2> UsesOptionalsExhaust_fan_speed_frequency_sensor_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_speed_frequency_sensor_2) {
				UsesOptionalsExhaust_fan_speed_frequency_sensor_2.add((Exhaust_fan_speed_frequency_sensor_2)action);
			}
		});
		return UsesOptionalsExhaust_fan_speed_frequency_sensor_2;
	}


  public void addUsesOptionalsExhaust_fan_speed_frequency_sensor_3 (IExhaust_fan_speed_frequency_sensor_3 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IExhaust_fan_speed_frequency_sensor_3> getUsesOptionalsExhaust_fan_speed_frequency_sensor_3 (){
		Set<IExhaust_fan_speed_frequency_sensor_3> UsesOptionalsExhaust_fan_speed_frequency_sensor_3 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_speed_frequency_sensor_3) {
				UsesOptionalsExhaust_fan_speed_frequency_sensor_3.add((Exhaust_fan_speed_frequency_sensor_3)action);
			}
		});
		return UsesOptionalsExhaust_fan_speed_frequency_sensor_3;
	}


  public void addUsesOptionalsExhaust_fan_speed_frequency_sensor_4 (IExhaust_fan_speed_frequency_sensor_4 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IExhaust_fan_speed_frequency_sensor_4> getUsesOptionalsExhaust_fan_speed_frequency_sensor_4 (){
		Set<IExhaust_fan_speed_frequency_sensor_4> UsesOptionalsExhaust_fan_speed_frequency_sensor_4 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_speed_frequency_sensor_4) {
				UsesOptionalsExhaust_fan_speed_frequency_sensor_4.add((Exhaust_fan_speed_frequency_sensor_4)action);
			}
		});
		return UsesOptionalsExhaust_fan_speed_frequency_sensor_4;
	}


  public void addUsesOptionalsExhaust_fan_speed_percentage_sensor_1 (IExhaust_fan_speed_percentage_sensor_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IExhaust_fan_speed_percentage_sensor_1> getUsesOptionalsExhaust_fan_speed_percentage_sensor_1 (){
		Set<IExhaust_fan_speed_percentage_sensor_1> UsesOptionalsExhaust_fan_speed_percentage_sensor_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_speed_percentage_sensor_1) {
				UsesOptionalsExhaust_fan_speed_percentage_sensor_1.add((Exhaust_fan_speed_percentage_sensor_1)action);
			}
		});
		return UsesOptionalsExhaust_fan_speed_percentage_sensor_1;
	}


  public void addUsesOptionalsExhaust_fan_speed_percentage_sensor_2 (IExhaust_fan_speed_percentage_sensor_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IExhaust_fan_speed_percentage_sensor_2> getUsesOptionalsExhaust_fan_speed_percentage_sensor_2 (){
		Set<IExhaust_fan_speed_percentage_sensor_2> UsesOptionalsExhaust_fan_speed_percentage_sensor_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_speed_percentage_sensor_2) {
				UsesOptionalsExhaust_fan_speed_percentage_sensor_2.add((Exhaust_fan_speed_percentage_sensor_2)action);
			}
		});
		return UsesOptionalsExhaust_fan_speed_percentage_sensor_2;
	}


  public void addUsesOptionalsExhaust_fan_speed_percentage_sensor_3 (IExhaust_fan_speed_percentage_sensor_3 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IExhaust_fan_speed_percentage_sensor_3> getUsesOptionalsExhaust_fan_speed_percentage_sensor_3 (){
		Set<IExhaust_fan_speed_percentage_sensor_3> UsesOptionalsExhaust_fan_speed_percentage_sensor_3 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_speed_percentage_sensor_3) {
				UsesOptionalsExhaust_fan_speed_percentage_sensor_3.add((Exhaust_fan_speed_percentage_sensor_3)action);
			}
		});
		return UsesOptionalsExhaust_fan_speed_percentage_sensor_3;
	}


  public void addUsesOptionalsExhaust_fan_speed_percentage_sensor_4 (IExhaust_fan_speed_percentage_sensor_4 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), parameter);
	}

	public Set<IExhaust_fan_speed_percentage_sensor_4> getUsesOptionalsExhaust_fan_speed_percentage_sensor_4 (){
		Set<IExhaust_fan_speed_percentage_sensor_4> UsesOptionalsExhaust_fan_speed_percentage_sensor_4 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#usesOptional"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_speed_percentage_sensor_4) {
				UsesOptionalsExhaust_fan_speed_percentage_sensor_4.add((Exhaust_fan_speed_percentage_sensor_4)action);
			}
		});
		return UsesOptionalsExhaust_fan_speed_percentage_sensor_4;
	}


  public void addUsesExhaust_fan_run_command_1 (IExhaust_fan_run_command_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IExhaust_fan_run_command_1> getUsesExhaust_fan_run_command_1 (){
		Set<IExhaust_fan_run_command_1> UsesExhaust_fan_run_command_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_run_command_1) {
				UsesExhaust_fan_run_command_1.add((Exhaust_fan_run_command_1)action);
			}
		});
		return UsesExhaust_fan_run_command_1;
	}


  public void addUsesExhaust_fan_run_command_2 (IExhaust_fan_run_command_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IExhaust_fan_run_command_2> getUsesExhaust_fan_run_command_2 (){
		Set<IExhaust_fan_run_command_2> UsesExhaust_fan_run_command_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_run_command_2) {
				UsesExhaust_fan_run_command_2.add((Exhaust_fan_run_command_2)action);
			}
		});
		return UsesExhaust_fan_run_command_2;
	}


  public void addUsesExhaust_fan_run_command_3 (IExhaust_fan_run_command_3 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IExhaust_fan_run_command_3> getUsesExhaust_fan_run_command_3 (){
		Set<IExhaust_fan_run_command_3> UsesExhaust_fan_run_command_3 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_run_command_3) {
				UsesExhaust_fan_run_command_3.add((Exhaust_fan_run_command_3)action);
			}
		});
		return UsesExhaust_fan_run_command_3;
	}


  public void addUsesExhaust_fan_run_command_4 (IExhaust_fan_run_command_4 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IExhaust_fan_run_command_4> getUsesExhaust_fan_run_command_4 (){
		Set<IExhaust_fan_run_command_4> UsesExhaust_fan_run_command_4 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_run_command_4) {
				UsesExhaust_fan_run_command_4.add((Exhaust_fan_run_command_4)action);
			}
		});
		return UsesExhaust_fan_run_command_4;
	}


  public void addUsesExhaust_fan_run_status_1 (IExhaust_fan_run_status_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IExhaust_fan_run_status_1> getUsesExhaust_fan_run_status_1 (){
		Set<IExhaust_fan_run_status_1> UsesExhaust_fan_run_status_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_run_status_1) {
				UsesExhaust_fan_run_status_1.add((Exhaust_fan_run_status_1)action);
			}
		});
		return UsesExhaust_fan_run_status_1;
	}


  public void addUsesExhaust_fan_run_status_2 (IExhaust_fan_run_status_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IExhaust_fan_run_status_2> getUsesExhaust_fan_run_status_2 (){
		Set<IExhaust_fan_run_status_2> UsesExhaust_fan_run_status_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_run_status_2) {
				UsesExhaust_fan_run_status_2.add((Exhaust_fan_run_status_2)action);
			}
		});
		return UsesExhaust_fan_run_status_2;
	}


  public void addUsesExhaust_fan_run_status_3 (IExhaust_fan_run_status_3 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IExhaust_fan_run_status_3> getUsesExhaust_fan_run_status_3 (){
		Set<IExhaust_fan_run_status_3> UsesExhaust_fan_run_status_3 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_run_status_3) {
				UsesExhaust_fan_run_status_3.add((Exhaust_fan_run_status_3)action);
			}
		});
		return UsesExhaust_fan_run_status_3;
	}


  public void addUsesExhaust_fan_run_status_4 (IExhaust_fan_run_status_4 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IExhaust_fan_run_status_4> getUsesExhaust_fan_run_status_4 (){
		Set<IExhaust_fan_run_status_4> UsesExhaust_fan_run_status_4 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_run_status_4) {
				UsesExhaust_fan_run_status_4.add((Exhaust_fan_run_status_4)action);
			}
		});
		return UsesExhaust_fan_run_status_4;
	}


  public void addUsesExhaust_fan_speed_percentage_command_1 (IExhaust_fan_speed_percentage_command_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IExhaust_fan_speed_percentage_command_1> getUsesExhaust_fan_speed_percentage_command_1 (){
		Set<IExhaust_fan_speed_percentage_command_1> UsesExhaust_fan_speed_percentage_command_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_speed_percentage_command_1) {
				UsesExhaust_fan_speed_percentage_command_1.add((Exhaust_fan_speed_percentage_command_1)action);
			}
		});
		return UsesExhaust_fan_speed_percentage_command_1;
	}


  public void addUsesExhaust_fan_speed_percentage_command_2 (IExhaust_fan_speed_percentage_command_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IExhaust_fan_speed_percentage_command_2> getUsesExhaust_fan_speed_percentage_command_2 (){
		Set<IExhaust_fan_speed_percentage_command_2> UsesExhaust_fan_speed_percentage_command_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_speed_percentage_command_2) {
				UsesExhaust_fan_speed_percentage_command_2.add((Exhaust_fan_speed_percentage_command_2)action);
			}
		});
		return UsesExhaust_fan_speed_percentage_command_2;
	}


  public void addUsesExhaust_fan_speed_percentage_command_3 (IExhaust_fan_speed_percentage_command_3 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IExhaust_fan_speed_percentage_command_3> getUsesExhaust_fan_speed_percentage_command_3 (){
		Set<IExhaust_fan_speed_percentage_command_3> UsesExhaust_fan_speed_percentage_command_3 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_speed_percentage_command_3) {
				UsesExhaust_fan_speed_percentage_command_3.add((Exhaust_fan_speed_percentage_command_3)action);
			}
		});
		return UsesExhaust_fan_speed_percentage_command_3;
	}


  public void addUsesExhaust_fan_speed_percentage_command_4 (IExhaust_fan_speed_percentage_command_4 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IExhaust_fan_speed_percentage_command_4> getUsesExhaust_fan_speed_percentage_command_4 (){
		Set<IExhaust_fan_speed_percentage_command_4> UsesExhaust_fan_speed_percentage_command_4 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_fan_speed_percentage_command_4) {
				UsesExhaust_fan_speed_percentage_command_4.add((Exhaust_fan_speed_percentage_command_4)action);
			}
		});
		return UsesExhaust_fan_speed_percentage_command_4;
	}

	public static Set<IEfvsc4x> getAllEfvsc4xsObjectsCreated(){
		Set<IEfvsc4x> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Efvsc4x")).subjects().stream()
		.map(mapper->(IEfvsc4x)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}