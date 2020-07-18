package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.IEntityType;
import www.google.com.digitalbuildings._0_0_1.EntityType;

/**
* Class Functionality 
* The class of all functionalities
*/
@SuppressWarnings("serial")
public class Functionality extends www.google.com.digitalbuildings._0_0_1.EntityType implements IFunctionality{

	IRI newInstance;
	public Functionality(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Functionality"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IFunctionality> getAllFunctionalitysObjectsCreated(){
		Set<IFunctionality> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Functionality")).subjects().stream()
		.map(mapper->(IFunctionality)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}