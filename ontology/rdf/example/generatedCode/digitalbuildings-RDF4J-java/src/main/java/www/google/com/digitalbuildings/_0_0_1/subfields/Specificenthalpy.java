package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Specificenthalpy 
* Measure of energy of air per unit mass.
*/
@SuppressWarnings("serial")
public class Specificenthalpy extends www.google.com.digitalbuildings._0_0_1.subfields.Measurement implements ISpecificenthalpy{

	IRI newInstance;
	public Specificenthalpy(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Specificenthalpy"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<ISpecificenthalpy> getAllSpecificenthalpysObjectsCreated(){
		Set<ISpecificenthalpy> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Specificenthalpy")).subjects().stream()
		.map(mapper->(ISpecificenthalpy)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}