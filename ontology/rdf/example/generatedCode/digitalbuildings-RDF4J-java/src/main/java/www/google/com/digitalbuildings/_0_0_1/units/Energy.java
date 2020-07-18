package www.google.com.digitalbuildings._0_0_1.units;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Energy 
*/
@SuppressWarnings("serial")
public class Energy extends www.google.com.digitalbuildings._0_0_1.units.Unit implements IEnergy{

	IRI newInstance;
	public Energy(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/units#Energy"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IEnergy> getAllEnergysObjectsCreated(){
		Set<IEnergy> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/units#Energy")).subjects().stream()
		.map(mapper->(IEnergy)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}