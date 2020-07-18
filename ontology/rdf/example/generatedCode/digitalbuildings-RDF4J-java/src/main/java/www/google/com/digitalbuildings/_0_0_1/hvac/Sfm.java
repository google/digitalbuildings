package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.Monitoring;
import www.google.com.digitalbuildings._0_0_1.fields.ISupply_air_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Supply_air_flowrate_sensor;

/**
* Class Sfm 
* Supply air flow monitoring.
*/
@SuppressWarnings("serial")
public class Sfm extends www.google.com.digitalbuildings._0_0_1.Monitoring implements ISfm{

	IRI newInstance;
	public Sfm(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Sfm"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesSupply_air_flowrate_sensor (ISupply_air_flowrate_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<ISupply_air_flowrate_sensor> getUsesSupply_air_flowrate_sensor (){
		Set<ISupply_air_flowrate_sensor> UsesSupply_air_flowrate_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Supply_air_flowrate_sensor) {
				UsesSupply_air_flowrate_sensor.add((Supply_air_flowrate_sensor)action);
			}
		});
		return UsesSupply_air_flowrate_sensor;
	}

	public static Set<ISfm> getAllSfmsObjectsCreated(){
		Set<ISfm> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Sfm")).subjects().stream()
		.map(mapper->(ISfm)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}