package www.google.com.digitalbuildings._0_0_1.units;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Current 
*/
@SuppressWarnings("serial")
public class Current extends www.google.com.digitalbuildings._0_0_1.units.Unit implements ICurrent{

	IRI newInstance;
	public Current(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/units#Current"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<ICurrent> getAllCurrentsObjectsCreated(){
		Set<ICurrent> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/units#Current")).subjects().stream()
		.map(mapper->(ICurrent)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}