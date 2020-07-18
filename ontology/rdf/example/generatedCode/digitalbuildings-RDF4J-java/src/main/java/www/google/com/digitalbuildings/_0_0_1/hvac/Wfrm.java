package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IMonitoring;
import www.google.com.digitalbuildings._0_0_1.Monitoring;
import www.google.com.digitalbuildings._0_0_1.fields.IFlowrate_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Flowrate_sensor;

/**
* Class Wfrm 
* Water flowrate monitoring.
*/
@SuppressWarnings("serial")
public class Wfrm extends www.google.com.digitalbuildings._0_0_1.Monitoring implements IWfrm{

	IRI newInstance;
	public Wfrm(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Wfrm"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesFlowrate_sensor (IFlowrate_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IFlowrate_sensor> getUsesFlowrate_sensor (){
		Set<IFlowrate_sensor> UsesFlowrate_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Flowrate_sensor) {
				UsesFlowrate_sensor.add((Flowrate_sensor)action);
			}
		});
		return UsesFlowrate_sensor;
	}

	public static Set<IWfrm> getAllWfrmsObjectsCreated(){
		Set<IWfrm> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Wfrm")).subjects().stream()
		.map(mapper->(IWfrm)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}