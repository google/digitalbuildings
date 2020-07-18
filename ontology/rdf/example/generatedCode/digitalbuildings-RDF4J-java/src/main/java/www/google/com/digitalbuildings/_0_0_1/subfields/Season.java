package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Season 
* Weather conditions under which certain systems or processes are enabled.
*/
@SuppressWarnings("serial")
public class Season extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements ISeason{

	IRI newInstance;
	public Season(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Season"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<ISeason> getAllSeasonsObjectsCreated(){
		Set<ISeason> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Season")).subjects().stream()
		.map(mapper->(ISeason)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}