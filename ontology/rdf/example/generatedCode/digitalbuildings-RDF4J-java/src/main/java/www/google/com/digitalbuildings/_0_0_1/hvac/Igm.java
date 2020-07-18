package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IOperational;
import www.google.com.digitalbuildings._0_0_1.Operational;
import www.google.com.digitalbuildings._0_0_1.fields.IInlet_guidevane_percentage_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Inlet_guidevane_percentage_sensor;

/**
* Class Igm 
* Inlet guidevane monitoring.
*/
@SuppressWarnings("serial")
public class Igm extends www.google.com.digitalbuildings._0_0_1.Operational implements IIgm{

	IRI newInstance;
	public Igm(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Igm"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesInlet_guidevane_percentage_sensor (IInlet_guidevane_percentage_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IInlet_guidevane_percentage_sensor> getUsesInlet_guidevane_percentage_sensor (){
		Set<IInlet_guidevane_percentage_sensor> UsesInlet_guidevane_percentage_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Inlet_guidevane_percentage_sensor) {
				UsesInlet_guidevane_percentage_sensor.add((Inlet_guidevane_percentage_sensor)action);
			}
		});
		return UsesInlet_guidevane_percentage_sensor;
	}

	public static Set<IIgm> getAllIgmsObjectsCreated(){
		Set<IIgm> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Igm")).subjects().stream()
		.map(mapper->(IIgm)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}