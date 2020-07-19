package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.facilities.IPhysicalLocation;
import www.google.com.digitalbuildings._0_0_1.facilities.PhysicalLocation;

/**
* Class Fan_ss 
* Basic fan with start/stop and status.
*/
@SuppressWarnings("serial")
public class Fan_ss extends www.google.com.digitalbuildings._0_0_1.hvac.Ss implements IFan_ss{

	IRI newInstance;
	public Fan_ss(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Fan_ss"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addPhysicalLocation(IPhysicalLocation parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#hasPhysicalLocation"), parameter);
	}

	public Set<IPhysicalLocation> getPhysicalLocation(){
		Set<IPhysicalLocation> physicalLocations = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#hasPhysicalLocation"), null)
		.objects().forEach(action->{
			if(action instanceof PhysicalLocation) {
				physicalLocations.add((PhysicalLocation)action);
			}
		});
		return physicalLocations;
	}

	public static Set<IFan_ss> getAllFan_sssObjectsCreated(){
		Set<IFan_ss> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Fan_ss")).subjects().stream()
		.map(mapper->(IFan_ss)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}