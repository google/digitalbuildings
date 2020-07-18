package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Water 
* Water in liquid form, conditioned or unconditioned
*/
@SuppressWarnings("serial")
public class Water extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IWater{

	IRI newInstance;
	public Water(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Water"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IWater> getAllWatersObjectsCreated(){
		Set<IWater> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Water")).subjects().stream()
		.map(mapper->(IWater)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}