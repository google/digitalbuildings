package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Concentration 
* Concentration of chemical (usually in parts per million or parts per billion).
*/
@SuppressWarnings("serial")
public class Concentration extends www.google.com.digitalbuildings._0_0_1.subfields.Measurement implements IConcentration{

	IRI newInstance;
	public Concentration(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Concentration"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IConcentration> getAllConcentrationsObjectsCreated(){
		Set<IConcentration> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Concentration")).subjects().stream()
		.map(mapper->(IConcentration)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}