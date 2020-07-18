package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.Monitoring;
import www.google.com.digitalbuildings._0_0_1.fields.ICondensing_water_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Condensing_water_flowrate_sensor;

/**
* Class Cdwfrm 
* Condenser water flowrate monitoring.
*/
@SuppressWarnings("serial")
public class Cdwfrm extends www.google.com.digitalbuildings._0_0_1.Monitoring implements ICdwfrm{

	IRI newInstance;
	public Cdwfrm(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Cdwfrm"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesCondensing_water_flowrate_sensor (ICondensing_water_flowrate_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ICondensing_water_flowrate_sensor> getUsesCondensing_water_flowrate_sensor (){
		Set<ICondensing_water_flowrate_sensor> UsesCondensing_water_flowrate_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Condensing_water_flowrate_sensor) {
				UsesCondensing_water_flowrate_sensor.add((Condensing_water_flowrate_sensor)action);
			}
		});
		return UsesCondensing_water_flowrate_sensor;
	}

	public static Set<ICdwfrm> getAllCdwfrmsObjectsCreated(){
		Set<ICdwfrm> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Cdwfrm")).subjects().stream()
		.map(mapper->(ICdwfrm)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}