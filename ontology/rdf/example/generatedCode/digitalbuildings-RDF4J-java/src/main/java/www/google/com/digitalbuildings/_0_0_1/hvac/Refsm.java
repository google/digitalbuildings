package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.Monitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IRefrigerant_evaporator_saturation_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Refrigerant_evaporator_saturation_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IRefrigerant_condenser_saturation_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Refrigerant_condenser_saturation_temperature_sensor;

/**
* Class Refsm 
* Refrigerant saturation monitoring.
*/
@SuppressWarnings("serial")
public class Refsm extends www.google.com.digitalbuildings._0_0_1.Monitoring implements IRefsm{

	IRI newInstance;
	public Refsm(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Refsm"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesRefrigerant_condenser_saturation_temperature_sensor (IRefrigerant_condenser_saturation_temperature_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IRefrigerant_condenser_saturation_temperature_sensor> getUsesRefrigerant_condenser_saturation_temperature_sensor (){
		Set<IRefrigerant_condenser_saturation_temperature_sensor> UsesRefrigerant_condenser_saturation_temperature_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Refrigerant_condenser_saturation_temperature_sensor) {
				UsesRefrigerant_condenser_saturation_temperature_sensor.add((Refrigerant_condenser_saturation_temperature_sensor)action);
			}
		});
		return UsesRefrigerant_condenser_saturation_temperature_sensor;
	}


  public void addUsesRefrigerant_evaporator_saturation_temperature_sensor (IRefrigerant_evaporator_saturation_temperature_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IRefrigerant_evaporator_saturation_temperature_sensor> getUsesRefrigerant_evaporator_saturation_temperature_sensor (){
		Set<IRefrigerant_evaporator_saturation_temperature_sensor> UsesRefrigerant_evaporator_saturation_temperature_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Refrigerant_evaporator_saturation_temperature_sensor) {
				UsesRefrigerant_evaporator_saturation_temperature_sensor.add((Refrigerant_evaporator_saturation_temperature_sensor)action);
			}
		});
		return UsesRefrigerant_evaporator_saturation_temperature_sensor;
	}

	public static Set<IRefsm> getAllRefsmsObjectsCreated(){
		Set<IRefsm> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Refsm")).subjects().stream()
		.map(mapper->(IRefsm)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}