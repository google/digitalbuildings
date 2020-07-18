package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.Monitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IDifferential_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Differential_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.ICondenser_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Condenser_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IEvaporator_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Evaporator_pressure_sensor;

/**
* Class Chpm 
* Chiller pressure monitoring.
*/
@SuppressWarnings("serial")
public class Chpm extends www.google.com.digitalbuildings._0_0_1.Monitoring implements IChpm{

	IRI newInstance;
	public Chpm(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Chpm"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesCondenser_pressure_sensor (ICondenser_pressure_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ICondenser_pressure_sensor> getUsesCondenser_pressure_sensor (){
		Set<ICondenser_pressure_sensor> UsesCondenser_pressure_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Condenser_pressure_sensor) {
				UsesCondenser_pressure_sensor.add((Condenser_pressure_sensor)action);
			}
		});
		return UsesCondenser_pressure_sensor;
	}


  public void addUsesDifferential_pressure_sensor (IDifferential_pressure_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IDifferential_pressure_sensor> getUsesDifferential_pressure_sensor (){
		Set<IDifferential_pressure_sensor> UsesDifferential_pressure_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Differential_pressure_sensor) {
				UsesDifferential_pressure_sensor.add((Differential_pressure_sensor)action);
			}
		});
		return UsesDifferential_pressure_sensor;
	}


  public void addUsesEvaporator_pressure_sensor (IEvaporator_pressure_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IEvaporator_pressure_sensor> getUsesEvaporator_pressure_sensor (){
		Set<IEvaporator_pressure_sensor> UsesEvaporator_pressure_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Evaporator_pressure_sensor) {
				UsesEvaporator_pressure_sensor.add((Evaporator_pressure_sensor)action);
			}
		});
		return UsesEvaporator_pressure_sensor;
	}

	public static Set<IChpm> getAllChpmsObjectsCreated(){
		Set<IChpm> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Chpm")).subjects().stream()
		.map(mapper->(IChpm)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}