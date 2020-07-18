package www.google.com.digitalbuildings._0_0_1.units;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Resistance 
*/
@SuppressWarnings("serial")
public class Resistance extends www.google.com.digitalbuildings._0_0_1.units.Unit implements IResistance{

	IRI newInstance;
	public Resistance(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/units#Resistance"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IResistance> getAllResistancesObjectsCreated(){
		Set<IResistance> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/units#Resistance")).subjects().stream()
		.map(mapper->(IResistance)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}