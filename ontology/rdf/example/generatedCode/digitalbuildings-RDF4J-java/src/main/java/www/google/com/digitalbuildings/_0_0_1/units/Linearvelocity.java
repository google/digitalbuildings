package www.google.com.digitalbuildings._0_0_1.units;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Linearvelocity 
*/
@SuppressWarnings("serial")
public class Linearvelocity extends www.google.com.digitalbuildings._0_0_1.units.Unit implements ILinearvelocity{

	IRI newInstance;
	public Linearvelocity(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/units#Linearvelocity"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<ILinearvelocity> getAllLinearvelocitysObjectsCreated(){
		Set<ILinearvelocity> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/units#Linearvelocity")).subjects().stream()
		.map(mapper->(ILinearvelocity)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}