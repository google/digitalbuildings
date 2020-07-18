package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Wind 
* Movement of ambient air.
*/
@SuppressWarnings("serial")
public class Wind extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IWind{

	IRI newInstance;
	public Wind(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Wind"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IWind> getAllWindsObjectsCreated(){
		Set<IWind> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Wind")).subjects().stream()
		.map(mapper->(IWind)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}