package www.google.com.digitalbuildings._0_0_1.units;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Frequency 
*/
@SuppressWarnings("serial")
public class Frequency extends www.google.com.digitalbuildings._0_0_1.units.Unit implements IFrequency{

	IRI newInstance;
	public Frequency(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/units#Frequency"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IFrequency> getAllFrequencysObjectsCreated(){
		Set<IFrequency> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/units#Frequency")).subjects().stream()
		.map(mapper->(IFrequency)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}