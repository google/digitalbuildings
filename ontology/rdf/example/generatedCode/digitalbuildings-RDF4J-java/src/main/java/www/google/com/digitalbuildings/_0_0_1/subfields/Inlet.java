package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Inlet 
* Area of media entrance.
*/
@SuppressWarnings("serial")
public class Inlet extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IInlet{

	IRI newInstance;
	public Inlet(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Inlet"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IInlet> getAllInletsObjectsCreated(){
		Set<IInlet> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Inlet")).subjects().stream()
		.map(mapper->(IInlet)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}