package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Electric 
* Process or component driven by electricity (as to distinguish from natural gas, for instance).
*/
@SuppressWarnings("serial")
public class Electric extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IElectric{

	IRI newInstance;
	public Electric(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Electric"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IElectric> getAllElectricsObjectsCreated(){
		Set<IElectric> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Electric")).subjects().stream()
		.map(mapper->(IElectric)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}