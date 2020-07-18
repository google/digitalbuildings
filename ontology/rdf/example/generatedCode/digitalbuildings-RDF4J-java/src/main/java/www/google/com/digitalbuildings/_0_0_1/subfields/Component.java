package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Component 
*/
@SuppressWarnings("serial")
public class Component extends www.google.com.digitalbuildings._0_0_1.subfields.SubField implements IComponent{

	IRI newInstance;
	public Component(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Component"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IComponent> getAllComponentsObjectsCreated(){
		Set<IComponent> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Component")).subjects().stream()
		.map(mapper->(IComponent)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}