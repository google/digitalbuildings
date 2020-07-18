package www.google.com.digitalbuildings._0_0_1.facilities;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IEntityType;
import www.google.com.digitalbuildings._0_0_1.EntityType;

/**
* Class PhysicalLocation 
* The class of all physical locations
*/
@SuppressWarnings("serial")
public class PhysicalLocation extends www.google.com.digitalbuildings._0_0_1.EntityType implements IPhysicalLocation{

	IRI newInstance;
	public PhysicalLocation(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/facilities#PhysicalLocation"));
	}

	public IRI iri()
	{
		return newInstance;
	}


	public void setCode(String param)
	{
	 GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#hasCode"), GLOBAL.factory.createLiteral(param));
	}

	public String getCode(){
		return (GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#hasCode"), null).objects().iterator().next()).stringValue();
	}

	public void setFriendlyName(String param)
	{
	 GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#hasFriendlyName"), GLOBAL.factory.createLiteral(param));
	}

	public String getFriendlyName(){
		return (GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#hasFriendlyName"), null).objects().iterator().next()).stringValue();
	}
	public static Set<IPhysicalLocation> getAllPhysicalLocationsObjectsCreated(){
		Set<IPhysicalLocation> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/facilities#PhysicalLocation")).subjects().stream()
		.map(mapper->(IPhysicalLocation)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}