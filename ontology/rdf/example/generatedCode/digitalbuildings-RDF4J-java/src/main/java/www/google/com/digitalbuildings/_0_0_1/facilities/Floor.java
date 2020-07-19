package www.google.com.digitalbuildings._0_0_1.facilities;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Floor 
* This is a type for FLOOR facilities object
*/
@SuppressWarnings("serial")
public class Floor extends www.google.com.digitalbuildings._0_0_1.facilities.PhysicalLocation implements IFloor{

	IRI newInstance;
	public Floor(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/facilities#Floor"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addRoom(IRoom parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#hasRoom"), parameter);
	}

	public Set<IRoom> getRooms(){
		Set<IRoom> rooms = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#hasRoom"), null)
		.objects().forEach(action->{
			if(action instanceof Room) {
				rooms.add((Room)action);
			}
		});
		return rooms;
	}

	public static Set<IFloor> getAllFloorsObjectsCreated(){
		Set<IFloor> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/facilities#Floor")).subjects().stream()
		.map(mapper->(IFloor)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}