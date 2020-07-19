package www.google.com.digitalbuildings._0_0_1.facilities;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Building 
* This is a type for BUILDING facilities object
*/
@SuppressWarnings("serial")
public class Building extends www.google.com.digitalbuildings._0_0_1.facilities.PhysicalLocation implements IBuilding{

	IRI newInstance;
	public Building(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/facilities#Building"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addFloor(IFloor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#hasFloor"), parameter);
	}

	public Set<IFloor> getFloors (){
		Set<IFloor> floors = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#hasFloor"), null)
		.objects().forEach(action->{
			if(action instanceof Floor) {
				floors.add((Floor)action);
			}
		});
		return floors;
	}

	public static Set<IBuilding> getAllBuildingsObjectsCreated(){
		Set<IBuilding> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/facilities#Building")).subjects().stream()
		.map(mapper->(IBuilding)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}