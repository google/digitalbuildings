package www.google.com.digitalbuildings._0_0_1;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Equipment 
* The class of all equipment
*/
@SuppressWarnings("serial")
public class Equipment extends www.google.com.digitalbuildings._0_0_1.EntityType implements IEquipment{

	IRI newInstance;
	public Equipment(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#Equipment"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IEquipment> getAllEquipmentsObjectsCreated(){
		Set<IEquipment> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1#Equipment")).subjects().stream()
		.map(mapper->(IEquipment)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}