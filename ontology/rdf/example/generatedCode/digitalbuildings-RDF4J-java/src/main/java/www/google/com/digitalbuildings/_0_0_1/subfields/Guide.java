package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Guide 
* Component used to guide flow of media or movement of component.
*/
@SuppressWarnings("serial")
public class Guide extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IGuide{

	IRI newInstance;
	public Guide(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Guide"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IGuide> getAllGuidesObjectsCreated(){
		Set<IGuide> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Guide")).subjects().stream()
		.map(mapper->(IGuide)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}