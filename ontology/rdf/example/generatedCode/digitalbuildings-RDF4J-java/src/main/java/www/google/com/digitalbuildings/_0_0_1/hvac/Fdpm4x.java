package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.Monitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IFilter_differential_pressure_sensor_4;
import www.google.com.digitalbuildings._0_0_1.fields.Filter_differential_pressure_sensor_4;
import www.google.com.digitalbuildings._0_0_1.fields.IFilter_differential_pressure_sensor_3;
import www.google.com.digitalbuildings._0_0_1.fields.Filter_differential_pressure_sensor_3;
import www.google.com.digitalbuildings._0_0_1.fields.IFilter_differential_pressure_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.Filter_differential_pressure_sensor_2;
import www.google.com.digitalbuildings._0_0_1.fields.IFilter_differential_pressure_sensor_1;
import www.google.com.digitalbuildings._0_0_1.fields.Filter_differential_pressure_sensor_1;

/**
* Class Fdpm4x 
* Filter pressure monitoring (4 sensors).
*/
@SuppressWarnings("serial")
public class Fdpm4x extends www.google.com.digitalbuildings._0_0_1.Monitoring implements IFdpm4x{

	IRI newInstance;
	public Fdpm4x(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Fdpm4x"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesFilter_differential_pressure_sensor_1 (IFilter_differential_pressure_sensor_1 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IFilter_differential_pressure_sensor_1> getUsesFilter_differential_pressure_sensor_1 (){
		Set<IFilter_differential_pressure_sensor_1> UsesFilter_differential_pressure_sensor_1 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Filter_differential_pressure_sensor_1) {
				UsesFilter_differential_pressure_sensor_1.add((Filter_differential_pressure_sensor_1)action);
			}
		});
		return UsesFilter_differential_pressure_sensor_1;
	}


  public void addUsesFilter_differential_pressure_sensor_2 (IFilter_differential_pressure_sensor_2 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IFilter_differential_pressure_sensor_2> getUsesFilter_differential_pressure_sensor_2 (){
		Set<IFilter_differential_pressure_sensor_2> UsesFilter_differential_pressure_sensor_2 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Filter_differential_pressure_sensor_2) {
				UsesFilter_differential_pressure_sensor_2.add((Filter_differential_pressure_sensor_2)action);
			}
		});
		return UsesFilter_differential_pressure_sensor_2;
	}


  public void addUsesFilter_differential_pressure_sensor_3 (IFilter_differential_pressure_sensor_3 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IFilter_differential_pressure_sensor_3> getUsesFilter_differential_pressure_sensor_3 (){
		Set<IFilter_differential_pressure_sensor_3> UsesFilter_differential_pressure_sensor_3 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Filter_differential_pressure_sensor_3) {
				UsesFilter_differential_pressure_sensor_3.add((Filter_differential_pressure_sensor_3)action);
			}
		});
		return UsesFilter_differential_pressure_sensor_3;
	}


  public void addUsesFilter_differential_pressure_sensor_4 (IFilter_differential_pressure_sensor_4 parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IFilter_differential_pressure_sensor_4> getUsesFilter_differential_pressure_sensor_4 (){
		Set<IFilter_differential_pressure_sensor_4> UsesFilter_differential_pressure_sensor_4 = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Filter_differential_pressure_sensor_4) {
				UsesFilter_differential_pressure_sensor_4.add((Filter_differential_pressure_sensor_4)action);
			}
		});
		return UsesFilter_differential_pressure_sensor_4;
	}

	public static Set<IFdpm4x> getAllFdpm4xsObjectsCreated(){
		Set<IFdpm4x> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Fdpm4x")).subjects().stream()
		.map(mapper->(IFdpm4x)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}