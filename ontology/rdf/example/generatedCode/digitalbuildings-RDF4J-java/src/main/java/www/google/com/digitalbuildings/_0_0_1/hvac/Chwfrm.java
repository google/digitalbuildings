package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.Monitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IChilled_water_flowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Chilled_water_flowrate_sensor;

/**
* Class Chwfrm 
* Chilled water flowrate monitoring.
*/
@SuppressWarnings("serial")
public class Chwfrm extends www.google.com.digitalbuildings._0_0_1.Monitoring implements IChwfrm{

	IRI newInstance;
	public Chwfrm(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Chwfrm"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesChilled_water_flowrate_sensor (IChilled_water_flowrate_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IChilled_water_flowrate_sensor> getUsesChilled_water_flowrate_sensor (){
		Set<IChilled_water_flowrate_sensor> UsesChilled_water_flowrate_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Chilled_water_flowrate_sensor) {
				UsesChilled_water_flowrate_sensor.add((Chilled_water_flowrate_sensor)action);
			}
		});
		return UsesChilled_water_flowrate_sensor;
	}

	public static Set<IChwfrm> getAllChwfrmsObjectsCreated(){
		Set<IChwfrm> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Chwfrm")).subjects().stream()
		.map(mapper->(IChwfrm)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}