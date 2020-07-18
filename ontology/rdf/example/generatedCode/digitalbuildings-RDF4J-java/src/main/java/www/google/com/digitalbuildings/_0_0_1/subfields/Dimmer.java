package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Dimmer 
* Adjustment device of dimming light level for controlling output of a lighting fixture.
*/
@SuppressWarnings("serial")
public class Dimmer extends www.google.com.digitalbuildings._0_0_1.subfields.Component implements IDimmer{

	IRI newInstance;
	public Dimmer(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Dimmer"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IDimmer> getAllDimmersObjectsCreated(){
		Set<IDimmer> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Dimmer")).subjects().stream()
		.map(mapper->(IDimmer)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}