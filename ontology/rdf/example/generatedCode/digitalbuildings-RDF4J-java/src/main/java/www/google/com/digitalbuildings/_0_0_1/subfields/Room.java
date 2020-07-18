package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Room 
* A space that can be occupied, or a part or division of a building or floor enclosed by walls.
*/
@SuppressWarnings("serial")
public class Room extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IRoom{

	IRI newInstance;
	public Room(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Room"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IRoom> getAllRoomsObjectsCreated(){
		Set<IRoom> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Room")).subjects().stream()
		.map(mapper->(IRoom)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}