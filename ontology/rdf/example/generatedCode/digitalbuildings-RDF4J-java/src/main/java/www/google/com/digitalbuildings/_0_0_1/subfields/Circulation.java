package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Circulation 
* Process or component used to circulate fluid through a device or system (typically onboard a boiler).
*/
@SuppressWarnings("serial")
public class Circulation extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements ICirculation{

	IRI newInstance;
	public Circulation(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Circulation"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<ICirculation> getAllCirculationsObjectsCreated(){
		Set<ICirculation> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Circulation")).subjects().stream()
		.map(mapper->(ICirculation)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}