package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Filter 
* Component used for removing dust and other particulate matter from the air.
*/
@SuppressWarnings("serial")
public class Filter extends www.google.com.digitalbuildings._0_0_1.subfields.Component implements IFilter{

	IRI newInstance;
	public Filter(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Filter"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IFilter> getAllFiltersObjectsCreated(){
		Set<IFilter> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Filter")).subjects().stream()
		.map(mapper->(IFilter)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}