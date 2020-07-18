package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Energy 
*  The quantitative property that must be transferred to an object to perform work (default electrical unless otherwise modified).
*/
@SuppressWarnings("serial")
public class Energy extends www.google.com.digitalbuildings._0_0_1.subfields.Measurement implements IEnergy{

	IRI newInstance;
	public Energy(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Energy"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IEnergy> getAllEnergysObjectsCreated(){
		Set<IEnergy> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Energy")).subjects().stream()
		.map(mapper->(IEnergy)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}