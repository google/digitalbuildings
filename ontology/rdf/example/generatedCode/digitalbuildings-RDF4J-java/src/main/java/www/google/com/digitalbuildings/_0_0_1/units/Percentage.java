package www.google.com.digitalbuildings._0_0_1.units;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Percentage 
*/
@SuppressWarnings("serial")
public class Percentage extends www.google.com.digitalbuildings._0_0_1.units.Unit implements IPercentage{

	IRI newInstance;
	public Percentage(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/units#Percentage"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IPercentage> getAllPercentagesObjectsCreated(){
		Set<IPercentage> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/units#Percentage")).subjects().stream()
		.map(mapper->(IPercentage)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}