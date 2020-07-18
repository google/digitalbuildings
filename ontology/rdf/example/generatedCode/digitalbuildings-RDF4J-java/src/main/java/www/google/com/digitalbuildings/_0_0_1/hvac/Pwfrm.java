package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.Monitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IProcess_water_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Process_water_flowrate_sensor;

/**
* Class Pwfrm 
* Flowrate monitoring for process water.
*/
@SuppressWarnings("serial")
public class Pwfrm extends www.google.com.digitalbuildings._0_0_1.Monitoring implements IPwfrm{

	IRI newInstance;
	public Pwfrm(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Pwfrm"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesProcess_water_flowrate_sensor (IProcess_water_flowrate_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IProcess_water_flowrate_sensor> getUsesProcess_water_flowrate_sensor (){
		Set<IProcess_water_flowrate_sensor> UsesProcess_water_flowrate_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Process_water_flowrate_sensor) {
				UsesProcess_water_flowrate_sensor.add((Process_water_flowrate_sensor)action);
			}
		});
		return UsesProcess_water_flowrate_sensor;
	}

	public static Set<IPwfrm> getAllPwfrmsObjectsCreated(){
		Set<IPwfrm> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Pwfrm")).subjects().stream()
		.map(mapper->(IPwfrm)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}