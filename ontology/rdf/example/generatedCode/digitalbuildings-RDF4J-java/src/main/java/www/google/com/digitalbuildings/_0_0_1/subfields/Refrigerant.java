package www.google.com.digitalbuildings._0_0_1.subfields;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;

/**
* Class Refrigerant 
* Substance used in the mechanical refrigeration process (e.g. R-134a)
*/
@SuppressWarnings("serial")
public class Refrigerant extends www.google.com.digitalbuildings._0_0_1.subfields.Descriptor implements IRefrigerant{

	IRI newInstance;
	public Refrigerant(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Refrigerant"));
	}

	public IRI iri()
	{
		return newInstance;
	}

	public static Set<IRefrigerant> getAllRefrigerantsObjectsCreated(){
		Set<IRefrigerant> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/subfields#Refrigerant")).subjects().stream()
		.map(mapper->(IRefrigerant)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}